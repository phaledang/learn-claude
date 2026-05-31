# Introduction to Agent Skills – Troubleshooting Skills

## Source
https://anthropic.skilljar.com/introduction-to-agent-skills/434530

---

# 1. Summary

This lesson explains how to troubleshoot issues when Claude skills do not work as expected.

Most problems fall into four common categories:

- Skill does not trigger
- Skill does not load
- Wrong skill is used
- Skill fails at runtime

A systematic approach is recommended:
- Start with validation (structure issues)
- Diagnose behavior (triggering, loading)
- Resolve conflicts or runtime problems

Key tools:
- Skills validator → check structure
- `claude --debug` → diagnose loading/runtime issues

---

# 2. Troubleshooting Categories

## 2.1 Skill Does Not Trigger
**Cause:** Description does not match user request

**Fix:**
- Add trigger phrases
- Align description with real user wording
- Test variations

---

## 2.2 Skill Does Not Load
**Fix:**
- Ensure structure:
  ```
  .claude/skills/<skill-name>/SKILL.md
  ```
- Run:
  ```bash
  claude --debug
  ```

---

## 2.3 Wrong Skill Gets Used
**Fix:**
- Make descriptions distinct

---

## 2.4 Skill Priority Conflict
**Priority (high → low):**
1. Enterprise
2. Personal
3. Project
4. Plugin

---

## 2.5 Runtime Errors
**Fix:**
```bash
uv add <package>
chmod +x script.sh
```

---

# 3. Debugging Tools

## Skills Validator
- Detects structural issues

## Debug Command
```bash
claude --debug
```

---

# 4. Checklist

- Not triggering → fix description
- Not loading → fix structure
- Wrong skill → adjust descriptions
- Runtime error → install dependencies

---

# 5. Key Takeaways

- Classify issue type first
- Use validator and debug tools
- Keep descriptions clear
- Follow strict structure
- Ensure environment is correct

---

# 6. Practical Workflow

```bash
claude
claude --debug
uv add <package>
```

---

# 7. Final Insight

Most problems are predictable and easy to fix when approached systematically.
