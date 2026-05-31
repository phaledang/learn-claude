# Use uv
### Python Package Management with uv
```
Use uv exclusively.

- Install: uv add <package>
- Remove: uv remove <package>
- Run: uv run script.py
```
# Skill folder structure
```
~/.claude/skills → global
.claude/skills → project

my-project/
  .claude/
    skills/
      troubleshooting/
        SKILL.md

```
# Sample Install skills from marketplace
```
/plugin marketplace add anthropics/skills

/plugin install example-skills@anthropic-agent-skills
```
# Sample manual install skill
```
mkdir -p ~/.claude/skills
git clone <repo> ~/.claude/skills/<skill-name>
```
