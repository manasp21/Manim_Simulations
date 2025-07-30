"""
Mini-Mandelbrot Safari: Smooth Continuous Zoom with Enhanced Self-Similarity

This scene creates a smooth, continuous safari through the Mandelbrot set to discover
perfect miniature copies hidden at microscopic scales. Each mini-Mandelbrot is an
exact replica of the full set, demonstrating ultimate mathematical self-similarity.

Features:
- Smooth continuous zooming (no jump cuts)
- 16:10 aspect ratio for widescreen viewing
- Distance estimation coloring for enhanced self-similarity visibility
- Electric color palette optimized for discovery and exploration
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

class MiniMandelbrotSafari(Scene):
    """
    Smooth continuous safari through Mini-Mandelbrot locations with enhanced copy visibility.
    """
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        # Configure 16:10 aspect ratio
        AspectRatioManager.configure_manim_16_10('high')
        self.camera.background_color = "#001122"  # Deep safari night
        
        # High-quality parameters for smooth zoom
        self.base_resolution = 1600  # Higher resolution for 16:10
        self.aspect_ratio = 1.6  # 16:10 ratio
        
        # Mini-Mandelbrot safari locations
        self.safari_locations = self._create_safari_locations()
        
        # Initialize enhanced fractal systems
        self.fractal_calculator = self._initialize_calculator()
        self.zoom_engine = self._initialize_zoom_engine()
        self.similarity_colorizer = self._initialize_similarity_colorizer()
        
    def construct(self):
        """Create the smooth Mini-Mandelbrot safari journey."""
        
        if not UTILS_AVAILABLE or not self.fractal_calculator:
            self.create_fallback()
            return
        
        print("🔍 Starting Enhanced Mini-Mandelbrot Safari")
        print(f"📐 Aspect Ratio: 16:10 ({config.pixel_width}x{config.pixel_height})")
        print(f"🎯 Self-Similarity Enhancement: ENABLED")
        print(f"🎬 Smooth Zoom Engine: ACTIVE")
        
        self.create_smooth_safari_journey()
    
    def _create_safari_locations(self) -> List[Tuple[complex, float, str]]:
        """
        Create safari locations for discovering Mini-Mandelbrot copies.
        
        Returns:
            List of (center, zoom, description) tuples for mini-Mandelbrot locations
        """
        return [
            # Safari through famous Mini-Mandelbrot locations
            (0+0j, 1.0, "Original Mandelbrot Set"),
            (-0.1+1.0j, 12.0, "Approaching Upper Antenna"),
            (-0.16070135+1.0375665j, 80.0, "First Mini-Mandelbrot Sighting"),
            (-0.16070135+1.0375665j, 500.0, "Mini-Mandelbrot Emergence"),
            (-0.16070135+1.0375665j, 3000.0, "Perfect Mandelbrot Copy"),
            (-1.25+0j, 15.0, "Approaching Main Antenna"),
            (-1.769+0j, 100.0, "Antenna Mini-Mandelbrot"),
            (-1.7690+0j, 600.0, "Antenna Perfect Copy"),
            (-0.744+0.148j, 200.0, "Seahorse Valley Mini-Mandelbrot"),
            (-0.7440+0.1480j, 1200.0, "Final Perfect Copy Discovery")
        ]
    
    def create_smooth_safari_journey(self):
        """
        Create smooth continuous safari journey through mini-Mandelbrot locations.
        """
        
        print(f"\n🌟 Generating smooth safari through {len(self.safari_locations)} discovery locations")
        
        # Generate all frames for smooth multi-location safari
        all_frames_data = self.zoom_engine.generate_multi_location_zoom(
            locations=self.safari_locations,
            transition_duration=2.5,  # Medium speed for discovery feel
            pause_duration=2.2,       # Longer pauses to appreciate discoveries
            fps=30,                   # 30 FPS for smooth animation
            width=int(self.base_resolution * self.aspect_ratio),  # 16:10 width
            height=self.base_resolution                           # 16:10 height
        )
        
        print(f"\n🎬 Converting {len(all_frames_data)} frames to safari discovery images...")
        
        # Convert fractal data to Manim image objects with enhanced coloring
        manim_frames = []
        for i, (fractal_data, description) in enumerate(all_frames_data):
            
            # Extract zoom level from description for adaptive coloring
            zoom_level = self._extract_zoom_from_description(description, i)
            
            # Create enhanced RGB image using self-similarity colorizer
            rgb_image = self._create_enhanced_safari_image(
                fractal_data, zoom_level, description
            )
            
            if rgb_image is not None:
                # Convert to PIL Image and save with unique filename
                rgb_uint8 = (np.clip(rgb_image, 0, 1) * 255).astype(np.uint8)
                pil_image = Image.fromarray(rgb_uint8)
                
                # Save with unique filename to prevent caching
                timestamp = int(time.time() * 1000000)
                temp_filename = f"/tmp/safari_smooth_{i:04d}_{timestamp}_{hash(description) % 10000}.png"
                pil_image.save(temp_filename, optimize=True, quality=95)
                
                # Create Manim ImageMobject
                image_mob = ImageMobject(temp_filename)
                image_mob.scale_to_fit_height(config.frame_height * 0.95)
                image_mob.center()
                
                manim_frames.append((image_mob, description, zoom_level))
                
                if i % 15 == 0:
                    print(f"   🔄 Processed frame {i+1}/{len(all_frames_data)}: {description}")
        
        if not manim_frames:
            print("❌ No frames generated successfully")
            self.create_fallback()
            return
        
        print(f"\n🎥 Starting smooth safari animation with {len(manim_frames)} frames")
        
        # Create smooth continuous animation
        self._animate_smooth_frames(manim_frames)
        
        print("✅ Mini-Mandelbrot Safari completed successfully!")
    
    def _create_enhanced_safari_image(self, fractal_data: np.ndarray, 
                                    zoom_level: float, description: str) -> Optional[np.ndarray]:
        """
        Create enhanced safari fractal image with self-similarity coloring.
        
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
            Enhanced RGB image array with safari discovery theme
        """
        try:
            # Create mini-Mandelbrot optimized distance data
            distance_data = self._create_mini_mandelbrot_distance_data(fractal_data)
            
            # Apply self-similarity enhanced coloring with electric discovery theme
            rgb_array = self.similarity_colorizer.colorize_with_distance_estimation(
                escape_data=fractal_data,
                distance_data=distance_data,
                max_iterations=2048,  # High iterations for copy detail
                zoom_level=zoom_level
            )
            
            # Add discovery highlighting for mini-Mandelbrot features
            rgb_array = self._add_discovery_highlighting(rgb_array, fractal_data)
            
            return rgb_array
            
        except Exception as e:
            print(f"   ❌ Error creating enhanced safari image: {e}")
            return None
    
    def _create_mini_mandelbrot_distance_data(self, escape_data: np.ndarray) -> np.ndarray:
        """
        Create distance data optimized for Mini-Mandelbrot copy detection.
        """
        # Create enhanced gradient analysis for detecting self-similar copies
        escape_gradient = np.gradient(escape_data)
        gradient_magnitude = np.sqrt(escape_gradient[0]**2 + escape_gradient[1]**2)
        
        # Detect circular/cardioid patterns typical of Mini-Mandelbrots
        circular_features = self._detect_circular_patterns(escape_data)
        
        # Combine gradient and circular pattern detection
        max_gradient = np.max(gradient_magnitude)
        if max_gradient > 0:
            normalized_gradient = gradient_magnitude / max_gradient
            
            # Distance metric emphasizing Mini-Mandelbrot boundaries
            mini_distance = 1.0 - normalized_gradient
            
            # Boost areas with circular patterns (typical of Mini-Mandelbrots)
            mini_distance *= (1.0 + 0.8 * circular_features)
            
        else:
            mini_distance = np.ones_like(escape_data)
        
        return mini_distance
    
    def _detect_circular_patterns(self, data: np.ndarray) -> np.ndarray:
        """Detect circular/cardioid patterns typical of Mini-Mandelbrot sets."""
        height, width = data.shape
        y, x = np.ogrid[:height, :width]
        
        # Create radial pattern detection
        cy, cx = height // 2, width // 2
        radial_dist = np.sqrt((x - cx)**2 + (y - cy)**2)
        
        # Detect concentric patterns using radial derivative
        radial_gradient = np.gradient(data, axis=0)**2 + np.gradient(data, axis=1)**2
        
        # Areas with strong radial gradients are likely circular features
        max_radial = np.max(radial_gradient)
        if max_radial > 0:
            circular_strength = radial_gradient / max_radial
        else:
            circular_strength = np.zeros_like(data)
        
        return circular_strength
    
    def _add_discovery_highlighting(self, rgb_array: np.ndarray, escape_data: np.ndarray) -> np.ndarray:
        """Add discovery highlighting for interesting Mini-Mandelbrot features."""
        # Detect areas likely to contain Mini-Mandelbrot copies
        # These are typically areas with moderate escape values (not in set, not far outside)
        in_set_mask = (escape_data >= 1000)  # Likely in the set
        far_outside_mask = (escape_data < 10)  # Far outside
        interesting_mask = ~(in_set_mask | far_outside_mask)  # The interesting boundary regions
        
        # Add subtle highlighting to interesting regions
        enhanced_rgb = rgb_array.copy()
        highlight_factor = 1.15
        
        enhanced_rgb[interesting_mask] *= highlight_factor
        
        return np.clip(enhanced_rgb, 0, 1)
    
    def _extract_zoom_from_description(self, description: str, frame_index: int) -> float:
        """Extract zoom level from frame description or estimate from index."""
        # Moderate zoom progression for safari exploration
        base_zoom = 1.0
        zoom_progression = base_zoom * (1.12 ** frame_index)  # Moderate zoom for discovery
        return min(zoom_progression, 1e8)  # Cap at 100 million zoom
    
    def _animate_smooth_frames(self, manim_frames: List[Tuple]):
        """
        Create smooth safari animation from processed Manim frames.
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
            
            # Fast transitions (0.09s) for smooth safari feel
            self.play(
                ReplacementTransform(current_frame, next_frame),
                run_time=0.09,
                rate_func=linear  # Linear for consistent exploration speed
            )
            
            current_frame = next_frame
            
            # Status updates for major discoveries
            if i % 20 == 0:
                print(f"   🔍 Frame {i}: {description} (zoom {zoom_level:,.0f}x)")
        
        # Final pause to appreciate the ultimate mini-Mandelbrot discovery
        print(f"🏁 Final discovery: {description} (zoom {zoom_level:,.0f}x)")
        self.wait(3.0)
        
        # Fade out with discovery completion
        self.play(FadeOut(current_frame, run_time=2.0), rate_func=smooth)
    
    def create_fallback(self):
        """Fallback if enhanced safari rendering fails."""
        error_text = Text(
            "Enhanced Mini-Mandelbrot\nSafari System\nNot Available", 
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
                max_iterations=2048,  # High iterations for copy detail
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
        """Initialize self-similarity colorizer for mini-Mandelbrot discovery."""
        try:
            return SelfSimilarityColorizer(
                base_palette=ColorPalette.ELECTRIC,  # Electric theme for discovery
                edge_emphasis=3.5,                   # Strong edge enhancement for copies
                structure_contrast=2.2               # High contrast for copy visibility
            )
        except Exception as e:
            print(f"Failed to initialize similarity colorizer: {e}")
        return None

if __name__ == "__main__":
    print("🔍 Enhanced Mini-Mandelbrot Safari - Smooth Zoom with Self-Similarity")
    print("Usage: manim -pql mini_mandelbrot_safari.py MiniMandelbrotSafari")
    print("Features: 16:10 aspect ratio, smooth continuous zoom, enhanced copy visibility")