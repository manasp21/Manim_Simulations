# External Libraries

Useful libraries and tools that work with Manim to extend its capabilities.

## Plugin Libraries

### manim-physics
A plugin for creating physics-related animations.

```bash
# Installation
pip install manim-physics

# Usage
from manim import *
from manim_physics import *

class PhysicsExample(Scene):
    def construct(self):
        # Create a rigid body
        body = RigidBody()
        
        # Apply forces
        force = Force(body, direction=UP)
        
        self.play(Create(body))
        self.play(ApplyForce(force))
```

### manim-voiceover
Add voiceovers to your Manim animations.

```bash
# Installation
pip install manim-voiceover

# Usage
from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.recorder import RecorderService

class VoiceoverExample(VoiceoverScene):
    def construct(self):
        self.set_speech_service(RecorderService())
        
        circle = Circle()
        
        with self.voiceover(text="This is a circle.") as tracker:
            self.play(Create(circle), run_time=tracker.duration)
```

### manim-slides
Convert Manim animations into interactive slides.

```bash
# Installation
pip install manim-slides

# Usage
# After creating your Manim scenes
manim-slides render my_scene.py
manim-slides present MyScene
```

### manim-demos
Collection of demonstration scenes and examples.

```bash
# Installation
pip install manim-demos

# Usage
from manim_demos import *
```

## Mathematical Libraries

### NumPy
Essential for mathematical computations in Manim.

```bash
# Installation
pip install numpy

# Usage in Manim
from manim import *
import numpy as np

class NumpyExample(Scene):
    def construct(self):
        # Create points using NumPy
        points = np.array([
            [0, 0, 0],
            [1, 1, 0],
            [2, 0, 0]
        ])
        
        # Create polygon from points
        polygon = Polygon(*points)
        
        # Use NumPy for calculations
        center = np.mean(points, axis=0)
        center_dot = Dot(center, color=RED)
        
        self.play(Create(polygon))
        self.play(Create(center_dot))
```

### SciPy
Scientific computing library for advanced mathematical operations.

```bash
# Installation
pip install scipy

# Usage in Manim
from manim import *
from scipy.integrate import quad
import numpy as np

class ScipyExample(Scene):
    def construct(self):
        # Use SciPy for numerical integration
        def func(x):
            return np.sin(x**2)
        
        result, error = quad(func, 0, 2)
        
        # Display result
        text = Text(f"∫₀² sin(x²) dx = {result:.4f}")
        self.play(Write(text))
```

### SymPy
Symbolic mathematics library for algebraic manipulations.

```bash
# Installation
pip install sympy

# Usage in Manim
from manim import *
from sympy import symbols, diff, integrate, latex

class SympyExample(Scene):
    def construct(self):
        # Use SymPy for symbolic math
        x = symbols('x')
        expr = x**2 + 2*x + 1
        
        # Calculate derivative
        derivative = diff(expr, x)
        
        # Convert to LaTeX for Manim
        expr_latex = latex(expr)
        deriv_latex = latex(derivative)
        
        # Display equations
        expr_text = MathTex(f"f(x) = {expr_latex}")
        deriv_text = MathTex(f"f'(x) = {deriv_latex}")
        
        deriv_text.next_to(expr_text, DOWN)
        
        self.play(Write(expr_text))
        self.play(Write(deriv_text))
```

## Data Visualization Libraries

### Matplotlib
For creating static plots that can be combined with Manim.

```bash
# Installation
pip install matplotlib

# Usage
from manim import *
import matplotlib.pyplot as plt
import numpy as np

class MatplotlibExample(Scene):
    def construct(self):
        # Create data
        x = np.linspace(0, 2*np.pi, 100)
        y = np.sin(x)
        
        # Create matplotlib plot
        fig, ax = plt.subplots()
        ax.plot(x, y)
        ax.set_title("Sine Wave")
        
        # Save plot
        fig.savefig("sine_wave.png")
        plt.close()
        
        # Import into Manim
        image = ImageMobject("sine_wave.png")
        self.play(FadeIn(image))
```

### Plotly
Interactive plotting library that can export to various formats.

```bash
# Installation
pip install plotly

# Usage
from manim import *
import plotly.graph_objects as go
import plotly.io as pio

class PlotlyExample(Scene):
    def construct(self):
        # Create Plotly figure
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=[1, 2, 3, 4], y=[10, 11, 12, 13]))
        
        # Export as SVG
        pio.write_image(fig, "plot.svg")
        
        # Import into Manim
        svg = SVGMobject("plot.svg")
        self.play(Create(svg))
```

## Image and Media Libraries

### Pillow
Python Imaging Library for image manipulation.

```bash
# Installation
pip install Pillow

# Usage in Manim
from manim import *
from PIL import Image
import numpy as np

class PillowExample(Scene):
    def construct(self):
        # Create or manipulate images with Pillow
        img = Image.new('RGB', (100, 100), color='red')
        
        # Save image
        img.save('red_square.png')
        
        # Use in Manim
        manim_img = ImageMobject('red_square.png')
        self.play(FadeIn(manim_img))
```

### OpenCV
Computer vision library for advanced image processing.

```bash
# Installation
pip install opencv-python

# Usage in Manim
from manim import *
import cv2
import numpy as np

class OpenCVExample(Scene):
    def construct(self):
        # Create image with OpenCV
        img = np.zeros((100, 100, 3), dtype=np.uint8)
        cv2.circle(img, (50, 50), 30, (255, 255, 255), -1)
        
        # Save image
        cv2.imwrite('opencv_circle.png', img)
        
        # Use in Manim
        manim_img = ImageMobject('opencv_circle.png')
        self.play(FadeIn(manim_img))
```

## Audio Libraries

### PyDub
Audio manipulation library for working with sound files.

```bash
# Installation
pip install pydub

# Usage in Manim
from manim import *
from pydub import AudioSegment

class PyDubExample(Scene):
    def construct(self):
        # Load and manipulate audio
        audio = AudioSegment.from_file("input.wav")
        
        # Trim audio
        trimmed = audio[1000:3000]  # 1-3 seconds
        
        # Export
        trimmed.export("trimmed.wav", format="wav")
        
        # Use in Manim scene
        self.add_sound("trimmed.wav")
        circle = Circle()
        self.play(Create(circle))
```

## Development Tools

### Black
Code formatter for Python to maintain consistent style.

```bash
# Installation
pip install black

# Usage
# Format Manim code
black my_scene.py
```

### Flake8
Code linting tool for identifying issues in Python code.

```bash
# Installation
pip install flake8

# Usage
# Check Manim code for issues
flake8 my_scene.py
```

### Pytest
Testing framework for validating Manim scenes.

```bash
# Installation
pip install pytest

# Usage
# Create test file test_scenes.py
import pytest
from manim import *

def test_circle_creation():
    scene = CircleScene()
    scene.render()
    assert len(scene.mobjects) > 0

# Run tests
pytest test_scenes.py
```

## Configuration Management

### PyYAML
For managing complex configuration files.

```bash
# Installation
pip install PyYAML

# Usage in Manim
from manim import *
import yaml

class YAMLConfigExample(Scene):
    def construct(self):
        # Load configuration
        with open('config.yaml', 'r') as f:
            config = yaml.safe_load(f)
        
        # Use configuration in scene
        text = Text(config['title'])
        self.play(Write(text))
```

Sample `config.yaml`:
```yaml
title: "My Animation"
duration: 10
colors:
  primary: RED
  secondary: BLUE
```

## Version Control Integration

### Pre-commit
Framework for managing pre-commit hooks.

```bash
# Installation
pip install pre-commit

# Configuration in .pre-commit-config.yaml
repos:
  - repo: https://github.com/psf/black
    rev: 22.3.0
    hooks:
      - id: black
        types: [python]
```

## Documentation Tools

### Sphinx
Documentation generator for creating project documentation.

```bash
# Installation
pip install sphinx

# Usage
# Generate documentation for Manim projects
sphinx-quickstart docs
```

### MkDocs
Static site generator for project documentation.

```bash
# Installation
pip install mkdocs

# Usage
# Create documentation site
mkdocs new my-project-docs
```

## Performance and Profiling

### cProfile
Built-in Python profiler for identifying performance bottlenecks.

```python
# Usage in Manim
import cProfile
from manim import *

class ProfiledScene(Scene):
    def construct(self):
        # Profile complex animations
        profiler = cProfile.Profile()
        profiler.enable()
        
        # Complex animation code here
        complex_group = VGroup(*[Circle() for _ in range(1000)])
        self.play(Create(complex_group))
        
        profiler.disable()
        profiler.dump_stats('scene_profile.prof')
```

### Memory Profiler
Tool for monitoring memory usage.

```bash
# Installation
pip install memory-profiler

# Usage
from manim import *
from memory_profiler import profile

class MemoryProfiledScene(Scene):
    @profile
    def construct(self):
        # Memory-intensive operations
        large_group = VGroup(*[Circle() for _ in range(10000)])
        self.play(Create(large_group))
```

## Integration Libraries

### Jupyter
For creating interactive notebooks with Manim.

```bash
# Installation
pip install jupyter

# Usage
# In Jupyter notebook
from manim import *
from manim.utils.ipython_magic import ManimMagic

# Register magic command
get_ipython().register_magics(ManimMagic)

# Use %%manim cell magic
```

### Streamlit
For creating web applications with Manim animations.

```bash
# Installation
pip install streamlit

# Usage in app.py
import streamlit as st
from manim import *

class StreamlitApp:
    def render_animation(self):
        # Generate Manim animation
        scene = MyScene()
        scene.render()
        
        # Display in Streamlit
        st.video("media/videos/my_scene.mp4")
```

## Best Practices for Using External Libraries

### 1. Dependency Management
```bash
# Use requirements.txt
pip freeze > requirements.txt

# Install from requirements
pip install -r requirements.txt
```

### 2. Virtual Environments
```bash
# Create virtual environment
python -m venv manim_env

# Activate
source manim_env/bin/activate  # Linux/macOS
# or
manim_env\Scripts\activate     # Windows

# Install dependencies
pip install manim numpy scipy
```

### 3. Version Pinning
```txt
# requirements.txt with pinned versions
manim==0.17.2
numpy==1.24.1
scipy==1.10.0
matplotlib==3.6.3
```

### 4. Error Handling
```python
class RobustScene(Scene):
    def construct(self):
        try:
            import numpy as np
        except ImportError:
            raise ImportError("NumPy is required for this scene")
        
        # Continue with NumPy-dependent code
        pass
```

## Compatibility Considerations

### Python Version Compatibility
- Check library compatibility with your Python version
- Use tools like `pip check` to verify dependencies

### Manim Version Compatibility
- Some libraries may require specific Manim versions
- Check library documentation for compatibility matrix

### Operating System Compatibility
- Some libraries may have OS-specific dependencies
- Test on target deployment platforms

These external libraries can significantly enhance your Manim projects by providing additional functionality, improving workflow, and enabling integration with other tools and technologies. Always check the documentation of each library for the most up-to-date installation instructions and usage examples.