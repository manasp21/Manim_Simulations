# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Manim tutorial repository focused on mathematical animation education. It contains comprehensive tutorials organized by difficulty level, project examples, and utility functions for creating educational mathematical animations.

## Critical Prerequisites

**LaTeX System Required**: This repository depends on LaTeX for mathematical notation rendering. Ensure LaTeX is installed and accessible via `which latex`. On macOS, MacTeX provides `/Library/TeX/texbin/latex`. Without LaTeX, MathTex rendering will fail with `FileNotFoundError`.

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

### Testing and Validation
```bash
# Test basic imports
python3 test_imports.py

# Test detailed imports with error reporting  
python3 test_imports_detailed.py

# Test utility functions (common failure point)
python3 -c "from manim_tutorials.utils.constants import QUALITY_SETTINGS; print('✅ Utils working')"
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

**Interactive Tutorial Imports**: All `*_interactive.py` files require path manipulation to import `widget_utils`:
```python
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from utils.widget_utils import *
```

## Development Workflow

1. **Create new tutorials**: Follow the existing naming convention and difficulty progression
2. **Test tutorials**: Run individual scenes with `manim -pql` for quick testing
3. **Interactive versions**: Use the widget utilities from `utils/widget_utils.py` for creating interactive tutorials
4. **Quality assurance**: Run the full test suite with `run_all_tutorials.sh` before committing

## Dependencies

- **manim>=0.18.0**: Core animation engine (currently tested with 0.19.0)
- **numpy>=1.24.0**: Mathematical operations
- **matplotlib>=3.6.0**: Additional plotting capabilities
- **jupyter>=1.0.0**: Notebook support
- **ipywidgets>=8.0.0**: Interactive widgets (critical for interactive tutorials)
- **pandas>=1.5.0**: Data manipulation for data visualization projects
- **scipy>=1.9.0**: Scientific computing for physics simulations

**System Requirements**: Python 3.8+ recommended, LaTeX system mandatory.

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

## Known Issues & Solutions

**Utility Import Errors**: If `manim_tutorials.utils.constants` fails with `NameError`, check for invalid Manim color references. Use `GREEN_E` instead of `DARK_GREEN`, `PURPLE_E` instead of `DARK_PURPLE`.

**LaTeX Rendering Failures**: Use `MathTex()` for mathematical expressions, not `Text()`. Verify LaTeX installation with `which latex`.

**Interactive Tutorial Path Issues**: All interactive files need the sys.path manipulation shown above to locate `widget_utils`.

## Repository Stats

- **Total Files**: 71 (41 Python tutorials + 15 interactive + 15 Jupyter notebooks)
- **Tutorial Coverage**: 51 complete scenarios across beginner/intermediate/advanced/projects
- **Quality Levels**: 4 (480p15, 720p30, 1080p60, 4K60)
- **Success Rate**: 100% when prerequisites are met