"""
Seahorse Valley Journey: True Self-Similar Mandelbrot Zoom

This scene takes viewers on a mathematically accurate journey into the famous
Seahorse Valley region of the Mandelbrot set, revealing how seahorse-like 
structures repeat at increasingly smaller scales, demonstrating the infinite
self-similarity that makes fractals so mesmerizing.

Based on coordinates from Robert Munafo's Mu-ency (mrob.com) and mathematical literature.
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

class SeahorseValleyJourney(Scene):
    """
    Journey into Seahorse Valley showing self-similar structures at all scales.
    """
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.camera.background_color = "#000000"
        
        # High-quality parameters for deep zoom
        self.base_resolution = 800
        self.max_iterations = 1024  # Higher for deep detail
        
        # Mathematically accurate Seahorse Valley coordinates
        self.zoom_sequence = self._create_seahorse_zoom_sequence()
        
        # Initialize fractal tools
        self.fractal_calculator = self._initialize_calculator()
        self.colorizer = self._initialize_colorizer()
        
    def construct(self):
        """Create the Seahorse Valley journey."""
        
        if not UTILS_AVAILABLE or not self.fractal_calculator:
            self.create_fallback()
            return
        
        self.create_seahorse_valley_journey()
    
    def _create_seahorse_zoom_sequence(self) -> List[Tuple[complex, float, str]]:
        """
        Create mathematically accurate zoom sequence into Seahorse Valley.
        
        Based on coordinates from Robert Munafo's Mu-ency and mathematical literature.
        Each step reveals new self-similar structures.
        
        Returns:
            List of (center, zoom, description) tuples
        """
        return [
            # 1. Full Mandelbrot set overview
            (0+0j, 1.0, "Full Mandelbrot Set"),
            
            # 2. Approach the main cardioid boundary  
            (-0.5+0j, 3.0, "Approaching Main Cardioid"),
            
            # 3. Enter Seahorse Valley region
            (-0.75+0.1j, 15.0, "Entering Seahorse Valley"),
            
            # 4. First seahorse structures emerge
            (-0.7548+0.1167j, 100.0, "First Seahorse Structures"),
            
            # 5. Detailed seahorse valley (from MROB coordinates)
            (-0.74548+0.11669j, 800.0, "Detailed Seahorse Valley"),
            
            # 6. Mini-seahorses emerge
            (-0.7454860+0.1166920j, 5000.0, "Mini-Seahorse Emergence"),
            
            # 7. Deep zoom - recursive seahorses
            (-0.74548603+0.11669203j, 40000.0, "Recursive Seahorse Patterns"),
            
            # 8. Ultra-deep - infinite self-similarity (MROB precision)
            (-0.7454860356+0.1166920341j, 300000.0, "Infinite Self-Similarity"),
            
            # 9. Microscopic detail - identical structures
            (-0.74548603559+0.11669203415j, 2000000.0, "Microscopic Seahorse Copies"),
            
            # 10. Maximum zoom - perfect self-similarity
            (-0.745486035590838+0.116692034154248j, 15000000.0, "Perfect Self-Similar Structures")
        ]
    
    def create_seahorse_valley_journey(self):
        """
        Create the journey through Seahorse Valley revealing self-similar structures.
        """
        
        print(f"\n🐴 Starting Seahorse Valley Journey")
        print(f"Zoom sequence: {len(self.zoom_sequence)} mathematically significant locations")
        
        # Pre-render all frames for smooth animation
        fractal_frames = []
        for i, (center, zoom, description) in enumerate(self.zoom_sequence):
            print(f"\n📍 Frame {i+1}/{len(self.zoom_sequence)}: {description}")
            print(f"   Center: {center}")
            print(f"   Zoom: {zoom:,.0f}x")
            
            fractal_image = self.render_seahorse_frame(
                center=center, 
                zoom=zoom, 
                frame_id=i,
                description=description
            )
            
            if fractal_image:
                fractal_image.scale_to_fit_height(config.frame_height * 0.95)
                fractal_image.center()
                fractal_frames.append((fractal_image, description, zoom))
                print(f"   ✅ Successfully rendered")
            else:
                print(f"   ❌ Failed to render")
                break
        
        if not fractal_frames:
            print("❌ No frames rendered successfully")
            self.create_fallback()
            return
        
        print(f"\n🎬 Successfully rendered {len(fractal_frames)} frames")
        print("🎥 Starting animation sequence...")
        
        # Start with first frame
        current_frame, description, zoom = fractal_frames[0]
        self.play(FadeIn(current_frame, run_time=2.0), rate_func=smooth)
        self.wait(1.0)  # Let viewers appreciate the full set
        
        # Journey through each zoom level
        for i in range(1, len(fractal_frames)):
            next_frame, description, zoom = fractal_frames[i]
            
            print(f"🔄 Transition {i}: {description} (zoom {zoom:,.0f}x)")
            
            # Variable timing based on zoom significance
            if zoom < 100:
                transition_time = 1.5  # Slower for initial approach
                pause_time = 0.8
            elif zoom < 10000:
                transition_time = 1.2  # Medium for structure emergence
                pause_time = 1.0
            else:
                transition_time = 1.0  # Faster for deep similarity
                pause_time = 1.2  # Longer pause to appreciate detail
            
            # Smooth transition using ReplacementTransform
            self.play(
                ReplacementTransform(current_frame, next_frame),
                run_time=transition_time,
                rate_func=smooth
            )
            
            current_frame = next_frame
            
            # Pause to let viewers appreciate the self-similar structures
            if zoom in [100, 5000, 40000, 2000000]:  # Key structural emergence points
                print(f"   ⏸️  Pausing to show self-similar structures...")
                self.wait(pause_time)
        
        # Final dramatic pause at maximum zoom
        print("🏁 Reached maximum zoom - showing perfect self-similarity")
        self.wait(3.0)
        
        # Fade out
        print("🎬 Ending sequence...")
        self.play(FadeOut(current_frame, run_time=2.0), rate_func=smooth)
    
    def render_seahorse_frame(self, center: complex, zoom: float, 
                             frame_id: int, description: str) -> Optional[ImageMobject]:
        """
        Render single frame of Seahorse Valley with optimized settings for deep zoom.
        """
        try:
            print(f"   🔄 Computing fractal data...")
            
            # Use adaptive iterations based on zoom level for better detail
            iterations = min(self.max_iterations, max(256, int(100 + np.log10(zoom) * 100)))
            print(f"   📊 Using {iterations} iterations for zoom {zoom:,.0f}x")
            
            # Calculate Mandelbrot data
            mandelbrot_data = self.fractal_calculator.mandelbrot_set(
                width=self.base_resolution,
                height=self.base_resolution,
                center=center,
                zoom=zoom
            )
            
            # Analyze data quality
            unique_values = len(set(mandelbrot_data.flatten()))
            data_range = f"{mandelbrot_data.min():.2f}-{mandelbrot_data.max():.2f}"
            print(f"   📈 Data quality: range={data_range}, unique_values={unique_values}")
            
            if unique_values < 10:
                print(f"   ⚠️  Low diversity detected - may need higher iterations")
            
            # Apply sophisticated coloring for seahorse structures
            rgb_array = self.colorizer.colorize_escape_data(
                mandelbrot_data,
                max_iterations=iterations,
                cycle_speed=frame_id * 0.05 + np.log10(zoom) * 0.02,  # Subtle color evolution
                use_histogram_equalization=True
            )
            
            # Enhance contrast for deep zoom detail
            if zoom > 1000:
                contrast_boost = 1.0 + min(0.4, (zoom - 1000) / 100000.0)
                rgb_array = np.clip((rgb_array - 0.5) * contrast_boost + 0.5, 0, 1)
                print(f"   🎨 Applied contrast boost: {contrast_boost:.2f}")
            
            # Convert to PIL Image
            rgb_uint8 = (np.clip(rgb_array, 0, 1) * 255).astype(np.uint8)
            pil_image = Image.fromarray(rgb_uint8)
            
            # Unique filename to prevent caching
            timestamp = int(time.time() * 1000000)
            safe_description = description.replace(" ", "_").replace("-", "_")
            temp_filename = f"/tmp/seahorse_{frame_id:02d}_{safe_description}_{timestamp}_{hash((center, zoom)) % 10000}.png"
            pil_image.save(temp_filename, optimize=True, quality=95)
            
            print(f"   💾 Saved: {temp_filename}")
            
            return ImageMobject(temp_filename)
            
        except Exception as e:
            print(f"   ❌ Error rendering frame {frame_id}: {e}")
            import traceback
            traceback.print_exc()
            return None
    
    def create_fallback(self):
        """Fallback if fractal rendering fails."""
        error_text = Text("Seahorse Valley\nRendering Error", font_size=36, color=RED)
        self.play(Write(error_text))
        self.wait(2)
        self.play(FadeOut(error_text))
    
    def _initialize_calculator(self) -> Optional[FractalCalculator]:
        """Initialize high-precision fractal calculator for deep zoom."""
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
        """Initialize colorizer optimized for seahorse structures."""
        try:
            if FractalColorizer:
                return FractalColorizer(
                    palette=ColorPalette.OCEAN,  # Ocean palette for seahorse theme
                    gamma=0.7,
                    contrast=1.4
                )
        except Exception as e:
            print(f"Failed to initialize colorizer: {e}")
        return None

if __name__ == "__main__":
    print("🐴 Seahorse Valley Journey - Mathematically Accurate Self-Similar Zoom")
    print("Usage: manim -pql seahorse_valley_journey.py SeahorseValleyJourney")