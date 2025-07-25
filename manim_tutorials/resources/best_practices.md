# Manim Best Practices

Guidelines for writing efficient, maintainable, and readable Manim code.

## Code Organization

### Scene Structure
```python
from manim import *

class WellOrganizedScene(Scene):
    def setup(self):
        """Initialize objects and variables used across the scene."""
        self.circle = Circle()
        self.square = Square()
        self.setup_axes()
    
    def construct(self):
        """Main animation sequence."""
        self.introduction()
        self.main_content()
        self.conclusion()
    
    def teardown(self):
        """Cleanup operations (rarely needed)."""
        pass
    
    def introduction(self):
        """Introduction animation sequence."""
        self.play(Create(self.circle))
        self.wait(1)
    
    def main_content(self):
        """Main content animation sequence."""
        self.play(Transform(self.circle, self.square))
        self.wait(1)
    
    def conclusion(self):
        """Conclusion animation sequence."""
        self.play(FadeOut(self.square))
        self.wait(1)
    
    def setup_axes(self):
        """Helper method for creating axes."""
        self.axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[-3, 3, 1]
        )
```

### File Organization
```
project/
├── scenes/
│   ├── introduction.py
│   ├── main_content.py
│   └── conclusion.py
├── utils/
│   ├── helpers.py
│   └── constants.py
├── assets/
│   ├── images/
│   └── sounds/
├── manim.cfg
└── requirements.txt
```

## Naming Conventions

### Variables and Objects
```python
# Good naming practices
background_rectangle = Rectangle(width=10, height=8)
main_circle = Circle(radius=2)
rotating_square = Square(side_length=1)
equation_1 = MathTex("x^2 + y^2 = r^2")
title_text = Text("Pythagorean Theorem")

# Avoid generic names
# obj1, obj2, thing, stuff, etc.
```

### Scene Classes
```python
# Descriptive scene names
class PythagoreanTheoremProof(Scene):
    pass

class DerivativeVisualization(ThreeDScene):
    pass

class FourierSeriesAnimation(Scene):
    pass
```

## Performance Optimization

### Efficient Object Creation
```python
# Efficient: Use VGroup for similar objects
class EfficientCircles(Scene):
    def construct(self):
        # Good: Create all circles at once
        circles = VGroup(*[
            Circle(radius=0.2, color=WHITE)
            for _ in range(50)
        ])
        circles.arrange_in_grid(5, 10, buff=0.1)
        
        self.play(Create(circles, run_time=2))

# Inefficient: Create circles individually
class InefficientCircles(Scene):
    def construct(self):
        # Bad: Create circles one by one
        circles = []
        for i in range(50):
            circle = Circle(radius=0.2, color=WHITE)
            circles.append(circle)
        
        group = VGroup(*circles)
        group.arrange_in_grid(5, 10, buff=0.1)
        
        for circle in circles:
            self.play(Create(circle), run_time=0.01)  # Very slow
```

### Animation Timing
```python
# Appropriate timing for different animations
class ProperTiming(Scene):
    def construct(self):
        circle = Circle()
        
        # Simple creation: 1-2 seconds
        self.play(Create(circle, run_time=1.5))
        
        # Complex transformation: 2-3 seconds
        square = Square()
        self.play(Transform(circle, square, run_time=2.5))
        
        # Movement: proportional to distance
        self.play(circle.animate.shift(RIGHT * 3), run_time=2)
        
        # Rotation: 1-2 seconds for full rotation
        self.play(Rotate(circle, 2*PI, run_time=3))
```

### Memory Management
```python
# Remove objects when no longer needed
class MemoryManagement(Scene):
    def construct(self):
        # Create background elements
        background = VGroup(*[Circle() for _ in range(20)])
        background.arrange_in_grid()
        
        self.add(background)
        self.wait(1)
        
        # Remove background when no longer needed
        self.remove(background)
        
        # Continue with foreground elements
        foreground = Circle(color=RED)
        self.play(Create(foreground))
```

## Code Readability

### Commenting and Documentation
```python
class WellDocumentedScene(Scene):
    def construct(self):
        # Create the main geometric object
        circle = Circle(radius=2, color=BLUE)
        
        # Add styling to make it visually appealing
        circle.set_fill(BLUE, opacity=0.5)
        circle.set_stroke(WHITE, width=5)
        
        # Animate the creation with appropriate timing
        self.play(Create(circle, run_time=2))
        
        # Pause to let the audience appreciate the circle
        self.wait(1)
        
        # Transform to demonstrate the relationship between shapes
        square = Square(side_length=2, color=RED)
        square.set_fill(RED, opacity=0.5)
        self.play(Transform(circle, square, run_time=2))
```

### Modular Code
```python
class ModularScene(Scene):
    def construct(self):
        # Break complex scenes into logical sections
        self.setup_coordinate_system()
        self.plot_function()
        self.highlight_key_points()
        self.show_derivatives()
    
    def setup_coordinate_system(self):
        """Create and display the coordinate system."""
        self.axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-2, 2, 1]
        )
        self.play(Create(self.axes))
    
    def plot_function(self):
        """Plot the main function."""
        self.function = self.axes.plot(lambda x: x**2, color=YELLOW)
        self.play(Create(self.function))
    
    def highlight_key_points(self):
        """Highlight important points on the graph."""
        # Implementation here
        pass
    
    def show_derivatives(self):
        """Visualize the derivative."""
        # Implementation here
        pass
```

## Animation Techniques

### Smooth Transitions
```python
# Use appropriate transition techniques
class SmoothTransitions(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        
        # Good: Clear transformation
        self.play(Create(circle))
        self.wait(0.5)
        self.play(ReplacementTransform(circle, square))
        self.wait(0.5)
        self.play(FadeOut(square))
        
        # Avoid: Abrupt changes without transitions
        # self.add(circle)
        # self.remove(circle)
        # self.add(square)  # Jarring change
```

### Visual Hierarchy
```python
class VisualHierarchy(Scene):
    def construct(self):
        # Main focus object
        main_object = Circle(radius=2, color=YELLOW)
        main_object.set_fill(YELLOW, opacity=0.7)
        
        # Supporting objects
        supporting_objects = VGroup(*[
            Circle(radius=0.3, color=WHITE)
            for _ in range(5)
        ])
        supporting_objects.arrange(RIGHT, buff=0.5)
        supporting_objects.shift(DOWN * 2)
        
        # Animate main object first
        self.play(Create(main_object))
        self.wait(1)
        
        # Then introduce supporting elements
        self.play(Create(supporting_objects))
        self.wait(1)
```

## Error Handling and Debugging

### Defensive Programming
```python
class RobustScene(Scene):
    def construct(self):
        try:
            # Main animation sequence
            self.create_main_visual()
            self.animate_transformation()
        except Exception as e:
            # Handle errors gracefully
            print(f"Animation error: {e}")
            # Fallback animation
            self.fallback_animation()
    
    def create_main_visual(self):
        """Create the main visual element."""
        self.main_object = Circle()
        self.play(Create(self.main_object))
    
    def fallback_animation(self):
        """Simplified animation for error cases."""
        text = Text("Animation Error")
        self.play(Write(text))
```

### Debugging Techniques
```python
class DebuggingScene(Scene):
    def construct(self):
        circle = Circle()
        
        # Debug object properties
        print(f"Circle center: {circle.get_center()}")
        print(f"Circle radius: {circle.radius}")
        
        self.play(Create(circle))
        
        # Debug time information
        print(f"Time after creation: {self.time}")
        
        self.play(circle.animate.shift(RIGHT))
        
        # Debug final position
        print(f"Circle final position: {circle.get_center()}")
```

## Configuration Management

### Custom Configuration Files
```ini
# manim.cfg
[CLI]
# Default quality settings
quality = medium_quality
preview = True

# Output settings
output_file = animations
save_last_frame = False
save_pngs = False

# Performance settings
disable_caching = False
flush_cache = False

# Custom directories
video_dir = ./videos/
images_dir = ./images/
text_dir = ./text/
```

### Environment-Specific Settings
```python
# utils/config.py
from manim import config

class SceneConfig:
    def __init__(self, development=True):
        self.development = development
        self.setup_config()
    
    def setup_config(self):
        if self.development:
            config.quality = "low_quality"
            config.preview = True
        else:
            config.quality = "high_quality"
            config.preview = False
```

## Testing and Validation

### Scene Testing
```python
# test_scenes.py
import unittest
from manim import *
from manim.utils.testing import ManimTestCase

class TestMyScene(ManimTestCase):
    def test_circle_creation(self):
        """Test that circle is created correctly."""
        scene = MyScene()
        scene.render()
        
        # Check that circle was created
        self.assertTrue(any(isinstance(mob, Circle) for mob in scene.mobjects))
    
    def test_animation_sequence(self):
        """Test animation sequence."""
        scene = MyScene()
        scene.construct()
        
        # Check number of animations
        self.assertEqual(len(scene.animations), 3)
```

## Reusability and Extensibility

### Custom Mobjects
```python
class CustomMobject(VMobject):
    """A reusable custom mobject."""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.create_shape()
    
    def create_shape(self):
        """Define the custom shape."""
        # Implementation here
        pass
    
    def animate_creation(self):
        """Define custom creation animation."""
        return Create(self)

class CustomAnimation(Animation):
    """A reusable custom animation."""
    def __init__(self, mobject, custom_param=1, **kwargs):
        self.custom_param = custom_param
        super().__init__(mobject, **kwargs)
    
    def interpolate_mobject(self, alpha):
        """Define custom animation behavior."""
        # Implementation here
        pass
```

### Utility Functions
```python
# utils/helpers.py
from manim import *

def create_labeled_arrow(start, end, label_text, **kwargs):
    """Create an arrow with a label."""
    arrow = Arrow(start, end, **kwargs)
    label = Text(label_text, font_size=24)
    label.next_to(arrow, UP, buff=0.1)
    return VGroup(arrow, label)

def animate_counting(number_line, start, end, run_time=3):
    """Animate counting on a number line."""
    tracker = ValueTracker(start)
    decimal = DecimalNumber(start)
    decimal.add_updater(lambda d: d.set_value(tracker.get_value()))
    
    return AnimationGroup(
        Write(decimal),
        tracker.animate.set_value(end),
        run_time=run_time
    )
```

## Version Control and Collaboration

### Git Best Practices
```
# .gitignore for Manim projects
/media/
/videos/
/images/
/text/
/partial_movie_files/
/__pycache__/
*.pyc
.DS_Store
```

### Documentation Comments
```python
class DocumentedScene(Scene):
    """
    A scene that demonstrates the Pythagorean theorem.
    
    This scene creates a visual proof of the Pythagorean theorem
    using geometric transformations and animations.
    
    Attributes:
        triangle (Polygon): The main right triangle
        squares (VGroup): Squares on each side of the triangle
    """
    
    def construct(self):
        """
        Main animation sequence.
        
        This method creates the triangle, squares, and animates
        the transformation that proves the theorem.
        """
        self.create_triangle()
        self.create_squares()
        self.animate_proof()
```

## Accessibility Considerations

### Color Blindness
```python
class AccessibleColors(Scene):
    def construct(self):
        # Use colorblind-friendly palettes
        colors = [RED, BLUE, GREEN, YELLOW, PURPLE]
        
        # Ensure sufficient contrast
        background = Rectangle(width=10, height=8, color=BLACK, fill_opacity=1)
        self.add(background)
        
        # Add text labels for color-coded elements
        elements = VGroup()
        labels = VGroup()
        
        for i, color in enumerate(colors):
            element = Circle(radius=0.5, color=color, fill_opacity=0.7)
            label = Text(f"Element {i+1}", font_size=20)
            label.next_to(element, DOWN, buff=0.1)
            
            elements.add(element)
            labels.add(label)
        
        group = VGroup(elements, labels)
        group.arrange(RIGHT, buff=0.5)
        self.play(Create(group))
```

## Summary

Following these best practices will help you create:

1. **Efficient** animations that render quickly
2. **Maintainable** code that's easy to update and modify
3. **Readable** scenes that others can understand and contribute to
4. **Robust** implementations that handle errors gracefully
5. **Reusable** components that can be used across projects

Remember to always balance code quality with the needs of your specific project. These are guidelines, not rigid rules, and should be adapted to fit your particular use case.