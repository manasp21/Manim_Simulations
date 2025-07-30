"""
Pure White-on-Black Mandelbrot Set Visualization

Ultra-high quality static image generation of the Mandelbrot set using
the classic mathematical representation: pure white exterior, pure black set.

This scene creates the iconic mathematical visualization where the Mandelbrot
set appears as a black silhouette against a white background, suitable for
research papers, mathematical texts, and high-quality mathematical art.

Features:
- Multiple zoom regions and resolutions
- Configurable image quality and iterations
- Support for different mathematical regions of interest
- Clean, academic-style output
"""

from manim import *
import numpy as np
import sys
import os
from typing import Tuple, Optional, List, Dict
from PIL import Image
import datetime

# Add project root to path for imports
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)

try:
    from utils.fractal_algorithms import FractalCalculator, create_fractal_calculator
    from utils.color_schemes import FractalColorizer, ColorPalette, WHITE_ON_BLACK_COLORIZER
    UTILS_AVAILABLE = True
except ImportError as e:
    print(f"Import error: {e}")
    UTILS_AVAILABLE = False

class MandelbrotWhiteOnBlack(Scene):
    """
    High-quality white-on-black Mandelbrot set visualization.
    
    Generates ultra-clean mathematical representations suitable for
    academic papers, textbooks, and mathematical art.
    """
    
    def __init__(self, **kwargs):
        """Initialize white-on-black Mandelbrot scene."""
        super().__init__(**kwargs)
        self.camera.background_color = BLACK  # Black background for dramatic white-on-black visualization
        
        # High-quality rendering parameters
        self.base_resolution = 2048  # Ultra-high resolution for crisp detail
        self.max_iterations = 1024   # High iteration count for smooth boundaries
        self.bailout_radius = 2.0    # Standard mathematical definition
        
        # Configurable viewing parameters
        self.center = 0.0 + 0.0j     # Default: full Mandelbrot set
        self.zoom = 1.0              # Default: full view
        self.rotation = 0.0          # Default: no rotation
        
        # Quality and output settings
        self.antialias_factor = 2    # 2x oversampling for smooth edges
        self.image_quality = 95      # High PNG compression quality
        
        # Initialize computational tools
        self.fractal_calculator = self._initialize_calculator()
        self.colorizer = self._initialize_colorizer()
        
        # Predefined interesting regions
        self.regions = self._define_interesting_regions()
    
    def construct(self):
        """Generate the white-on-black Mandelbrot image."""
        
        if not UTILS_AVAILABLE or not self.fractal_calculator:
            self.create_fallback_visualization()
            return
        
        # Generate the Mandelbrot set image
        mandelbrot_image = self.generate_mandelbrot_image()
        
        if mandelbrot_image:
            # Display the image
            mandelbrot_image.scale_to_fit_width(config.frame_width * 0.95)
            mandelbrot_image.center()
            
            # Clean presentation - immediate display
            self.add(mandelbrot_image)
            self.wait(2.0)  # Hold for viewing
            
        else:
            self.create_fallback_visualization()
    
    def generate_mandelbrot_image(self) -> Optional[ImageMobject]:
        """
        Generate high-quality white-on-black Mandelbrot set image.
        
        Returns
        -------
        Optional[ImageMobject]
            High-quality Mandelbrot set visualization
        """
        try:
            # Calculate effective resolution with antialiasing
            effective_resolution = self.base_resolution * self.antialias_factor
            
            print(f"Generating Mandelbrot set...")
            print(f"Resolution: {effective_resolution}x{effective_resolution}")
            print(f"Center: {self.center}")
            print(f"Zoom: {self.zoom}")
            print(f"Iterations: {self.max_iterations}")
            
            # Calculate Mandelbrot escape data
            mandelbrot_data = self.fractal_calculator.mandelbrot_set(
                width=effective_resolution,
                height=effective_resolution,
                center=self.center,
                zoom=self.zoom
            )
            
            print(f"Fractal calculation complete.")
            
            # Apply white-on-black coloring
            rgb_array = self.colorizer.colorize_escape_data(
                mandelbrot_data,
                max_iterations=self.max_iterations,
                cycle_speed=0.0,  # No color cycling for static image
                use_histogram_equalization=False  # Pure binary coloring
            )
            
            # Apply antialiasing by downsampling
            if self.antialias_factor > 1:
                rgb_array = self._apply_antialiasing(rgb_array)
            
            print(f"Color processing complete.")
            
            # Convert to PIL Image with high quality
            rgb_uint8 = (np.clip(rgb_array, 0, 1) * 255).astype(np.uint8)
            pil_image = Image.fromarray(rgb_uint8)
            
            # Apply rotation if specified
            if abs(self.rotation) > 0.01:
                pil_image = pil_image.rotate(
                    np.degrees(self.rotation),
                    resample=Image.BICUBIC,
                    fillcolor=(0, 0, 0)  # Black background
                )
            
            # Save high-quality image
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"/tmp/mandelbrot_white_black_{timestamp}_{self.base_resolution}.png"
            pil_image.save(filename, optimize=True, quality=self.image_quality)
            
            print(f"High-quality image saved: {filename}")
            
            return ImageMobject(filename)
            
        except Exception as e:
            print(f"Error generating Mandelbrot image: {e}")
            return None
    
    def _apply_antialiasing(self, rgb_array: np.ndarray) -> np.ndarray:
        """
        Apply antialiasing by intelligent downsampling.
        
        For white-on-black images, we use averaging to smooth boundaries
        while preserving the binary nature of the final image.
        """
        factor = self.antialias_factor
        height, width = rgb_array.shape[:2]
        
        # Calculate target dimensions
        target_height = height // factor
        target_width = width // factor
        
        # Initialize output array
        downsampled = np.zeros((target_height, target_width, 3))
        
        # Average blocks for smooth antialiasing
        for i in range(target_height):
            for j in range(target_width):
                # Extract block
                block = rgb_array[i*factor:(i+1)*factor, j*factor:(j+1)*factor]
                
                # Average the block
                downsampled[i, j] = np.mean(block, axis=(0, 1))
        
        return downsampled
    
    def set_region(self, region_name: str):
        """
        Set viewing region to a predefined interesting area.
        
        Parameters
        ----------
        region_name : str
            Name of the region ('overview', 'seahorse', 'lightning', etc.)
        """
        if region_name in self.regions:
            region = self.regions[region_name]
            self.center = region['center']
            self.zoom = region['zoom']
            self.rotation = region.get('rotation', 0.0)
            print(f"Set region to '{region_name}': center={self.center}, zoom={self.zoom}")
        else:
            print(f"Unknown region '{region_name}'. Available: {list(self.regions.keys())}")
    
    def set_custom_view(self, center: complex, zoom: float, rotation: float = 0.0):
        """
        Set custom viewing parameters.
        
        Parameters
        ----------
        center : complex
            Center point in complex plane
        zoom : float
            Zoom level (higher = more zoomed in)
        rotation : float, optional
            Rotation angle in radians
        """
        self.center = center
        self.zoom = zoom
        self.rotation = rotation
        print(f"Custom view: center={center}, zoom={zoom}, rotation={rotation}")
    
    def set_quality(self, resolution: int, iterations: int, antialias: int = 2):
        """
        Configure image quality settings.
        
        Parameters
        ----------
        resolution : int
            Base image resolution (pixels)
        iterations : int
            Maximum iterations for fractal calculation
        antialias : int
            Antialiasing factor (1 = none, 2 = 2x, 4 = 4x)
        """
        self.base_resolution = resolution
        self.max_iterations = iterations
        self.antialias_factor = antialias
        
        # Reinitialize calculator with new parameters
        self.fractal_calculator = self._initialize_calculator()
        
        print(f"Quality settings: {resolution}x{resolution}, {iterations} iterations, {antialias}x AA")
    
    def create_fallback_visualization(self):
        """Create simple fallback if fractal computation fails."""
        # Simple geometric approximation of Mandelbrot set shape
        main_body = Circle(radius=1.2, color=BLACK, fill_opacity=1.0)
        main_body.shift(LEFT * 0.5)
        
        small_circle = Circle(radius=0.3, color=BLACK, fill_opacity=1.0)
        small_circle.shift(LEFT * 1.8)
        
        # Approximate bulb shapes
        mandelbrot_approx = VGroup(main_body, small_circle)
        mandelbrot_approx.center()
        
        self.add(mandelbrot_approx)
        self.wait(2.0)
    
    def _define_interesting_regions(self) -> Dict[str, Dict]:
        """Define mathematically interesting regions of the Mandelbrot set."""
        return {
            'overview': {
                'center': 0.0 + 0.0j,
                'zoom': 1.0,
                'description': 'Full Mandelbrot set overview'
            },
            'seahorse_valley': {
                'center': -0.7269 + 0.1889j,
                'zoom': 100.0,
                'description': 'Famous seahorse valley with intricate detail'
            },
            'lightning': {
                'center': -1.8 + 0.0j,
                'zoom': 50.0,
                'description': 'Lightning-like tendrils on the left side'
            },
            'spiral_detail': {
                'center': 0.001643721971153 + 0.822467633298876j,
                'zoom': 1000.0,
                'description': 'Spiral structures with self-similarity'
            },
            'mini_mandelbrot': {
                'center': -0.16070135 + 1.0375665j,
                'zoom': 200.0,
                'description': 'Miniature copy of the full set'
            },
            'cusp_detail': {
                'center': -0.75 + 0.0j,
                'zoom': 10.0,
                'description': 'Cusp region between main body and bulb'
            }
        }
    
    def _initialize_calculator(self) -> Optional[FractalCalculator]:
        """Initialize high-precision fractal calculator."""
        try:
            if FractalCalculator:
                return create_fractal_calculator(
                    fractal_type='mandelbrot',
                    max_iterations=self.max_iterations,
                    bailout_radius=self.bailout_radius
                )
        except Exception as e:
            print(f"Failed to initialize calculator: {e}")
        return None
    
    def _initialize_colorizer(self) -> Optional[FractalColorizer]:
        """Initialize white-on-black colorizer."""
        try:
            if WHITE_ON_BLACK_COLORIZER:
                return WHITE_ON_BLACK_COLORIZER
        except Exception as e:
            print(f"Failed to initialize colorizer: {e}")
        return None

class TestMandelbrotWhiteOnBlack(MandelbrotWhiteOnBlack):
    """Quick test version with reduced quality for development."""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        # Reduced quality for faster testing
        self.base_resolution = 512    # Lower resolution
        self.max_iterations = 256     # Fewer iterations
        self.antialias_factor = 1     # No antialiasing
        
        # Reinitialize with test parameters
        self.fractal_calculator = self._initialize_calculator()
        
        print("Test mode: Low quality for rapid development")

# Region-specific scene classes for easy generation
class MandelbrotOverview(MandelbrotWhiteOnBlack):
    """Full overview of the Mandelbrot set."""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.set_region('overview')

class MandelbrotSeahorseValley(MandelbrotWhiteOnBlack):
    """Seahorse valley region detail."""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.set_region('seahorse_valley')

class MandelbrotLightning(MandelbrotWhiteOnBlack):
    """Lightning tendril region."""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.set_region('lightning')

class MandelbrotSpiral(MandelbrotWhiteOnBlack):
    """Spiral detail region."""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.set_region('spiral_detail')

# High-resolution versions for final output
class MandelbrotWhiteOnBlack4K(MandelbrotWhiteOnBlack):
    """Ultra-high resolution 4K version."""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.set_quality(resolution=4096, iterations=2048, antialias=2)

class MandelbrotWhiteOnBlack8K(MandelbrotWhiteOnBlack):
    """Extreme high resolution 8K version."""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.set_quality(resolution=8192, iterations=4096, antialias=1)

if __name__ == "__main__":
    print("White-on-Black Mandelbrot Set Generator")
    print("=" * 50)
    print("Available scenes:")
    print("  Basic:")
    print("    manim -pqh mandelbrot_white_black.py MandelbrotWhiteOnBlack")
    print("    manim -pql mandelbrot_white_black.py TestMandelbrotWhiteOnBlack")
    print("  Regions:")
    print("    manim -pqh mandelbrot_white_black.py MandelbrotOverview")
    print("    manim -pqh mandelbrot_white_black.py MandelbrotSeahorseValley")
    print("    manim -pqh mandelbrot_white_black.py MandelbrotLightning")
    print("    manim -pqh mandelbrot_white_black.py MandelbrotSpiral")
    print("  High Resolution:")
    print("    manim -pqh mandelbrot_white_black.py MandelbrotWhiteOnBlack4K")
    print("    manim -pqh mandelbrot_white_black.py MandelbrotWhiteOnBlack8K")
    print("=" * 50)