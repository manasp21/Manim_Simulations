# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Manim tutorial repository focused on mathematical animation education. It contains comprehensive tutorials organized by difficulty level, project examples, and utility functions for creating educational mathematical animations.

## Key Commands

### Running Manim Animations
```bash
# Render a scene with low quality (for development)
manim -pql file.py SceneName

# Render with medium quality
manim -pqm file.py SceneName

# Render with high quality (for production)
manim -pqh file.py SceneName

# Render without preview (just create the file)
manim -ql file.py SceneName
```

### Running All Tutorials
```bash
# Run all tutorials
./manim_tutorials/run_all_tutorials.sh

# Run specific tutorial levels
./manim_tutorials/run_all_tutorials.sh beginner
./manim_tutorials/run_all_tutorials.sh intermediate
./manim_tutorials/run_all_tutorials.sh advanced
./manim_tutorials/run_all_tutorials.sh projects
```

### Installation and Setup
```bash
# Install dependencies
pip install -r manim_tutorials/requirements.txt

# Enable Jupyter widgets for interactive tutorials
jupyter nbextension enable --py widgetsnbextension
```

### Testing Imports
```bash
# Test basic imports
python test_imports.py

# Test detailed imports with error reporting
python test_imports_detailed.py
```

## Project Structure

The repository follows a structured educational approach:

- **manim_tutorials/**: Main tutorial directory with progressive difficulty levels
  - `beginner/`: Basic shapes, animations, text, and colors (5 tutorials)
  - `intermediate/`: Coordinate systems, transformations, updaters, 3D scenes, custom objects (5 tutorials)
  - `advanced/`: Complex animations, timing, physics simulations, interactive scenes (5 tutorials)
  - `projects/`: Complete project examples across 5 domains
  - `utils/`: Shared utility functions and constants
  - `resources/`: Documentation and best practices
  - `troubleshooting/`: Common issues and solutions

- **File Naming Convention**: All tutorial files use numeric prefixes (01_, 02_, etc.) with three versions:
  - `.py`: Standard tutorial file
  - `_interactive.py`: Interactive version with widgets
  - `.ipynb`: Jupyter notebook version

## Core Architecture

### Tutorial Utilities (`manim_tutorials/utils/`)

- **helpers.py**: Common functions for creating labeled arrows, coordinate systems, animated titles, grid arrangements, and zoom animations
- **constants.py**: Centralized configuration for colors, timing, quality settings, and common mathematical functions
- **config.py**: Scene configuration and setup utilities
- **testing.py**: Testing utilities for tutorial validation
- **widget_utils.py**: Interactive widget helpers for Jupyter notebooks

### Scene Classes

All tutorial scenes inherit from Manim's `Scene` class and follow the pattern:
```python
class SceneName(Scene):
    def construct(self):
        # Scene construction logic here
```

### Import Considerations

Due to numeric prefixes in filenames, tutorials should be imported using `importlib.util` or run directly with Manim CLI rather than standard Python imports.

## Development Workflow

1. **Create new tutorials**: Follow the existing naming convention and difficulty progression
2. **Test tutorials**: Run individual scenes with `manim -pql` for quick testing
3. **Interactive versions**: Use the widget utilities from `utils/widget_utils.py` for creating interactive tutorials
4. **Quality assurance**: Run the full test suite with `run_all_tutorials.sh` before committing

## Dependencies

- **manim>=0.18.0**: Core animation engine
- **numpy>=1.24.0**: Mathematical operations
- **matplotlib>=3.6.0**: Additional plotting capabilities
- **jupyter>=1.0.0**: Notebook support
- **ipywidgets>=8.0.0**: Interactive widgets
- **pandas>=1.5.0**: Data manipulation for data visualization projects
- **scipy>=1.9.0**: Scientific computing for physics simulations

## Quality Settings

The project supports four quality levels defined in `constants.py`:
- **low**: 480p, 15fps (development)
- **medium**: 854p, 30fps (preview)
- **high**: 1080p, 60fps (final)
- **production**: 4K, 60fps (publishing)

## Common Patterns

- Use utilities from `helpers.py` for consistent styling and common operations
- Reference colors and settings from `constants.py` for consistency
- Follow the educational progression: simple concepts first, building complexity gradually
- Include both static and interactive versions when creating new tutorials
- Use descriptive scene names that match the class names for easy CLI access