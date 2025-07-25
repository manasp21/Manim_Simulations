# Intermediate Tutorials

This section contains tutorials for users who have mastered the basics of Manim and want to learn more advanced techniques.

## Running These Tutorials

### Standard Python Files (.py)

These tutorials can be run directly with Python or using Manim's CLI:

```bash
# Run with Python directly
python 01_coordinate_systems.py

# Or render with Manim CLI
manim -pql 01_coordinate_systems.py CoordinateSystemExample
```

### Interactive Python Files (_interactive.py)

Interactive tutorials require the `ipywidgets` package and Jupyter notebook environment:

```bash
# Install required dependencies (if not already installed)
pip install ipywidgets jupyter

# Enable widgets extension
jupyter nbextension enable --py widgetsnbextension

# Run in Jupyter
jupyter notebook 01_coordinate_systems_interactive.py
```

### Jupyter Notebook Files (.ipynb)

Notebook files can be opened directly in Jupyter:

```bash
jupyter notebook 01_coordinate_systems.ipynb
```

## Tutorials

1. [Coordinate Systems](01_coordinate_systems.py) - Working with axes, number planes, and coordinate systems
2. [Transformations](02_transformations.py) - Advanced transformation techniques
3. [Updaters](03_updaters.py) - Using updaters for dynamic animations
4. [3D Scenes](04_3d_scenes.py) - Creating and animating 3D objects
5. [Custom Mobjects](05_custom_mobjects.py) - Creating your own mobjects

## Interactive Tutorials

Some tutorials have interactive versions that demonstrate how to use Jupyter widgets with Manim:

- [Coordinate Systems Interactive](01_coordinate_systems_interactive.py) - Interactive version with widgets for coordinate system parameters
- [Transformations Interactive](02_transformations_interactive.py) - Interactive version with widgets for transformation parameters
- [Updaters Interactive](03_updaters_interactive.py) - Interactive version with widgets for updater parameters
- [3D Scenes Interactive](04_3d_scenes_interactive.py) - Interactive version with widgets for 3D scene parameters
- [Custom Mobjects Interactive](05_custom_mobjects_interactive.py) - Interactive version with widgets for custom mobject parameters