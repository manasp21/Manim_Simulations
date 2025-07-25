# Manim Tutorial Execution Plan

This document provides a systematic execution plan for all Manim tutorial files, organized by section. Each entry includes the file path, scene class names, and the appropriate command structure for execution.

## 1. Beginner Tutorials

### 1.1 Standard Python Files (.py)

| File | Scene Classes | Command |
|------|---------------|---------|
| `manim_tutorials/beginner/01_getting_started.py` | GettingStarted | `manim -pql manim_tutorials/beginner/01_getting_started.py GettingStarted` |
| `manim_tutorials/beginner/02_basic_shapes.py` | BasicShapes | `manim -pql manim_tutorials/beginner/02_basic_shapes.py BasicShapes` |
| `manim_tutorials/beginner/03_simple_animations.py` | SimpleAnimations | `manim -pql manim_tutorials/beginner/03_simple_animations.py SimpleAnimations` |
| `manim_tutorials/beginner/04_text_and_latex.py` | TextAndLaTeX | `manim -pql manim_tutorials/beginner/04_text_and_latex.py TextAndLaTeX` |
| `manim_tutorials/beginner/05_colors_and_styling.py` | ColorsAndStyling | `manim -pql manim_tutorials/beginner/05_colors_and_styling.py ColorsAndStyling` |

### 1.2 Interactive Python Files (_interactive.py)

| File | Scene Classes | Command |
|------|---------------|---------|
| `manim_tutorials/beginner/01_getting_started_interactive.py` | InteractiveGettingStarted | `manim -pql manim_tutorials/beginner/01_getting_started_interactive.py InteractiveGettingStarted` |
| `manim_tutorials/beginner/03_simple_animations_interactive.py` | InteractiveSimpleAnimations | `manim -pql manim_tutorials/beginner/03_simple_animations_interactive.py InteractiveSimpleAnimations` |
| `manim_tutorials/beginner/04_text_and_latex_interactive.py` | InteractiveTextAndLaTeX | `manim -pql manim_tutorials/beginner/04_text_and_latex_interactive.py InteractiveTextAndLaTeX` |
| `manim_tutorials/beginner/05_colors_and_styling_interactive.py` | InteractiveColorsAndStyling | `manim -pql manim_tutorials/beginner/05_colors_and_styling_interactive.py InteractiveColorsAndStyling` |

### 1.3 Jupyter Notebook Files (.ipynb)

| File | Usage |
|------|-------|
| `manim_tutorials/beginner/01_getting_started.ipynb` | Run with `jupyter notebook manim_tutorials/beginner/01_getting_started.ipynb` |
| `manim_tutorials/beginner/02_basic_shapes.ipynb` | Run with `jupyter notebook manim_tutorials/beginner/02_basic_shapes.ipynb` |
| `manim_tutorials/beginner/03_simple_animations.ipynb` | Run with `jupyter notebook manim_tutorials/beginner/03_simple_animations.ipynb` |
| `manim_tutorials/beginner/04_text_and_latex.ipynb` | Run with `jupyter notebook manim_tutorials/beginner/04_text_and_latex.ipynb` |
| `manim_tutorials/beginner/05_colors_and_styling.ipynb` | Run with `jupyter notebook manim_tutorials/beginner/05_colors_and_styling.ipynb` |

## 2. Intermediate Tutorials

### 2.1 Standard Python Files (.py)

| File | Scene Classes | Command |
|------|---------------|---------|
| `manim_tutorials/intermediate/01_coordinate_systems.py` | CoordinateSystems | `manim -pql manim_tutorials/intermediate/01_coordinate_systems.py CoordinateSystems` |
| `manim_tutorials/intermediate/02_transformations.py` | Transformations | `manim -pql manim_tutorials/intermediate/02_transformations.py Transformations` |
| `manim_tutorials/intermediate/03_updaters.py` | Updaters | `manim -pql manim_tutorials/intermediate/03_updaters.py Updaters` |
| `manim_tutorials/intermediate/04_3d_scenes.py` | ThreeDSceneExample, SurfaceExample | `manim -pql manim_tutorials/intermediate/04_3d_scenes.py ThreeDSceneExample` or `manim -pql manim_tutorials/intermediate/04_3d_scenes.py SurfaceExample` |
| `manim_tutorials/intermediate/05_custom_mobjects.py` | CustomMobjects | `manim -pql manim_tutorials/intermediate/05_custom_mobjects.py CustomMobjects` |

### 2.2 Interactive Python Files (_interactive.py)

| File | Scene Classes | Command |
|------|---------------|---------|
| `manim_tutorials/intermediate/01_coordinate_systems_interactive.py` | InteractiveCoordinateSystems | `manim -pql manim_tutorials/intermediate/01_coordinate_systems_interactive.py InteractiveCoordinateSystems` |
| `manim_tutorials/intermediate/04_3d_scenes_interactive.py` | InteractiveThreeDSceneExample, InteractiveSurfaceExample | `manim -pql manim_tutorials/intermediate/04_3d_scenes_interactive.py InteractiveThreeDSceneExample` or `manim -pql manim_tutorials/intermediate/04_3d_scenes_interactive.py InteractiveSurfaceExample` |

### 2.3 Jupyter Notebook Files (.ipynb)

| File | Usage |
|------|-------|
| `manim_tutorials/intermediate/01_coordinate_systems.ipynb` | Run with `jupyter notebook manim_tutorials/intermediate/01_coordinate_systems.ipynb` |
| `manim_tutorials/intermediate/02_transformations.ipynb` | Run with `jupyter notebook manim_tutorials/intermediate/02_transformations.ipynb` |
| `manim_tutorials/intermediate/03_updaters.ipynb` | Run with `jupyter notebook manim_tutorials/intermediate/03_updaters.ipynb` |
| `manim_tutorials/intermediate/04_3d_scenes.ipynb` | Run with `jupyter notebook manim_tutorials/intermediate/04_3d_scenes.ipynb` |
| `manim_tutorials/intermediate/05_custom_mobjects.ipynb` | Run with `jupyter notebook manim_tutorials/intermediate/05_custom_mobjects.ipynb` |

## 3. Advanced Tutorials

### 3.1 Standard Python Files (.py)

| File | Scene Classes | Command |
|------|---------------|---------|
| `manim_tutorials/advanced/01_animations_and_timing.py` | AnimationsAndTiming | `manim -pql manim_tutorials/advanced/01_animations_and_timing.py AnimationsAndTiming` |
| `manim_tutorials/advanced/02_custom_animations.py` | CustomAnimations | `manim -pql manim_tutorials/advanced/02_custom_animations.py CustomAnimations` |
| `manim_tutorials/advanced/03_scene_composition.py` | SceneComposition, MultiSceneComposition | `manim -pql manim_tutorials/advanced/03_scene_composition.py SceneComposition` or `manim -pql manim_tutorials/advanced/03_scene_composition.py MultiSceneComposition` |
| `manim_tutorials/advanced/04_physics_simulations.py` | PhysicsSimulations, WaveSimulation | `manim -pql manim_tutorials/advanced/04_physics_simulations.py PhysicsSimulations` or `manim -pql manim_tutorials/advanced/04_physics_simulations.py WaveSimulation` |
| `manim_tutorials/advanced/05_interactive_scenes.py` | InteractiveScenes, ValueTrackers, KeyboardInput | `manim -pql manim_tutorials/advanced/05_interactive_scenes.py InteractiveScenes` or `manim -pql manim_tutorials/advanced/05_interactive_scenes.py ValueTrackers` or `manim -pql manim_tutorials/advanced/05_interactive_scenes.py KeyboardInput` |

### 3.2 Interactive Python Files (_interactive.py)

| File | Scene Classes | Command |
|------|---------------|---------|
| `manim_tutorials/advanced/01_animations_and_timing_interactive.py` | InteractiveAnimationsAndTiming | `manim -pql manim_tutorials/advanced/01_animations_and_timing_interactive.py InteractiveAnimationsAndTiming` |

### 3.3 Jupyter Notebook Files (.ipynb)

| File | Usage |
|------|-------|
| `manim_tutorials/advanced/01_animations_and_timing.ipynb` | Run with `jupyter notebook manim_tutorials/advanced/01_animations_and_timing.ipynb` |
| `manim_tutorials/advanced/02_custom_animations.ipynb` | Run with `jupyter notebook manim_tutorials/advanced/02_custom_animations.ipynb` |
| `manim_tutorials/advanced/03_scene_composition.ipynb` | Run with `jupyter notebook manim_tutorials/advanced/03_scene_composition.ipynb` |
| `manim_tutorials/advanced/04_physics_simulations.ipynb` | Run with `jupyter notebook manim_tutorials/advanced/04_physics_simulations.ipynb` |
| `manim_tutorials/advanced/05_interactive_scenes.ipynb` | Run with `jupyter notebook manim_tutorials/advanced/05_interactive_scenes.ipynb` |

## 4. Project Tutorials

### 4.1 Mathematical Visualization

| File | Scene Classes | Command |
|------|---------------|---------|
| `manim_tutorials/projects/01_mathematical_visualization/pythagorean_theorem.py` | PythagoreanTheorem, PythagoreanProof | `manim -pql manim_tutorials/projects/01_mathematical_visualization/pythagorean_theorem.py PythagoreanTheorem` or `manim -pql manim_tutorials/projects/01_mathematical_visualization/pythagorean_theorem.py PythagoreanProof` |

### 4.2 Physics Animations

| File | Scene Classes | Command |
|------|---------------|---------|
| `manim_tutorials/projects/02_physics_animations/projectile_motion.py` | ProjectileMotion, MultipleProjectiles | `manim -pql manim_tutorials/projects/02_physics_animations/projectile_motion.py ProjectileMotion` or `manim -pql manim_tutorials/projects/02_physics_animations/projectile_motion.py MultipleProjectiles` |

### 4.3 Data Visualization

| File | Scene Classes | Command |
|------|---------------|---------|
| `manim_tutorials/projects/03_data_visualization/bar_charts.py` | BarCharts, Histogram, StackedBarChart | `manim -pql manim_tutorials/projects/03_data_visualization/bar_charts.py BarCharts` or `manim -pql manim_tutorials/projects/03_data_visualization/bar_charts.py Histogram` or `manim -pql manim_tutorials/projects/03_data_visualization/bar_charts.py StackedBarChart` |

### 4.4 Educational Content

| File | Scene Classes | Command |
|------|---------------|---------|
| `manim_tutorials/projects/04_educational_content/algebra_basics.py` | AlgebraBasics, QuadraticEquations, Functions | `manim -pql manim_tutorials/projects/04_educational_content/algebra_basics.py AlgebraBasics` or `manim -pql manim_tutorials/projects/04_educational_content/algebra_basics.py QuadraticEquations` or `manim -pql manim_tutorials/projects/04_educational_content/algebra_basics.py Functions` |

### 4.5 Creative Art

| File | Scene Classes | Command |
|------|---------------|---------|
| `manim_tutorials/projects/05_creative_art/fractals.py` | Fractals, MandelbrotSet, JuliaSet, FractalAnimations | `manim -pql manim_tutorials/projects/05_creative_art/fractals.py Fractals` or `manim -pql manim_tutorials/projects/05_creative_art/fractals.py MandelbrotSet` or `manim -pql manim_tutorials/projects/05_creative_art/fractals.py JuliaSet` or `manim -pql manim_tutorials/projects/05_creative_art/fractals.py FractalAnimations` |

## Quality Settings and Output Directory Considerations

### Quality Options

Manim provides several quality settings that can be used with the command line:

- `-pql` or `--quality low` - Low quality (480p15)
- `-pqm` or `--quality medium` - Medium quality (720p30)
- `-pqh` or `--quality high` - High quality (1080p60)
- `-p` or `--preview` - Preview the animation without saving
- `-w` or `--write_to_movie` - Write the animation to a file

### Output Directories

By default, Manim saves output files in the `media/` directory within the project folder. The structure is:
```
media/
├── videos/
│   └── [scene_name]/
│       └── [quality]/
│           ├── [scene_name].mp4
│           └── partial_movie_files/
└── images/
    └── [scene_name]/
```

To specify a custom output directory, use the `--media_dir` option:
```bash
manim -pql --media_dir /path/to/output/directory file.py SceneName
```

## Error Handling and Troubleshooting

### Common Issues and Solutions

1. **Missing Dependencies**
   - Error: `ModuleNotFoundError`
   - Solution: Install all dependencies using `pip install -r manim_tutorials/requirements.txt`

2. **LaTeX Errors**
   - Error: LaTeX compilation errors
   - Solution: Ensure a complete LaTeX distribution is installed (see setup_instructions.md)

3. **FFmpeg Not Found**
   - Error: FFmpeg-related errors
   - Solution: Install FFmpeg and ensure it's in your system PATH

4. **Import Errors with Interactive Tutorials**
   - Error: Widget import errors
   - Solution: Enable Jupyter widgets extension with `jupyter nbextension enable --py widgetsnbextension`

5. **3D Scene Issues**
   - Error: OpenGL-related errors
   - Solution: Ensure proper graphics drivers are installed

### Execution Script Template

For systematic execution of all tutorials, you can create a shell script like this:

```bash
#!/bin/bash

# Function to run a tutorial and handle errors
run_tutorial() {
    local file=$1
    local scene=$2
    local quality=${3:-l}  # Default to low quality
    
    echo "Running: manim -pq${quality} ${file} ${scene}"
    
    if manim -pq${quality} "${file}" "${scene}"; then
        echo "Successfully rendered ${scene} from ${file}"
    else
        echo "Error rendering ${scene} from ${file}"
        echo "Check the error message above for details"
    fi
    
    echo "----------------------------------------"
}

# Example usage for beginner tutorials
run_tutorial "manim_tutorials/beginner/01_getting_started.py" "GettingStarted" "l"
run_tutorial "manim_tutorials/beginner/02_basic_shapes.py" "BasicShapes" "l"
# ... continue for all tutorials
```

This approach allows for systematic execution with proper error handling.

## Systematic Execution Script

For automated execution of all tutorials, here's a comprehensive shell script:

```bash
#!/bin/bash

# Manim Tutorial Execution Script

# Function to run a tutorial and handle errors
run_tutorial() {
    local file=$1
    local scene=$2
    local quality=${3:-l}  # Default to low quality
    local section=$4       # Section name for logging
    
    echo "=== Running ${section}: ${scene} from ${file} ==="
    
    # Check if file exists
    if [ ! -f "$file" ]; then
        echo "ERROR: File $file not found!"
        return 1
    fi
    
    # Run the tutorial
    if manim -pq${quality} "${file}" "${scene}"; then
        echo "SUCCESS: Rendered ${scene} from ${file}"
    else
        echo "ERROR: Failed to render ${scene} from ${file}"
        echo "Check the error message above for details"
        return 1
    fi
    
    echo ""
}

# Function to run all beginner tutorials
run_beginner_tutorials() {
    echo "=== BEGINNER TUTORIALS ==="
    
    run_tutorial "manim_tutorials/beginner/01_getting_started.py" "GettingStarted" "l" "Beginner"
    run_tutorial "manim_tutorials/beginner/02_basic_shapes.py" "BasicShapes" "l" "Beginner"
    run_tutorial "manim_tutorials/beginner/03_simple_animations.py" "SimpleAnimations" "l" "Beginner"
    run_tutorial "manim_tutorials/beginner/04_text_and_latex.py" "TextAndLaTeX" "l" "Beginner"
    run_tutorial "manim_tutorials/beginner/05_colors_and_styling.py" "ColorsAndStyling" "l" "Beginner"
    
    # Interactive versions
    run_tutorial "manim_tutorials/beginner/01_getting_started_interactive.py" "InteractiveGettingStarted" "l" "Beginner Interactive"
    run_tutorial "manim_tutorials/beginner/03_simple_animations_interactive.py" "InteractiveSimpleAnimations" "l" "Beginner Interactive"
    run_tutorial "manim_tutorials/beginner/04_text_and_latex_interactive.py" "InteractiveTextAndLaTeX" "l" "Beginner Interactive"
    run_tutorial "manim_tutorials/beginner/05_colors_and_styling_interactive.py" "InteractiveColorsAndStyling" "l" "Beginner Interactive"
}

# Function to run all intermediate tutorials
run_intermediate_tutorials() {
    echo "=== INTERMEDIATE TUTORIALS ==="
    
    run_tutorial "manim_tutorials/intermediate/01_coordinate_systems.py" "CoordinateSystems" "l" "Intermediate"
    run_tutorial "manim_tutorials/intermediate/02_transformations.py" "Transformations" "l" "Intermediate"
    run_tutorial "manim_tutorials/intermediate/03_updaters.py" "Updaters" "l" "Intermediate"
    run_tutorial "manim_tutorials/intermediate/04_3d_scenes.py" "ThreeDSceneExample" "l" "Intermediate"
    run_tutorial "manim_tutorials/intermediate/04_3d_scenes.py" "SurfaceExample" "l" "Intermediate"
    run_tutorial "manim_tutorials/intermediate/05_custom_mobjects.py" "CustomMobjects" "l" "Intermediate"
    
    # Interactive versions
    run_tutorial "manim_tutorials/intermediate/01_coordinate_systems_interactive.py" "InteractiveCoordinateSystems" "l" "Intermediate Interactive"
    run_tutorial "manim_tutorials/intermediate/04_3d_scenes_interactive.py" "InteractiveThreeDSceneExample" "l" "Intermediate Interactive"
    run_tutorial "manim_tutorials/intermediate/04_3d_scenes_interactive.py" "InteractiveSurfaceExample" "l" "Intermediate Interactive"
}

# Function to run all advanced tutorials
run_advanced_tutorials() {
    echo "=== ADVANCED TUTORIALS ==="
    
    run_tutorial "manim_tutorials/advanced/01_animations_and_timing.py" "AnimationsAndTiming" "l" "Advanced"
    run_tutorial "manim_tutorials/advanced/02_custom_animations.py" "CustomAnimations" "l" "Advanced"
    run_tutorial "manim_tutorials/advanced/03_scene_composition.py" "SceneComposition" "l" "Advanced"
    run_tutorial "manim_tutorials/advanced/03_scene_composition.py" "MultiSceneComposition" "l" "Advanced"
    run_tutorial "manim_tutorials/advanced/04_physics_simulations.py" "PhysicsSimulations" "l" "Advanced"
    run_tutorial "manim_tutorials/advanced/04_physics_simulations.py" "WaveSimulation" "l" "Advanced"
    run_tutorial "manim_tutorials/advanced/05_interactive_scenes.py" "InteractiveScenes" "l" "Advanced"
    run_tutorial "manim_tutorials/advanced/05_interactive_scenes.py" "ValueTrackers" "l" "Advanced"
    run_tutorial "manim_tutorials/advanced/05_interactive_scenes.py" "KeyboardInput" "l" "Advanced"
    
    # Interactive versions
    run_tutorial "manim_tutorials/advanced/01_animations_and_timing_interactive.py" "InteractiveAnimationsAndTiming" "l" "Advanced Interactive"
}

# Function to run all project tutorials
run_project_tutorials() {
    echo "=== PROJECT TUTORIALS ==="
    
    # Mathematical Visualization
    run_tutorial "manim_tutorials/projects/01_mathematical_visualization/pythagorean_theorem.py" "PythagoreanTheorem" "l" "Projects/Mathematical Visualization"
    run_tutorial "manim_tutorials/projects/01_mathematical_visualization/pythagorean_theorem.py" "PythagoreanProof" "l" "Projects/Mathematical Visualization"
    
    # Physics Animations
    run_tutorial "manim_tutorials/projects/02_physics_animations/projectile_motion.py" "ProjectileMotion" "l" "Projects/Physics Animations"
    run_tutorial "manim_tutorials/projects/02_physics_animations/projectile_motion.py" "MultipleProjectiles" "l" "Projects/Physics Animations"
    
    # Data Visualization
    run_tutorial "manim_tutorials/projects/03_data_visualization/bar_charts.py" "BarCharts" "l" "Projects/Data Visualization"
    run_tutorial "manim_tutorials/projects/03_data_visualization/bar_charts.py" "Histogram" "l" "Projects/Data Visualization"
    run_tutorial "manim_tutorials/projects/03_data_visualization/bar_charts.py" "StackedBarChart" "l" "Projects/Data Visualization"
    
    # Educational Content
    run_tutorial "manim_tutorials/projects/04_educational_content/algebra_basics.py" "AlgebraBasics" "l" "Projects/Educational Content"
    run_tutorial "manim_tutorials/projects/04_educational_content/algebra_basics.py" "QuadraticEquations" "l" "Projects/Educational Content"
    run_tutorial "manim_tutorials/projects/04_educational_content/algebra_basics.py" "Functions" "l" "Projects/Educational Content"
    
    # Creative Art
    run_tutorial "manim_tutorials/projects/05_creative_art/fractals.py" "Fractals" "l" "Projects/Creative Art"
    run_tutorial "manim_tutorials/projects/05_creative_art/fractals.py" "MandelbrotSet" "l" "Projects/Creative Art"
    run_tutorial "manim_tutorials/projects/05_creative_art/fractals.py" "JuliaSet" "l" "Projects/Creative Art"
    run_tutorial "manim_tutorials/projects/05_creative_art/fractals.py" "FractalAnimations" "l" "Projects/Creative Art"
}

# Main execution function
main() {
    echo "Manim Tutorial Execution Script"
    echo "=============================="
    
    # Check if manim is installed
    if ! command -v manim &> /dev/null; then
        echo "ERROR: Manim is not installed. Please install it first."
        echo "Run: pip install -r manim_tutorials/requirements.txt"
        exit 1
    fi
    
    # Parse command line arguments
    case "${1:-all}" in
        beginner)
            run_beginner_tutorials
            ;;
        intermediate)
            run_intermediate_tutorials
            ;;
        advanced)
            run_advanced_tutorials
            ;;
        projects)
            run_project_tutorials
            ;;
        all)
            run_beginner_tutorials
            run_intermediate_tutorials
            run_advanced_tutorials
            run_project_tutorials
            ;;
        *)
            echo "Usage: $0 [beginner|intermediate|advanced|projects|all]"
            echo "Default: all"
            exit 1
            ;;
    esac
    
    echo "=== EXECUTION COMPLETE ==="
}

# Run main function with all arguments
main "$@"
```

This script provides a comprehensive way to run all tutorials systematically with proper error handling and logging.