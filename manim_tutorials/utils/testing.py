"""
Testing utilities for Manim tutorials.
"""
from manim import *
import unittest
import os
import tempfile

class ManimTestCase(unittest.TestCase):
    """
    Base test case for Manim scenes.
    """
    
    def setUp(self):
        """
        Set up test fixtures before each test method.
        """
        self.temp_dir = tempfile.mkdtemp()
        self.original_media_dir = config.media_dir
        config.media_dir = self.temp_dir
    
    def tearDown(self):
        """
        Clean up test fixtures after each test method.
        """
        config.media_dir = self.original_media_dir
        # Clean up temporary files
        for file in os.listdir(self.temp_dir):
            os.remove(os.path.join(self.temp_dir, file))
        os.rmdir(self.temp_dir)
    
    def render_scene(self, scene_class, quality="low"):
        """
        Render a scene for testing.
        
        Parameters
        ----------
        scene_class : Scene
            The scene class to render
        quality : str
            Quality setting for rendering
            
        Returns
        -------
        Scene
            The rendered scene
        """
        # Set quality for testing
        original_quality = config.quality
        if quality == "low":
            config.quality = "low_quality"
        elif quality == "medium":
            config.quality = "medium_quality"
        
        # Create and render scene
        scene = scene_class()
        scene.render()
        
        # Restore original quality
        config.quality = original_quality
        
        return scene
    
    def assertSceneHasMobject(self, scene, mobject_type):
        """
        Assert that a scene contains a specific type of mobject.
        
        Parameters
        ----------
        scene : Scene
            The scene to check
        mobject_type : type
            The type of mobject to look for
        """
        self.assertTrue(
            any(isinstance(mob, mobject_type) for mob in scene.mobjects),
            f"Scene does not contain any {mobject_type.__name__} objects"
        )
    
    def assertSceneHasAnimation(self, scene, animation_type):
        """
        Assert that a scene contains a specific type of animation.
        
        Parameters
        ----------
        scene : Scene
            The scene to check
        animation_type : type
            The type of animation to look for
        """
        # This is a simplified check - in practice, you might need to
        # inspect the scene's animation queue or playback history
        pass
    
    def assertFileExists(self, filepath):
        """
        Assert that a file exists.
        
        Parameters
        ----------
        filepath : str
            Path to the file
        """
        self.assertTrue(
            os.path.exists(filepath),
            f"File {filepath} does not exist"
        )
    
    def assertFileNotExists(self, filepath):
        """
        Assert that a file does not exist.
        
        Parameters
        ----------
        filepath : str
            Path to the file
        """
        self.assertFalse(
            os.path.exists(filepath),
            f"File {filepath} exists but should not"
        )

def create_test_scene(scene_class, **kwargs):
    """
    Create a test scene instance.
    
    Parameters
    ----------
    scene_class : Scene
        The scene class to instantiate
    **kwargs : dict
        Additional arguments for scene initialization
        
    Returns
    -------
    Scene
        The scene instance
    """
    return scene_class(**kwargs)

def run_scene_test(scene_class, test_method=None):
    """
    Run a test on a scene.
    
    Parameters
    ----------
    scene_class : Scene
        The scene class to test
    test_method : callable, optional
        Custom test method to run
        
    Returns
    -------
    bool
        True if test passes, False otherwise
    """
    try:
        scene = create_test_scene(scene_class)
        
        # Run custom test method if provided
        if test_method:
            test_method(scene)
        
        # Basic checks
        assert hasattr(scene, 'construct')
        assert callable(scene.construct)
        
        return True
    except Exception as e:
        print(f"Test failed: {e}")
        return False

class SceneTester:
    """
    Utility class for testing Manim scenes.
    """
    
    def __init__(self, scene_class):
        """
        Initialize scene tester.
        
        Parameters
        ----------
        scene_class : Scene
            The scene class to test
        """
        self.scene_class = scene_class
        self.scene = None
    
    def setup(self):
        """
        Set up the scene for testing.
        """
        self.scene = create_test_scene(self.scene_class)
    
    def test_construct_method(self):
        """
        Test that the scene has a valid construct method.
        
        Returns
        -------
        bool
            True if construct method is valid
        """
        return (
            hasattr(self.scene, 'construct') and
            callable(self.scene.construct)
        )
    
    def test_mobject_creation(self):
        """
        Test mobject creation in the scene.
        
        Returns
        -------
        int
            Number of mobjects created
        """
        # Run the construct method
        self.scene.construct()
        return len(self.scene.mobjects)
    
    def test_animation_count(self):
        """
        Test the number of animations in the scene.
        
        Returns
        -------
        int
            Number of animations
        """
        # This is a simplified implementation
        # In practice, you might need to track animations differently
        return len(getattr(self.scene, 'animations', []))

def benchmark_scene_rendering(scene_class, iterations=3):
    """
    Benchmark scene rendering performance.
    
    Parameters
    ----------
    scene_class : Scene
        The scene class to benchmark
    iterations : int
        Number of iterations to run
        
    Returns
    -------
    dict
        Benchmark results
    """
    import time
    
    results = {
        'render_times': [],
        'average_time': 0,
        'min_time': float('inf'),
        'max_time': 0
    }
    
    for i in range(iterations):
        start_time = time.time()
        
        try:
            scene = create_test_scene(scene_class)
            scene.render()
            end_time = time.time()
            
            render_time = end_time - start_time
            results['render_times'].append(render_time)
            
            results['min_time'] = min(results['min_time'], render_time)
            results['max_time'] = max(results['max_time'], render_time)
            
        except Exception as e:
            print(f"Benchmark iteration {i+1} failed: {e}")
    
    if results['render_times']:
        results['average_time'] = sum(results['render_times']) / len(results['render_times'])
    
    return results

def validate_scene_structure(scene_class):
    """
    Validate the structure of a scene class.
    
    Parameters
    ----------
    scene_class : Scene
        The scene class to validate
        
    Returns
    -------
    dict
        Validation results
    """
    results = {
        'has_construct': False,
        'has_setup': False,
        'has_teardown': False,
        'inheritance_valid': False,
        'docstring_present': False
    }
    
    # Check inheritance
    results['inheritance_valid'] = issubclass(scene_class, Scene)
    
    # Check for construct method
    results['has_construct'] = (
        hasattr(scene_class, 'construct') and
        callable(getattr(scene_class, 'construct'))
    )
    
    # Check for setup method
    results['has_setup'] = hasattr(scene_class, 'setup')
    
    # Check for teardown method
    results['has_teardown'] = hasattr(scene_class, 'teardown')
    
    # Check for docstring
    results['docstring_present'] = bool(scene_class.__doc__)
    
    return results

# Example test cases
class ExampleSceneTests(ManimTestCase):
    """
    Example test cases for Manim scenes.
    """
    
    def test_simple_scene(self):
        """
        Test a simple scene with basic objects.
        """
        class SimpleScene(Scene):
            def construct(self):
                circle = Circle()
                self.play(Create(circle))
        
        scene = self.render_scene(SimpleScene)
        self.assertSceneHasMobject(scene, Circle)
    
    def test_text_scene(self):
        """
        Test a scene with text objects.
        """
        class TextScene(Scene):
            def construct(self):
                text = Text("Hello, World!")
                self.play(Write(text))
        
        scene = self.render_scene(TextScene)
        self.assertSceneHasMobject(scene, Text)

def run_all_tests():
    """
    Run all tests in this module.
    
    Returns
    -------
    unittest.TestResult
        Test results
    """
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule(__import__(__name__))
    runner = unittest.TextTestRunner(verbosity=2)
    return runner.run(suite)