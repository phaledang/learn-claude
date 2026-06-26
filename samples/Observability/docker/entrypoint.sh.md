# `entrypoint.sh` with:

* ✅ **Summary (what / why / how)**
* ✅ **Inline comments (what / why / how per section)**
* ✅ Focus on **runtime + DevOps + container orchestration patterns**

***

# ✅ Summary

### What

* Bootstraps an **all-in-one observability container**
* Prepares and wires:
  * OpenTelemetry (OTel)
  * Prometheus
  * Loki
  * Grafana
  * Nginx (ingest + proxy)
* Delegates execution to **supervisord or CLI (`ccobs`)**

### Why

* Ensure **single image = fully working stack**
* Avoid manual config by:
  * Using **environment variables**
  * Rendering configs dynamically
* Support:
  * Local dev (no TLS)
  * Production (TLS, allowlist, custom endpoints)

### How

* Apply defaults → create runtime dirs
* Generate configs via `envsubst`
* Wire nginx + token auth
* Validate config early
* Start services via `supervisord`

***

# ✅ Annotated Script (What / Why / How inline)

```bash
#!/usr/bin/env bash

# WHAT: Entrypoint script for container startup
# WHY: Centralize initialization for all services in the image
# HOW: Prepare configs, validate, then launch process manager

set -euo pipefail
# WHAT: Strict bash mode
# WHY: Prevent silent failures (best practice for production scripts)
# HOW:
#   -e: exit on error
#   -u: fail on undefined vars
#   -o pipefail: fail if any pipe fails


# WHAT: Allow CLI passthrough mode
# WHY: Enable running `ccobs` management commands instead of full stack
# HOW: If first argument == ccobs → exec CLI directly
if [ "${1:-}" = "ccobs" ]; then
  shift
  exec /usr/local/bin/ccobs "$@"
fi


##############################################################################
# DEFAULTS (LOCAL-FIRST MODE)
##############################################################################

# WHAT: Define runtime defaults via environment variables
# WHY: Simplify first run (no config required)
# HOW: Use bash parameter expansion with fallback values

export OTEL_DOMAIN="${OTEL_DOMAIN:-_}"    
# "_" → nginx wildcard (match any host)

export GRAFANA_DOMAIN="${GRAFANA_DOMAIN:-_}"

export INGEST_PORT="${INGEST_PORT:-8080}"
# WHAT: OTLP ingest port
# WHY: Entry point for telemetry ingestion

export GRAFANA_PORT="${GRAFANA_PORT:-3001}"
# WHY: Avoid port conflict (Grafana internal uses 3000)

export OFFICE_IP="${OFFICE_IP:-}"
# WHAT: Optional allowlist IP
# WHY: Restrict Grafana access

export TLS_ENABLED="${TLS_ENABLED:-false}"
export TLS_CERT="${TLS_CERT:-/certs/fullchain.pem}"
export TLS_KEY="${TLS_KEY:-/certs/privkey.pem}"

export GF_ADMIN_USER="${GF_ADMIN_USER:-admin}"
export GF_ADMIN_PASSWORD="${GF_ADMIN_PASSWORD:-changeme}"

export GF_ROOT_URL="${GF_ROOT_URL:-http://localhost:${GRAFANA_PORT}/}"
# WHAT: Grafana base URL
# WHY: Required for correct redirects + links

export PROM_RETENTION="${PROM_RETENTION:-90d}"
export LOKI_RETENTION="${LOKI_RETENTION:-90d}"
# WHAT: Data retention policy
# WHY: Control storage usage

export OTEL_PUBLIC_ENDPOINT="${OTEL_PUBLIC_ENDPOINT:-http://localhost:${INGEST_PORT}}"
# WHAT: Public endpoint exposed to clients
# WHY: Used by CLI to generate install snippets


##############################################################################
# DIRECTORY SETUP
##############################################################################

TPL=/etc/ccobs/templates
RUNTIME=/etc/ccobs/runtime
TOKENS_DIR="${CCOBS_TOKENS_DIR:-/data/tokens}"

# WHAT: Ensure required directories exist
# WHY: Prevent runtime failure due to missing paths
# HOW: mkdir -p for idempotency
mkdir -p "$RUNTIME" "$TOKENS_DIR" /etc/nginx/conf.d \
         /data/prometheus /data/loki /data/grafana/plugins \
         /var/log/ccobs /run/ccobs


##############################################################################
# TOKEN MAP (PERSISTED AUTH)
##############################################################################

TOKEN_MAP="$TOKENS_DIR/00-otel-tokens.conf"

# WHAT: Initialize token map if not exists
# WHY: Provide persistent authentication for ingest endpoint
# HOW: Copy default template → persistent volume
if [ ! -f "$TOKEN_MAP" ]; then
  cp "$TPL/00-otel-tokens.conf" "$TOKEN_MAP"
fi

# WHAT: Inject token map into nginx config
# WHY: nginx handles token-based access control
cp "$TOKEN_MAP" /etc/nginx/conf.d/00-otel-tokens.conf


##############################################################################
# CONFIG RENDERING (CORE MECHANISM)
##############################################################################

# WHAT: Template rendering helper
# WHY: Convert *.tmpl → runtime configs with env vars
# HOW: envsubst replaces variables
render() { envsubst "$2" < "$1" > "$3"; }


# WHAT: Controlled variable substitution
# WHY: Avoid overriding nginx internal variables ($host, $uri, ...)
NGINX_VARS='${OTEL_DOMAIN} ${GRAFANA_DOMAIN} ${INGEST_PORT} ${GRAFANA_PORT} ${TLS_CERT} ${TLS_KEY} ${OFFICE_IP_ALLOW}'
GF_VARS='${GF_ROOT_URL} ${GF_ADMIN_USER} ${GF_ADMIN_PASSWORD}'
LOKI_VARS='${LOKI_RETENTION}'


# WHAT: Copy base configs (no substitution required)
cp "$TPL/otel-config.yaml.tmpl" "$RUNTIME/otel-config.yaml"
cp "$TPL/prometheus.yml.tmpl" "$RUNTIME/prometheus.yml"

# WHAT: Render Loki config (uses retention variable)
render "$TPL/loki-config.yaml.tmpl" "$LOKI_VARS" "$RUNTIME/loki-config.yaml"


##############################################################################
# GRAFANA CONFIG
##############################################################################

# WHAT: Render grafana.ini
# WHY: Inject admin credentials + root_url dynamically
render "$TPL/grafana.ini.tmpl" "$GF_VARS" "$RUNTIME/grafana.ini"

# WHAT: Install datasource config
# WHY: Connect Grafana to local services
cp "$TPL/datasources.yaml.tmpl" \
   /etc/grafana/provisioning/datasources/datasources.yaml


##############################################################################
# NGINX CONFIG
##############################################################################

# WHAT: Conditional allowlist
# WHY: Restrict access only when OFFICE_IP provided
if [ -n "$OFFICE_IP" ]; then
  export OFFICE_IP_ALLOW="allow ${OFFICE_IP}; deny all;"
else
  export OFFICE_IP_ALLOW=""
fi

# WHAT: Render Grafana reverse proxy config
render "$TPL/nginx-grafana.conf.tmpl" "$NGINX_VARS" \
       /etc/nginx/conf.d/grafana.conf


# WHAT: Render ingest endpoint config
# WHY: Support TLS and non-TLS modes dynamically
if [ "$TLS_ENABLED" = "true" ]; then

  # WHAT: Validate TLS cert existence
  # WHY: Fail fast instead of runtime nginx error
  if [ ! -f "$TLS_CERT" ] || [ ! -f "$TLS_KEY" ]; then
    echo "[entrypoint] TLS_ENABLED=true but cert/key not found at $TLS_CERT / $TLS_KEY" >&2
    exit 1
  fi

  render "$TPL/nginx-ingest-tls.conf.tmpl" "$NGINX_VARS" \
         /etc/nginx/conf.d/ingest.conf
else
  render "$TPL/nginx-ingest.conf.tmpl" "$NGINX_VARS" \
         /etc/nginx/conf.d/ingest.conf
fi


##############################################################################
# CLI ENV EXPORT (FOR docker exec)
##############################################################################

# WHAT: Persist runtime env for CLI usage
# WHY: Allow external commands to discover runtime config
cat > /etc/ccobs/env <<EOF
OTEL_PUBLIC_ENDPOINT=${OTEL_PUBLIC_ENDPOINT}
OTEL_TOKEN_MAP=${TOKEN_MAP}
NGINX_CONF_TOKEN_MAP=/etc/nginx/conf.d/00-otel-tokens.conf
EOF


##############################################################################
# VALIDATION
##############################################################################

# WHAT: Validate nginx config
# WHY: Fail-fast principle (DevOps best practice)
# HOW: nginx -t exits non-zero if invalid
nginx -t

echo "[entrypoint] config rendered. ingest=:${INGEST_PORT} grafana=:${GRAFANA_PORT} tls=${TLS_ENABLED}"


##############################################################################
# START SERVICES
##############################################################################

# WHAT: Default entrypoint = supervisord
# WHY:
#   - Manage multiple processes (nginx, grafana, loki, prom, otel)
#   - Ensure restart policies
if [ "${1:-supervisor}" = "supervisor" ]; then
  exec /usr/bin/supervisord -c /etc/supervisor/conf.d/ccobs.conf
else
  # WHAT: Custom command passthrough
  # WHY: Allow override for debugging / custom runs
  exec "$@"
fi
```

***

# ✅ Key Design Patterns (Important)

* **Env-driven configuration**
  * No hardcoded values → portable across environments

* **Template rendering (envsubst)**
  * Lightweight alternative to Helm / Jinja

* **Fail-fast validation**
  * `nginx -t` prevents delayed runtime errors

* **Process supervision**
  * Single container but multiple services (via supervisord)

* **Security built-in**
  * Token-based ingest
  * Optional IP allowlist
  * Optional TLS

***

If needed, can generate **architecture diagram (container → nginx → services)** or map this to **Kubernetes (InitContainer + ConfigMap + Sidecar)**.
