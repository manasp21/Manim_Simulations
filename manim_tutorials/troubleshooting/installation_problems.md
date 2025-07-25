# Installation Problems

This guide addresses common installation issues with Manim and their solutions.

## Problem: "manim: command not found"

### Description
After installing Manim, you receive an error saying "manim: command not found" when trying to run Manim commands.

### Common Causes
1. Manim was installed in a virtual environment that is not activated
2. The Python scripts directory is not in your PATH
3. Installation was incomplete or failed

### Solutions

#### Solution 1: Activate Virtual Environment
If you installed Manim in a virtual environment, make sure it's activated:

```bash
# Activate the virtual environment
source venv/bin/activate  # On Linux/macOS
# or
venv\Scripts\activate     # On Windows

# Then try running Manim
manim --version
```

#### Solution 2: Use Python Module Syntax
If the command is not found, try running Manim as a Python module:

```bash
python -m manim --version
```

#### Solution 3: Add Python Scripts to PATH
Add the Python scripts directory to your PATH:

```bash
# Find the scripts directory
python -m site --user-base
# Add /bin (Linux/macOS) or \Scripts (Windows) to this path to your PATH
```

## Problem: Installation Fails with "Microsoft Visual C++ 14.0 is required"

### Description
On Windows, installation fails with an error about missing Microsoft Visual C++ 14.0.

### Solution
Install Microsoft C++ Build Tools:

1. Download and install "Microsoft C++ Build Tools" from the official Microsoft website
2. During installation, make sure to select "C++ build tools" workload
3. Try installing Manim again:

```bash
pip install manim
```

## Problem: "No module named manimpango" or Similar Errors

### Description
Installation fails with errors related to missing dependencies like manimpango, cairo, or pango.

### Solutions

#### For macOS:
```bash
# Install dependencies using Homebrew
brew install cairo pkg-config ffmpeg pango

# Then install Manim
pip install manim
```

#### For Ubuntu/Debian:
```bash
# Install dependencies
sudo apt update
sudo apt install build-essential python3-dev libcairo2-dev libpango1.0-dev ffmpeg

# Then install Manim
pip install manim
```

#### For Windows:
1. Install GTK3 runtime from https://github.com/tschoonj/GTK3-runtime
2. Make sure to add GTK3 to your PATH during installation
3. Install Manim:

```bash
pip install manim
```

## Problem: "DLL load failed" on Windows

### Description
On Windows, you get an error like "DLL load failed while importing _cairo: The specified module could not be found."

### Solution
This is usually caused by missing or incompatible GTK3 libraries:

1. Download and install the GTK3 runtime from https://github.com/tschoonj/GTK3-runtime
2. During installation, make sure to select "Add to PATH"
3. Restart your terminal/command prompt
4. Try installing Manim again:

```bash
pip install manim
```

## Problem: Slow Installation or Timeout

### Description
Installation takes a very long time or times out.

### Solutions

#### Solution 1: Use a Different PyPI Mirror
```bash
pip install manim -i https://pypi.douban.com/simple/
```

#### Solution 2: Increase Timeout
```bash
pip install manim --timeout 1000
```

#### Solution 3: Install Pre-compiled Wheels
```bash
pip install manim --only-binary=all
```

## Prevention Tips

1. Always use a virtual environment for Python projects
2. Keep your system dependencies updated
3. Check the official Manim documentation for the latest installation instructions
4. If you're having persistent issues, try using the conda installation method:

```bash
conda install -c conda-forge manim
```

## Problem: "No module named 'ipywidgets'"

### Description
When trying to run interactive tutorials, you get an error: `ModuleNotFoundError: No module named 'ipywidgets'`

### Common Causes
1. ipywidgets is not installed
2. Jupyter notebook extensions are not enabled
3. Using an incompatible version of ipywidgets

### Solutions

#### Solution 1: Install ipywidgets
```bash
pip install ipywidgets
```

#### Solution 2: Enable Jupyter Extensions
```bash
jupyter nbextension enable --py widgetsnbextension
```

#### Solution 3: For JupyterLab Users
```bash
jupyter labextension install @jupyter-widgets/jupyterlab-manager
```

#### Solution 4: Install All Tutorial Dependencies
```bash
pip install -r requirements.txt
```

## Additional Resources

- [Official Manim Installation Guide](https://docs.manim.community/en/stable/installation.html)
- [Manim GitHub Issues](https://github.com/ManimCommunity/manim/issues)
- [Python Virtual Environments Guide](https://docs.python.org/3/tutorial/venv.html)