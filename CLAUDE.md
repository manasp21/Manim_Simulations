# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This repository contains two major components:
1. **IQB Simulations**: A world-class 18-20 minute quantum physics animation about Isotropic Quantum Beats (main project)
2. **Manim Tutorials**: Educational Manim tutorials organized by difficulty level

**Primary Focus**: The IQB Simulations project is the main deliverable - a professional scientific visualization suitable for physics researchers and graduate students.

## Critical Prerequisites

**LaTeX System Required**: All quantum physics animations depend on LaTeX for mathematical notation rendering. Ensure LaTeX is installed and accessible via `which latex`. On macOS, MacTeX provides `/Library/TeX/texbin/latex`. Without LaTeX, MathTex rendering will fail with `FileNotFoundError`.

## Key Commands

### IQB Simulations (Primary Project)

```bash
# Navigate to main project
cd "IQB Simulations"

# Render individual scenes for development (proven working)
manim -pql scenes/scene_01_classical_vs_quantum.py ClassicalVsQuantumIntro
manim -pql scenes/scene_02_mathematical_formalism.py MathematicalFormalism
manim -pql scenes/scene_03_isotropic_anisotropic.py IsotropicAnisotropic
manim -pql scenes/scene_04_physical_mechanisms.py PhysicalMechanisms

# Production quality rendering
manim -pqh scenes/scene_01_classical_vs_quantum.py ClassicalVsQuantumIntro

# Test quantum utilities (if imports fail)
python -c "from utils.color_schemes import QUANTUM_GOLD; print('✅ Colors working')"
```

### Manim Tutorials (Educational Content)

```bash
# Run all tutorials
./manim_tutorials/run_all_tutorials.sh

# Run specific tutorial levels
./manim_tutorials/run_all_tutorials.sh beginner
```

### Installation and Testing

```bash
# Install dependencies
pip install -r manim_tutorials/requirements.txt

# Test basic imports
python3 test_imports.py
python3 test_imports_detailed.py
```

## Architecture Overview

### IQB Simulations Structure (Main Project)

The quantum beats animation follows a proven 8-scene architecture:

```
IQB Simulations/
├── scenes/                    # Individual scene implementations (4 of 8 complete)
│   ├── scene_01_classical_vs_quantum.py      # ✅ Working (2.5 min)
│   ├── scene_02_mathematical_formalism.py    # ✅ Working (3.5 min) 
│   ├── scene_03_isotropic_anisotropic.py     # ✅ Working (3.0 min)
│   ├── scene_04_physical_mechanisms.py       # ✅ Working (2.5 min)
│   ├── scene_05_decoherence_effects.py       # 🚧 Pending (2.5 min)
│   ├── scene_06_experimental_detection.py    # 🚧 Pending (2.0 min)
│   ├── scene_07_interpretations.py           # 🚧 Pending (2.5 min)
│   ├── scene_08_future_directions.py         # 🚧 Pending (2.0 min)
│   └── scene_template.py                     # Proven template for new scenes
├── utils/                     # Quantum-specific utilities
│   ├── color_schemes.py       # Quantum color palettes and constants
│   ├── quantum_visualizations.py  # Bloch spheres, energy levels (complex - use cautiously)
│   ├── latex_formatting.py   # Standardized equations (has import issues)
│   └── experimental_setups.py # Lab equipment models
├── assets/                    # Supporting materials
│   ├── mathematical_expressions.py  # Pre-formatted equations (avoid - use direct LaTeX)
│   └── narration_scripts.py  # Synchronized narration
├── README.md                  # Comprehensive project documentation
└── DEVELOPMENT_GUIDE.md       # Critical debugging patterns and lessons learned
```

### Scene Development Pattern (PROVEN WORKING)

Each scene follows this tested architecture:

```python
class SceneName(Scene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.camera.background_color = QUANTUM_BACKGROUND
        
        # Scene timing parameters
        self.intro_duration = 15.0
        self.main_content_duration = 60.0
        self.conclusion_duration = 10.0
        
    def construct(self):
        # Segment-based construction
        self.create_scene_introduction()
        self.demonstrate_main_concepts()
        self.conclude_scene()
```

### Critical Lessons Learned (MUST FOLLOW)

**✅ What WORKS (Use These Patterns):**
1. **Direct LaTeX Strings**: `MathTex(r'\Delta\omega = \frac{E_2 - E_1}{\hbar}')`
2. **Simple VGroups**: Combine basic Manim objects (Line, Circle, Arrow, Rectangle)
3. **Import Fallbacks**: Always include try/except blocks with color fallbacks
4. **Basic Color Scheme**: QUANTUM_BACKGROUND, QUANTUM_GOLD, COHERENCE_GREEN, DECOHERENCE_RED

**🚫 What DOESN'T Work (Avoid These):**
1. **Complex Utility Classes**: `QuantumEnergyLevels.create_energy_level_diagram()` causes import issues
2. **Dictionary-Based LaTeX**: `QuantumBeatExpressions.CLASSICAL_BEATING['equation']` leads to LaTeX errors
3. **Double Backslash Escaping**: `r'\\Delta\\omega'` causes mysterious `\quad` insertion
4. **Complex Dependencies**: Accessing multiple utility modules simultaneously

### Testing Strategy

```bash
# ALWAYS test scenes incrementally during development
manim -pql scenes/scene_XX.py TestSceneClassName

# Use TestClass pattern for rapid iteration:
class TestSceneName(SceneName):
    def construct(self):
        # Test only introduction segment first
        self.create_scene_introduction()
```

## Quality Standards

### Rendering Quality Levels
- **Development**: `manim -pql` (480p, 15fps)
- **Preview**: `manim -pqm` (720p, 30fps)  
- **Production**: `manim -pqh` (1080p, 60fps)

### Color Scheme (Consistent Across All Scenes)
- **QUANTUM_GOLD (#FFD700)**: Key concepts, important equations
- **COHERENCE_GREEN (#00FF7F)**: Quantum coherence phenomena
- **DECOHERENCE_RED (#FF4500)**: Environmental effects, decay
- **WHITE**: Standard text and equations
- **QUANTUM_BACKGROUND (#0B1426)**: Scene backgrounds

### Scene Timing Guidelines
- **Total Target**: 18-20 minutes across 8 scenes
- **Current Progress**: 11.5 minutes (4 scenes complete)
- **Scene Transitions**: 1-2 second buffers between scenes
- **Animation Pacing**: 2-3 seconds per key equation or concept

## Dependencies and System Requirements

### Core Dependencies
- **manim>=0.18.0**: Animation engine (tested with 0.19.0)
- **numpy>=1.24.0**: Mathematical operations
- **scipy>=1.9.0**: Scientific computing for quantum calculations
- **matplotlib>=3.6.0**: Additional plotting capabilities

### System Requirements
- **LaTeX System**: Mandatory for mathematical notation
- **Python 3.8+**: Recommended version
- **Memory**: Minimum 8GB RAM for complex scene rendering
- **GPU Acceleration**: Recommended for smooth 3D quantum visualizations

## Common Development Tasks

### Adding New Scenes
1. Copy `scenes/scene_template.py` to new scene file
2. Update class name and timing parameters
3. Test incrementally with TestClass pattern
4. Follow proven LaTeX and VGroup patterns from working scenes

### Debugging LaTeX Errors
1. Use direct LaTeX strings, not dictionary lookups
2. Single backslash escaping: `r'\hat{H}'` not `r'\\hat{H}'`
3. Test equations individually before combining
4. Check DEVELOPMENT_GUIDE.md for emergency debugging patterns

### Import Error Resolution
1. Always include try/except blocks with fallback colors
2. Use simple Manim objects instead of complex utilities
3. Check project root path addition: `sys.path.append(project_root)`

## Repository Management

### Media Files (Auto-Generated)
All media files (videos, images, LaTeX renders) are automatically excluded from git via `.gitignore`. Only source code and documentation are tracked.

### File Organization
- **Source code only**: `.py`, `.md`, `.json`, configuration files tracked
- **Generated content ignored**: `media/`, `*.mp4`, `*.svg`, `*.tex`, `__pycache__/`
- **Development workflow**: Media regenerated automatically on each system

## Production Status

**Current Implementation Status:**
- ✅ **4 Scenes Complete** (11.5 minutes): Professional quality, fully tested
- 🚧 **4 Scenes Remaining** (6.5-8.5 minutes): Templates and patterns established
- ✅ **Technical Infrastructure**: Proven development workflow, debugging patterns
- ✅ **Quality Standards**: 150+ animations tested, LaTeX compilation perfect

**Next Development Priority:**
1. Scene 5: Decoherence Effects (2.5 min)
2. Scene 6: Experimental Detection (2.0 min)  
3. Scene 7: Interpretational Issues (2.5 min)
4. Scene 8: Future Directions (2.0 min)
5. Master orchestration file
6. Final production rendering

This project represents world-class scientific visualization suitable for physics research and graduate education, with established patterns for efficient completion of remaining content.