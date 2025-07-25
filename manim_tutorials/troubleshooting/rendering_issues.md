# Rendering Issues

This guide addresses common rendering problems with Manim and their solutions.

## Problem: Videos Not Rendering or Empty Output

### Description
When rendering a scene, the process completes but no video file is created or the video is empty.

### Common Causes
1. Scene construct method is empty or has no animations
2. Incorrect scene class name in the command
3. Output directory permissions issues
4. Scene has no play() or add() calls

### Solutions

#### Solution 1: Check Scene Construct Method
Ensure your scene has content in the construct method:

```python
from manim import *

class MyScene(Scene):
    def construct(self):
        # Make sure you have content here
        circle = Circle()
        self.play(Create(circle))  # Add animations
        self.wait(1)
```

#### Solution 2: Verify Scene Name in Command
Make sure the scene name in your command matches exactly:

```bash
# Correct - class name matches exactly
manim -pql scene.py MyScene

# Incorrect - case sensitivity matters
manim -pql scene.py myscene
```

#### Solution 3: Check Output Directory Permissions
Ensure you have write permissions in the output directory:

```bash
# Check current directory permissions
ls -la

# If needed, change permissions
chmod 755 .
```

## Problem: Low Quality or Pixelated Output

### Description
Rendered videos appear blurry or pixelated.

### Solutions

#### Solution 1: Use Higher Quality Settings
```bash
# Medium quality (720p30)
manim -qm scene.py MyScene

# High quality (1080p60)
manim -qh scene.py MyScene

# Production quality (2160p60)
manim -qp scene.py MyScene
```

#### Solution 2: Adjust Configuration
Create a `manim.cfg` file in your project directory:

```ini
[CLI]
quality = high_quality
```

## Problem: Long Rendering Times

### Description
Scenes take a very long time to render.

### Common Causes
1. Too many complex objects
2. High quality settings for simple scenes
3. Inefficient code
4. Large number of animations

### Solutions

#### Solution 1: Use Lower Quality for Development
```bash
# Use low quality during development
manim -ql scene.py MyScene

# Only use high quality for final render
manim -qh scene.py MyScene
```

#### Solution 2: Optimize Scene Code
```python
# Instead of creating many individual objects
# Use VGroup for better performance
from manim import *

class OptimizedScene(Scene):
    def construct(self):
        # Group similar objects
        circles = VGroup(*[
            Circle(radius=0.1)
            for _ in range(100)
        ])
        circles.arrange_in_grid()
        
        self.play(Create(circles, run_time=2))
```

#### Solution 3: Disable Caching When Not Needed
```bash
# Disable partial movie caching for simple scenes
manim -ql --disable_caching scene.py MyScene
```

## Problem: Memory Errors During Rendering

### Description
Rendering fails with "MemoryError" or "Killed" messages.

### Solutions

#### Solution 1: Reduce Scene Complexity
Break complex scenes into smaller parts:

```python
# Instead of one complex scene
class Part1(Scene):
    def construct(self):
        # First part of animation
        pass

class Part2(Scene):
    def construct(self):
        # Second part of animation
        pass
```

#### Solution 2: Increase System Memory
If possible, increase available RAM or use a machine with more memory.

#### Solution 3: Use --flush_cache Flag
```bash
# Clear cache before rendering
manim -ql --flush_cache scene.py MyScene
```

## Problem: Audio Issues in Rendered Videos

### Description
Videos have no audio or audio is out of sync.

### Solutions

#### Solution 1: Check Audio File Format
Ensure audio files are in supported formats (WAV, MP3):

```python
from manim import *

class AudioScene(Scene):
    def construct(self):
        # Use supported audio formats
        self.add_sound("audio.wav")  # Preferred
        # or
        self.add_sound("audio.mp3")
```

#### Solution 2: Verify Audio Path
Make sure audio files are in the correct location:

```bash
# Check if audio file exists
ls -la audio.wav

# If not, provide correct path
self.add_sound("sounds/audio.wav")
```

## Problem: Text Rendering Issues

### Description
Text appears garbled, missing, or incorrectly formatted.

### Solutions

#### Solution 1: Install Required Fonts
```bash
# On Ubuntu/Debian
sudo apt install texlive-fonts-recommended texlive-fonts-extra

# On macOS with Homebrew
brew install --cask mactex
```

#### Solution 2: Use Different Text Classes
```python
from manim import *

class TextScene(Scene):
    def construct(self):
        # For simple text, use Text
        simple_text = Text("Hello World")
        
        # For mathematical expressions, use MathTex
        math_text = MathTex(r"\int_0^\infty e^{-x^2} dx")
        
        # For LaTeX with more control, use Tex
        latex_text = Tex(r"\LaTeX")
        
        self.play(Write(simple_text))
```

## Problem: 3D Scene Rendering Issues

### Description
3D scenes don't render correctly or camera movements don't work.

### Solutions

#### Solution 1: Use Correct Scene Class
```python
from manim import *

# Use ThreeDScene for 3D scenes
class My3DScene(ThreeDScene):
    def construct(self):
        # Set camera orientation
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        
        # Create 3D objects
        sphere = Sphere()
        self.play(Create(sphere))
```

#### Solution 2: Proper Camera Controls
```python
class CameraMovement(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        
        # Animate camera movement
        self.move_camera(phi=45 * DEGREES, theta=-45 * DEGREES, run_time=3)
        
        # Or use ambient rotation
        self.begin_ambient_camera_rotation(rate=0.1)
        self.wait(5)
        self.stop_ambient_camera_rotation()
```

## Prevention Tips

1. Always test scenes at low quality first
2. Keep scene files organized and modular
3. Use version control to track changes
4. Monitor system resources during rendering
5. Regularly clear cache with `--flush_cache` when needed

## Additional Resources

- [Manim Configuration Guide](https://docs.manim.community/en/stable/guides/configuration.html)
- [Performance Optimization Tips](https://docs.manim.community/en/stable/guides/performance.html)
- [Scene Construction Guide](https://docs.manim.community/en/stable/tutorials/building_blocks.html)