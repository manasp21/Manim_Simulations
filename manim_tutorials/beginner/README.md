# Beginner Tutorials

This section contains tutorials for beginners who are just starting with Manim. These tutorials cover the basic concepts and simple animations.

## Running These Tutorials

### Standard Python Files (.py)

These tutorials can be run directly with Python or using Manim's CLI:

```bash
# Run with Python directly
python 01_getting_started.py

# Or render with Manim CLI
manim -pql 01_getting_started.py GettingStartedScene
```

### Interactive Python Files (_interactive.py)

Interactive tutorials require the `ipywidgets` package and Jupyter notebook environment:

```bash
# Install required dependencies (if not already installed)
pip install ipywidgets jupyter

# Enable widgets extension
jupyter nbextension enable --py widgetsnbextension

# Run in Jupyter
jupyter notebook 01_getting_started_interactive.py
```

### Jupyter Notebook Files (.ipynb)

Notebook files can be opened directly in Jupyter:

```bash
jupyter notebook 01_getting_started.ipynb
```

## Tutorials

1. Getting Started
   - Standard: [01_getting_started.py](01_getting_started.py)
   - Interactive: [01_getting_started_interactive.py](01_getting_started_interactive.py)
   - Notebook: [01_getting_started.ipynb](01_getting_started.ipynb)

2. Basic Shapes
   - Standard: [02_basic_shapes.py](02_basic_shapes.py)
   - Interactive: [02_basic_shapes_interactive.py](02_basic_shapes_interactive.py)
   - Notebook: [02_basic_shapes.ipynb](02_basic_shapes.ipynb)

3. Simple Animations
   - Standard: [03_simple_animations.py](03_simple_animations.py)
   - Interactive: [03_simple_animations_interactive.py](03_simple_animations_interactive.py)
   - Notebook: [03_simple_animations.ipynb](03_simple_animations.ipynb)

4. Text and LaTeX
   - Standard: [04_text_and_latex.py](04_text_and_latex.py)
   - Interactive: [04_text_and_latex_interactive.py](04_text_and_latex_interactive.py)
   - Notebook: [04_text_and_latex.ipynb](04_text_and_latex.ipynb)

5. Colors and Styling
   - Standard: [05_colors_and_styling.py](05_colors_and_styling.py)
   - Interactive: [05_colors_and_styling_interactive.py](05_colors_and_styling_interactive.py)
   - Notebook: [05_colors_and_styling.ipynb](05_colors_and_styling.ipynb)