# Dockerfile (inline comments)

***

```dockerfile
# Claude Code Observability — ALL-IN-ONE image
# WHAT: Single container running full observability stack
# WHY: Simplify deployment (docker run instead of docker-compose)
# HOW: Multi-stage build + supervisord orchestration

# --- Versions (centralized for consistency) ---
ARG OTELCOL_VERSION=0.119.0      # OTel Collector version
ARG PROMETHEUS_VERSION=3.1.0     # Prometheus version
ARG LOKI_VERSION=3.3.2           # Loki version
ARG GRAFANA_VERSION=11.4.0       # Grafana version


#####################################################################
# Stage 1 — Extract binaries from upstream images
#####################################################################

# --- OTel Collector ---
FROM otel/opentelemetry-collector-contrib:${OTELCOL_VERSION} AS otelcol
# WHAT: Official OTel image
# WHY: Reuse prebuilt binary (no compile needed)


# --- Grafana ---
FROM grafana/grafana:${GRAFANA_VERSION} AS grafana
# WHAT: Official Grafana image
# WHY: Grafana requires full install tree (plugins + UI assets)


# --- Fetch Prometheus & Loki binaries ---
FROM debian:bookworm-slim AS fetch

ARG PROMETHEUS_VERSION
ARG LOKI_VERSION
ARG TARGETARCH

RUN set -eux; \
    apt-get update; \
    # WHAT: install tools for downloading artifacts
    # WHY: curl (download), unzip (extract), certs (HTTPS)
    apt-get install -y --no-install-recommends ca-certificates curl unzip; \
    rm -rf /var/lib/apt/lists/*; \
    \
    # Detect architecture (amd64 / arm64)
    arch="${TARGETARCH:-amd64}"; \
    \
    # --- Prometheus ---
    curl -fsSL -o /tmp/prom.tar.gz \
      "https://github.com/prometheus/prometheus/releases/download/v${PROMETHEUS_VERSION}/prometheus-${PROMETHEUS_VERSION}.linux-${arch}.tar.gz"; \
    mkdir -p /out/prometheus; \
    tar -xzf /tmp/prom.tar.gz -C /out/prometheus --strip-components=1; \
    # WHAT: extract prometheus + promtool
    # WHY: binary distribution is tar.gz
    \
    # --- Loki ---
    curl -fsSL -o /tmp/loki.zip \
      "https://github.com/grafana/loki/releases/download/v${LOKI_VERSION}/loki-linux-${arch}.zip"; \
    unzip -o /tmp/loki.zip -d /tmp/loki; \
    mkdir -p /out/loki; \
    mv /tmp/loki/loki-linux-${arch} /out/loki/loki; \
    chmod +x /out/loki/loki
    # WHAT: extract + make executable
    # WHY: Loki distributed as zip


#####################################################################
# Stage 2 — Runtime image (final container)
#####################################################################

FROM debian:bookworm-slim AS runtime
# WHAT: final lightweight OS
# WHY: minimize runtime image size

ARG GRAFANA_VERSION

LABEL org.opencontainers.image.title="claude-code-observability (all-in-one)" \
      org.opencontainers.image.description="OTel Collector + Prometheus + Loki + Grafana + nginx in one container" \
      org.opencontainers.image.source="https://github.com/trongnguyenbinh/Claude-Code-Observability"
# WHAT: metadata for container registry
# WHY: traceability + documentation

ENV DEBIAN_FRONTEND=noninteractive
# WHAT: disable interactive prompts
# WHY: avoid hanging during apt install


# --- Install runtime dependencies ---
RUN set -eux; \
    apt-get update; \
    apt-get install -y --no-install-recommends \
      supervisor \        # process manager (run multiple services)
      nginx \             # reverse proxy + ingest gateway
      gettext-base \      # envsubst for template rendering
      openssl \           # token generation / TLS support
      jq \                # JSON processing
      curl \              # API calls / health checks
      ca-certificates \
      tzdata \            # correct timestamps
      bash; \
    rm -rf /var/lib/apt/lists/*; \
    \
    rm -f /etc/nginx/sites-enabled/default
    # WHAT: remove default nginx config
    # WHY: replace with custom configuration


# --- Copy binaries from previous stages ---
COPY --from=otelcol /otelcol-contrib /usr/local/bin/otelcol-contrib
# WHAT: OTel Collector binary

COPY --from=fetch /out/prometheus/prometheus /usr/local/bin/prometheus
COPY --from=fetch /out/prometheus/promtool   /usr/local/bin/promtool
# WHAT: Prometheus + promtool

COPY --from=fetch /out/loki/loki /usr/local/bin/loki
# WHAT: Loki binary


# --- Grafana setup ---
COPY --from=grafana /usr/share/grafana /usr/share/grafana
# WHAT: full Grafana install directory
# WHY: includes plugins + UI assets

RUN ln -sf /usr/share/grafana/bin/grafana /usr/local/bin/grafana \
 && ln -sf /usr/share/grafana/bin/grafana-server /usr/local/bin/grafana-server
# WHAT: symlinks binaries into PATH
# WHY: allow direct execution


# --- Config templates ---
COPY allinone/templates/ /etc/ccobs/templates/
# WHAT: templated configs (${ENV})
# WHY: runtime environment injection

COPY otel-collector/config.yaml /etc/ccobs/static/otel-config.yaml
COPY prometheus/prometheus.yml  /etc/ccobs/static/prometheus.yml
COPY loki/loki-config.yaml      /etc/ccobs/static/loki-config.yaml
# WHAT: static configs

COPY grafana/provisioning/ /etc/grafana/provisioning/
# WHAT: Grafana provisioning (datasources, dashboards)

COPY docs/claude-code-metrics-dashboard.json \
     /var/lib/grafana/dashboards/claude-code-metrics.json
# WHAT: prebuilt dashboard
# WHY: ready UI on first startup


# --- Management tools ---
COPY allinone/ccobs            /usr/local/bin/ccobs
# WHAT: custom CLI

COPY allinone/supervisord.conf /etc/supervisor/conf.d/ccobs.conf
# WHAT: supervisor config (defines services)

COPY allinone/entrypoint.sh    /usr/local/bin/entrypoint.sh
# WHAT: startup script (init + config rendering)

RUN chmod +x /usr/local/bin/ccobs /usr/local/bin/entrypoint.sh
# WHAT: make scripts executable


# --- Data directories (persisted via volumes) ---
RUN set -eux; \
    mkdir -p /data/prometheus /data/loki /data/grafana \
             /var/lib/grafana/dashboards /var/log/ccobs /run/ccobs; \
    chmod -R 0777 /data /var/lib/grafana /var/log/ccobs /run/ccobs
# WHAT: storage directories
# WHY: persist metrics, logs, dashboards
# NOTE: 0777 simplifies permissions (less secure)


# --- Ports ---
EXPOSE 8080 3001 9090
# 8080 → nginx ingest (OTLP HTTP)
# 3001 → Grafana UI via nginx
# 9090 → Prometheus


# --- Startup ---
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
# WHAT: initialization script
# HOW:
#   - render templates (envsubst)
#   - prepare configs

CMD ["supervisor"]
# WHAT: start all services via supervisord
```

***

# ✅ Final mental model (important)

```
ENTRYPOINT → entrypoint.sh
          → supervisord
                ├── nginx
                ├── otelcol
                ├── prometheus
                ├── loki
                └── grafana
```

***

# ✅ Key Takeaways

* **Multi-stage build**
  * extract binaries → small final image
* **Single container**
  * easy deploy (`docker run`)
* **supervisord**
  * enables multi-process architecture
* **templating**
  * dynamic config via env variables

***

# Source
https://github.com/trongnguyenbinh/Claude-Code-Observability/tree/main/allinone
