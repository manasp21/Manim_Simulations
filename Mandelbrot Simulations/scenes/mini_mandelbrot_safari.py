"""
Mini-Mandelbrot Safari: Perfect Self-Similar Copies

This scene takes viewers on a safari through the Mandelbrot set to discover
perfect miniature copies of the entire set hidden at microscopic scales.
Each mini-Mandelbrot is an exact replica of the full set, demonstrating
the ultimate mathematical self-similarity.

Based on documented mini-Mandelbrot locations in mathematical literature.
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

class MiniMandelbrotSafari(Scene):
    """
    Safari through mini-Mandelbrot locations showing perfect self-similar copies.
    """
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.camera.background_color = "#001122"  # Deep safari night
        
        # High-quality parameters for mini-Mandelbrot detail
        self.base_resolution = 800
        self.max_iterations = 1024
        
        # Mini-Mandelbrot safari locations
        self.safari_sequence = self._create_mini_mandelbrot_safari()
        
        # Initialize fractal tools
        self.fractal_calculator = self._initialize_calculator()
        self.colorizer = self._initialize_colorizer()
        
    def construct(self):
        """Create the Mini-Mandelbrot safari journey."""
        
        if not UTILS_AVAILABLE or not self.fractal_calculator:
            self.create_fallback()
            return
        
        self.create_mini_mandelbrot_safari()
    
    def _create_mini_mandelbrot_safari(self) -> List[Tuple[complex, float, str]]:
        """
        Create safari sequence visiting famous mini-Mandelbrot locations.
        
        Each location shows perfect copies of the full Mandelbrot set at different scales.
        Based on documented mini-Mandelbrot coordinates.
        
        Returns:
            List of (center, zoom, description) tuples
        """
        return [
            # 1. Full Mandelbrot set - the original
            (0+0j, 1.0, "Original Mandelbrot Set"),
            
            # 2. Approach first mini-Mandelbrot region (upper antenna area)
            (-0.1+1.0j, 5.0, "Approaching Upper Antenna"),
            
            # 3. Famous mini-Mandelbrot location
            (-0.16070135+1.0375665j, 25.0, "First Mini-Mandelbrot Sighting"),
            
            # 4. Zoom into the mini-Mandelbrot
            (-0.16070135+1.0375665j, 150.0, "Mini-Mandelbrot Emergence"),
            
            # 5. Show the perfect copy clearly
            (-0.16070135+1.0375665j, 800.0, "Perfect Mandelbrot Copy"),
            
            # 6. Move to antenna mini-Mandelbrot
            (-1.25+0j, 10.0, "Approaching Main Antenna"),
            
            # 7. Antenna mini-Mandelbrot location
            (-1.769+0j, 50.0, "Antenna Mini-Mandelbrot"),
            
            # 8. Deep zoom into antenna copy
            (-1.7690+0j, 300.0, "Antenna Perfect Copy"),
            
            # 9. Third location - seahorse valley mini
            (-0.744+0.148j, 100.0, "Seahorse Valley Mini-Mandelbrot"),
            
            # 10. Final deep zoom showing infinite copies
            (-0.7440+0.1480j, 500.0, "Infinite Mini-Mandelbrot Copies")
        ]
    
    def create_mini_mandelbrot_safari(self):
        """
        Create safari journey through mini-Mandelbrot locations.
        """
        
        print(f"\n🦁 Starting Mini-Mandelbrot Safari")
        print(f"Safari route: {len(self.safari_sequence)} legendary locations")
        
        # Pre-render all safari frames
        safari_frames = []
        for i, (center, zoom, description) in enumerate(self.safari_sequence):
            print(f"\n📍 Safari Stop {i+1}/{len(self.safari_sequence)}: {description}")
            print(f"   Coordinates: {center}")
            print(f"   Magnification: {zoom:,.0f}x")
            
            safari_image = self.render_safari_frame(
                center=center, 
                zoom=zoom, 
                frame_id=i,
                description=description
            )
            
            if safari_image:
                safari_image.scale_to_fit_height(config.frame_height * 0.95)
                safari_image.center()
                safari_frames.append((safari_image, description, zoom))
                print(f"   ✅ Successfully captured")
            else:
                print(f"   ❌ Failed to capture")
                break
        
        if not safari_frames:
            print("❌ No safari stops captured successfully")
            self.create_fallback()
            return
        
        print(f"\n🎬 Successfully captured {len(safari_frames)} safari stops")
        print("🦁 Beginning the great mini-Mandelbrot safari...")
        
        # Start with the original Mandelbrot set
        current_frame, description, zoom = safari_frames[0]
        self.play(FadeIn(current_frame, run_time=2.5), rate_func=smooth)
        self.wait(1.5)  # Let viewers see the original
        
        # Safari through each mini-Mandelbrot location
        for i in range(1, len(safari_frames)):
            next_frame, description, zoom = safari_frames[i]
            
            print(f"🦁 Safari Journey {i}: {description} (magnification {zoom:,.0f}x)")
            
            # Variable timing for safari discovery
            if "Approaching" in description:
                transition_time = 2.0  # Slower approach to build anticipation
                pause_time = 1.0
            elif "Sighting" in description or "Emergence" in description:
                transition_time = 1.5  # Medium for first discovery
                pause_time = 2.0  # Longer to appreciate the discovery
            elif "Perfect Copy" in description or "Copies" in description:
                transition_time = 1.3  # Medium for detailed viewing
                pause_time = 3.0  # Very long to appreciate the self-similarity
            else:
                transition_time = 1.4  # Standard safari timing
                pause_time = 1.5
            
            # Safari transition
            self.play(
                ReplacementTransform(current_frame, next_frame),
                run_time=transition_time,
                rate_func=smooth
            )
            
            current_frame = next_frame
            
            # Pause at significant discovery points
            if zoom in [150, 800, 300, 500]:  # Key mini-Mandelbrot viewing points
                print(f"   🔍 Pausing to observe perfect self-similarity...")
                self.wait(pause_time)
        
        # Final dramatic pause showing the ultimate self-similarity
        print("🦁 Safari complete - witnessed infinite perfect copies")
        self.wait(4.0)
        
        # Fade to safari night
        print("🎬 End of safari expedition...")
        self.play(FadeOut(current_frame, run_time=2.5), rate_func=smooth)
    
    def render_safari_frame(self, center: complex, zoom: float, 
                           frame_id: int, description: str) -> Optional[ImageMobject]:
        """
        Render single safari frame optimized for mini-Mandelbrot discovery.
        """
        try:
            print(f"   🔍 Computing mini-Mandelbrot data...")
            
            # Higher iterations for mini-Mandelbrot clarity
            iterations = min(self.max_iterations, max(400, int(200 + np.log10(zoom) * 150)))
            print(f"   📊 Using {iterations} iterations for magnification {zoom:,.0f}x")
            
            # Calculate Mandelbrot data
            mandelbrot_data = self.fractal_calculator.mandelbrot_set(
                width=self.base_resolution,
                height=self.base_resolution,
                center=center,
                zoom=zoom
            )
            
            # Analyze mini-Mandelbrot data quality
            unique_values = len(set(mandelbrot_data.flatten()))
            data_range = f"{mandelbrot_data.min():.2f}-{mandelbrot_data.max():.2f}"
            print(f"   📈 Safari data quality: range={data_range}, unique_values={unique_values}")
            
            # Apply safari coloring - warm earth tones for discovery theme
            rgb_array = self.colorizer.colorize_escape_data(
                mandelbrot_data,
                max_iterations=iterations,
                cycle_speed=frame_id * 0.06 + np.log10(zoom) * 0.025,  # Safari color progression
                use_histogram_equalization=True
            )
            
            # Enhance mini-Mandelbrot visibility
            if zoom > 50:
                # Mini-Mandelbrot specific contrast enhancement
                contrast_boost = 1.0 + min(0.6, (zoom - 50) / 200.0)
                rgb_array = np.clip((rgb_array - 0.5) * contrast_boost + 0.5, 0, 1)
                
                # Add warm safari glow for mini-Mandelbrot emphasis
                if "Perfect Copy" in description or "Mini-Mandelbrot" in description:
                    glow_factor = 1.0 + min(0.3, np.log10(zoom) * 0.03)
                    rgb_array = np.clip(rgb_array * glow_factor, 0, 1)
                    print(f"   🌟 Applied mini-Mandelbrot highlighting: contrast={contrast_boost:.2f}, glow={glow_factor:.2f}")
                else:
                    print(f"   🌟 Applied safari enhancement: contrast={contrast_boost:.2f}")
            
            # Convert to PIL Image
            rgb_uint8 = (np.clip(rgb_array, 0, 1) * 255).astype(np.uint8)
            pil_image = Image.fromarray(rgb_uint8)
            
            # Unique filename for safari expedition
            timestamp = int(time.time() * 1000000)
            safe_description = description.replace(" ", "_").replace("-", "_")
            temp_filename = f"/tmp/safari_{frame_id:02d}_{safe_description}_{timestamp}_{hash((center, zoom)) % 10000}.png"
            pil_image.save(temp_filename, optimize=True, quality=95)
            
            print(f"   💾 Safari photo saved: {temp_filename}")
            
            return ImageMobject(temp_filename)
            
        except Exception as e:
            print(f"   ❌ Safari capture failed for frame {frame_id}: {e}")
            import traceback
            traceback.print_exc()
            return None
    
    def create_fallback(self):
        """Fallback if safari expedition fails."""
        error_text = Text("Mini-Mandelbrot Safari\nExpedition Error", font_size=36, color=ORANGE)
        self.play(Write(error_text))
        self.wait(2)
        self.play(FadeOut(error_text))
    
    def _initialize_calculator(self) -> Optional[FractalCalculator]:
        """Initialize calculator for mini-Mandelbrot discovery."""
        try:
            if FractalCalculator:
                return create_fractal_calculator(
                    fractal_type='mandelbrot',
                    max_iterations=self.max_iterations,
                    bailout_radius=2.0
                )
        except Exception as e:
            print(f"Failed to initialize safari calculator: {e}")
        return None
    
    def _initialize_colorizer(self) -> Optional[FractalColorizer]:
        """Initialize safari colorizer with earth tones for discovery theme."""
        try:
            if FractalColorizer:
                return FractalColorizer(
                    palette=ColorPalette.ELECTRIC,  # Electric palette for discovery excitement
                    gamma=0.65,
                    contrast=1.6
                )
        except Exception as e:
            print(f"Failed to initialize safari colorizer: {e}")
        return None

if __name__ == "__main__":
    print("🦁 Mini-Mandelbrot Safari - Perfect Self-Similar Copy Expedition")
    print("Usage: manim -pql mini_mandelbrot_safari.py MiniMandelbrotSafari")