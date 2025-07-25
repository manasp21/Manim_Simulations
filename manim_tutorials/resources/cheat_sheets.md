# Manim Cheat Sheets

Quick reference guides for common Manim operations and syntax.

## Basic Scene Structure

```python
from manim import *

class MyScene(Scene):
    def construct(self):
        # Your animation code here
        circle = Circle()
        self.play(Create(circle))
        self.wait(1)
```

## Common Mobjects

### Geometric Shapes
```python
# Basic shapes
circle = Circle()
square = Square()
triangle = Triangle()
rectangle = Rectangle()
polygon = Polygon(point1, point2, point3, ...)
ellipse = Ellipse()
arrow = Arrow(start, end)
line = Line(start, end)

# 3D shapes
sphere = Sphere()
cube = Cube()
prism = Prism()
```

### Text Objects
```python
# Simple text
text = Text("Hello World")

# Mathematical expressions
math = MathTex(r"\int_0^\infty e^{-x^2} dx")

# LaTeX text
latex = Tex(r"\LaTeX")

# Markup text (for styling)
markup = MarkupText("Red <span fgcolor='RED'>text</span>")
```

## Common Animations

### Creation Animations
```python
# Create objects
self.play(Create(circle))
self.play(Write(text))
self.play(DrawBorderThenFill(square))
self.play(ShowCreationThenFadeOut(temp_object))
```

### Transformation Animations
```python
# Transform one object to another
self.play(Transform(circle, square))

# Replace object with another
self.play(ReplacementTransform(circle, square))

# Fade animations
self.play(FadeIn(object))
self.play(FadeOut(object))
```

### Movement Animations
```python
# Shift object
self.play(object.animate.shift(RIGHT))
self.play(object.animate.shift(UP * 2))

# Move to specific location
self.play(object.animate.move_to(position))

# Rotate object
self.play(Rotate(object, angle=PI))
self.play(object.animate.rotate(PI/2))
```

## Positioning and Arrangement

### Relative Positioning
```python
# Position relative to other objects
object.next_to(reference, direction, buff=0.5)
object.shift(direction * distance)
object.move_to(position)
object.align_to(reference, direction)

# Common directions
UP, DOWN, LEFT, RIGHT
UR, UL, DR, DL  # Up-right, up-left, etc.
```

### Group Arrangement
```python
# Arrange objects
objects.arrange(direction, buff=0.5)
objects.arrange_in_grid(rows, cols, buff=0.5)

# Create groups
group = VGroup(object1, object2, object3)
group = VDict({"key1": object1, "key2": object2})
```

## Styling

### Color and Fill
```python
# Set color
object.set_color(RED)
object.set_color_by_gradient(RED, BLUE, GREEN)

# Set fill
object.set_fill(color=BLUE, opacity=0.5)

# Set stroke
object.set_stroke(color=WHITE, width=5, opacity=1)
```

### Text Styling
```python
# Font properties
text = Text("Hello", font_size=36, font="Arial", weight="BOLD", slant="ITALIC")

# Color parts of MathTex
equation = MathTex("a", "+", "b", "=", "c")
equation[0].set_color(RED)  # Color first part
equation[2].set_color(BLUE)  # Color third part
```

## Coordinate Systems

### Axes and Planes
```python
# Create axes
axes = Axes(
    x_range=[-5, 5, 1],
    y_range=[-3, 3, 1],
    axis_config={"color": BLUE}
)

# Number plane
plane = NumberPlane()

# 3D axes
axes3d = ThreeDAxes()
```

### Plotting Functions
```python
# Plot a function
graph = axes.plot(lambda x: x**2, color=RED)

# Plot a parametric function
parametric = axes.plot_parametric_curve(
    lambda t: [t, np.sin(t), 0],
    t_range=[-PI, PI]
)
```

## 3D Scenes

### Basic 3D Setup
```python
class My3DScene(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        
        # 3D objects
        sphere = Sphere()
        cube = Cube()
        
        self.play(Create(sphere))
        self.play(Create(cube))
```

### Camera Controls
```python
# Move camera
self.move_camera(phi=45 * DEGREES, theta=-45 * DEGREES)

# Rotate camera
self.begin_ambient_camera_rotation(rate=0.1)
self.wait(5)
self.stop_ambient_camera_rotation()
```

## Updaters

### Time-Based Updaters
```python
# Add updater function
def update_function(mob, dt):
    mob.shift(RIGHT * dt)  # Move right at 1 unit/second

object.add_updater(update_function)

# Remove updaters
object.clear_updaters()
```

### Value Trackers
```python
# Create value tracker
tracker = ValueTracker(0)

# Use in updaters
decimal = DecimalNumber(0)
decimal.add_updater(lambda d: d.set_value(tracker.get_value()))

# Animate tracker
self.play(tracker.animate.set_value(10))
```

## Configuration

### Quality Settings
```bash
# Low quality (480p15)
manim -ql scene.py SceneName

# Medium quality (720p30)
manim -qm scene.py SceneName

# High quality (1080p60)
manim -qh scene.py SceneName

# Production quality (2160p60)
manim -qp scene.py SceneName
```

### Custom Configuration
```ini
# manim.cfg
[CLI]
quality = high_quality
preview = True
save_last_frame = False
```

## Useful Constants

### Directions
```python
UP, DOWN, LEFT, RIGHT
UR, UL, DR, DL
IN, OUT
ORIGIN = [0, 0, 0]
```

### Colors
```python
RED, GREEN, BLUE, YELLOW, PURPLE, ORANGE, PINK, WHITE, BLACK
GREY, DARK_GREY, LIGHT_GREY
TEAL, MAROON, LIME, OLIVE, NAVY, DARK_BROWN, LIGHT_BROWN
```

### Mathematical Constants
```python
PI, TAU  # TAU = 2 * PI
DEGREES  # For degree conversions
```

## Common Patterns

### Animation Sequences
```python
# Sequential animations
self.play(Create(circle))
self.play(circle.animate.shift(RIGHT))
self.play(FadeOut(circle))

# Parallel animations
self.play(
    circle.animate.shift(LEFT),
    square.animate.shift(RIGHT)
)

# Staggered animations
self.play(
    AnimationGroup(
        Create(circle),
        Create(square),
        Create(triangle),
        lag_ratio=0.5
    )
)
```

### Scene Organization
```python
class OrganizedScene(Scene):
    def setup(self):
        # Setup code (runs before construct)
        pass
    
    def construct(self):
        # Main animation code
        pass
    
    def teardown(self):
        # Cleanup code (runs after construct)
        pass
```

## Debugging Tips

### Verbose Output
```bash
# Debug mode
manim -v DEBUG scene.py SceneName

# Show output directory
manim -v INFO scene.py SceneName
```

### Common Debugging Code
```python
# Print object information
print(f"Object position: {object.get_center()}")

# Print time information
print(f"Current time: {self.time}")

# Check if object is in scene
print(f"Object in scene: {object in self.mobjects}")
```

## Performance Tips

### Optimization Techniques
```python
# Use VGroup for similar objects
group = VGroup(*[Circle() for _ in range(100)])

# Use appropriate run_time
self.play(Create(object, run_time=2))  # Not too fast or slow

# Disable caching for simple scenes
# manim --disable_caching scene.py SceneName
```

This cheat sheet covers the most commonly used Manim features. For more detailed information, refer to the official documentation at https://docs.manim.community/