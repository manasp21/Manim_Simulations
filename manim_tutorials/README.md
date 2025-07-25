# Manim Tutorial Series

Welcome to the comprehensive Manim tutorial series! This repository contains tutorials and examples for learning Manim, a powerful mathematical animation engine.

## Directory Structure

- `beginner/` - Basic concepts and simple animations
- `intermediate/` - More complex animations and techniques
- `advanced/` - Advanced features and custom implementations
- `projects/` - Complete project examples
- `troubleshooting/` - Common issues and solutions
- `resources/` - Additional learning materials
- `utils/` - Utility functions and helper scripts

## Installation Requirements

Before running the tutorials, ensure you have installed all required dependencies:

```bash
pip install -r requirements.txt
```

This will install all necessary packages including Manim, Jupyter, and ipywidgets.

### Special Requirements for Interactive Tutorials

Some tutorials have interactive versions that require additional setup:

- **ipywidgets**: Required for interactive tutorials (automatically installed via requirements.txt)
- **Jupyter Notebook**: Required for running .ipynb files (automatically installed via requirements.txt)

For Jupyter notebook extensions (required for interactive widgets):

```bash
jupyter nbextension enable --py widgetsnbextension
```

## Tutorial File Naming Convention

Tutorial files use numeric prefixes to indicate the order of progression:

- `01_getting_started.py` - Standard tutorial file
- `01_getting_started_interactive.py` - Interactive version with widgets
- `01_getting_started.ipynb` - Jupyter notebook version

### Importing Tutorial Files

Due to the numeric prefixes, tutorial files should be imported using `importlib.util`:

```python
import importlib.util

spec = importlib.util.spec_from_file_location("tutorial", "01_getting_started.py")
tutorial = importlib.util.module_from_spec(spec)
spec.loader.exec_module(tutorial)
```

Alternatively, you can run tutorials directly using Manim's CLI:

```bash
manim -pql 01_getting_started.py GettingStartedScene
```

## Running Tutorials

### Standard Python Files (.py)

Run standard tutorial files directly with Python:

```bash
python 01_getting_started.py
```

Or use Manim's CLI for rendering:

```bash
manim -pql 01_getting_started.py GettingStartedScene
```

### Interactive Python Files (_interactive.py)

Interactive tutorials require Jupyter notebook environment:

```bash
jupyter notebook 01_getting_started_interactive.py
```

### Jupyter Notebook Files (.ipynb)

Run notebook files in Jupyter:

```bash
jupyter notebook 01_getting_started.ipynb
```

## Getting Started

Please refer to `setup_instructions.md` for detailed installation and setup instructions.

## Requirements

See `requirements.txt` for a complete list of required packages.