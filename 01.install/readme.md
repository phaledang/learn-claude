## Installing Ollama on Ubuntu

Ollama enables you to run large language models locally on Ubuntu, offering privacy, control, and offline AI inference capabilities. Follow these steps to install and verify Ollama on your system.

* Update your system’s package list and upgrade installed packages by running:
  
  ```
  sudo apt update && sudo apt upgrade -y.
  ```
* Install Ollama using the official installation script:
  
  ```
  curl -fsSL https://ollama.com/install.sh | sh.
 ```
Wait for the script to complete; it will install the Ollama binary, create a dedicated user, and set up a systemd service.

Verify the installation by checking the version: ollama -v A successful output will display the installed version number.

(Optional) Download a model, for example Llama 2, by running: ollama pull llama2.

Run the downloaded model interactively with: ollama run llama2 Type /bye or press Ctrl+D to exit.

List all installed models using: ollama list.

If needed, manually start the Ollama service with: ollama serve.

(Optional) For GPU acceleration, ensure NVIDIA drivers are installed: sudo ubuntu-drivers autoinstall Also install the NVIDIA Container Toolkit if required.
