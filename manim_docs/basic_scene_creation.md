TITLE: Manim Python Scene Creation: Square to Circle Animation
DESCRIPTION: Demonstrates how to create a basic Manim scene in Python, defining a `SquareToCircle` animation with transformations and fill properties. This code defines the visual elements and their animation sequence, showing object creation, manipulation, and animation playback.
SOURCE: https://github.com/manimcommunity/manim/blob/main/README.md#_snippet_0

LANGUAGE: python
CODE:
```
from manim import *


class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        square.flip(RIGHT)
        square.rotate(-3 * TAU / 8)
        circle.set_fill(PINK, opacity=0.5)

        self.play(Create(square))
        self.play(Transform(square, circle))
        self.play(FadeOut(square))
```

----------------------------------------

TITLE: Manim Toy Example Scene Definition
DESCRIPTION: Defines a basic Manim scene demonstrating object creation, transformations, updaters, and animations. This example initializes a square and a circle, transforms the square into the circle, adds a dot with an updater that follows the circle's movement, and concludes by fading out all mobjects.
SOURCE: https://github.com/manimcommunity/manim/blob/main/docs/source/guides/deep_dive.rst#_snippet_0

LANGUAGE: python
CODE:
```
from manim import *

class ToyExample(Scene):
    def construct(self):
        orange_square = Square(color=ORANGE, fill_opacity=0.5)
        blue_circle = Circle(color=BLUE, fill_opacity=0.5)
        self.add(orange_square)
        self.play(ReplacementTransform(orange_square, blue_circle, run_time=3))
        small_dot = Dot()
        small_dot.add_updater(lambda mob: mob.next_to(blue_circle, DOWN))
        self.play(Create(small_dot))
        self.play(blue_circle.animate.shift(RIGHT))
        self.wait()
        self.play(FadeOut(blue_circle, small_dot))
```

----------------------------------------

TITLE: Instantiate a Manim Scene Object
DESCRIPTION: Demonstrates the basic instantiation of a Manim scene object. This action triggers the `Scene.__init__` method, which handles initial setup, attribute assignment, and renderer instantiation (either `CairoRenderer` or `OpenGLRenderer`).
SOURCE: https://github.com/manimcommunity/manim/blob/main/docs/source/guides/deep_dive.rst#_snippet_7

LANGUAGE: python
CODE:
```
scene = ToyExample()
```

----------------------------------------

TITLE: Define a Manim Scene to Create a Circle
DESCRIPTION: This Python code defines a Manim Scene class named `CreateCircle`. Within its `construct` method, it creates a `Circle` object, sets its fill color to pink with 50% opacity, and then animates its creation on screen.
SOURCE: https://github.com/manimcommunity/manim/blob/main/docs/source/tutorials/quickstart.rst#_snippet_1

LANGUAGE: python
CODE:
```
from manim import *


class CreateCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        self.play(Create(circle))  # show the circle on screen
```

----------------------------------------

TITLE: Example Manim Local Configuration File
DESCRIPTION: Demonstrates a basic `manim.cfg` file for local scene configuration, setting output file, GIF saving, and background color. This file must be named `manim.cfg` and placed in the same directory as the scene code to be effective.
SOURCE: https://github.com/manimcommunity/manim/blob/main/docs/source/guides/configuration.rst#_snippet_6

LANGUAGE: ini
CODE:
```
[CLI]
# my config file
output_file = myscene
save_as_gif = True
background_color = WHITE
```

----------------------------------------

TITLE: Define Manim Scene Class
DESCRIPTION: Defines the basic canvas class in Manim, representing a scene. It outlines attributes like camera and mobjects, and serves as the fundamental container for visual elements and their animations.
SOURCE: https://github.com/manimcommunity/manim/blob/main/__wiki__/Roadmap.md#_snippet_0

LANGUAGE: python
CODE:
```
class Scene:
	"""
    A scene is Manim's basic canvas.
    """
    # Attributes 
	camera  # <- might be owned by the renderer
    mobjects
    renderer  # <- might be owned by the camera
    
    # Methods
```

----------------------------------------

TITLE: Manim Python Scene Example for High Quality Render
DESCRIPTION: This Python code defines a Manim scene demonstrating basic animation concepts, including creating and styling shapes (Circle, Square), applying transformations (flip, rotate), and animating their appearance and interpolation. This specific scene is used to illustrate the output of high-quality rendering commands.
SOURCE: https://github.com/manimcommunity/manim/blob/main/docs/source/tutorials/output_and_config.rst#_snippet_3

LANGUAGE: python
CODE:
```
class SquareToCircle3(Scene):
    def construct(self):
        circle = Circle()                    # create a circle
        circle.set_fill(PINK, opacity=0.5)   # set color and transparency

        square = Square()                    # create a square
        square.flip(RIGHT)                   # flip horizontally
        square.rotate(-3 * TAU / 8)          # rotate a certain amount

        self.play(Create(square))      # animate the creation of the square
        self.play(Transform(square, circle)) # interpolate the square into the circle
        self.play(FadeOut(square))           # fade out animation
```

----------------------------------------

TITLE: Basic Manim Scene with Circle
DESCRIPTION: This example defines a simple Manim scene named `Example1` that adds a `Circle` object to the display. It utilizes Manim's Jupyter magic command (`%%manim`) for quick rendering with specific output settings like warning suppression and quality.
SOURCE: https://github.com/manimcommunity/manim/blob/main/example_scenes/manim_jupyter_example.ipynb#_snippet_1

LANGUAGE: python
CODE:
```
%%manim -v WARNING --disable_caching -ql -s Example1

class Example1(Scene):
    def construct(self):
        self.add(Circle())
```

----------------------------------------

TITLE: Define and Render a Complete Manim Scene Example
DESCRIPTION: Presents a full Manim scene definition, `ToyExample`, showcasing various animation methods like `ReplacementTransform`, `Create`, `add_updater`, and `animate.shift`. The snippet also includes the necessary programmatic call to render the defined scene using `tempconfig`.
SOURCE: https://github.com/manimcommunity/manim/blob/main/docs/source/guides/deep_dive.rst#_snippet_4

LANGUAGE: python
CODE:
```
from manim import *

class ToyExample(Scene):
    def construct(self):
        orange_square = Square(color=ORANGE, fill_opacity=0.5)
        blue_circle = Circle(color=BLUE, fill_opacity=0.5)
        self.add(orange_square)
        self.play(ReplacementTransform(orange_square, blue_circle, run_time=3))
        small_dot = Dot()
        small_dot.add_updater(lambda mob: mob.next_to(blue_circle, DOWN))
        self.play(Create(small_dot))
        self.play(blue_circle.animate.shift(RIGHT))
        self.wait()
        self.play(FadeOut(blue_circle, small_dot))

with tempconfig({"quality": "medium_quality", "preview": True}):
    scene = ToyExample()
    scene.render()
```

----------------------------------------

TITLE: Basic Manim Voiceover Scene Example
DESCRIPTION: This Python code demonstrates how to create a Manim scene with integrated voiceovers using the `manim-voiceover` plugin. It shows inheriting from `VoiceoverScene`, setting a speech service (e.g., `RecorderService` for live recording), and synchronizing animations with voiceover durations using the `self.voiceover` context manager.
SOURCE: https://github.com/manimcommunity/manim/blob/main/docs/source/guides/add_voiceovers.rst#_snippet_1

LANGUAGE: python
CODE:
```
from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.recorder import RecorderService


# Simply inherit from VoiceoverScene instead of Scene to get all the
# voiceover functionality.
class RecorderExample(VoiceoverScene):
    def construct(self):
        # You can choose from a multitude of TTS services,
        # or in this example, record your own voice:
        self.set_speech_service(RecorderService())

        circle = Circle()

        # Surround animation sections with with-statements:
        with self.voiceover(text="This circle is drawn as I speak.") as tracker:
            self.play(Create(circle), run_time=tracker.duration)
            # The duration of the animation is received from the audio file
            # and passed to the tracker automatically.

        # This part will not start playing until the previous voiceover is finished.
        with self.voiceover(text="Let's shift it to the left 2 units.") as tracker:
            self.play(circle.animate.shift(2 * LEFT), run_time=tracker.duration)
```

----------------------------------------

TITLE: Basic Mobject Addition to Manim Scene
DESCRIPTION: This snippet demonstrates the fundamental way to add a mobject, such as `orange_square`, to a Manim scene using the `self.add()` method within the `construct` function. This action makes the mobject visible and interactive within the animation.
SOURCE: https://github.com/manimcommunity/manim/blob/main/docs/source/guides/deep_dive.rst#_snippet_14

LANGUAGE: Python
CODE:
```
self.add(orange_square)
```

----------------------------------------

TITLE: Manim CLI: Project Management Commands
DESCRIPTION: Introduces command-line tools for streamlined Manim project setup and scene creation. `manim init` sets up default files, `manim new project` creates a new project folder, and `manim new scene` inserts new scenes into files.
SOURCE: https://github.com/manimcommunity/manim/blob/main/docs/source/changelog/0.7.0-changelog.rst#_snippet_4

LANGUAGE: APIDOC
CODE:
```
manim init
  - Quickly sets up default files for a Manim project.
manim new project <project_name>
  - Lets the user set project settings and creates a new project folder.
manim new scene [file_name]
  - Used to quickly insert new scenes into files. Defaults to 'main.py' if file_name is not provided.
```

----------------------------------------

TITLE: Manim Basic Geometric Mobjects
DESCRIPTION: Common pre-defined mobject classes for basic geometric shapes and mathematical constructs, ready for instantiation and display in Manim scenes.
SOURCE: https://github.com/manimcommunity/manim/blob/main/docs/source/tutorials/building_blocks.rst#_snippet_7

LANGUAGE: APIDOC
CODE:
```
Circle:
  - A Mobject representing a circle.

Square:
  - A Mobject representing a square.

Triangle:
  - A Mobject representing a triangle.

Arrow:
  - A Mobject representing an arrow.

Rectangle:
  - A Mobject representing a rectangle.

Axes:
  - A Mobject representing a coordinate axis system.

FunctionGraph:
  - A Mobject for plotting mathematical functions.

BarChart:
  - A Mobject for creating bar charts.
```

----------------------------------------

TITLE: Manim Scene Class and Construct Method Structure
DESCRIPTION: This snippet illustrates the fundamental structure of a Manim animation script. Most animation logic is encapsulated within the `construct` method of a class derived from `Scene`, where objects are created, displayed, and animated.
SOURCE: https://github.com/manimcommunity/manim/blob/main/docs/source/tutorials/quickstart.rst#_snippet_4

LANGUAGE: python
CODE:
```
class CreateCircle(Scene):
    def construct(self):
        [...]
```

----------------------------------------

TITLE: Correctly Defining the Manim Scene `construct` Method
DESCRIPTION: This snippet illustrates the essential structure for a Manim scene, highlighting the `construct` method. It explains that animation code must reside within this method (or be called from it) for Manim to render the scene correctly, preventing common issues like an unexpected black frame output.
SOURCE: https://github.com/manimcommunity/manim/blob/main/docs/source/faq/general.md#_snippet_1

LANGUAGE: python
CODE:
```
class MyAwesomeScene(Scene):
    def construct(self):
        ...
        # your animation code
```

----------------------------------------

TITLE: Render Manim Scene via Command Line Interface
DESCRIPTION: Illustrates how to render a Manim scene using the command line interface. This command specifies a quick mode (`-q`), enables preview (`-p`), points to the Python script (`toy_example.py`), and identifies the scene class (`ToyExample`) to be rendered.
SOURCE: https://github.com/manimcommunity/manim/blob/main/docs/source/guides/deep_dive.rst#_snippet_5

LANGUAGE: bash
CODE:
```
manim -qm -p toy_example.py ToyExample
```

----------------------------------------

TITLE: Displaying and Removing Mobjects in Manim
DESCRIPTION: Demonstrates how to create a basic `Circle` mobject, add it to the scene using `self.add()`, wait for a duration, and then remove it using `self.remove()` within a Manim `Scene`'s `construct` method.
SOURCE: https://github.com/manimcommunity/manim/blob/main/docs/source/tutorials/building_blocks.rst#_snippet_0

LANGUAGE: Python
CODE:
```
class CreatingMobjects(Scene):
    def construct(self):
        circle = Circle()
        self.add(circle)
        self.wait(1)
        self.remove(circle)
        self.wait(1)
```

----------------------------------------

TITLE: Embedding Manim Scene in reStructuredText Documentation
DESCRIPTION: This example demonstrates how to define and embed a Manim animation scene within a reStructuredText (`.rst`) file for documentation purposes. It uses the `.. manim::` directive to specify the scene class to be rendered and includes the `:save_last_frame:` flag to capture only the final state of the animation. The Python code defines a `Formula1` class inheriting from `Scene` that displays a mathematical integral using `MathTex`.
SOURCE: https://github.com/manimcommunity/manim/blob/main/docs/source/contributing/docs/examples.rst#_snippet_0

LANGUAGE: reStructuredText
CODE:
```
Formulas
========

.. manim:: Formula1
    :save_last_frame:

    class Formula1(Scene):
        def construct(self):
            t = MathTex(r"\int_a^b f'(x) dx = f(b) - f(a)")
            self.add(t)
            self.wait(1)
```

----------------------------------------

TITLE: Create a Square to Circle Transformation Animation in Manim
DESCRIPTION: This snippet demonstrates how to create a basic animation in Manim where a square transforms into a circle. It covers creating Mobjects, setting their properties like fill color and opacity, and animating their creation and transformation using `self.play`.
SOURCE: https://github.com/manimcommunity/manim/blob/main/docs/source/tutorials/quickstart.rst#_snippet_7

LANGUAGE: python
CODE:
```
class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set color and transparency

        square = Square()  # create a square
        square.rotate(PI / 4)  # rotate a certain amount

        self.play(Create(square))  # animate the creation of the square
        self.play(Transform(square, circle))  # interpolate the square into the circle
        self.play(FadeOut(square))  # fade out animation
```

LANGUAGE: bash
CODE:
```
manim -pql scene.py SquareToCircle
```

----------------------------------------

TITLE: Manim Scene Class API Reference
DESCRIPTION: Comprehensive documentation for the `Scene` class in Manim, detailing its role as the central component for displaying mobjects, playing animations, and managing time. It outlines key methods like `add`, `remove`, `play`, `wait`, and the `construct` method.
SOURCE: https://github.com/manimcommunity/manim/blob/main/docs/source/tutorials/building_blocks.rst#_snippet_25

LANGUAGE: APIDOC
CODE:
```
Scene Class:
  Description: The connective tissue of manim. Every mobject has to be added to a scene to be displayed, or removed from it to cease being displayed. Every animation has to be played by a scene, and every time interval where no animation occurs is determined by a call to wait. All of the code of your video must be contained in the construct method of a class that derives from Scene. Finally, a single file may contain multiple Scene subclasses if multiple scenes are to be rendered at the same time.
  Methods:
    - add(mobject):
      Description: Adds a mobject to the scene to be displayed.
      Parameters:
        - mobject: The mobject to add to the scene.
    - remove(mobject):
      Description: Removes a mobject from the scene, causing it to cease being displayed.
      Parameters:
        - mobject: The mobject to remove from the scene.
    - play(animation, ...):
      Description: Plays one or more animations.
      Parameters:
        - animation: One or more animation objects to play.
    - wait(duration):
      Description: Pauses the scene for a specified duration.
      Parameters:
        - duration: The time in seconds to wait.
    - construct():
      Description: Abstract method where all video code must be contained. This method is automatically called when the scene is rendered.
```

----------------------------------------

TITLE: Manim Scene: Text, Transformations, and Grid Animations
DESCRIPTION: This Manim scene demonstrates various animation techniques. It shows how to render LaTeX text, arrange objects, perform `Write` and `FadeIn` animations, and apply `Transform` animations. It also includes an example of creating a `NumberPlane` grid and applying a non-linear function to it using `apply_function`.
SOURCE: https://github.com/manimcommunity/manim/blob/main/docs/source/examples.rst#_snippet_29

LANGUAGE: Python
CODE:
```
class OpeningManim(Scene):
    def construct(self):
        title = Tex(r"This is some \LaTeX")
        basel = MathTex(r"\sum_{n=1}^\infty \frac{1}{n^2} = \frac{\pi^2}{6}")
        VGroup(title, basel).arrange(DOWN)
        self.play(
            Write(title),
            FadeIn(basel, shift=DOWN),
        )
        self.wait()

        transform_title = Tex("That was a transform")
        transform_title.to_corner(UP + LEFT)
        self.play(
            Transform(title, transform_title),
            LaggedStart(*[FadeOut(obj, shift=DOWN) for obj in basel]),
        )
        self.wait()

        grid = NumberPlane()
        grid_title = Tex("This is a grid", font_size=72)
        grid_title.move_to(transform_title)

        self.add(grid, grid_title)  # Make sure title is on top of grid
        self.play(
            FadeOut(title),
            FadeIn(grid_title, shift=UP),
            Create(grid, run_time=3, lag_ratio=0.1),
        )
        self.wait()

        grid_transform_title = Tex(
            r"That was a non-linear function \\ applied to the grid"
        )
        grid_transform_title.move_to(grid_title, UL)
        grid.prepare_for_nonlinear_transform()
        self.play(
            grid.animate.apply_function(
                lambda p: p
                          + np.array(
                    [
                        np.sin(p[1]),
                        np.sin(p[0]),
                        0,
                    ]
                )
            ),
            run_time=3,
        )
        self.wait()
        self.play(Transform(grid_title, grid_transform_title))
        self.wait()
```

----------------------------------------

TITLE: Manim Scene and Animation Methods
DESCRIPTION: Documentation for key Manim `Scene` methods for managing mobjects and animations, including how to add mobjects to the scene (controlling Z-order) and play various animation types.
SOURCE: https://github.com/manimcommunity/manim/blob/main/docs/source/tutorials/building_blocks.rst#_snippet_15

LANGUAGE: APIDOC
CODE:
```
.Scene.add(*mobjects)
  - Description: Adds one or more mobjects to the scene. The order of arguments determines their Z-order (display order), with mobjects listed earlier appearing behind those listed later.
  - Parameters:
    - *mobjects: Variable number of mobject instances to add.
  - Usage: `self.add(circle, square, triangle)`

.Scene.play(*animations)
  - Description: Executes one or more animations sequentially. Animations are procedures that interpolate between two states of a mobject.
  - Parameters:
    - *animations: Variable number of animation objects (e.g., `FadeIn`, `Rotate`).
  - Usage: `self.play(FadeIn(square))`

.FadeIn(mobject, **kwargs)
  - Description: An animation that makes a mobject gradually appear by interpolating its opacity from 0.0 (fully transparent) to 1.0 (fully opaque).
  - Parameters:
    - mobject: The mobject to fade in.
    - **kwargs: Additional animation parameters (e.g., `run_time`, `rate_func`).
  - Usage: `FadeIn(square)`

.FadeOut(mobject, **kwargs)
  - Description: An animation that makes a mobject gradually disappear by interpolating its opacity from 1.0 (fully opaque) to 0.0 (fully transparent).
  - Parameters:
    - mobject: The mobject to fade out.
    - **kwargs: Additional animation parameters.
  - Usage: `FadeOut(square)`

.Rotate(mobject, angle, axis=OUT, about_point=None, **kwargs)
  - Description: An animation that rotates a mobject by a specified angle around a given axis or point.
  - Parameters:
    - mobject: The mobject to rotate.
    - angle: The angle of rotation in radians (e.g., `PI/4`).
    - axis: (Optional) The axis of rotation (default is `OUT`, perpendicular to the screen).
    - about_point: (Optional) The point around which the rotation occurs.
    - **kwargs: Additional animation parameters.
  - Usage: `Rotate(square, PI/4)`
```

----------------------------------------

TITLE: Initializing Mobjects for Placement in Manim
DESCRIPTION: Shows the initial creation of `Circle`, `Square`, and `Triangle` mobjects within a Manim `Scene`'s `construct` method, setting them up for subsequent placement operations like `move_to`, `next_to`, and `align_to`.
SOURCE: https://github.com/manimcommunity/manim/blob/main/docs/source/tutorials/building_blocks.rst#_snippet_2

LANGUAGE: Python
CODE:
```
class MobjectPlacement(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        triangle = Triangle()
```

----------------------------------------

TITLE: Initialize Manim Scene Renderer
DESCRIPTION: Illustrates the internal call to initialize the scene's renderer. The `init_scene` method is responsible for instantiating a `SceneFileWriter` object, which acts as Manim's interface to `libav` (FFMPEG) for writing the movie file.
SOURCE: https://github.com/manimcommunity/manim/blob/main/docs/source/guides/deep_dive.rst#_snippet_8

LANGUAGE: python
CODE:
```
self.renderer.init_scene(self)
```

----------------------------------------

TITLE: Programmatic Manim Scene Rendering
DESCRIPTION: Demonstrates how to render a Manim scene directly from a Python script. It uses `tempconfig` to temporarily set rendering quality and enable preview mode, bypassing the command-line interface for scene execution.
SOURCE: https://github.com/manimcommunity/manim/blob/main/docs/source/guides/deep_dive.rst#_snippet_1

LANGUAGE: python
CODE:
```
with tempconfig({"quality": "medium_quality", "preview": True}):
    scene = ToyExample()
    scene.render()
```

----------------------------------------

TITLE: Interactive Scene Embedding for OpenGL
DESCRIPTION: Adds the `interactive_embed` method to the `Scene` class, enabling interactive control of a scene using mouse, keyboard, and an iPython terminal for dynamic commands, specifically for OpenGL rendering.
SOURCE: https://github.com/manimcommunity/manim/blob/main/docs/source/changelog/0.6.0-changelog.rst#_snippet_7

LANGUAGE: APIDOC
CODE:
```
Scene.interactive_embed()
```

----------------------------------------

TITLE: Render Manim Scene from Python File
DESCRIPTION: Command-line instruction to render a specific Manim scene (e.g., `AnimatedSquareToCircle`) from a Python script (`scene.py`) in preview quality (`-pql`). This command executes the Manim engine to generate the animation.
SOURCE: https://github.com/manimcommunity/manim/blob/main/docs/source/tutorials/quickstart.rst#_snippet_12

LANGUAGE: bash
CODE:
```
manim -pql scene.py AnimatedSquareToCircle
```

----------------------------------------

TITLE: Manim Scene Methods: add, remove, and construct
DESCRIPTION: Core methods for managing mobjects within a Manim `Scene`. `construct` defines the animation sequence. `add` displays mobjects, and `remove` hides them from the screen.
SOURCE: https://github.com/manimcommunity/manim/blob/main/docs/source/tutorials/building_blocks.rst#_snippet_4

LANGUAGE: APIDOC
CODE:
```
Scene.construct():
  - The main method within a Scene class where animation logic is defined.
  - Manim executes the code inside this method to generate the video.

Scene.add(*mobjects):
  - Adds one or more mobjects to the scene, making them visible.
  - Parameters:
    - *mobjects: Variable number of Mobject instances to add.

Scene.remove(*mobjects):
  - Removes one or more mobjects from the scene, making them invisible.
  - Parameters:
    - *mobjects: Variable number of Mobject instances to remove.
```

----------------------------------------

TITLE: Render Manim Scene with Different Rotation Techniques
DESCRIPTION: Command-line instruction to render the `DifferentRotations` Manim scene from `scene.py`, showcasing the effects of different rotation animation methods. This allows visual comparison of `.animate` versus `Rotate`.
SOURCE: https://github.com/manimcommunity/manim/blob/main/docs/source/tutorials/quickstart.rst#_snippet_14

LANGUAGE: bash
CODE:
```
manim -pql scene.py DifferentRotations
```

----------------------------------------

TITLE: Execute Manim Scene from Command Line
DESCRIPTION: Shows how to render a Manim scene using the command-line interface. The `-p` flag enables previewing the video file automatically after rendering, and `-ql` sets a lower quality for faster rendering, useful for quick iterations.
SOURCE: https://github.com/manimcommunity/manim/blob/main/README.md#_snippet_1

LANGUAGE: sh
CODE:
```
manim -p -ql example.py SquareToCircle
```

----------------------------------------

TITLE: Render Manim Scene in Low Quality and Play
DESCRIPTION: This command executes Manim on a specified scene file, rendering a particular scene in low quality (480p15) and automatically playing the generated video. The flags `-pql` control playback, quality, and resolution, while `scene.py` and `SquareToCircle` specify the source file and the scene to render.
SOURCE: https://github.com/manimcommunity/manim/blob/main/docs/source/tutorials/output_and_config.rst#_snippet_0

LANGUAGE: bash
CODE:
```
manim -pql scene.py SquareToCircle
```

----------------------------------------

TITLE: Animate Ambient 3D Camera Rotation in Manim
DESCRIPTION: This Manim 3D scene demonstrates continuous ambient rotation of the camera around a 3D scene. It shows how to start and stop the rotation, and then manually move the camera.
SOURCE: https://github.com/manimcommunity/manim/blob/main/docs/source/examples.rst#_snippet_25

LANGUAGE: Python
CODE:
```
    class ThreeDCameraRotation(ThreeDScene):
        def construct(self):
            axes = ThreeDAxes()
            circle=Circle()
            self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
            self.add(circle,axes)
            self.begin_ambient_camera_rotation(rate=0.1)
            self.wait()
            self.stop_ambient_camera_rotation()
            self.move_camera(phi=75 * DEGREES, theta=30 * DEGREES)
            self.wait()
```

----------------------------------------

TITLE: Render a Manim Scene from the Command Line
DESCRIPTION: This command-line instruction renders a specific Manim scene from a Python file. The `-pql` flags indicate that Manim should play the animation, render it in low quality, and quit after rendering.
SOURCE: https://github.com/manimcommunity/manim/blob/main/docs/source/tutorials/quickstart.rst#_snippet_2

LANGUAGE: bash
CODE:
```
manim -pql main.py CreateCircle
```

----------------------------------------

TITLE: Manim Zoomed Scene with Dynamic Camera
DESCRIPTION: This snippet demonstrates the configuration of a `ZoomedScene` in Manim, allowing for a magnified view of a specific area within the scene. It highlights various parameters for customizing the zoom factor, display dimensions, frame stroke width, and camera settings, useful for focusing on intricate details during an animation.
SOURCE: https://github.com/manimcommunity/manim/blob/main/docs/source/examples.rst#_snippet_21

LANGUAGE: Python
CODE:
```
class MovingZoomedSceneAround(ZoomedScene):
# contributed by TheoremofBeethoven, www.youtube.com/c/TheoremofBeethoven
    def __init__(self, **kwargs):
        ZoomedScene.__init__(
            self,
            zoom_factor=0.3,
            zoomed_display_height=1,
            zoomed_display_width=6,
            image_frame_stroke_width=20,
            zoomed_camera_config={
                "default_frame_stroke_width": 3,
                },
            **kwargs
        )
```

----------------------------------------

TITLE: Debugging Manim Scenes in IDEs
DESCRIPTION: This snippet demonstrates how to debug Manim scenes directly within an IDE like VS Code or PyCharm. Instead of running Manim from the command line, you call the `Scene.render()` function directly from your Python file, allowing standard Python debuggers to attach and step through your scene's execution.
SOURCE: https://github.com/manimcommunity/manim/blob/main/__wiki__/FAQ.md#_snippet_0

LANGUAGE: python
CODE:
```
from manim import *

class MyScene(Scene):
    ...

with tempconfig({'quality': 'medium_quality', 'preview': True}):
    scene_object = MyScene()
    scene_object.render()
```

----------------------------------------

TITLE: Manim Scene: Visualize Sine Curve with Unit Circle
DESCRIPTION: This Manim scene visualizes the generation of a sine curve using a unit circle. It sets up axes, draws a unit circle, and animates a dot moving around the circle. It uses `add_updater` to draw a line from the origin to the dot and another line from the dot to the corresponding point on the sine curve, effectively tracing the sine wave.
SOURCE: https://github.com/manimcommunity/manim/blob/main/docs/source/examples.rst#_snippet_30

LANGUAGE: Python
CODE:
```
class SineCurveUnitCircle(Scene):
    # contributed by heejin_park, https://infograph.tistory.com/230
    def construct(self):
        self.show_axis()
        self.show_circle()
        self.move_dot_and_draw_curve()
        self.wait()

    def show_axis(self):
        x_start = np.array([-6,0,0])
        x_end = np.array([6,0,0])

        y_start = np.array([-4,-2,0])
        y_end = np.array([-4,2,0])

        x_axis = Line(x_start, x_end)
        y_axis = Line(y_start, y_end)

        self.add(x_axis, y_axis)
        self.add_x_labels()

        self.origin_point = np.array([-4,0,0])
        self.curve_start = np.array([-3,0,0])

    def add_x_labels(self):
        x_labels = [
            MathTex(r"\pi"), MathTex(r"2 \pi"),
            MathTex(r"3 \pi"), MathTex(r"4 \pi"),
        ]

        for i in range(len(x_labels)):
            x_labels[i].next_to(np.array([-1 + 2*i, 0, 0]), DOWN)
            self.add(x_labels[i])

    def show_circle(self):
        circle = Circle(radius=1)
        circle.move_to(self.origin_point)
        self.add(circle)
        self.circle = circle

    def move_dot_and_draw_curve(self):
        orbit = self.circle
        origin_point = self.origin_point

        dot = Dot(radius=0.08, color=YELLOW)
        dot.move_to(orbit.point_from_proportion(0))
        self.t_offset = 0
        rate = 0.25

        def go_around_circle(mob, dt):
            self.t_offset += (dt * rate)
            # print(self.t_offset)
            mob.move_to(orbit.point_from_proportion(self.t_offset % 1))

        def get_line_to_circle():
            return Line(origin_point, dot.get_center(), color=BLUE)

        def get_line_to_curve():
            x = self.curve_start[0] + self.t_offset * 4
            y = dot.get_center()[1]
            return Line(dot.get_center(), np.array([x,y,0]), color=YELLOW_A, stroke_width=2 )


        self.curve = VGroup()
```

----------------------------------------

TITLE: Manim Core Classes: Mobject, Animation, Scene, and VMobject
DESCRIPTION: Defines the fundamental building blocks of Manim animations. `Mobject` is the abstract base class for all displayable objects. `VMobject` is a specialized `Mobject` using vector graphics. `Animation` represents transformations over time. `Scene` orchestrates mobjects and animations.
SOURCE: https://github.com/manimcommunity/manim/blob/main/docs/source/tutorials/building_blocks.rst#_snippet_3

LANGUAGE: APIDOC
CODE:
```
Mobject:
  - Abstract base class for all displayable objects in Manim.
  - Derived classes like Circle, Square, etc., have visual shapes.

VMobject:
  - Derived from Mobject, uses vector graphics for display.
  - Most common type of mobject encountered.

Animation:
  - Represents a change or transformation applied to mobjects over time.

Scene:
  - The primary container for Manim animations.
  - Orchestrates mobjects and animations within its `construct` method.
```

----------------------------------------

TITLE: Manim Scene Lifecycle Methods
DESCRIPTION: Describes the core methods that define the lifecycle of a Manim animation scene, from initial setup to animation execution and final cleanup. It also includes the rendering completion callback.
SOURCE: https://github.com/manimcommunity/manim/blob/main/docs/source/guides/deep_dive.rst#_snippet_10

LANGUAGE: APIDOC
CODE:
```
.Scene.setup()
  - Purpose: Intended for preparing and setting up the scene for animation.
  - Examples: Adding initial mobjects, assigning custom attributes to the scene class.

.Scene.construct()
  - Purpose: The main script for the animation, containing programmatic descriptions of animations.

.Scene.tear_down()
  - Purpose: For operations to run on the scene after the last frame has been rendered.
  - Examples: Generating a custom thumbnail based on the scene's object state. Relevant when Manim is used within other Python scripts.

.CairoRenderer.scene_finished()
  - Purpose: Gracefully completes the rendering process after setup, construct, and tear_down are run.
  - Behavior: Checks if animations were played; if so,