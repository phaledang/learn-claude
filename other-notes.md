# Summary
Claude Code = Runtime

CLAUDE.md = policy

Skills = workflows

## To work effectively:

Install → claude

Init → claude init

Add uv → clean env

Create skill → .claude/skills/.../SKILL.md

Run → claude

Debug → claude --debug

uv = environment 

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
