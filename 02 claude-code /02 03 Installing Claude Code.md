# Installing Claude Code

## Summary
Page: https://anthropic.skilljar.com/claude-code-101/469790

- Claude Code supports multiple environments:
  - Terminal
  - VS Code
  - JetBrains IDEs
  - Desktop
  - Web (GitHub only)
- Terminal installation:
  - macOS/Linux: curl or Homebrew (no auto-update)
  - Windows: PowerShell, CMD, winget (no auto-update)
- Run `claude` after install
- Setup includes:
  - Theme selection
  - Account login (Pro / Max / Enterprise / API key)
- Access scope:
  - Current directory + subfolders
- IDE support:
  - VS Code extension (Anthropic)
  - JetBrains plugin
- Platform comparison:
  - Terminal → latest features
  - IDE → integrated coding experience
  - Desktop → background usage
  - Web → GitHub repo only

---
## Install

### Ubuntu / Linux 
```
curl -fsSL https://claude.ai/install.sh | bash

```
### MacOS

#### native installer
```
curl -fsSL https://claude.ai/install.sh | bash
```
#### Homebrew 
```
brew install --cask claude-code
```
### Windows

#### Powershell
```
irm https://claude.ai/install.ps1 | iex
```
#### CMD
```
curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd
```
#### WinGet(package manager)
```
winget install Anthropic.ClaudeCode

winget upgrade Anthropic.ClaudeCode
```


## Reload shell (if needed)
```
source ~/.bashrc
```
## Verify install
```
claude --version

```

## Start claude
```
mkdir demo-claude
cd demo-claude
claude
```
Claude now has access to this folder (important concept from your training)

## Q&A
**Q: What environments can Claude Code run on?**  
A: Terminal, VS Code, JetBrains IDEs, Desktop app, and Web (GitHub repos).

**Q: How do you start Claude Code after installation?**  
A: Navigate to a project folder and run `claude`.

**Q: What happens during first-time setup?**  
A: You select theme and sign in using Claude account or API key.

**Q: What scope does Claude Code have in a project?**  
A: It accesses the current directory and all subfolders.

**Q: What is a limitation of Homebrew and winget installs?**  
A: They do not support auto-updates.

**Q: How does Claude Code work in VS Code?**  
A: Through an Anthropic extension that integrates into the editor.

**Q: What is special about the web version?**  
A: It only works with GitHub repositories.

---

## Quiz

### 1. Where can Claude Code run?
- [ ] A. Only in terminal
- [x] B. Terminal, IDEs, Desktop, Web
- [ ] C. Only in browser
- [ ] D. Only in cloud

### 2. What command starts Claude Code?
- [ ] A. start claude
- [x] B. claude
- [ ] C. run claude
- [ ] D. code start

### 3. What does Claude Code access?
- [ ] A. Entire system
- [ ] B. Only one file
- [x] C. Current directory and subfolders
- [ ] D. Internet automatically

### 4. Which method provides latest features first?
- [x] A. Terminal
- [ ] B. Desktop
- [ ] C. Web
- [ ] D. IDE

### 5. What is required for login?
- [ ] A. GitHub account
- [x] B. Claude account or API key
- [ ] C. Google account
- [ ] D. None

---

## Key Takeaways

- Claude Code is multi-platform and flexible
- Terminal provides latest features
- IDE gives best developer experience
- Runs within a project directory context
- Web version is GitHub only
- Installation method affects auto-updates

---

## References

- https://anthropic.skilljar.com/claude-code-101/469790
- https://support.claude.com/
- https://claude.ai/code
