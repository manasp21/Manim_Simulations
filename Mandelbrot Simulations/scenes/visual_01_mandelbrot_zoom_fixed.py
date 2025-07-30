"""
Fixed Visual Scene 1: Pure Mandelbrot Deep Zoom (60 seconds)

Fixed version that creates proper zoom sequences without the loop-back issues.
"""

from manim import *
import numpy as np
import sys
import os
from typing import Tuple, Optional, List
from PIL import Image

# Add project root to path for imports
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)

try:
    from utils.fractal_algorithms import FractalCalculator, create_fractal_calculator
    from utils.color_schemes import FractalColorizer, ColorPalette
    UTILS_AVAILABLE = True
except ImportError as e:
    print(f"Import error: {e}")
    UTILS_AVAILABLE = False

class VisualMandelbrotZoomFixed(Scene):
    """
    Fixed version of pure visual Mandelbrot zoom with proper parameter progression.
    """
    
    def __init__(self, **kwargs):
        """Initialize visual-only Mandelbrot scene."""
        super().__init__(**kwargs)
        self.camera.background_color = "#000000"  # Pure black background
        
        # Visual parameters - reduced for testing
        self.total_duration = 20.0  # Shorter for testing
        self.zoom_frames = 20  # Fewer frames for testing
        
        # High-quality rendering parameters
        self.base_resolution = 400  # Smaller for faster testing
        self.max_iterations = 256
        self.color_intensity = 1.2
        
        # Initialize fractal tools
        self.fractal_calculator = self._initialize_calculator()
        self.colorizer = self._initialize_colorizer()
        
    def construct(self):
        """Pure visual construction with fixed zoom progression."""
        
        if not UTILS_AVAILABLE or not self.fractal_calculator:
            self.create_visual_fallback()
            return
        
        # Create the fixed zoom sequence
        self.create_fixed_mandelbrot_zoom()
    
    def create_fixed_mandelbrot_zoom(self):
        """
        Create proper zoom sequence with manually defined keyframes.
        """
        
        # Define proper zoom sequence (seahorse valley)
        zoom_keyframes = [
            (0+0j, 1.0),                           # Overview
            (-0.5+0j, 3.0),                        # Approach
            (-0.7+0.1j, 10.0),                     # Enter region
            (-0.7269+0.1889j, 50.0),               # Seahorse valley
            (-0.72691+0.18891j, 200.0),            # Deeper
            (-0.726920+0.188910j, 1000.0),         # Deep zoom
            (-0.7269200+0.1889100j, 5000.0),       # Very deep
            (-0.72692000+0.18891000j, 20000.0),    # Maximum zoom
        ]
        
        # Generate time progression
        frame_times = np.linspace(0.0, 1.0, self.zoom_frames)
        keyframe_times = np.linspace(0.0, 1.0, len(zoom_keyframes))
        
        # Start with first frame
        initial_center, initial_zoom = zoom_keyframes[0]
        current_fractal = self.render_mandelbrot_visual(
            center=initial_center,
            zoom=initial_zoom,
            color_time=0.0
        )
        
        if current_fractal:
            current_fractal.scale_to_fit_height(config.frame_height * 0.9)
            current_fractal.center()
            
            # Smooth entry
            self.play(FadeIn(current_fractal, run_time=1.5), rate_func=smooth)
            
            # Execute zoom sequence
            for i, t in enumerate(frame_times[1:], 1):
                # Interpolate between keyframes
                center, zoom = self._interpolate_keyframes(zoom_keyframes, t)
                
                # Add some color cycling based on zoom level
                color_time = t + np.log10(zoom) * 0.1
                
                # Render next frame
                next_fractal = self.render_mandelbrot_visual(
                    center=center,
                    zoom=zoom,
                    color_time=color_time
                )
                
                if next_fractal:
                    next_fractal.scale_to_fit_height(config.frame_height * 0.9)
                    next_fractal.center()
                    
                    # Variable transition time based on zoom progression
                    transition_time = 0.8 if zoom < 100 else 0.5
                    
                    # Smooth morph between frames
                    self.play(
                        Transform(current_fractal, next_fractal, run_time=transition_time),
                        rate_func=smooth
                    )
                    
                    # Brief pause at key zoom levels
                    if zoom in [10.0, 50.0, 1000.0]:
                        self.wait(0.3)
            
            # Final pause
            self.wait(1.0)
            
            # Fade out
            self.play(FadeOut(current_fractal, run_time=1.5), rate_func=smooth)
        
        else:
            self.create_visual_fallback()
    
    def _interpolate_keyframes(self, keyframes: List[Tuple[complex, float]], t: float) -> Tuple[complex, float]:
        """
        Manually interpolate between keyframes with proper time distribution.
        """
        if len(keyframes) < 2:
            return keyframes[0] if keyframes else (0+0j, 1.0)
        
        # Create time points for keyframes
        times = np.linspace(0.0, 1.0, len(keyframes))
        
        # Find surrounding keyframes
        for i in range(len(times) - 1):
            if times[i] <= t <= times[i + 1]:
                # Linear interpolation between keyframes i and i+1
                local_t = (t - times[i]) / (times[i + 1] - times[i])
                
                center1, zoom1 = keyframes[i]
                center2, zoom2 = keyframes[i + 1]
                
                # Linear interpolation for center
                center = center1 + local_t * (center2 - center1)
                
                # Exponential interpolation for zoom
                log_zoom1 = np.log(max(zoom1, 1e-10))
                log_zoom2 = np.log(max(zoom2, 1e-10))
                zoom = np.exp(log_zoom1 + local_t * (log_zoom2 - log_zoom1))
                
                return center, zoom
        
        # If t is at the end, return last keyframe
        return keyframes[-1]
    
    def render_mandelbrot_visual(self, center: complex, zoom: float, 
                                color_time: float) -> Optional[ImageMobject]:
        """
        Render visual Mandelbrot frame.
        """
        try:
            # Calculate Mandelbrot data
            mandelbrot_data = self.fractal_calculator.mandelbrot_set(
                width=self.base_resolution,
                height=self.base_resolution,
                center=center,
                zoom=zoom
            )
            
            # Apply coloring
            rgb_array = self.colorizer.colorize_escape_data(
                mandelbrot_data,
                max_iterations=self.max_iterations,
                cycle_speed=color_time * 2.0,
                use_histogram_equalization=True
            )
            
            # Convert to PIL Image
            rgb_uint8 = (np.clip(rgb_array, 0, 1) * 255).astype(np.uint8)
            pil_image = Image.fromarray(rgb_uint8)
            
            # Save with unique filename including zoom info for debugging
            temp_filename = f"/tmp/mandelbrot_fixed_{abs(hash((center, zoom, color_time))) % 100000}.png"
            pil_image.save(temp_filename, optimize=True, quality=95)
            
            print(f"Generated: center={center}, zoom={zoom:.2f}, file={temp_filename}")
            
            return ImageMobject(temp_filename)
            
        except Exception as e:
            print(f"Visual rendering error: {e}")
            return None
    
    def create_visual_fallback(self):
        """Create simple visual fallback if fractal rendering fails."""
        # Create gradient circle as aesthetic placeholder
        circles = VGroup()
        for i in range(10):
            radius = 3.0 - i * 0.25
            opacity = 1.0 - i * 0.08
            color_intensity = i / 10.0
            
            circle = Circle(
                radius=radius,
                color=[color_intensity, 0.3, 1.0 - color_intensity],
                fill_opacity=opacity,
                stroke_width=0
            )
            circles.add(circle)
        
        circles.center()
        
        # Smooth animation sequence
        self.play(Create(circles, run_time=2.0), rate_func=smooth)
        
        # Gentle rotation
        for _ in range(5):
            self.play(
                Rotate(circles, angle=PI/4, run_time=1.5),
                rate_func=smooth
            )
        
        self.wait(1.0)
        self.play(FadeOut(circles, run_time=1.5))
    
    def _initialize_calculator(self) -> Optional[FractalCalculator]:
        """Initialize fractal calculator."""
        try:
            if FractalCalculator:
                return create_fractal_calculator(
                    fractal_type='mandelbrot',
                    max_iterations=self.max_iterations,
                    bailout_radius=2.0
                )
        except Exception as e:
            print(f"Failed to initialize calculator: {e}")
        return None
    
    def _initialize_colorizer(self) -> Optional[FractalColorizer]:
        """Initialize colorizer with fire palette."""
        try:
            if FractalColorizer:
                return FractalColorizer(
                    palette=ColorPalette.FIRE,
                    gamma=0.8,
                    contrast=self.color_intensity
                )
        except Exception as e:
            print(f"Failed to initialize colorizer: {e}")
        return None

if __name__ == "__main__":
    print("Fixed Pure Visual Mandelbrot Zoom Scene")
    print("Test: manim -pql visual_01_mandelbrot_zoom_fixed.py VisualMandelbrotZoomFixed")