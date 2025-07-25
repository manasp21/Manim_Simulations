# Manim Projects

This section contains complete project examples that demonstrate real-world applications of Manim.

## Prerequisites

Before running these projects, ensure you have installed all required dependencies:

```bash
pip install -r ../requirements.txt
```

This will install all necessary packages including Manim, Jupyter, and ipywidgets.

## Projects

1. [Mathematical Visualization](01_mathematical_visualization/) - Visualizing mathematical concepts and theorems
2. [Physics Animations](02_physics_animations/) - Animating physics principles and simulations
3. [Data Visualization](03_data_visualization/) - Creating animated charts and data representations
4. [Educational Content](04_educational_content/) - Educational animations for teaching various subjects
5. [Creative Art](05_creative_art/) - Artistic and creative animations using Manim

## Running Projects

Each project directory contains its own README with specific instructions. Generally, you can run any scene with:

```bash
manim -pql project_file.py SceneName
```

For example, to run the Pythagorean theorem visualization:

```bash
cd 01_mathematical_visualization
manim -pql pythagorean_theorem.py PythagoreanTheorem
```

## Project Structure

Each project directory contains:
- Project-specific Python files with Manim scenes
- A README.md with project description and usage instructions
- Output media files (after rendering)