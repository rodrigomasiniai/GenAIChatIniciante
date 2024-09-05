To change the Python version **after the container is already running** inside a GitHub Codespace, you can follow these steps:

### Step 1: Check Available Python Versions
First, check which Python versions are installed on the Codespace.

```bash
pyenv versions
```

This will list the versions available for you to switch between, including Python 3.11 if it has been pre-installed.

### Step 2: Install Python 3.11 (If Not Already Installed)
If Python 3.11 is not installed, you can install it using `pyenv`:

1. Install `pyenv` if not available:
   ```bash
   curl https://pyenv.run | bash
   ```
   Then add `pyenv` to your shell profile:
   ```bash
   echo 'export PATH="$HOME/.pyenv/bin:$PATH"' >> ~/.bashrc
   echo 'eval "$(pyenv init --path)"' >> ~/.bashrc
   source ~/.bashrc
   ```

2. Install Python 3.11:
   ```bash
   pyenv install 3.11.0
   ```

### Step 3: Set Python 3.11 as the Global or Local Version
Once Python 3.11 is installed, you can switch to it either globally or locally within the project:

- **To set Python 3.11 globally** (for the entire Codespace):
  ```bash
  pyenv global 3.11.0
  ```

- **To set Python 3.11 locally** (only for the current project):
  ```bash
  pyenv local 3.11.0
  ```

### Step 4: Verify the Python Version
After switching, verify that the active Python version is now 3.11:

```bash
python --version
```

This command should output Python 3.11.0.

### Step 5: Reconfigure Your Environment
If you're using virtual environments, you may need to update your virtual environment to use Python 3.11:

1. Deactivate the current virtual environment:
   ```bash
   deactivate
   ```

2. Create a new virtual environment with Python 3.11:
   ```bash
   python -m venv venv
   ```

3. Activate the new virtual environment:
   ```bash
   source venv/bin/activate
   ```