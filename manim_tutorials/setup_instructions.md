# Manim Setup Instructions

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## Installation

### Option 1: Using pip with requirements.txt (Recommended)

For the tutorials in this repository, we recommend installing all dependencies using the provided requirements.txt file:

```bash
pip install -r requirements.txt
```

This will install Manim along with all required dependencies including Jupyter and ipywidgets for interactive tutorials.

### Option 2: Using pip for Manim only

```bash
pip install manim
```

### Option 3: Using conda

```bash
conda install -c conda-forge manim
```

### Option 4: Installing from source

```bash
git clone https://github.com/ManimCommunity/manim.git
cd manim
pip install -e .
```

## System Dependencies

### Windows

On Windows, you need to install:

- [FFmpeg](https://ffmpeg.org/download.html)
- [dvisvgm](https://dvisvgm.de/Downloads/)
- A LaTeX distribution like [TeX Live](https://www.tug.org/texlive/) or [MiKTeX](https://miktex.org/)

### macOS

On macOS, you can install the required dependencies using Homebrew:

```bash
brew install cairo ffmpeg pkg-config dvisvgm
```

You'll also need a LaTeX distribution like [MacTeX](http://www.tug.org/mactex/).

### Linux (Ubuntu/Debian)

On Ubuntu/Debian, you can install the required dependencies using apt:

```bash
sudo apt update
sudo apt install build-essential python3-dev libcairo2-dev libpango1.0-dev ffmpeg dvisvgm texlive texlive-latex-extra texlive-fonts-extra texlive-latex-recommended texlive-science tipa
```

## Jupyter Notebook Setup for Interactive Tutorials

Some tutorials in this repository are designed to work with Jupyter notebooks and interactive widgets:

1. Install Jupyter and ipywidgets (included in requirements.txt):

```bash
pip install jupyter ipywidgets
```

2. Enable the widgets extension:

```bash
jupyter nbextension enable --py widgetsnbextension
```

3. For JupyterLab users, also install the JupyterLab extension:

```bash
jupyter labextension install @jupyter-widgets/jupyterlab-manager
```

## Verification

To verify that Manim is installed correctly, run:

```bash
manim --version
```

To verify that all tutorial dependencies are installed, try importing ipywidgets:

```bash
python -c "import ipywidgets; print('ipywidgets installed successfully')"
```

## Troubleshooting Common Installation Issues

### Issue: Missing System Dependencies

**Symptom**: Error messages about missing libraries or executables
**Solution**: Install the required system dependencies for your operating system as listed above

### Issue: LaTeX Errors

**Symptom**: Errors related to LaTeX compilation when rendering text
**Solution**: Ensure you have a complete LaTeX distribution installed

### Issue: FFmpeg Not Found

**Symptom**: Error messages about FFmpeg not being found
**Solution**: Install FFmpeg and ensure it's in your system PATH

### Issue: ipywidgets Import Error

**Symptom**: `ModuleNotFoundError: No module named 'ipywidgets'`
**Solution**: Install ipywidgets:

```bash
pip install ipywidgets
```

Then enable the extension:

```bash
jupyter nbextension enable --py widgetsnbextension
```

### Issue: Jupyter Notebook Widgets Not Displaying

**Symptom**: Interactive widgets don't appear in Jupyter notebooks
**Solution**: Ensure the widgets extension is enabled:

```bash
jupyter nbextension list
```

Look for `jupyter-js-widgets/extension enabled` in the output.

## Running Your First Scene

Create a file called `scene.py` with the following content:

```python
from manim import *

class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        square.flip(RIGHT)
        square.rotate(-3 * TAU / 8)
        circle.set_fill(PINK, opacity=0.5)

        self.play(Create(square))
        self.play(Transform(square, circle))
        self.play(FadeOut(square))
```

Then render the scene:

```bash
manim -pql scene.py SquareToCircle
```

This will render the animation in low quality and play it automatically.