## What is pip and how packages are installed

`pip` is the standard package manager for Python. It allows you to install, upgrade, and remove Python packages from the Python Package Index (PyPI) and other indexes. Pip makes it easy to add new functionality to your Python projects by installing libraries and tools published by the community.

**Basic installation example:**
```bash
pip install requests
```
This command installs the `requests` package, which lets you make HTTP requests easily in Python.

**Upgrading a package:**
```bash
pip install --upgrade numpy
```

**Uninstalling a package:**
```bash
pip uninstall pandas
```

**Installing a specific version:**
```bash
pip install django==3.2.5
```

Packages are usually installed from PyPI, but you can also install from local files, GitHub, or other sources.

## What is a virtual environment in Python?

A virtual environment is an isolated workspace for Python projects. It creates a self-contained directory that contains its own Python interpreter and installed packages, separate from the global Python installation. This isolation ensures that dependencies required for one project do not affect other projects or the system Python.

For example, if you are working on multiple projects that require different versions of the same package, virtual environments prevent version conflicts and make your development process more reliable.

## Why is it required? (Real life example)

Suppose you have two projects:

- Project A needs `Django==3.2`
- Project B needs `Django==4.0`

If you install both versions globally, one will overwrite the other, causing errors. With virtual environments, you can create separate environments for each project:

```bash
python3 -m venv envA  # For Project A
python3 -m venv envB  # For Project B
```
Each environment will have its own set of packages, so you can work on both projects without conflicts.

## How to create a virtual environment

To create a virtual environment, use the `venv` module. Replace `myenv` with your desired environment name.

**Windows:**
```cmd
python -m venv myenv
```

**macOS/Linux:**
```bash
python3 -m venv myenv
```

This creates a folder called `myenv` containing the isolated Python environment.

## How to activate the virtual environment

After creating the environment, you need to activate it so your terminal uses the environment's Python and packages.

**Windows (Command Prompt):**
```cmd
myenv\Scripts\activate
```

**Windows (PowerShell):**
```powershell
.\myenv\Scripts\Activate.ps1
```

**macOS/Linux:**
```bash
source myenv/bin/activate
```

Once activated, your prompt will usually change to show the environment name, e.g., `(myenv)`.

## How to deactivate

To exit the virtual environment and return to your system Python, simply run:
```bash
deactivate
```
This works on all platforms. Your prompt will return to normal, and your terminal will use the global Python again.

## How to create a venv with a specific Python version

You can create a virtual environment with a specific Python version by specifying the path to the desired Python executable.

**macOS/Linux:**
```bash
python3.9 -m venv myenv
```
This uses Python 3.9 to create the environment. Make sure Python 3.9 is installed on your system.

**Windows:**
```cmd
py -3.9 -m venv myenv
```
The `py` launcher lets you select the Python version if you have multiple installed.

## Details about pip freeze

`pip freeze` lists all installed packages and their versions in the current environment. This is useful for sharing your environment setup with others or for deploying your project.

**Example output:**
```
Django==4.0.0
requests==2.26.0
numpy==1.21.2
```

**Save to requirements.txt:**
```bash
pip freeze > requirements.txt
```
You can then use this file to recreate the environment elsewhere:
```bash
pip install -r requirements.txt
```

## How to configure custom index URLs

Sometimes you may need to install packages from a private or custom package index (other than PyPI).

**Install from a custom index:**
```bash
pip install --index-url https://custom.index/simple package_name
```

**Add extra index (fallback to PyPI if not found):**
```bash
pip install --extra-index-url https://custom.index/simple package_name
```

**Persistent configuration:**
- On Linux/macOS, edit or create `~/.pip/pip.conf`:
	```ini
	[global]
	index-url = https://custom.index/simple
	```
- On Windows, edit or create `%APPDATA%\pip\pip.ini`:
	```ini
	[global]
	index-url = https://custom.index/simple
	```

This is useful for organizations hosting their own package repositories or for accessing packages not available on PyPI.
