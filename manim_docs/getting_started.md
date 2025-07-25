TITLE: Import Manim Library
DESCRIPTION: This snippet imports all necessary components from the Manim library, making them available for use in any Manim scene or animation script. It's a standard starting point for Manim projects.
SOURCE: https://github.com/manimcommunity/manim/blob/main/example_scenes/manim_jupyter_example.ipynb#_snippet_0

LANGUAGE: python
CODE:
```
from manim import *
```

----------------------------------------

TITLE: Python Manim Import Statement
DESCRIPTION: A standard Python import statement used to bring the Manim library into a Python script, enabling access to its functionalities. This is a basic example for starting a Manim project.
SOURCE: https://github.com/manimcommunity/manim/blob/main/docs/source/installation/uv.md#_snippet_11

LANGUAGE: python
CODE:
```
import manim
```

----------------------------------------

TITLE: Install Manim Plugin Template for Development
DESCRIPTION: Installs the `manim-plugintemplate` package, which serves as an in-depth tutorial and a starting point for creating new Manim plugins. It provides a structured example for plugin development.
SOURCE: https://github.com/manimcommunity/manim/blob/main/docs/source/plugins.rst#_snippet_4

LANGUAGE: bash
CODE:
```
pip install manim-plugintemplate
```

----------------------------------------

TITLE: Animate Square to Circle Transformation with Dynamic Properties
DESCRIPTION: Demonstrates how to create a square, rotate it, and transform it into a circle using Manim's `.animate` property for dynamic property changes like rotation and fill color. This method interpolates between start and end states, showing the animation of property changes.
SOURCE: https://github.com/manimcommunity/manim/blob/main/docs/source/tutorials/quickstart.rst#_snippet_11

LANGUAGE: python
CODE:
```
class AnimatedSquareToCircle2(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        square = Square()  # create a square

        self.play(Create(square))  # show the square on screen
        self.play(square.animate.rotate(PI / 4))  # rotate the square
        self.play(Transform(square, circle))  # transform the square into a circle
        self.play(square.animate.set_fill(PINK, opacity=0.5))  # color the circle on screen
```

----------------------------------------

TITLE: Initialize a New Manim Project
DESCRIPTION: This command initializes a new Manim project with a default folder structure. It creates a root folder for your project, including necessary Manim files and output directories.
SOURCE: https://github.com/manimcommunity/manim/blob/main/docs/source/tutorials/quickstart.rst#_snippet_0

LANGUAGE: bash
CODE:
```
manim init project my-project --default
```

----------------------------------------

TITLE: Start a Named Manim Docker Container
DESCRIPTION: This command starts a previously created and stopped named Docker container (`my-manim-container`) in the background. It is a prerequisite for executing commands within the container using `docker exec` or accessing its services.
SOURCE: https://github.com/manimcommunity/manim/blob/main/docs/source/installation/docker.rst#_snippet_2

LANGUAGE: sh
CODE:
```
docker start my-manim-container
```

----------------------------------------

TITLE: Initialize Manim Project with uv
DESCRIPTION: Instructions to create a new Python project directory, navigate into it, and add Manim as a dependency using `uv`. This process is applicable across Windows, MacOS, and Linux operating systems.
SOURCE: https://github.com/manimcommunity/manim/blob/main/docs/source/installation/uv.md#_snippet_4

LANGUAGE: bash
CODE:
```
uv init manimations
cd manimations
uv add manim
```

----------------------------------------

TITLE: Manim Output Container Setup and Animation Beginning
DESCRIPTION: Details the process of opening an output container for rendered frames using `SceneFileWriter` and `libav`. It also explains how animations are formally "begun" by calling their setup methods, adding new mobjects to the scene, and preparing mobjects for their initial animation state.
SOURCE: https://github.com/manimcommunity/manim/blob/main/docs/source/guides/deep_dive.rst#_snippet_21

LANGUAGE: APIDOC
CODE:
```
Manim Output Container Setup
  - Initiator: SceneFileWriter.
  - Process: Opens an output container via a call to libav.
  - Access: The container is accessible via the 'output_container' attribute of the file writer.
  - Purpose: To write rendered raw frames.

Manim Animation Beginning
  - Methods Called: Animation._setup_scene(), Animation.begin().
  - Mobject Introduction: Mobjects newly introduced by an animation (e.g., via Create) are added to the scene.
  - Updater Suspension: Updater functions on the animation's mobject are suspended.
  - Initial State: The mobject is set to the state corresponding to the first frame of the animation.
```

----------------------------------------

TITLE: List of Required LaTeX Packages for Manim
DESCRIPTION: A comprehensive list of LaTeX packages that Manim requires. This is particularly useful for users setting up minimal LaTeX distributions like TinyTeX, ensuring all necessary components for Manim's rendering capabilities are present.
SOURCE: https://github.com/manimcommunity/manim/blob/main/docs/source/installation/uv.md#_snippet_3

LANGUAGE: text
CODE:
```
amsmath babel-english cbfonts-fd cm-super count1to ctex doublestroke dvisvgm everysel
fontspec frcursive fundus-calligra gnu-freefont jknapltx latex-bin
mathastext microtype multitoc physics preview prelim2e ragged2e relsize rsfs
setspace standalone tipa wasy wasysym xcolor xetex xkeyval
```

----------------------------------------

TITLE: Initialize a New Manim Project with Specific Python Version using uv
DESCRIPTION: This snippet demonstrates how to create a new Python project directory (`manimations`) with a specified Python version (3.12) using `uv init`, navigate into the new directory, and then add the `manim` package to the environment using `uv add`. This sets up a dedicated virtual environment for your Manim project.
SOURCE: https://github.com/manimcommunity/manim/blob/main/docs/source/installation/uv.md#_snippet_14

LANGUAGE: Shell
CODE:
```
uv init --python 3.12 manimations
cd manimations
uv add manim
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

TITLE: Assigning Data to Manim OpenGLMobject Attributes
DESCRIPTION: Shows how to assign a NumPy array of XYZ points to the `points` attribute of an `OpenGLMobject` instance, which then gets processed for the vertex shader.
SOURCE: https://github.com/manimcommunity/manim/blob/main/__wiki__/Developer-documentation-(WIP).md#_snippet_4

LANGUAGE: python
CODE:
```
self.points = points # numpy array containing xyz points with shape (n, 3)
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

TITLE: Create and Style a Manim Mobject
DESCRIPTION: This code demonstrates how to instantiate a `Circle` object, which is a type of `Mobject` in Manim. It then applies visual styling by setting the fill color to pink and adjusting its opacity.
SOURCE: https://github.com/manimcommunity/manim/blob/main/docs/source/tutorials/quickstart.rst#_snippet_5

LANGUAGE: python
CODE:
```
circle = Circle()  # create a circle
circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
```

----------------------------------------

TITLE: Get Global uv Tool Directory
DESCRIPTION: Command to retrieve the base directory where `uv` stores its globally installed tools. This is useful for configuring IDEs to properly locate and resolve Manim's environment when installed as a global tool.
SOURCE: https://github.com/manimcommunity/manim/blob/main/docs/source/installation/uv.md#_snippet_13

LANGUAGE: bash
CODE:
```
uv tool dir
```

----------------------------------------

TITLE: Install Manim with Pixi
DESCRIPTION: This snippet shows how to initialize a new project with `pixi` and add Manim as a dependency. `pixi` automatically manages the environment and installs Manim along with its required dependencies.
SOURCE: https://github.com/manimcommunity/manim/blob/main/docs/source/installation/conda.rst#_snippet_1

LANGUAGE: bash
CODE:
```
pixi init
pixi add manim
```

----------------------------------------

TITLE: Access Mobject Coordinates in Manim Python
DESCRIPTION: Illustrates how to retrieve various coordinate points (start, end, center, top, bottom) from a Manim mobject using methods like `get_start()` and `get_center()`. It also shows how to add visual indicators (Dots) at these specific points on the screen.
SOURCE: https://github.com/manimcommunity/manim/blob/main/docs/source/tutorials/building_blocks.rst#_snippet_22

LANGUAGE: python
CODE:
```
class MobjectExample(Scene):
    def construct(self):
        p1 = [-1,-1, 0]
        p2 = [ 1,-1, 0]
        p3 = [ 1, 1, 0]
        p4 = [-1, 1, 0]
        a  = Line(p1,p2).append_points(Line(p2,p3).points).append_points(Line(p3,p4).points)
        point_start  = a.get_start()
        point_end    = a.get_end()
        point_center = a.get_center()
        self.add(Text(f"a.get_start() = {np.round(point_start,2).tolist()}", font_size=24).to_edge(UR).set_color(YELLOW))
        self.add(Text(f"a.get_end() = {np.round(point_end,2).tolist()}", font_size=24).next_to(self.mobjects[-1],DOWN).set_color(RED))
        self.add(Text(f"a.get_center() = {np.round(point_center,2).tolist()}", font_size=24).next_to(self.mobjects[-1],DOWN).set_color(BLUE))

        self.add(Dot(a.get_start()).set_color(YELLOW).scale(2))
        self.add(Dot(a.get_end()).set_color(RED).scale(2))
        self.add(Dot(a.get_top()).set_color(GREEN_A).scale(2))
        self.add(Dot(a.get_bottom()).set_color(GREEN_D).scale(2))
        self.add(Dot(a.get_center()).set_color(BLUE).scale(2))
        self.add(Dot(a.point_from_proportion(0.5)).set_color(ORANGE).scale(2))
        self.add(*[Dot(x) for x in a.points])
        self.add(a)
```

----------------------------------------

TITLE: Manim Library Import Statement
DESCRIPTION: This line imports all public names from the Manim library into the current namespace. It is the recommended way to use Manim, as scripts often utilize multiple components from the library.
SOURCE: https://github.com/manimcommunity/manim/blob/main/docs/source/tutorials/quickstart.rst#_snippet_3

LANGUAGE: python
CODE:
```
from manim import *
```

----------------------------------------

TITLE: Install Linux System Dependencies (Arch Linux/pacman)
DESCRIPTION: Installs base development tools, Cairo, and Pango on Arch Linux systems using `pacman`. These packages are essential for compiling Manim's dependencies.
SOURCE: https://github.com/manimcommunity/manim/blob/main/docs/source/installation/uv.md#_snippet_9

LANGUAGE: bash
CODE:
```
sudo pacman -Syu base-devel cairo pango
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

TITLE: Install Optional Manim Dependencies with uv
DESCRIPTION: Installs additional, optional dependency groups defined in the `pyproject.toml` file using `uv`. `--all-extras` installs all available optional groups, while `--extra <group_name>` installs a specific one, such as `jupyterhub`.
SOURCE: https://github.com/manimcommunity/manim/blob/main/docs/source/contributing/development.md#_snippet_4

LANGUAGE: shell
CODE:
```
uv sync --all-extras
```

LANGUAGE: shell
CODE:
```
uv sync --extra jupyterhub
```

----------------------------------------

TITLE: Install Linux System Dependencies (Debian/apt)
DESCRIPTION: Commands to update package lists and install necessary build tools, Python development headers, Cairo, and Pango development headers on Debian-based Linux distributions using `apt`.
SOURCE: https://github.com/manimcommunity/manim/blob/main/docs/source/installation/uv.md#_snippet_7

LANGUAGE: bash
CODE:
```
sudo apt update
sudo apt install build-essential python3-dev libcairo2-dev libpango1.0-dev
```

----------------------------------------

TITLE: Install TeX Live for LaTeX on Linux
DESCRIPTION: Commands for installing the full TeX Live distribution on common Linux systems. LaTeX is optional but recommended for rendering complex mathematical formulas in Manim animations.
SOURCE: https://github.com/manimcommunity/manim/blob/main/docs/source/installation/uv.md#_snippet_2

LANGUAGE: bash
CODE:
```
sudo apt install texlive-full
```

LANGUAGE: bash
CODE:
```
sudo dnf install texlive-scheme-full
```

----------------------------------------

TITLE: Define Manim Plugin Entry Point in pyproject.toml
DESCRIPTION: Specifies how Manim discovers plugins available in the user's environment by defining an entry point in `pyproject.toml`. The `name` is the plugin's identifier, and `object_reference` points to its main module or function within the package.
SOURCE: https://github.com/manimcommunity/manim/blob/main/docs/source/plugins.rst#_snippet_5

LANGUAGE: toml
CODE:
```
[project.entry-points."manim.plugins"]
"name" = "object_reference"
```

----------------------------------------

TITLE: Adding Custom LaTeX Packages to Manim
DESCRIPTION: This code shows how to load additional LaTeX packages, such as `mathrsfs`, by adding them to the preamble of a `TexTemplate`. This is necessary to use commands like `\mathscr` that are not included in Manim's default LaTeX setup.
SOURCE: https://github.com/manimcommunity/manim/blob/main/docs/source/guides/using_text.rst#_snippet_20

LANGUAGE: Python
CODE:
```
class AddPackageLatex(Scene):
    def construct(self):
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{mathrsfs}")
        tex = Tex(
            r"$\mathscr{H} \rightarrow \mathbb{H}$",
            tex_template=myTemplate,
            font_size=144,
        )
        self.add(tex)
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

TITLE: Initialize Manim Global Configuration System
DESCRIPTION: Shows an internal Manim import responsible for initializing the library's global configuration system. This line processes configuration options from `.cfg` files and integrates command-line arguments, setting up the environment for scene rendering.
SOURCE: https://github.com/manimcommunity/manim/blob/main/docs/source/guides/deep_dive.rst#_snippet_3

LANGUAGE: python
CODE:
```
from ._config import *
```

----------------------------------------

TITLE: Play a Manim Animation
DESCRIPTION: This line executes an animation within a Manim scene. The `self.play()` method is used to display the `Create` animation, which makes the `circle` object appear on the screen.
SOURCE: https://github.com/manimcommunity/manim/blob/main/docs/source/tutorials/quickstart.rst#_snippet_6

LANGUAGE: python
CODE:
```
self.play(Create(circle))  # show the circle on screen
```

----------------------------------------

TITLE: Install Python using uv
DESCRIPTION: Command to install the latest compatible version of Python using the `uv` environment manager. This is the first step in setting up the Python environment for Manim.
SOURCE: https://github.com/manimcommunity/manim/blob/main/docs/source/installation/uv.md#_snippet_1

LANGUAGE: bash
CODE:
```
uv python install
```

----------------------------------------

TITLE: Type Hinting for Manim Colors
DESCRIPTION: Provides an example of how to type hint functions dealing with Manim colors, specifically using `ParsableManimColor` for flexibility when any color type (RGB, RGBA, HSV) is acceptable. This snippet is typically used within a `TYPE_CHECKING` block to avoid runtime import issues.
SOURCE: https://github.com/manimcommunity/manim/blob/main/docs/source/contributing/docs/types.rst#_snippet_2

LANGUAGE: python
CODE:
```
if TYPE_CHECKING:
    from manim.utils.color import ParsableManimColor

# type hint stuff with ParsableManimColor
```

----------------------------------------

TITLE: Resolving ManimPango Build Errors
DESCRIPTION: Command to install Cython, which frequently resolves issues where `manimpango/cmanimpango.c` cannot be found during Manim installation. This problem typically occurs when the system needs to build a ManimPango wheel locally.
SOURCE: https://github.com/manimcommunity/manim/blob/main/docs/source/faq/installation.md#_snippet_5

LANGUAGE: bash
CODE:
```
pip3 install Cython
```

----------------------------------------

TITLE: Manim Mobject Positioning Method: next_to
DESCRIPTION: Documentation for the `next_to` method of Manim's `Mobject` class, used for positioning Mobjects relative to a reference point. It details parameters for specifying the reference object, direction, and buffer distance.
SOURCE: https://github.com/manimcommunity/manim/blob/main/docs/source/tutorials/quickstart.rst#_snippet_10

LANGUAGE: APIDOC
CODE:
```
Mobject.next_to(reference_mobject, direction, buff=0.5)
  - Positions the Mobject relative to another Mobject.
  - Parameters:
    - reference_mobject: The Mobject to position relative to.
    - direction: The direction relative to the reference_mobject (e.g., RIGHT, LEFT, UP, DOWN).
    - buff: (Optional) A float specifying the buffer distance between the two Mobjects.
  - Returns: The Mobject itself, after being positioned.
  - Usage Example: square.next_to(circle, RIGHT, buff=0.5)
```

----------------------------------------

TITLE: Install Manim and Dependencies in Google Colaboratory
DESCRIPTION: This set of shell commands installs Manim and its required dependencies (like Cairo, TeX Live, and Pango) within a Google Colaboratory environment. It first updates apt, then installs system libraries, and finally uses pip to install Manim and a specific IPython version. A runtime restart is required after execution.
SOURCE: https://github.com/manimcommunity/manim/blob/main/docs/source/installation/jupyter.rst#_snippet_1

LANGUAGE: bash
CODE:
```
!sudo apt update
!sudo apt install libcairo2-dev \
    texlive texlive-latex-extra texlive-fonts-extra \
    texlive-latex-recommended texlive-science \
    tipa libpango1.0-dev
!pip install manim
!pip install IPython==8.21.0
```

----------------------------------------

TITLE: Install Manim as a Global uv Tool
DESCRIPTION: Installs Manim as a system-wide `uv`-managed tool, making the `manim` executable directly available on the PATH without requiring virtual environment activation. This is an alternative installation method for users with multiple Manim projects.
SOURCE: https://github.com/manimcommunity/manim/blob/main/docs/source/installation/uv.md#_snippet_12

LANGUAGE: bash
CODE:
```
uv tool install manim
```

----------------------------------------

TITLE: Manim Mobject Initialization Hierarchy
DESCRIPTION: Documents the inheritance and constructor call chain for Manim mobjects, tracing the initialization flow from `Square` through `Rectangle`, `Polygon`, `Polygram`, and finally `VMobject`. It explains how attributes like `side_length`, `width`, and `height` are handled and how points are set in the lower-level classes.
SOURCE: https://github.com/manimcommunity/manim/blob/main/docs/source/guides/deep_dive.rst#_snippet_13

LANGUAGE: APIDOC
CODE:
```
Square(color=ORANGE, fill_opacity=0.5)
  - Purpose: Initializes a square mobject with specified color and opacity.
  - Calls: Square.__init__
  - Delegates to: Rectangle.__init__ via super()

Rectangle.__init__(UR, UL, DL, DR, color, width, height, **kwargs)
  - Purpose: Initializes a rectangle mobject from corner points.
  - Calls: Polygon.__init__ via super()
  - Operations:
    - super().__init__(UR, UL, DL, DR, color=color, **kwargs)
    - self.stretch_to_fit_width(width)
    - self.stretch_to_fit_height(height)

Polygon.__init__(corners, color, **kwargs)
  - Purpose: Initializes a polygon mobject from a list of corner points.
  - Calls: Polygram.__init__ via super()

Polygram.__init__(...)
  - Purpose: Initializes a polygram mobject, handling the base structure for polygons.
  - Calls: VMobject.__init__ via super()
  - Operations: Sets points using VMobject.start_new_path and VMobject.add_points_as_corners.

VMobject.__init__(...)
  - Purpose: Base initializer for all vectorized mobjects, setting up attributes related to Bézier curve construction.

Scene.construct()
  - Purpose: The primary method in a Manim scene where mobjects are created, configured, and animations are defined.
```

----------------------------------------

TITLE: Install Linux System Dependencies (Fedora/dnf)
DESCRIPTION: Installs Python development headers, `pkg-config`, Cairo, and Pango development headers on Fedora Linux systems using `dnf`. These are required for building Manim's dependencies from source.
SOURCE: https://github.com/manimcommunity/manim/blob/main/docs/source/installation/uv.md#_snippet_8

LANGUAGE: bash
CODE:
```
sudo dnf install python3-devel pkg-config cairo-devel pango-devel
```

----------------------------------------

TITLE: Positioning Manim Mobjects Relative to Each Other
DESCRIPTION: This example illustrates how to position Manim Mobjects relative to each other using the `next_to` method. It shows how to specify a reference Mobject, a direction (e.g., `RIGHT`), and a buffer distance to precisely arrange objects on the screen.
SOURCE: https://github.com/manimcommunity/manim/blob/main/docs/source/tutorials/quickstart.rst#_snippet_8

LANGUAGE: python
CODE:
```
class SquareAndCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency

        square = Square()  # create a square
        square.set_fill(BLUE, opacity=0.5)  # set the color and transparency

        square.next_to(circle, RIGHT, buff=0.5)  # set the position
        self.play(Create(circle), Create(square))  # show the shapes on screen
```

LANGUAGE: bash
CODE:
```
manim -pql scene.py SquareAndCircle
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

TITLE: Verify Manim Installation
DESCRIPTION: Executes a health check command to confirm that Manim is correctly installed and operational within the local `uv`-managed Python environment. This step ensures Manim is ready for use.
SOURCE: https://github.com/manimcommunity/manim/blob/main/docs/source/installation/uv.md#_snippet_10

LANGUAGE: bash
CODE:
```
uv run manim checkhealth
```

----------------------------------------

TITLE: Install MacOS System Dependencies with Homebrew
DESCRIPTION: Installs `cairo` and `pkg-config`, essential system utilities for Manim's `pycairo` dependency, using Homebrew on MacOS. These are prerequisites for a successful Manim installation.
SOURCE: https://github.com/manimcommunity/manim/blob/main/docs/source/installation/uv.md#_snippet_6

LANGUAGE: bash
CODE:
```
brew install cairo pkg-config
```

----------------------------------------

TITLE: Installing Manim with Chocolatey
DESCRIPTION: Command for installing Manim using Chocolatey on Windows. It is crucial to run this command with administrator permissions to prevent installation failures.
SOURCE: https://github.com/manimcommunity/manim/blob/main/docs/source/faq/installation.md#_snippet_3

LANGUAGE: bash
CODE:
```
choco install manimce
```

----------------------------------------

TITLE: Manually Publish Manim Release to PyPI (Backup)
DESCRIPTION: These commands provide a backup method for publishing the Manim package to PyPI if the automated process fails. It involves checking out the specific release tag and then using `poetry publish --build` to build and upload the package.
SOURCE: https://github.com/manimcommunity/manim/blob/main/__wiki__/Making-a-new-Release.md#_snippet_2

LANGUAGE: bash
CODE:
```
git checkout <tag>
poetry publish --build
```

----------------------------------------

TITLE: Type Hinting Functions for 2D and 3D Points in Manim
DESCRIPTION: Demonstrates how to type hint functions that accept and return 2D and 3D point coordinates in Manim. It illustrates the use of `Point2DLike`, `Point3DLike`, `Point2DLike_Array`, and `Point3DLike_Array` for flexible input parameters, and `Point3D` for specific return types, adhering to the 'broad parameters, specific returns' principle.
SOURCE: https://github.com/manimcommunity/manim/blob/main/docs/source/contributing/docs/types.rst#_snippet_0

LANGUAGE: python
CODE:
```
def print_point2D(coord: Point2DLike) -> None:
    x, y = coord
    print(f"Point at {x=},{y=}")


def print_point3D(coord: Point3DLike) -> None:
    x, y, z = coord
    print(f"Point at {x=},{y=},{z=}")


def print_point_array(coords: Point2DLike_Array | Point3DLike_Array) -> None:
    for coord in coords:
        if len(coord) == 2:
            # it's a Point2DLike
            print_point2D(coord)
        else:
            # it's a Point3DLike
            print_point3D(coord)

def shift_point_up(coord: Point3DLike) -> Point3D:
    result = np.asarray(coord)
    result += UP
    print(f"New point: {result}")
    return result
```

----------------------------------------

TITLE: Animating Mobject Property Changes Using .animate Syntax in Manim
DESCRIPTION: This snippet demonstrates Manim's `.animate` syntax, which allows direct animation of Mobject method calls. It shows how to animate rotations and property changes (like `set_fill`) by prepending `.animate` to the method call within `self.play`.
SOURCE: https://github.com/manimcommunity/manim/blob/main/docs/source/tutorials/quickstart.rst#_snippet_9

LANGUAGE: python
CODE:
```
class AnimatedSquareToCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        square = Square()  # create a square

        self.play(Create(square))  # show the square on screen
        self.play(square.animate.rotate(PI / 4))  # rotate the square
        self.play(Transform(square, circle))  # transform the square into a circle
        self.play(
            square.animate.set_fill(PINK, opacity=0.5)
        )
```

----------------------------------------

TITLE: Accessing Manim Subcommand Help
DESCRIPTION: This snippet illustrates how to execute a Manim subcommand, such as 'render', and how to retrieve its specific help documentation. Using the '--help' flag provides a comprehensive overview of the subcommand's available options, arguments, and usage examples.
SOURCE: https://github.com/manimcommunity/manim/blob/main/docs/source/guides/configuration.rst#_snippet_16

LANGUAGE: Bash
CODE:
```
manim render
manim render --help
```

----------------------------------------

TITLE: Install Manim via Chocolatey Packages using PowerShell
DESCRIPTION: This snippet describes the installation process for Manim using Chocolatey packages, which internally leverage PowerShell scripts to execute `pip` commands. It covers the installation of `pycairo` and Manim from its master branch, as well as the Chocolatey commands for installing `manimce`, `manim.portable`, and the general `manim` package.
SOURCE: https://github.com/manimcommunity/manim/blob/main/__wiki__/Maintainer's-Guidelines-Chocolatey.md#_snippet_0

LANGUAGE: PowerShell
CODE:
```
pip install pycairo
pip install https://github.com/ManimCommunity/manim/archive/master.zip
```

LANGUAGE: Command Line
CODE:
```
choco install manimce
```

LANGUAGE: Command Line
CODE:
```
choco install manim.portable
```

LANGUAGE: Command Line
CODE:
```
choco install manim
```

----------------------------------------

TITLE: Render Simple Text with Manim Text Class
DESCRIPTION: Demonstrates the basic usage of the `Text` class in Manim to display 'Hello world' with a large font size. This uses the Pango library for text rendering.
SOURCE: https://github.com/manimcommunity/manim/blob/main/docs/source/guides/using_text.rst#_snippet_0

LANGUAGE: Python
CODE:
```
class HelloWorld(Scene):
    def construct(self):
        text = Text("Hello world", font_size=144)
        self.add(text)
```

----------------------------------------

TITLE: Build Manim Documentation on Windows
DESCRIPTION: Executes the Sphinx build process for Manim documentation on Windows systems. This command should be run from within the `docs/` directory of the Manim repository.
SOURCE: https://github.com/manimcommunity/manim/blob/main/docs/source/contributing/docs.rst#_snippet_0

LANGUAGE: Shell
CODE:
```
./make.bat html
```

----------------------------------------

TITLE: Manim Mobject Hierarchy and Initialization
DESCRIPTION: Explains the fundamental Mobject class, its initialization process, and the different types of renderable Mobjects in Manim. It details how base Mobjects are structured and how vectorized Mobjects (VMobjects) are rendered using Bézier curves.
SOURCE: https://github.com/manimcommunity/manim/blob/main/docs/source/guides/deep_dive.rst#_snippet_11

LANGUAGE: APIDOC
CODE:
```
.Mobject
  - Description: Base class for all objects intended to be displayed on screen. Stands for "mathematical object" or "Manim object".
  - Initialization (.Mobject.__init__):
    - Assigns initial attribute values (e.g., 'name', 'submobjects' (empty list), 'color').
    - Calls .Mobject.reset_points()
    - Calls .Mobject.generate_points()
    - Calls .Mobject.init_colors()
  - Usage: Not intended to be used as an actual displayable object; cannot appear in rendered output directly.

.Mobject.reset_points()
  - Purpose: Sets the 'points' attribute of the mobject to an empty NumPy vector.

.Mobject.generate_points()
  - Purpose: Implemented as 'pass' in the base .Mobject class. Actual point generation happens in subclasses.

.Mobject.init_colors()
  - Purpose: Implemented as 'pass' in the base .Mobject class. Actual color initialization happens in subclasses.

Renderable Mobject Types (Cairo Renderer):

.ImageMobject
  - Description: Represents images that can be displayed in the scene.

.PMobject
  - Description: Very special mobjects used to represent point clouds. Not discussed further in this guide.

.VMobject
  - Description: Vectorized mobjects, consisting of points connected via curves.
  - Rendering: The camera processes the 'points' attribute, dividing it into sets of four points. Each set constructs a cubic Bézier curve (first/last points as anchors, second/third as control points).
```

----------------------------------------

TITLE: Running Manim Commands on Windows
DESCRIPTION: Provides alternative methods to execute Manim and pip commands on Windows when executables are not recognized, suggesting `uv run` for virtual environments or prepending `python -m` to commands.
SOURCE: https://github.com/manimcommunity/manim/blob/main/docs/source/faq/installation.md#_snippet_2

LANGUAGE: bash
CODE:
```
uv run manim ...
python -m manim
python -m pip
```

----------------------------------------

TITLE: Building Manim Documentation Locally
DESCRIPTION: Command to build the project's Sphinx-based documentation locally. This allows contributors to preview how their documentation changes will appear and check for any Sphinx errors before submission. Requires Graphviz for inheritance diagrams.
SOURCE: https://github.com/manimcommunity/manim/blob/main/docs/source/contributing/development.md#_snippet_12

LANGUAGE: Shell
CODE:
```
make html
```

----------------------------------------

TITLE: Styling Manim Mobjects with Stroke and Fill
DESCRIPTION: Shows how to apply visual styles to Manim mobjects using `set_stroke` for the border and `set_fill` for the interior. It emphasizes that for `set_fill`, the `opacity` parameter must be specified to make the color visible, as mobjects are transparent by default.
SOURCE: https://github.com/manimcommunity/manim/blob/main/docs/source/tutorials/building_blocks.rst#_snippet_10

LANGUAGE: python
CODE:
```
class MobjectStyling(Scene):
    def construct(self):
        circle = Circle().shift(LEFT)
        square = Square().shift(UP)
        triangle = Triangle().shift(RIGHT)

        circle.set_stroke(color=GREEN, width=20)
        square.set_fill(YELLOW, opacity=1.0)
        triangle.set_fill(PINK, opacity=0.5)

        self.add(circle, square, triangle)
        self.wait(1)
```

----------------------------------------

TITLE: Path Specifications for Sphinx Python References
DESCRIPTION: Guidelines for constructing paths when referencing Python objects in Sphinx documentation, covering standard library, local, and external module references. Includes usage of the '~' prefix for shortened display.
SOURCE: https://github.com/manimcommunity/manim/blob/main/docs/source/contributing/docs/references.rst#_snippet_1

LANGUAGE: reStructuredText
CODE:
```
1. Standard Library:
   - Use direct name for classes: :class:`int`, :class:`str`, :class:`float`, :class:`bool`
   - Use dotted names for methods/attributes: :meth:`str.to_lower`

2. Same File/Class:
   - Direct name: :class:`MyClass` (class in same file)
   - Direct name: :meth:`push` (method in same class)
   - Dotted name: :meth:`MyClass.push` (method in different class in same file)
   - Direct name: :attr:`color` (attribute in same class)
   - Dotted name: :attr:`MyClass.color` (attribute in different class in same file)

3. Different File (Shortened Display):
   - Use '~' prefix for shortened display (e.g., only 'Animation' instead of full path).
   - Example: :class:`~.Animation`, :meth:`~.VMobject.set_color`, :attr:`~.VMobject.color`
   - Note: Full dotted name (e.g., ~manim.animations.Animation) can be used for disambiguation.

4. Different Module (Full Dotted Syntax):
   - Specify full dotted syntax for external modules.
   - Example: :class:`numpy.ndarray`
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

TITLE: Manim Mobject Styling Methods
DESCRIPTION: Documentation for Manim methods used to apply visual styles (stroke, fill, and general color) to mobjects, specifying their applicability to `VMobject` and `Mobject` instances.
SOURCE: https://github.com/manimcommunity/manim/blob/main/docs/source/tutorials/building_blocks.rst#_snippet_14

LANGUAGE: APIDOC
CODE:
```
.set_stroke(color=None, width=None, opacity=None, background=False)
  - Description: Sets the stroke (border) properties of a `VMobject`. By default, mobjects have no visible stroke.
  - Parameters:
    - color: The color of the stroke.
    - width: The width of the stroke.
    - opacity: The opacity of the stroke (0.0 for transparent, 1.0 for opaque).
    - background: If True, applies to the background stroke.
  - Applies to: Instances of `.VMobject`.
  - Usage: `circle.set_stroke(color=GREEN, width=20)`

.set_fill(color=None, opacity=None)
  - Description: Sets the fill (interior) properties of a `VMobject`. Mobjects are fully transparent by default, so `opacity` must be set to make the fill visible.
  - Parameters:
    - color: The color of the fill.
    - opacity: The opacity of the fill (0.0 for transparent, 1.0 for opaque).
  - Applies to: Instances of `.VMobject`.
  - Usage: `square.set_fill(YELLOW, opacity=1.0)`

.set_color(color)
  - Description: Sets the overall color of an `Mobject`. This is a more general method available on the base `Mobject` class.
  - Parameters:
    - color: The color to set.
  - Applies to: Instances of `.Mobject` (and its subclasses like `.VMobject`).
```

----------------------------------------

TITLE: General Documentation Improvements and Examples
DESCRIPTION: Various updates to the Manim documentation, including copyediting of existing guides (e.g., `troubleshooting.rst`, `configurations.rst`), adding new examples (`PolygonOnAxes`, `arrange_in_grid`), re-adding missing documentation (`value_tracker`), fixing typos, and updating copyright information. This also includes adding documentation and type hints for `utils/iterables.py` and instructions for installing extra dependencies with Poetry.
SOURCE: https://github.com/manimcommunity/manim/blob/main/docs/source/changelog/0.15.2-changelog.rst#_snippet_19

LANGUAGE: APIDOC
CODE:
```
# Documentation Updates:
# - Copyediting: troubleshooting.rst, tutorials/configurations.rst, general documentation.
# - New Examples: Added examples for PolygonOnAxes and improved arrange_in_grid example
```

----------------------------------------

TITLE: Use MarkupText for Pango Markup in Manim
DESCRIPTION: Illustrates how to use the `MarkupText` class to render text with Pango Markup. This example shows how to apply different colors to parts of a single line using `<span>` tags within the text string.
SOURCE: https://github.com/manimcommunity/manim/blob/main/docs/source/guides/using_text.rst#_snippet_1

LANGUAGE: Python
CODE:
```
class SingleLineColor(Scene):
    def construct(self):
        text = MarkupText(
            f'all in red <span fgcolor="{YELLOW}">except this</span>', color=RED
        )
        self.add(text)
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

TITLE: Manimpango Font and Weight Utilities
DESCRIPTION: Documentation for utility functions and classes from the `manimpango` library, which Manim uses for font management. Includes `list_fonts` for enumerating available fonts and `Weight` for defining font boldness levels.
SOURCE: https://github.com/manimcommunity/manim/blob/main/docs/source/guides/using_text.rst#_snippet_8

LANGUAGE: APIDOC
CODE:
```
manimpango.list_fonts() -> list[str]
  - Returns a list of font names available on the system that Pango can recognize.

class manimpango.Weight:
  - An enumeration defining various font weight constants.
  - Examples: NORMAL, BOLD, ULTRABOLD, LIGHT, THIN.
  - Usage: Text("Bold Text", weight=manimpango.Weight.BOLD.name) or Text("Bold Text", weight="BOLD")
```

----------------------------------------

TITLE: Install uv Python Environment Manager
DESCRIPTION: Provides commands to install `uv`, a highly recommended tool for managing Python environments and dependencies, on both MacOS/Linux and Windows systems. `uv` simplifies the setup process for Manim animations.
SOURCE: https://github.com/manimcommunity/manim/blob/main/docs/source/installation/uv.md#_snippet_0

LANGUAGE: bash
CODE:
```
curl -LsSf https://astral.sh/uv/install.sh | sh
```

LANGUAGE: powershell
CODE:
```
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

----------------------------------------

TITLE: Manim Example Gallery and Installation Documentation Updates
DESCRIPTION: Summarizes various updates to Manim's example gallery and installation documentation. This includes additions of new examples for a wide range of geometric `Mobjects` (e.g., `Ellipse`, `Polygon`, `Arrow`, `Square`, `Circle`), removal of outdated examples (`BezierSpline`, `SmallDot`), and the inclusion of a new guide for installing Manim on Google Colab. Also covers adding new SVG files for documentation and examples.
SOURCE: https://github.com/manimcommunity/manim/blob/main/docs/source/changelog/0.5.0-changelog.rst#_snippet_12

LANGUAGE: APIDOC
CODE:
```
Manim Example Gallery and Installation:

Example Additions:
  - New examples added for:
    - Ellipse, Polygon, RegularPolygon, Triangle, RoundedRectangle
    - DashedLine, TangentLine, Elbow, Arrow, Vector, DoubleArrow
    - Square, Dot, Circle, Rectangle
    - SurroundingRectangle
    - Rotation examples
    - Sounds examples

Example Removals:
  - Removed BezierSpline from the example gallery.
  - Removed SmallDot from examples.

Installation Guides:
  - Added: Documentation for installing Manim on Google Colab.

Documentation Assets:
  - Added: New SVG files for use in documentation and examples.