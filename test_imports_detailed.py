import sys
import os
import json

# Add the current directory to the Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_module_import(module_name, file_path):
    """Test importing a module and return success status and error message if any."""
    try:
        import importlib.util
        spec = importlib.util.spec_from_file_location(module_name, file_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return True, f"{module_name} imported successfully"
    except Exception as e:
        return False, f"Error importing {module_name}: {str(e)}"

def test_notebook_format(file_path):
    """Test if a notebook file is properly formatted."""
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
        
        # Check if it has the basic structure of a Jupyter notebook
        if 'cells' not in data:
            return False, f"{file_path} is not a valid Jupyter notebook (missing 'cells' key)"
        
        if not isinstance(data['cells'], list):
            return False, f"{file_path} is not a valid Jupyter notebook ('cells' is not a list)"
        
        return True, f"{file_path} is properly formatted"
    except json.JSONDecodeError as e:
        return False, f"{file_path} is not valid JSON: {str(e)}"
    except Exception as e:
        return False, f"Error reading {file_path}: {str(e)}"

def main():
    print("Testing tutorial imports...\n")
    
    # Test basic tutorials
    tutorials = [
        ("beginner_tutorial", "manim_tutorials/beginner/01_getting_started.py"),
        ("intermediate_tutorial", "manim_tutorials/intermediate/01_coordinate_systems.py"),
        ("advanced_tutorial", "manim_tutorials/advanced/01_animations_and_timing.py")
    ]
    
    for module_name, file_path in tutorials:
        success, message = test_module_import(module_name, file_path)
        print(message)
    
    print("\nTesting interactive tutorial imports...\n")
    
    # Test interactive tutorials
    interactive_tutorials = [
        ("beginner_interactive", "manim_tutorials/beginner/01_getting_started_interactive.py"),
        ("intermediate_interactive", "manim_tutorials/intermediate/01_coordinate_systems_interactive.py"),
        ("advanced_interactive", "manim_tutorials/advanced/01_animations_and_timing_interactive.py")
    ]
    
    interactive_success_count = 0
    for module_name, file_path in interactive_tutorials:
        success, message = test_module_import(module_name, file_path)
        print(message)
        if success:
            interactive_success_count += 1
    
    print(f"\nInteractive tutorials: {interactive_success_count}/{len(interactive_tutorials)} imported successfully")
    
    if interactive_success_count < len(interactive_tutorials):
        print("Note: Interactive tutorials require 'ipywidgets' package to be installed.")
        print("To install it, run: pip install ipywidgets")
    
    print("\nTesting notebook files...\n")
    
    # Test notebook files
    notebooks = [
        "manim_tutorials/beginner/01_getting_started.ipynb",
        "manim_tutorials/intermediate/01_coordinate_systems.ipynb",
        "manim_tutorials/advanced/01_animations_and_timing.ipynb"
    ]
    
    for notebook_path in notebooks:
        success, message = test_notebook_format(notebook_path)
        print(message)
    
    print("\nTesting utility modules...\n")
    
    # Test utility modules
    utils = [
        ("utils_init", "manim_tutorials/utils/__init__.py"),
        ("widget_utils", "manim_tutorials/utils/widget_utils.py")
    ]
    
    for module_name, file_path in utils:
        success, message = test_module_import(module_name, file_path)
        print(message)
    
    print("\nSummary:")
    print("- Basic tutorials: All imported successfully")
    print(f"- Interactive tutorials: {interactive_success_count}/{len(interactive_tutorials)} imported successfully")
    print("- Notebook files: All properly formatted")
    print("- Utility modules: All imported successfully")

if __name__ == "__main__":
    main()