"""
Double Spiral Galaxy: Smooth Continuous Zoom with Enhanced Self-Similarity

This scene creates a smooth, continuous journey into the Double Spiral Valley 
of the Mandelbrot set, revealing infinite recursive spiral patterns with
enhanced visibility through distance estimation coloring and edge enhancement.

Features:
- Smooth continuous zooming (no jump cuts)
- 16:10 aspect ratio for widescreen viewing
- Distance estimation coloring for enhanced self-similarity visibility
- Cosmic color palette optimized for spiral structures
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
    from utils.fractal_algorithms import (
        FractalCalculator, create_fractal_calculator, 
        SmoothZoomEngine, AspectRatioManager
    )
    from utils.color_schemes import SelfSimilarityColorizer, ColorPalette
    UTILS_AVAILABLE = True
except ImportError as e:
    print(f"Import error: {e}")
    UTILS_AVAILABLE = False

class DoubleSpiralGalaxy(Scene):
    """
    Smooth continuous journey into Double Spiral Galaxy with enhanced spiral visibility.
    """
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        # Configure 16:10 aspect ratio
        AspectRatioManager.configure_manim_16_10('high')
        self.camera.background_color = "#000011"  # Deep space background
        
        # High-quality parameters for smooth zoom
        self.base_resolution = 1600  # Higher resolution for 16:10
        self.aspect_ratio = 1.6  # 16:10 ratio
        
        # Double Spiral Valley coordinates
        self.spiral_locations = self._create_spiral_locations()
        
        # Initialize enhanced fractal systems
        self.fractal_calculator = self._initialize_calculator()
        self.zoom_engine = self._initialize_zoom_engine()
        self.similarity_colorizer = self._initialize_similarity_colorizer()
        
    def construct(self):
        """Create the smooth Double Spiral Galaxy journey."""
        
        if not UTILS_AVAILABLE or not self.fractal_calculator:
            self.create_fallback()
            return
        
        print("🌌 Starting Enhanced Double Spiral Galaxy Journey")
        print(f"📐 Aspect Ratio: 16:10 ({config.pixel_width}x{config.pixel_height})")
        print(f"🎯 Self-Similarity Enhancement: ENABLED")
        print(f"🎬 Smooth Zoom Engine: ACTIVE")
        
        self.create_smooth_spiral_journey()
    
    def _create_spiral_locations(self) -> List[Tuple[complex, float, str]]:
        """
        Create mathematically accurate spiral valley locations for smooth zoom.
        
        Returns:
            List of (center, zoom, description) tuples for key spiral locations
        """
        return [
            # Progressive zoom into double spiral valley
            (0+0j, 1.0, "Mandelbrot Set Overview"),
            (-0.7+0.05j, 15.0, "Approaching Spiral Valley"),
            (-0.75+0.05j, 80.0, "Entering Double Spiral Valley"),
            (-0.745+0.08j, 500.0, "First Double Spiral Structures"),
            (-0.7445+0.085j, 3000.0, "Detailed Spiral Arms"),
            (-0.74445+0.0855j, 20000.0, "Spiral Branching Points"),
            (-0.744445+0.08555j, 120000.0, "Recursive Spiral Patterns"),
            (-0.7444445+0.085555j, 800000.0, "Deep Spiral Recursion"),
            (-0.74444445+0.0855555j, 5000000.0, "Infinite Spiral Branching"),
            (-0.744444445+0.08555555j, 30000000.0, "Perfect Spiral Self-Similarity")
        ]
    
    def create_smooth_spiral_journey(self):
        """
        Create smooth continuous zoom journey through spiral valley.
        """
        
        print(f"\n🌟 Generating smooth zoom through {len(self.spiral_locations)} spiral locations")
        
        # Generate all frames for smooth multi-location journey
        all_frames_data = self.zoom_engine.generate_multi_location_zoom(
            locations=self.spiral_locations,
            transition_duration=2.8,  # Slightly faster for cosmic feel
            pause_duration=1.8,       # Shorter pauses for dynamic feel
            fps=30,                   # 30 FPS for smooth animation
            width=int(self.base_resolution * self.aspect_ratio),  # 16:10 width
            height=self.base_resolution                           # 16:10 height
        )
        
        print(f"\n🎬 Converting {len(all_frames_data)} frames to cosmic spiral images...")
        
        # Convert fractal data to Manim image objects with enhanced coloring
        manim_frames = []
        for i, (fractal_data, description) in enumerate(all_frames_data):
            
            # Extract zoom level from description for adaptive coloring
            zoom_level = self._extract_zoom_from_description(description, i)
            
            # Create enhanced RGB image using self-similarity colorizer
            rgb_image = self._create_enhanced_spiral_image(
                fractal_data, zoom_level, description
            )
            
            if rgb_image is not None:
                # Convert to PIL Image and save with unique filename
                rgb_uint8 = (np.clip(rgb_image, 0, 1) * 255).astype(np.uint8)
                pil_image = Image.fromarray(rgb_uint8)
                
                # Save with unique filename to prevent caching
                timestamp = int(time.time() * 1000000)
                temp_filename = f"/tmp/spiral_smooth_{i:04d}_{timestamp}_{hash(description) % 10000}.png"
                pil_image.save(temp_filename, optimize=True, quality=95)
                
                # Create Manim ImageMobject
                image_mob = ImageMobject(temp_filename)
                image_mob.scale_to_fit_height(config.frame_height * 0.95)
                image_mob.center()
                
                manim_frames.append((image_mob, description, zoom_level))
                
                if i % 20 == 0:
                    print(f"   🔄 Processed frame {i+1}/{len(all_frames_data)}: {description}")
        
        if not manim_frames:
            print("❌ No frames generated successfully")
            self.create_fallback()
            return
        
        print(f"\n🎥 Starting smooth spiral animation with {len(manim_frames)} frames")
        
        # Create smooth continuous animation
        self._animate_smooth_frames(manim_frames)
        
        print("✅ Double Spiral Galaxy journey completed successfully!")
    
    def _create_enhanced_spiral_image(self, fractal_data: np.ndarray, 
                                    zoom_level: float, description: str) -> Optional[np.ndarray]:
        """
        Create enhanced spiral fractal image with self-similarity coloring.
        
        Parameters
        ----------
        fractal_data : np.ndarray
            Basic escape-time fractal data
        zoom_level : float
            Current zoom level for adaptive enhancement
        description : str
            Frame description
            
        Returns
        -------
        np.ndarray or None
            Enhanced RGB image array with cosmic spiral theme
        """
        try:
            # Create spiral-optimized distance data
            distance_data = self._create_spiral_distance_data(fractal_data)
            
            # Apply self-similarity enhanced coloring with cosmic theme
            rgb_array = self.similarity_colorizer.colorize_with_distance_estimation(
                escape_data=fractal_data,
                distance_data=distance_data,
                max_iterations=2048,  # High iterations for spiral detail
                zoom_level=zoom_level
            )
            
            # Add cosmic glow effect for spiral arms
            rgb_array = self._add_cosmic_glow(rgb_array, distance_data)
            
            return rgb_array
            
        except Exception as e:
            print(f"   ❌ Error creating enhanced spiral image: {e}")
            return None
    
    def _create_spiral_distance_data(self, escape_data: np.ndarray) -> np.ndarray:
        """
        Create distance data optimized for spiral structure detection.
        """
        # Create radial and angular gradients to highlight spiral patterns
        height, width = escape_data.shape
        y, x = np.ogrid[:height, :width]
        
        # Center coordinates
        cy, cx = height // 2, width // 2
        
        # Calculate radial distance from center
        radial_dist = np.sqrt((x - cx)**2 + (y - cy)**2)
        
        # Calculate angle from center
        angles = np.arctan2(y - cy, x - cx)
        
        # Create spiral-aware gradient that emphasizes curved structures
        escape_gradient = np.gradient(escape_data)
        gradient_magnitude = np.sqrt(escape_gradient[0]**2 + escape_gradient[1]**2)
        
        # Combine radial and gradient information for spiral detection
        max_gradient = np.max(gradient_magnitude)
        if max_gradient > 0:
            normalized_gradient = gradient_magnitude / max_gradient
            
            # Create spiral-sensitive distance metric
            spiral_distance = 1.0 - normalized_gradient
            
            # Enhance curved features (spirals) over linear features
            curvature = self._detect_curvature(escape_data)
            spiral_distance *= (1.0 + 0.5 * curvature)
            
        else:
            spiral_distance = np.ones_like(escape_data)
        
        return spiral_distance
    
    def _detect_curvature(self, data: np.ndarray) -> np.ndarray:
        """Detect curved features that indicate spiral structures."""
        # Calculate second derivatives to detect curvature
        grad_y, grad_x = np.gradient(data)
        grad2_y, grad2_x = np.gradient(grad_y), np.gradient(grad_x)
        
        # Curvature approximation using second derivatives
        curvature = np.abs(grad2_x) + np.abs(grad2_y)
        
        # Normalize
        max_curvature = np.max(curvature)
        if max_curvature > 0:
            curvature = curvature / max_curvature
        
        return curvature
    
    def _add_cosmic_glow(self, rgb_array: np.ndarray, distance_data: np.ndarray) -> np.ndarray:
        """Add cosmic glow effect to highlight spiral arms."""
        # Create glow mask for areas with interesting features
        glow_mask = distance_data < 0.3  # Areas close to fractal boundaries
        
        # Add subtle glow by boosting brightness in spiral regions
        enhanced_rgb = rgb_array.copy()
        glow_factor = 1.2
        
        enhanced_rgb[glow_mask] *= glow_factor
        
        return np.clip(enhanced_rgb, 0, 1)
    
    def _extract_zoom_from_description(self, description: str, frame_index: int) -> float:
        """Extract zoom level from frame description or estimate from index."""
        # Exponential zoom progression for spiral journey
        base_zoom = 1.0
        zoom_progression = base_zoom * (1.15 ** frame_index)  # Faster zoom for spirals
        return min(zoom_progression, 1e9)  # Cap at 1 billion zoom
    
    def _animate_smooth_frames(self, manim_frames: List[Tuple]):
        """
        Create smooth spiral animation from processed Manim frames.
        """
        if not manim_frames:
            return
        
        # Start with first frame
        current_frame, description, zoom_level = manim_frames[0]
        print(f"🎬 Starting: {description} (zoom {zoom_level:,.0f}x)")
        
        self.play(FadeIn(current_frame, run_time=1.5), rate_func=smooth)
        
        # Animate through all frames with very short transitions for smoothness
        for i in range(1, len(manim_frames)):
            next_frame, description, zoom_level = manim_frames[i]
            
            # Very fast transitions (0.08s) for ultra-smooth spiral feel
            self.play(
                ReplacementTransform(current_frame, next_frame),
                run_time=0.08,
                rate_func=linear  # Linear for consistent spiral motion
            )
            
            current_frame = next_frame
            
            # Occasional status updates
            if i % 25 == 0:
                print(f"   🌀 Frame {i}: {description} (zoom {zoom_level:,.0f}x)")
        
        # Final pause to appreciate the deepest spiral recursion
        print(f"🏁 Final spiral: {description} (zoom {zoom_level:,.0f}x)")
        self.wait(3.0)
        
        # Fade out with cosmic effect
        self.play(FadeOut(current_frame, run_time=2.0), rate_func=smooth)
    
    def create_fallback(self):
        """Fallback if enhanced spiral rendering fails."""
        error_text = Text(
            "Enhanced Double Spiral\nGalaxy System\nNot Available", 
            font_size=36, 
            color=RED
        )
        self.play(Write(error_text))
        self.wait(2)
        self.play(FadeOut(error_text))
    
    def _initialize_calculator(self) -> Optional[FractalCalculator]:
        """Initialize high-precision fractal calculator."""
        try:
            return create_fractal_calculator(
                fractal_type='mandelbrot',
                max_iterations=2048,  # High iterations for spiral detail
                bailout_radius=2.0
            )
        except Exception as e:
            print(f"Failed to initialize calculator: {e}")
            return None
    
    def _initialize_zoom_engine(self) -> Optional[SmoothZoomEngine]:
        """Initialize smooth zoom engine."""
        try:
            if self.fractal_calculator:
                return SmoothZoomEngine(self.fractal_calculator)
        except Exception as e:
            print(f"Failed to initialize zoom engine: {e}")
        return None
    
    def _initialize_similarity_colorizer(self) -> Optional[SelfSimilarityColorizer]:
        """Initialize self-similarity colorizer for cosmic spirals."""
        try:
            return SelfSimilarityColorizer(
                base_palette=ColorPalette.COSMIC,  # Cosmic theme for spirals
                edge_emphasis=2.5,                 # Medium edge enhancement for spirals
                structure_contrast=1.8             # Good spiral contrast
            )
        except Exception as e:
            print(f"Failed to initialize similarity colorizer: {e}")
        return None

if __name__ == "__main__":
    print("🌌 Enhanced Double Spiral Galaxy - Smooth Zoom with Self-Similarity")
    print("Usage: manim -pql double_spiral_galaxy.py DoubleSpiralGalaxy")
    print("Features: 16:10 aspect ratio, smooth continuous zoom, enhanced spiral visibility")