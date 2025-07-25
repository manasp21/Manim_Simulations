# Performance Optimization

This guide provides tips and techniques to improve Manim rendering speed and efficiency.

## Understanding Manim Performance

Manim's performance can be affected by several factors:
- Scene complexity (number of objects)
- Animation complexity (transformations, updaters)
- Quality settings (resolution, frame rate)
- System resources (CPU, memory, disk I/O)

## Optimization Techniques

### 1. Reduce Scene Complexity

#### Use VGroup for Similar Objects
Instead of creating individual objects, group them:

```python
from manim import *

class OptimizedCircles(Scene):
    def construct(self):
        # Inefficient - 100 individual circles
        # circles = [Circle() for _ in range(100)]
        
        # Efficient - one VGroup with 100 circles
        circles = VGroup(*[Circle() for _ in range(100)])
        circles.arrange_in_grid(10, 10, buff=0.1)
        
        self.play(Create(circles, run_time=2))
```

#### Simplify Complex Paths
Reduce the number of points in custom shapes:

```python
class OptimizedPath(Scene):
    def construct(self):
        # Instead of high-resolution curve
        # complex_curve = ParametricFunction(lambda t: [t, np.sin(50*t), 0], t_range=[0, 2*PI])
        
        # Use lower resolution
        simple_curve = ParametricFunction(
            lambda t: [t, np.sin(5*t), 0], 
            t_range=[0, 2*PI],
            scaling=0.1  # Reduce number of points
        )
        
        self.play(Create(simple_curve))
```

### 2. Optimize Animation Parameters

#### Adjust Run Time and Frame Rate
```python
class OptimizedTiming(Scene):
    def construct(self):
        circle = Circle()
        
        # Use appropriate run_time for complexity
        self.play(Create(circle, run_time=1))  # Simple animation
        
        # For complex animations, consider longer run_time
        # to reduce frame density
        self.play(Rotate(circle, 2*PI, run_time=3))
```

#### Use Lag Ratios for Group Animations
```python
class LagRatioOptimization(Scene):
    def construct(self):
        squares = VGroup(*[Square() for _ in range(5)])
        squares.arrange(RIGHT)
        
        # Animate with lag_ratio to reduce computational load
        self.play(
            Create(squares),
            lag_ratio=0.1,  # Animate one by one with delay
            run_time=2
        )
```

### 3. Quality Settings Optimization

#### Use Appropriate Quality Levels
```bash
# For development and testing
manim -ql scene.py MyScene

# For final renders
manim -qh scene.py MyScene

# For production quality (only when necessary)
manim -qp scene.py MyScene
```

#### Custom Quality Configuration
Create a `manim.cfg` file:

```ini
[CLI]
quality = medium_quality
frame_rate = 30
pixel_height = 720
pixel_width = 1280
```

### 4. Caching Strategies

#### Enable Partial Movie Caching
```bash
# Enable caching (default behavior)
manim -ql scene.py MyScene

# Disable caching for simple scenes
manim -ql --disable_caching scene.py MyScene

# Clear cache when needed
manim -ql --flush_cache scene.py MyScene
```

#### Strategic Cache Usage
```python
class CacheOptimizedScene(Scene):
    def construct(self):
        # Complex static background - cache this part
        background = VGroup(*[Circle() for _ in range(50)])
        background.arrange_in_grid()
        
        self.add(background)
        
        # Animate only the dynamic parts
        moving_object = Circle(color=RED)
        self.play(Create(moving_object))
        self.play(moving_object.animate.shift(RIGHT))
```

### 5. Updater Optimization

#### Efficient Updaters
```python
class EfficientUpdater(Scene):
    def construct(self):
        dot = Dot()
        path = VMobject()
        path.set_points_as_corners([dot.get_center(), dot.get_center()])
        
        # Efficient updater - minimal computation
        def update_path(path):
            previous_path = path.copy()
            previous_path.add_points_as_corners([dot.get_center()])
            path.become(previous_path)
        
        path.add_updater(update_path)
        self.add(path)
        
        # Move dot (this will trigger updater)
        self.play(dot.animate.shift(RIGHT * 3), run_time=2)
        path.clear_updaters()
```

#### Limit Updater Scope
```python
class LimitedUpdater(Scene):
    def construct(self):
        dot = Dot()
        
        # Instead of continuous updates, use specific timing
        # Only update when needed
        def limited_updater(mob, dt):
            # Add conditions to limit computation
            if self.time < 5:  # Only update for first 5 seconds
                mob.shift(RIGHT * dt)
        
        dot.add_updater(limited_updater)
        self.add(dot)
        self.wait(6)  # 1 second without updates
        dot.clear_updaters()
```

### 6. Memory Management

#### Clear Unused Objects
```python
class MemoryManagement(Scene):
    def construct(self):
        # Create objects
        group1 = VGroup(*[Circle() for _ in range(50)])
        group2 = VGroup(*[Square() for _ in range(50)])
        
        self.play(Create(group1))
        self.wait(1)
        
        # Remove objects no longer needed
        self.play(FadeOut(group1))
        self.remove(group1)  # Explicitly remove from scene
        
        self.play(Create(group2))
```

#### Use Suspending and Resuming
```python
class SuspendResume(Scene):
    def construct(self):
        # For complex scenes, suspend rendering during setup
        self.camera.background_color = WHITE
        
        # Create complex scene elements
        complex_group = VGroup(*[
            Circle(color=RED) for _ in range(100)
        ])
        complex_group.arrange_in_grid()
        
        # Resume normal rendering
        self.play(Create(complex_group, run_time=3))
```

## System-Level Optimizations

### 1. Hardware Considerations
- Use SSD storage for temporary files
- Ensure adequate RAM (8GB minimum, 16GB recommended)
- Close unnecessary applications during rendering

### 2. Software Optimizations
```bash
# Use multiple CPU cores
manim -ql --threads 4 scene.py MyScene

# Adjust buffer size for I/O operations
manim -ql --buffer-size 1000 scene.py MyScene
```

### 3. Environment Variables
```bash
# Set temporary directory to fast storage
export TEMP=/path/to/fast/ssd/temp

# Increase Python memory limit (Linux/macOS)
ulimit -m 8388608  # 8GB
```

## Profiling and Monitoring

### 1. Time Your Animations
```python
import time

class ProfiledScene(Scene):
    def construct(self):
        start_time = time.time()
        
        # Your animation code here
        circle = Circle()
        self.play(Create(circle))
        
        end_time = time.time()
        print(f"Animation took {end_time - start_time:.2f} seconds")
```

### 2. Monitor System Resources
Use system monitoring tools during rendering:
- `htop` or `top` (Linux/macOS)
- Task Manager (Windows)
- Activity Monitor (macOS)

## Best Practices Summary

1. **Development Workflow**:
   - Use low quality (`-ql`) during development
   - Test with simple versions of complex scenes
   - Use `--disable_caching` for simple scenes

2. **Scene Design**:
   - Group similar objects with `VGroup`
   - Minimize the use of complex updaters
   - Remove unnecessary objects from scene

3. **Animation Techniques**:
   - Use appropriate `run_time` values
   - Apply `lag_ratio` for group animations
   - Avoid overly complex transformations

4. **System Management**:
   - Monitor resource usage
   - Use SSD storage for temporary files
   - Close unnecessary applications

## Advanced Optimization Techniques

### 1. Custom Renderer Settings
```python
# In your scene file
config.frame_rate = 15  # Reduce frame rate
config.pixel_height = 480  # Reduce resolution
config.pixel_width = 854
```

### 2. Selective Rendering
```python
class SelectiveScene(Scene):
    def construct(self):
        # Only render specific sections
        if config["frame_rate"] > 30:
            # High quality version
            complex_animation()
        else:
            # Low quality version
            simple_animation()
```

### 3. Parallel Processing
For very complex scenes, consider breaking them into parts:

```bash
# Render parts separately
manim -ql part1.py Part1Scene
manim -ql part2.py Part2Scene

# Combine videos using ffmpeg
ffmpeg -i part1.mp4 -i part2.mp4 -filter_complex "[0:v] [1:v] concat=n=2:v=1 [v]" -map "[v]" final.mp4
```

## When to Optimize

1. **Early Development**: Focus on functionality, use low quality
2. **Testing**: Optimize complex scenes that take >30 seconds to render
3. **Final Render**: Apply all optimizations for production quality

## Additional Resources

- [Manim Configuration Documentation](https://docs.manim.community/en/stable/guides/configuration.html)
- [Performance Profiling Tools](https://docs.manim.community/en/stable/guides/performance.html)
- [Scene Construction Best Practices](https://docs.manim.community/en/stable/tutorials/building_blocks.html)