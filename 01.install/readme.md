## S𝗲𝘁𝘂𝗽 :
1. Install Ollama
2. Pull a coding model
```
ollama pull qwen2.5-coder
```
3. Install Claude Code
```
npm install -g @anthropic-ai/claude-code
```
5. Point to localhost
```
export ANTHROPIC_AUTH_TOKEN=ollama
export ANTHROPIC_BASE_URL=http://localhost:11434
```
6. Run it
```
claude --model qwen2.5-coder
```
## Installing Ollama on Ubuntu

Ollama enables you to run large language models locally on Ubuntu, offering privacy, control, and offline AI inference capabilities. Follow these steps to install and verify Ollama on your system.

* Update your system’s package list and upgrade installed packages by running:
  
```
sudo apt update && sudo apt upgrade -y.
```
* Install Ollama using the official installation script:
  
```
curl -fsSL https://ollama.com/install.sh | sh
```
Wait for the script to complete; it will install the Ollama binary, create a dedicated user, and set up a systemd service.

Verify the installation by checking the version: ollama -v A successful output will display the installed version number.
## Some error:
 This version requires zstd for extraction. Please install zstd and try again:
  - Debian/Ubuntu: sudo apt-get install zstd
  - RHEL/CentOS/Fedora: sudo dnf install zstd
  - Arch: sudo pacman -S zstd

The error means the installer is trying to extract a `.tar.zst` (Zstandard compressed) file, but the **zstd** utility is not installed.

### Check your Linux distribution

#### Ubuntu / Debian / WSL2 Ubuntu

```bash
sudo apt update
sudo apt install -y zstd
```

Verify:

```bash
zstd --version
```

***

#### Fedora / RHEL / Rocky Linux

```bash
sudo dnf install -y zstd
```

***

#### Arch Linux

```bash
sudo pacman -S zstd
```

***

### If you are using WSL2 Ubuntu

This is the most likely fix:

```bash
sudo apt update
sudo apt install -y zstd
```

Then rerun your installation command.

***

### If the error still occurs

Check whether `zstd` is in PATH:

```bash
which zstd
```

Expected:

```text
/usr/bin/zstd
```

If not found:

```bash
sudo apt reinstall zstd
```

***

### For Claude Code / Claude Desktop on Linux

Many installation scripts also require:

```bash
sudo apt install -y zstd curl wget tar unzip build-essential
```

This avoids common dependency failures during installation.

Can you paste the **exact command** you were running when this error appeared? I can identify the next dependency that may be missing.


## use model
* Download a model: 

```
 ollama pull llama2.
```
* Run the downloaded model interactively with: ollama run llama2 Type /bye or press Ctrl+D to exit.

* List all installed models using:
```
ollama list.
```
* Manually start the Ollama service:
```ollama serve
```

(Optional) For GPU acceleration, ensure NVIDIA drivers are installed: sudo ubuntu-drivers autoinstall Also install the NVIDIA Container Toolkit if required.
