"""
Double Spiral Galaxy: Infinite Recursive Spiral Patterns

This scene explores the Double Spiral Valley of the Mandelbrot set, where
infinite double spirals branch into more double spirals at every scale.
Shows the cosmic-like spiral structures that demonstrate perfect mathematical
self-similarity in nature.

Based on mathematical literature about spiral structures in the Mandelbrot set.
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

class DoubleSpiralGalaxy(Scene):
    """
    Journey into Double Spiral Valley showing infinite recursive spiral patterns.
    """
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.camera.background_color = "#000011"  # Deep space background
        
        # High-quality parameters for spiral detail
        self.base_resolution = 800
        self.max_iterations = 1024
        
        # Double Spiral Valley coordinates (R2.1/2a side)
        self.spiral_sequence = self._create_spiral_zoom_sequence()
        
        # Initialize fractal tools
        self.fractal_calculator = self._initialize_calculator()
        self.colorizer = self._initialize_colorizer()
        
    def construct(self):
        """Create the Double Spiral Galaxy journey."""
        
        if not UTILS_AVAILABLE or not self.fractal_calculator:
            self.create_fallback()
            return
        
        self.create_spiral_galaxy_journey()
    
    def _create_spiral_zoom_sequence(self) -> List[Tuple[complex, float, str]]:
        """
        Create zoom sequence into Double Spiral Valley.
        
        Focuses on locations known for spiral structures and recursive patterns.
        Based on coordinates for spiral centers and Misiurewicz points.
        
        Returns:
            List of (center, zoom, description) tuples
        """
        return [
            # 1. Full set with spiral regions visible
            (0+0j, 1.0, "Mandelbrot Set Overview"),
            
            # 2. Approach the main spiral region
            (-0.7+0.05j, 8.0, "Approaching Spiral Valley"),
            
            # 3. Enter Double Spiral Valley (R2.1/2a side)
            (-0.75+0.05j, 25.0, "Entering Double Spiral Valley"),
            
            # 4. First double spirals emerge
            (-0.745+0.08j, 150.0, "First Double Spiral Structures"),
            
            # 5. Detailed spiral arms
            (-0.7445+0.085j, 800.0, "Detailed Spiral Arms"),
            
            # 6. Spiral branching points
            (-0.74445+0.0855j, 4500.0, "Spiral Branching Points"),
            
            # 7. Recursive spiral emergence
            (-0.744445+0.08555j, 25000.0, "Recursive Spiral Patterns"),
            
            # 8. Deep spiral recursion
            (-0.7444445+0.085555j, 140000.0, "Deep Spiral Recursion"),
            
            # 9. Infinite spiral branching
            (-0.74444445+0.0855555j, 800000.0, "Infinite Spiral Branching"),
            
            # 10. Perfect spiral self-similarity
            (-0.744444445+0.08555555j, 4500000.0, "Perfect Spiral Self-Similarity")
        ]
    
    def create_spiral_galaxy_journey(self):
        """
        Create journey through spiral galaxy showing recursive patterns.
        """
        
        print(f"\n🌌 Starting Double Spiral Galaxy Journey")
        print(f"Spiral sequence: {len(self.spiral_sequence)} cosmic locations")
        
        # Pre-render all spiral frames
        spiral_frames = []
        for i, (center, zoom, description) in enumerate(self.spiral_sequence):
            print(f"\n🌀 Frame {i+1}/{len(self.spiral_sequence)}: {description}")
            print(f"   Center: {center}")
            print(f"   Zoom: {zoom:,.0f}x")
            
            spiral_image = self.render_spiral_frame(
                center=center, 
                zoom=zoom, 
                frame_id=i,
                description=description
            )
            
            if spiral_image:
                spiral_image.scale_to_fit_height(config.frame_height * 0.95)
                spiral_image.center()
                spiral_frames.append((spiral_image, description, zoom))
                print(f"   ✅ Successfully rendered")
            else:
                print(f"   ❌ Failed to render")
                break
        
        if not spiral_frames:
            print("❌ No frames rendered successfully")
            self.create_fallback()
            return
        
        print(f"\n🎬 Successfully rendered {len(spiral_frames)} frames")
        print("🌌 Starting cosmic spiral journey...")
        
        # Start with overview
        current_frame, description, zoom = spiral_frames[0]
        self.play(FadeIn(current_frame, run_time=2.5), rate_func=smooth)
        self.wait(1.2)  # Let viewers locate the spiral regions
        
        # Journey through each spiral level
        for i in range(1, len(spiral_frames)):
            next_frame, description, zoom = spiral_frames[i]
            
            print(f"🌀 Spiral Transition {i}: {description} (zoom {zoom:,.0f}x)")
            
            # Variable timing for spiral appreciation
            if zoom < 200:
                transition_time = 1.8  # Slower for initial spiral discovery
                pause_time = 1.0
            elif zoom < 10000:
                transition_time = 1.4  # Medium for spiral arm details
                pause_time = 1.2  
            else:
                transition_time = 1.2  # Faster for deep recursive patterns
                pause_time = 1.5  # Longer pause to appreciate infinite recursion
            
            # Smooth spiral transition
            self.play(
                ReplacementTransform(current_frame, next_frame),
                run_time=transition_time,
                rate_func=smooth
            )
            
            current_frame = next_frame
            
            # Pause at key spiral emergence points
            if zoom in [150, 4500, 25000, 800000]:
                print(f"   🌀 Pausing to show spiral recursion...")
                self.wait(pause_time)
        
        # Final dramatic pause showing infinite spiral patterns
        print("🌌 Reached maximum spiral depth - showing infinite recursion")
        self.wait(4.0)
        
        # Fade to cosmic black
        print("🎬 Ending cosmic journey...")
        self.play(FadeOut(current_frame, run_time=2.5), rate_func=smooth)
    
    def render_spiral_frame(self, center: complex, zoom: float, 
                           frame_id: int, description: str) -> Optional[ImageMobject]:
        """
        Render single frame optimized for spiral structures.
        """
        try:
            print(f"   🌀 Computing spiral fractal data...")
            
            # Higher iterations for spiral detail
            iterations = min(self.max_iterations, max(300, int(150 + np.log10(zoom) * 120)))
            print(f"   📊 Using {iterations} iterations for zoom {zoom:,.0f}x")
            
            # Calculate Mandelbrot data
            mandelbrot_data = self.fractal_calculator.mandelbrot_set(
                width=self.base_resolution,
                height=self.base_resolution,
                center=center,
                zoom=zoom
            )
            
            # Analyze spiral data quality
            unique_values = len(set(mandelbrot_data.flatten()))
            data_range = f"{mandelbrot_data.min():.2f}-{mandelbrot_data.max():.2f}"
            print(f"   📈 Spiral data quality: range={data_range}, unique_values={unique_values}")
            
            # Apply cosmic coloring for spiral galaxy effect
            rgb_array = self.colorizer.colorize_escape_data(
                mandelbrot_data,
                max_iterations=iterations,
                cycle_speed=frame_id * 0.08 + np.log10(zoom) * 0.03,  # Cosmic color cycling
                use_histogram_equalization=True
            )
            
            # Enhance spiral contrast and add cosmic glow
            if zoom > 500:
                # Spiral-specific contrast enhancement
                contrast_boost = 1.0 + min(0.5, (zoom - 500) / 50000.0)
                rgb_array = np.clip((rgb_array - 0.5) * contrast_boost + 0.5, 0, 1)
                
                # Add subtle cosmic glow effect
                glow_factor = 1.0 + min(0.2, np.log10(zoom) * 0.02)
                rgb_array = np.clip(rgb_array * glow_factor, 0, 1)
                
                print(f"   🌌 Applied cosmic enhancement: contrast={contrast_boost:.2f}, glow={glow_factor:.2f}")
            
            # Convert to PIL Image
            rgb_uint8 = (np.clip(rgb_array, 0, 1) * 255).astype(np.uint8)
            pil_image = Image.fromarray(rgb_uint8)
            
            # Unique filename for spiral frames
            timestamp = int(time.time() * 1000000)
            safe_description = description.replace(" ", "_").replace("-", "_")
            temp_filename = f"/tmp/spiral_{frame_id:02d}_{safe_description}_{timestamp}_{hash((center, zoom)) % 10000}.png"
            pil_image.save(temp_filename, optimize=True, quality=95)
            
            print(f"   💾 Saved: {temp_filename}")
            
            return ImageMobject(temp_filename)
            
        except Exception as e:
            print(f"   ❌ Error rendering spiral frame {frame_id}: {e}")
            import traceback
            traceback.print_exc()
            return None
    
    def create_fallback(self):
        """Fallback if spiral rendering fails."""
        error_text = Text("Double Spiral Galaxy\nRendering Error", font_size=36, color=BLUE)
        self.play(Write(error_text))
        self.wait(2)
        self.play(FadeOut(error_text))
    
    def _initialize_calculator(self) -> Optional[FractalCalculator]:
        """Initialize calculator for spiral structures."""
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
        """Initialize cosmic colorizer for spiral galaxy effect."""
        try:
            if FractalColorizer:
                return FractalColorizer(
                    palette=ColorPalette.COSMIC,  # Cosmic palette for galaxy theme
                    gamma=0.6,
                    contrast=1.5
                )
        except Exception as e:
            print(f"Failed to initialize colorizer: {e}")
        return None

if __name__ == "__main__":
    print("🌌 Double Spiral Galaxy - Infinite Recursive Spiral Journey")
    print("Usage: manim -pql double_spiral_galaxy.py DoubleSpiralGalaxy")