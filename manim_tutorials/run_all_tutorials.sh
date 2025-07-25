#!/bin/bash

# Manim Tutorial Execution Script

# Create a log file for recording results
LOG_FILE="tutorial_execution_log.txt"
ERROR_LOG="tutorial_execution_errors.txt"

# Initialize log files
echo "Manim Tutorial Execution Log - $(date)" > "$LOG_FILE"
echo "Manim Tutorial Error Log - $(date)" > "$ERROR_LOG"

# Function to run a tutorial and handle errors
run_tutorial() {
    local file=$1
    local scene=$2
    local quality=${3:-l}  # Default to low quality
    local section=$4       # Section name for logging
    
    echo "=== Running ${section}: ${scene} from ${file} ===" | tee -a "$LOG_FILE"
    echo "Command: manim -pq${quality} ${file} ${scene}" | tee -a "$LOG_FILE"
    
    # Check if file exists
    if [ ! -f "$file" ]; then
        echo "ERROR: File $file not found!" | tee -a "$ERROR_LOG"
        echo "ERROR: File $file not found!" | tee -a "$LOG_FILE"
        return 1
    fi
    
    # Run the tutorial
    if manim -pq${quality} "${file}" "${scene}"; then
        echo "SUCCESS: Rendered ${scene} from ${file}" | tee -a "$LOG_FILE"
    else
        echo "ERROR: Failed to render ${scene} from ${file}" | tee -a "$ERROR_LOG"
        echo "ERROR: Failed to render ${scene} from ${file}" | tee -a "$LOG_FILE"
        echo "Check the error message above for details" | tee -a "$LOG_FILE"
        return 1
    fi
    
    echo "" | tee -a "$LOG_FILE"
}

# Function to run all beginner tutorials
run_beginner_tutorials() {
    echo "=== BEGINNER TUTORIALS ===" | tee -a "$LOG_FILE"
    
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
    echo "=== INTERMEDIATE TUTORIALS ===" | tee -a "$LOG_FILE"
    
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
    echo "=== ADVANCED TUTORIALS ===" | tee -a "$LOG_FILE"
    
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
    echo "=== PROJECT TUTORIALS ===" | tee -a "$LOG_FILE"
    
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
    echo "Manim Tutorial Execution Script" | tee -a "$LOG_FILE"
    echo "==============================" | tee -a "$LOG_FILE"
    
    # Check if manim is installed
    if ! command -v manim &> /dev/null; then
        echo "ERROR: Manim is not installed. Please install it first." | tee -a "$ERROR_LOG"
        echo "ERROR: Manim is not installed. Please install it first." | tee -a "$LOG_FILE"
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
    
    echo "=== EXECUTION COMPLETE ===" | tee -a "$LOG_FILE"
    echo "Execution log saved to: $LOG_FILE"
    echo "Error log saved to: $ERROR_LOG"
}

# Run main function with all arguments
main "$@"