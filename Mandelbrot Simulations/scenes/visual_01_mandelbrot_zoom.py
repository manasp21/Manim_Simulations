"""
Visual Scene 1: Pure Mandelbrot Deep Zoom (60 seconds)

No text, no explanations, no educational content.
Pure mathematical visualization of the Mandelbrot set with mesmerizing deep zoom
into the seahorse valley region, showcasing infinite complexity and beauty.

Visual Flow:
- Start with full Mandelbrot set overview
- Smooth zoom into seahorse valley 
- Deep exploration of fractal boundaries
- Seamless loop back to starting position
- Fire palette with zoom-synchronized color cycling
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
    from utils.zoom_paths import MANDELBROT_PATHS, ZoomPath, EasingFunction, ZoomKeyframe
    UTILS_AVAILABLE = True
except ImportError as e:
    print(f"Import error: {e}")
    UTILS_AVAILABLE = False

class VisualMandelbrotZoom(Scene):
    """
    Pure visual Mandelbrot zoom with no text or educational content.
    
    60-second mesmerizing journey through infinite fractal complexity.
    """
    
    def __init__(self, **kwargs):
        """Initialize visual-only Mandelbrot scene."""
        super().__init__(**kwargs)
        self.camera.background_color = "#000000"  # Pure black background
        
        # Visual parameters (no educational timing)
        self.total_duration = 60.0
        self.zoom_frames = 120  # 2 fps for smooth 60-second animation
        self.transition_smoothness = 0.8
        
        # High-quality rendering parameters
        self.base_resolution = 1000  # Higher quality for visual appeal
        self.max_iterations = 512   # More detail for deep zooms
        self.color_intensity = 1.2
        
        # Initialize fractal tools
        self.fractal_calculator = self._initialize_calculator()
        self.colorizer = self._initialize_colorizer()
        self.zoom_path = self._create_zoom_path()
        
    def construct(self):
        """Pure visual construction - no text, pure mathematical beauty."""
        
        if not UTILS_AVAILABLE or not self.fractal_calculator:
            # Fallback: Simple visual placeholder
            self.create_visual_fallback()
            return
        
        # Create the mesmerizing zoom sequence
        self.create_mandelbrot_zoom_sequence()
    
    def create_mandelbrot_zoom_sequence(self):
        """
        Create pure visual zoom sequence with no interruptions.
        """
        
        # Generate all frames for smooth animation
        frame_times = np.linspace(0.0, 1.0, self.zoom_frames)
        
        # Start with overview frame
        initial_center, initial_zoom, _ = self.zoom_path.interpolate_at_time(0.0)
        current_fractal = self.render_mandelbrot_visual(
            center=initial_center,
            zoom=initial_zoom,
            color_time=0.0
        )
        
        if current_fractal:
            # Scale to full screen for maximum visual impact
            current_fractal.scale_to_fit_height(config.frame_height * 0.95)
            current_fractal.center()
            
            # Immediate display with smooth fade-in
            self.play(FadeIn(current_fractal, run_time=2.0), rate_func=smooth)
            
            # Execute zoom sequence with smooth transitions
            for i, t in enumerate(frame_times[1:], 1):
                center, zoom, rotation = self.zoom_path.interpolate_at_time(t)
                
                # Render next frame
                next_fractal = self.render_mandelbrot_visual(
                    center=center,
                    zoom=zoom,
                    color_time=t,
                    rotation=rotation
                )
                
                if next_fractal:
                    next_fractal.scale_to_fit_height(config.frame_height * 0.95)
                    next_fractal.center()
                    
                    # Smooth transition timing based on zoom progression  
                    if zoom < 10:
                        transition_time = 0.8  # Slower for initial overview
                    elif zoom < 100:
                        transition_time = 0.6  # Medium for approach
                    elif zoom < 1000:
                        transition_time = 0.4  # Faster for deep zoom
                    else:
                        transition_time = 0.3  # Fastest for maximum detail
                    
                    # Smooth morph between frames
                    self.play(
                        Transform(current_fractal, next_fractal, run_time=transition_time),
                        rate_func=smooth
                    )
                    
                    # Brief pause for visual appreciation at key zoom levels
                    if zoom in [1.0, 10.0, 100.0, 1000.0, 10000.0]:
                        self.wait(0.5)
            
            # Final pause at maximum zoom before loop
            self.wait(1.0)
            
            # Smooth fade out to black for seamless looping
            self.play(FadeOut(current_fractal, run_time=2.0), rate_func=smooth)
        
        else:
            # Fallback if rendering fails
            self.create_visual_fallback()
    
    def render_mandelbrot_visual(self, center: complex, zoom: float, 
                                color_time: float, rotation: float = 0.0) -> Optional[ImageMobject]:
        """
        Render pure visual Mandelbrot frame optimized for beauty.
        
        Parameters
        ----------
        center : complex
            Center point in complex plane
        zoom : float
            Zoom level
        color_time : float
            Time parameter for color animation (0.0 to 1.0)
        rotation : float
            Rotation angle in radians
            
        Returns
        -------
        Optional[ImageMobject]
            High-quality visual fractal frame
        """
        try:
            # Fixed resolution for consistent image sizes in Transform
            resolution = self.base_resolution
            
            # Calculate Mandelbrot data
            mandelbrot_data = self.fractal_calculator.mandelbrot_set(
                width=resolution,
                height=resolution,
                center=center,
                zoom=zoom
            )
            
            # Apply dynamic coloring with time-based cycling
            rgb_array = self.colorizer.colorize_escape_data(
                mandelbrot_data,
                max_iterations=self.max_iterations,
                cycle_speed=color_time * 3.0 + zoom * 0.001,  # Dynamic color evolution
                use_histogram_equalization=True  # Enhanced color distribution
            )
            
            # Enhance contrast and saturation for visual appeal
            rgb_array = self._enhance_visual_quality(rgb_array, zoom)
            
            # Convert to PIL Image
            rgb_uint8 = (np.clip(rgb_array, 0, 1) * 255).astype(np.uint8)
            pil_image = Image.fromarray(rgb_uint8)
            
            # Apply rotation if specified
            if abs(rotation) > 0.01:
                pil_image = pil_image.rotate(
                    np.degrees(rotation), 
                    resample=Image.BICUBIC,
                    fillcolor=(0, 0, 0)
                )
            
            # Save with unique filename
            temp_filename = f"/tmp/mandelbrot_visual_{abs(hash((center, zoom, color_time))) % 100000}.png"
            pil_image.save(temp_filename, optimize=True, quality=95)
            
            return ImageMobject(temp_filename)
            
        except Exception as e:
            print(f"Visual rendering error: {e}")
            return None
    
    def _enhance_visual_quality(self, rgb_array: np.ndarray, zoom: float) -> np.ndarray:
        """
        Enhance visual quality with contrast and saturation adjustments.
        """
        # Increase contrast based on zoom level
        contrast_factor = 1.0 + min(0.3, zoom / 10000.0)
        enhanced = ((rgb_array - 0.5) * contrast_factor) + 0.5
        
        # Increase saturation for visual appeal
        saturation_boost = 1.2
        
        # Convert to HSV for saturation adjustment
        hsv = np.zeros_like(enhanced)
        for i in range(enhanced.shape[0]):
            for j in range(enhanced.shape[1]):
                r, g, b = enhanced[i, j]
                h, s, v = self._rgb_to_hsv(r, g, b)
                s = min(1.0, s * saturation_boost)
                hsv[i, j] = self._hsv_to_rgb(h, s, v)
        
        return np.clip(hsv, 0.0, 1.0)
    
    def _rgb_to_hsv(self, r: float, g: float, b: float) -> Tuple[float, float, float]:
        """Convert RGB to HSV color space."""
        max_val = max(r, g, b)
        min_val = min(r, g, b)
        diff = max_val - min_val
        
        # Value
        v = max_val
        
        # Saturation
        s = 0.0 if max_val == 0 else diff / max_val
        
        # Hue
        if diff == 0:
            h = 0.0
        elif max_val == r:
            h = (60 * ((g - b) / diff) + 360) % 360
        elif max_val == g:
            h = (60 * ((b - r) / diff) + 120) % 360
        else:
            h = (60 * ((r - g) / diff) + 240) % 360
        
        return h / 360.0, s, v
    
    def _hsv_to_rgb(self, h: float, s: float, v: float) -> Tuple[float, float, float]:
        """Convert HSV to RGB color space."""
        h *= 360.0
        c = v * s
        x = c * (1 - abs((h / 60) % 2 - 1))
        m = v - c
        
        if 0 <= h < 60:
            r, g, b = c, x, 0
        elif 60 <= h < 120:
            r, g, b = x, c, 0
        elif 120 <= h < 180:
            r, g, b = 0, c, x
        elif 180 <= h < 240:
            r, g, b = 0, x, c
        elif 240 <= h < 300:
            r, g, b = x, 0, c
        else:
            r, g, b = c, 0, x
        
        return r + m, g + m, b + m
    
    def create_visual_fallback(self):
        """Create simple visual fallback if fractal rendering fails."""
        
        # Create gradient circle as aesthetic placeholder
        circles = VGroup()
        for i in range(20):
            radius = 3.5 - i * 0.15
            opacity = 1.0 - i * 0.04
            color_intensity = i / 20.0
            
            circle = Circle(
                radius=radius,
                color=[color_intensity, 0.5, 1.0 - color_intensity],
                fill_opacity=opacity,
                stroke_width=0
            )
            circles.add(circle)
        
        circles.center()
        
        # Smooth animation sequence
        self.play(Create(circles, run_time=3.0), rate_func=smooth)
        
        # Gentle rotation and scaling
        for _ in range(10):
            self.play(
                Rotate(circles, angle=PI/6, run_time=2.0),
                circles.animate.scale(1.05).scale(0.95),
                rate_func=smooth
            )
        
        self.wait(2.0)
        self.play(FadeOut(circles, run_time=2.0))
    
    def _create_zoom_path(self) -> ZoomPath:
        """Create optimized zoom path for visual appeal."""
        
        if MANDELBROT_PATHS and 'seahorse_valley' in MANDELBROT_PATHS:
            path = MANDELBROT_PATHS['seahorse_valley']
            path.enable_loop_back(0.1)  # Quick loop back for 60-second duration
            return path
        
        # Fallback: Create simple zoom path
        path = ZoomPath("Visual Mandelbrot Zoom")
        
        # Key zoom points for visual journey
        path.add_keyframe(0+0j, 1.0, 0.0, easing=EasingFunction.EASE_IN)
        path.add_keyframe(-0.5+0j, 3.0, 0.15, easing=EasingFunction.EASE_IN_OUT)
        path.add_keyframe(-0.7+0.1j, 15.0, 0.35, easing=EasingFunction.EASE_IN_OUT)
        path.add_keyframe(-0.7269+0.1889j, 100.0, 0.60, easing=EasingFunction.EXPONENTIAL)
        path.add_keyframe(-0.72691+0.18891j, 1000.0, 0.80, easing=EasingFunction.EXPONENTIAL)
        path.add_keyframe(-0.726920+0.188910j, 10000.0, 0.90, easing=EasingFunction.CIRCULAR)
        
        path.enable_loop_back(0.05)  # Very smooth loop back
        return path
    
    def _initialize_calculator(self) -> Optional[FractalCalculator]:
        """Initialize high-quality fractal calculator."""
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
        """Initialize colorizer with fire palette for visual appeal."""
        try:
            if FractalColorizer:
                return FractalColorizer(
                    palette=ColorPalette.FIRE,
                    gamma=0.8,  # Slightly darker for more contrast
                    contrast=self.color_intensity
                )
        except Exception as e:
            print(f"Failed to initialize colorizer: {e}")
        return None

# Quick test version for development
class TestVisualMandelbrotZoom(VisualMandelbrotZoom):
    """Test version with reduced frames for faster development."""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.zoom_frames = 20  # Reduced for testing
        self.total_duration = 10.0  # Shorter test duration
    
    def construct(self):
        """Quick test with minimal frames."""
        
        if not UTILS_AVAILABLE:
            self.create_visual_fallback()
            return
        
        # Test with just a few key frames
        test_centers = [0+0j, -0.5+0j, -0.7+0.1j]
        test_zooms = [1.0, 10.0, 100.0]
        
        current_fractal = None
        
        for i, (center, zoom) in enumerate(zip(test_centers, test_zooms)):
            fractal = self.render_mandelbrot_visual(center, zoom, i/3.0)
            if fractal:
                fractal.scale_to_fit_height(config.frame_height * 0.9)
                fractal.center()
                
                if current_fractal is None:
                    self.play(FadeIn(fractal, run_time=1.0))
                    current_fractal = fractal
                else:
                    self.play(Transform(current_fractal, fractal, run_time=1.5))
                
                self.wait(0.5)
        
        if current_fractal:
            self.play(FadeOut(current_fractal, run_time=1.0))

if __name__ == "__main__":
    print("Pure Visual Mandelbrot Zoom Scene")
    print("Full: manim -pqh visual_01_mandelbrot_zoom.py VisualMandelbrotZoom")
    print("Test: manim -pql visual_01_mandelbrot_zoom.py TestVisualMandelbrotZoom")