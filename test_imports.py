import sys
import os

# Add the current directory to the Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    # Test importing beginner tutorial
    import importlib.util
    spec = importlib.util.spec_from_file_location("beginner_tutorial", "manim_tutorials/beginner/01_getting_started.py")
    beginner_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(beginner_module)
    print("Beginner tutorial imported successfully")
except Exception as e:
    print(f"Error importing beginner tutorial: {e}")

try:
    # Test importing intermediate tutorial
    spec = importlib.util.spec_from_file_location("intermediate_tutorial", "manim_tutorials/intermediate/01_coordinate_systems.py")
    intermediate_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(intermediate_module)
    print("Intermediate tutorial imported successfully")
except Exception as e:
    print(f"Error importing intermediate tutorial: {e}")

try:
    # Test importing advanced tutorial
    spec = importlib.util.spec_from_file_location("advanced_tutorial", "manim_tutorials/advanced/01_animations_and_timing.py")
    advanced_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(advanced_module)
    print("Advanced tutorial imported successfully")
except Exception as e:
    print(f"Error importing advanced tutorial: {e}")

try:
    # Test importing beginner interactive tutorial
    spec = importlib.util.spec_from_file_location("beginner_interactive", "manim_tutorials/beginner/01_getting_started_interactive.py")
    beginner_interactive_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(beginner_interactive_module)
    print("Beginner interactive tutorial imported successfully")
except Exception as e:
    print(f"Error importing beginner interactive tutorial: {e}")

try:
    # Test importing intermediate interactive tutorial
    spec = importlib.util.spec_from_file_location("intermediate_interactive", "manim_tutorials/intermediate/01_coordinate_systems_interactive.py")
    intermediate_interactive_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(intermediate_interactive_module)
    print("Intermediate interactive tutorial imported successfully")
except Exception as e:
    print(f"Error importing intermediate interactive tutorial: {e}")

try:
    # Test importing advanced interactive tutorial
    spec = importlib.util.spec_from_file_location("advanced_interactive", "manim_tutorials/advanced/01_animations_and_timing_interactive.py")
    advanced_interactive_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(advanced_interactive_module)
    print("Advanced interactive tutorial imported successfully")
except Exception as e:
    print(f"Error importing advanced interactive tutorial: {e}")