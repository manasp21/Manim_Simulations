"""
Ultrathink Visual Scene 1: True Continuous Mandelbrot Deep Zoom

This version uses ReplacementTransform to actually show different fractal images
instead of being fooled by Manim's caching system.
"""

from manim import *
import numpy as np
import sys
import os
from typing import Tuple, Optional, List
from PIL import Image
import time

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

class VisualMandelbrotZoomUltrathink(Scene):
    """
    True continuous zoom using ReplacementTransform to avoid caching issues.
    """
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.camera.background_color = "#000000"
        
        # Fewer frames but higher quality for true zoom effect
        self.zoom_frames = 15
        self.base_resolution = 600  # Higher resolution for better detail
        self.max_iterations = 512   # Higher iterations for deep zoom
        
        # Initialize fractal tools
        self.fractal_calculator = self._initialize_calculator()
        self.colorizer = self._initialize_colorizer()
        
    def construct(self):
        """Create true continuous zoom sequence."""
        
        if not UTILS_AVAILABLE or not self.fractal_calculator:
            self.create_visual_fallback()
            return
        
        self.create_true_continuous_zoom()
    
    def create_true_continuous_zoom(self):
        """
        Create TRUE continuous zoom by using ReplacementTransform.
        """
        
        # Define dramatic zoom sequence into seahorse valley
        zoom_sequence = []
        
        # Start with overview
        center = 0+0j
        zoom = 1.0
        zoom_sequence.append((center, zoom))
        
        # Progressive zoom into seahorse valley
        for i in range(self.zoom_frames - 1):
            t = (i + 1) / (self.zoom_frames - 1)
            
            # Interpolate center toward seahorse valley
            target_center = -0.7269 + 0.1889j
            center = (1 - t) * 0j + t * target_center
            
            # Exponential zoom progression
            zoom = 1.0 * (50.0 ** t)  # Zoom from 1 to 50
            
            zoom_sequence.append((center, zoom))
        
        print(f"Zoom sequence: {len(zoom_sequence)} frames")
        for i, (c, z) in enumerate(zoom_sequence):
            print(f"  Frame {i}: center={c}, zoom={z:.2f}")
        
        # Render all frames first to avoid caching issues
        fractal_frames = []
        for i, (center, zoom) in enumerate(zoom_sequence):
            print(f"Pre-rendering frame {i+1}/{len(zoom_sequence)}...")
            
            fractal_image = self.render_mandelbrot_frame(
                center=center, 
                zoom=zoom, 
                frame_id=i,
                color_cycle=i * 0.1
            )
            
            if fractal_image:
                fractal_image.scale_to_fit_height(config.frame_height * 0.9)
                fractal_image.center()
                fractal_frames.append(fractal_image)
            else:
                print(f"Failed to render frame {i}")
                break
        
        if not fractal_frames:
            print("No frames rendered successfully")
            self.create_visual_fallback()
            return
        
        print(f"Successfully rendered {len(fractal_frames)} frames")
        
        # Start with first frame
        current_frame = fractal_frames[0]
        self.play(FadeIn(current_frame, run_time=1.0))
        
        # Sequence through all frames using ReplacementTransform
        for i in range(1, len(fractal_frames)):
            next_frame = fractal_frames[i]
            
            print(f"Playing transition {i}: zoom {zoom_sequence[i-1][1]:.2f} -> {zoom_sequence[i][1]:.2f}")
            
            # Use ReplacementTransform to actually replace the image
            self.play(
                ReplacementTransform(current_frame, next_frame),
                run_time=0.8,
                rate_func=smooth
            )
            
            current_frame = next_frame
            
            # Brief pause at certain zoom levels
            zoom = zoom_sequence[i][1]
            if zoom in [2.0, 5.0, 10.0, 25.0]:
                self.wait(0.3)
        
        # Final pause and fade out
        self.wait(1.5)
        self.play(FadeOut(current_frame, run_time=1.0))
    
    def render_mandelbrot_frame(self, center: complex, zoom: float, 
                               frame_id: int, color_cycle: float = 0.0) -> Optional[ImageMobject]:
        """
        Render single Mandelbrot frame with unique filename to avoid caching.
        """
        try:
            print(f"  Computing Mandelbrot at center={center}, zoom={zoom:.2f}")
            
            # Calculate Mandelbrot data
            mandelbrot_data = self.fractal_calculator.mandelbrot_set(
                width=self.base_resolution,
                height=self.base_resolution,
                center=center,
                zoom=zoom
            )
            
            # Check for variation in the data
            unique_values = len(set(mandelbrot_data.flatten()))
            print(f"  Data range: {mandelbrot_data.min():.2f}-{mandelbrot_data.max():.2f}, unique: {unique_values}")
            
            # Apply dynamic coloring
            rgb_array = self.colorizer.colorize_escape_data(
                mandelbrot_data,
                max_iterations=self.max_iterations,
                cycle_speed=color_cycle + np.log10(zoom) * 0.05,
                use_histogram_equalization=True
            )
            
            # Enhance contrast for zoom levels
            if zoom > 10:
                contrast_boost = 1.0 + min(0.3, (zoom - 10) / 100.0)
                rgb_array = np.clip((rgb_array - 0.5) * contrast_boost + 0.5, 0, 1)
            
            # Convert to PIL Image
            rgb_uint8 = (np.clip(rgb_array, 0, 1) * 255).astype(np.uint8)
            pil_image = Image.fromarray(rgb_uint8)
            
            # CRITICAL: Use timestamp and frame_id to ensure unique filenames
            timestamp = int(time.time() * 1000000)  # microsecond precision
            temp_filename = f"/tmp/mandelbrot_ultrathink_{frame_id}_{timestamp}_{hash((center, zoom)) % 10000}.png"
            pil_image.save(temp_filename, optimize=True, quality=95)
            
            print(f"  Saved: {temp_filename}")
            
            return ImageMobject(temp_filename)
            
        except Exception as e:
            print(f"Error rendering frame {frame_id}: {e}")
            import traceback
            traceback.print_exc()
            return None
    
    def create_visual_fallback(self):
        """Fallback if fractal rendering fails."""
        text = Text("Fractal System Error", font_size=48, color=RED)
        self.play(Write(text))
        self.wait(2)
        self.play(FadeOut(text))
    
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
        """Initialize colorizer."""
        try:
            if FractalColorizer:
                return FractalColorizer(
                    palette=ColorPalette.FIRE,
                    gamma=0.8,
                    contrast=1.3
                )
        except Exception as e:
            print(f"Failed to initialize colorizer: {e}")
        return None

if __name__ == "__main__":
    print("Ultrathink Mandelbrot Zoom - True Continuous Zoom")
    print("manim -pql visual_01_mandelbrot_zoom_ultrathink.py VisualMandelbrotZoomUltrathink")