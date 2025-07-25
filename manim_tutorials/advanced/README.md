# Advanced Tutorials

This section contains tutorials for advanced users who want to explore the full capabilities of Manim. These tutorials cover complex animation techniques, custom animations, scene composition, physics simulations, and interactive scenes that go beyond the basics.

## Running These Tutorials

### Standard Python Files (.py)

These tutorials can be run directly with Python or using Manim's CLI:

```bash
# Run with Python directly
python 01_animations_and_timing.py

# Or render with Manim CLI
manim -pql 01_animations_and_timing.py AdvancedAnimations
```

### Interactive Python Files (_interactive.py)

Interactive tutorials require the `ipywidgets` package and Jupyter notebook environment:

```bash
# Install required dependencies (if not already installed)
pip install ipywidgets jupyter

# Enable widgets extension
jupyter nbextension enable --py widgetsnbextension

# Run in Jupyter
jupyter notebook 01_animations_and_timing_interactive.py
```

### Jupyter Notebook Files (.ipynb)

Notebook files can be opened directly in Jupyter:

```bash
jupyter notebook 01_animations_and_timing.ipynb
```

## Tutorials

1. [Animations and Timing](01_animations_and_timing.py) - Advanced animation techniques and timing control
   - [Jupyter Notebook Version](01_animations_and_timing.ipynb)
2. [Custom Animations](02_custom_animations.py) - Creating your own animation classes
   - [Jupyter Notebook Version](02_custom_animations.ipynb)
3. [Scene Composition](03_scene_composition.py) - Combining multiple scenes and complex layouts
   - [Jupyter Notebook Version](03_scene_composition.ipynb)
4. [Physics Simulations](04_physics_simulations.py) - Creating physics-based animations
   - [Jupyter Notebook Version](04_physics_simulations.ipynb)
5. [Interactive Scenes](05_interactive_scenes.py) - Creating interactive scenes with user input
   - [Jupyter Notebook Version](05_interactive_scenes.ipynb)

## Interactive Tutorials

Some tutorials have interactive versions that demonstrate how to use Jupyter widgets with Manim:

- [Animations and Timing Interactive](01_animations_and_timing_interactive.py) - Interactive version with widgets for animation parameters
- [Custom Animations Interactive](02_custom_animations_interactive.py) - Interactive version with widgets for custom animation parameters
- [Scene Composition Interactive](03_scene_composition_interactive.py) - Interactive version with widgets for scene composition parameters
- [Physics Simulations Interactive](04_physics_simulations_interactive.py) - Interactive version with widgets for physics simulation parameters
- [Interactive Scenes Interactive](05_interactive_scenes_interactive.py) - Interactive version with widgets for interactive scene parameters