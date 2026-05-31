# 1. install Claude
curl -fsSL https://claude.ai/install.sh | bash

# 2. create project
mkdir demo && cd demo
claude init

# 3. (optional) setup uv
uv init

# 4. create skill
mkdir -p .claude/skills/test-skill
touch .claude/skills/test-skill/SKILL.md

# 5. run project
claude

# 6. debug issues
claude --debug
