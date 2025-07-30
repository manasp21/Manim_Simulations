"""
Visual Scene 4: Tricorn Symmetry Dance (40 seconds)

Pure visual exploration of the Tricorn (Mandelbar) set showcasing its unique
three-fold rotational symmetry through dynamic rotation and zoom.

Visual Flow:
- Start with Tricorn overview showing three-fold symmetry
- Dynamic rotation revealing geometric patterns
- Zoom with synchronized rotation highlighting symmetry
- Electric color palette emphasizing geometric structures
- Return to starting position with final symmetry display
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
    from utils.zoom_paths import TRICORN_PATHS, ZoomPath, EasingFunction, ZoomKeyframe
    UTILS_AVAILABLE = True
except ImportError as e:
    print(f"Import error: {e}")
    UTILS_AVAILABLE = False

class VisualTricornSymmetry(Scene):
    """
    Pure visual Tricorn symmetry exploration with rotation and zoom.
    
    40-second geometric dance through Tricorn's three-fold symmetry.
    """
    
    def __init__(self, **kwargs):
        """Initialize visual-only Tricorn symmetry scene."""
        super().__init__(**kwargs)
        self.camera.background_color = "#000000"  # Pure black background
        
        # Visual parameters
        self.total_duration = 40.0
        self.symmetry_frames = 80  # 2 fps for smooth 40-second animation
        self.rotation_cycles = 3   # Number of complete 120-degree rotations
        
        # High-quality rendering parameters
        self.base_resolution = 850
        self.max_iterations = 384
        self.color_intensity = 1.4
        
        # Initialize fractal tools
        self.fractal_calculator = self._initialize_calculator()
        self.colorizer = self._initialize_colorizer()
        self.symmetry_path = self._create_symmetry_path()
        
    def construct(self):
        """Pure visual construction - geometric symmetry dance."""
        
        if not UTILS_AVAILABLE or not self.fractal_calculator:
            self.create_visual_fallback()
            return
        
        # Create the mesmerizing symmetry dance sequence
        self.create_tricorn_symmetry_dance()
    
    def create_tricorn_symmetry_dance(self):
        """
        Create pure visual symmetry dance through Tricorn rotations.
        """
        
        # Generate rotation sequence for symmetry exploration
        frame_times = np.linspace(0.0, 1.0, self.symmetry_frames)
        
        # Start with Tricorn overview
        initial_center, initial_zoom, initial_rotation = self.symmetry_path.interpolate_at_time(0.0)
        current_tricorn = self.render_tricorn_visual(
            center=initial_center,
            zoom=initial_zoom,
            rotation=initial_rotation,
            color_time=0.0
        )
        
        if current_tricorn:
            # Scale for full-screen geometric presentation
            current_tricorn.scale_to_fit_height(config.frame_height * 0.95)
            current_tricorn.center()
            
            # Elegant entrance with geometric precision
            self.play(
                FadeIn(current_tricorn, run_time=2.0),
                rate_func=self._geometric_ease
            )
            
            # Execute symmetry dance
            for i, t in enumerate(frame_times[1:], 1):
                center, zoom, rotation = self.symmetry_path.interpolate_at_time(t)
                
                # Render next symmetry frame
                next_tricorn = self.render_tricorn_visual(
                    center=center,
                    zoom=zoom,
                    rotation=rotation,
                    color_time=t
                )
                
                if next_tricorn:
                    next_tricorn.scale_to_fit_height(config.frame_height * 0.95) 
                    next_tricorn.center()
                    
                    # Variable dance tempo based on symmetry phase
                    symmetry_phase = (rotation % (2 * np.pi / 3)) / (2 * np.pi / 3)
                    
                    if symmetry_phase < 0.1 or symmetry_phase > 0.9:
                        dance_time = 0.8  # Slower at symmetry points
                    elif 0.4 < symmetry_phase < 0.6:
                        dance_time = 0.3  # Faster during transitions
                    else:
                        dance_time = 0.5  # Medium tempo
                    
                    # Smooth geometric transformation
                    self.play(
                        Transform(current_tricorn, next_tricorn, run_time=dance_time),
                        rate_func=self._symmetry_dance
                    )
                    
                    # Pause at perfect symmetry points
                    if abs(rotation % (2 * np.pi / 3)) < 0.1:
                        self.wait(0.4)
            
            # Final symmetry appreciation
            self.wait(1.0)
            
            # Geometric fade out
            self.play(
                FadeOut(current_tricorn, run_time=2.0),
                rate_func=self._geometric_ease
            )
        
        else:
            self.create_visual_fallback()
    
    def render_tricorn_visual(self, center: complex, zoom: float, 
                            rotation: float, color_time: float) -> Optional[ImageMobject]:
        """
        Render pure visual Tricorn frame with rotation emphasis.
        
        Parameters
        ----------
        center : complex
            Center point in complex plane
        zoom : float
            Zoom level for detail
        rotation : float
            Rotation angle for symmetry exploration
        color_time : float
            Time parameter for color animation (0.0 to 1.0)
            
        Returns
        -------
        Optional[ImageMobject]
            High-quality visual Tricorn frame
        """
        try:
            # Fixed resolution for consistent image sizes
            resolution = self.base_resolution
            
            # Calculate Tricorn data
            tricorn_data = self.fractal_calculator.tricorn_set(
                width=resolution,
                height=resolution,
                center=center,
                zoom=zoom
            )
            
            # Apply electric coloring with rotation-synchronized effects
            rgb_array = self.colorizer.colorize_escape_data(
                tricorn_data,
                max_iterations=self.max_iterations,
                cycle_speed=color_time * 4.0 + rotation * 0.5,  # Rotation-synced colors
                use_histogram_equalization=True
            )
            
            # Enhance geometric visual qualities
            rgb_array = self._enhance_geometric_visuals(rgb_array, rotation, zoom)
            
            # Convert to PIL Image
            rgb_uint8 = (np.clip(rgb_array, 0, 1) * 255).astype(np.uint8)
            pil_image = Image.fromarray(rgb_uint8)
            
            # Apply rotation for symmetry exploration
            if abs(rotation) > 0.01:
                pil_image = pil_image.rotate(
                    np.degrees(rotation), 
                    resample=Image.BICUBIC,
                    fillcolor=(0, 0, 0)
                )
            
            # Save with symmetry-themed filename
            temp_filename = f"/tmp/tricorn_symmetry_{abs(hash((center, zoom, rotation, color_time))) % 100000}.png"
            pil_image.save(temp_filename, optimize=True, quality=95)
            
            return ImageMobject(temp_filename)
            
        except Exception as e:
            print(f"Tricorn rendering error: {e}")
            return None
    
    def _enhance_geometric_visuals(self, rgb_array: np.ndarray, rotation: float, zoom: float) -> np.ndarray:
        """
        Enhance visuals with geometric/symmetry effects.
        """
        # Geometric contrast enhancement based on rotation
        rotation_phase = (rotation % (2 * np.pi)) / (2 * np.pi)
        contrast_factor = 1.2 + 0.2 * np.cos(rotation_phase * 6 * np.pi)  # 3-fold variation
        enhanced = ((rgb_array - 0.5) * contrast_factor) + 0.5
        
        # Electric saturation boost with symmetry modulation
        symmetry_boost = 1.3 + 0.3 * np.sin(rotation * 3)  # 3-fold symmetry
        enhanced = self._apply_electric_enhancement(enhanced, symmetry_boost)
        
        # Zoom-based sharpening for geometric details
        if zoom > 10:
            sharpening_factor = min(0.2, (zoom - 10) / 100.0)
            enhanced = self._apply_sharpening(enhanced, sharpening_factor)
        
        return np.clip(enhanced, 0.0, 1.0)
    
    def _apply_electric_enhancement(self, rgb_array: np.ndarray, boost_factor: float) -> np.ndarray:
        """Apply electric-style color enhancement."""
        # Enhance contrast in each color channel independently
        enhanced = rgb_array.copy()
        
        for c in range(3):
            channel_mean = np.mean(rgb_array[:, :, c])
            enhanced[:, :, c] = channel_mean + boost_factor * (rgb_array[:, :, c] - channel_mean)
        
        return enhanced
    
    def _apply_sharpening(self, rgb_array: np.ndarray, factor: float) -> np.ndarray:
        """Apply subtle sharpening for geometric detail enhancement."""
        # Simple unsharp mask effect
        from scipy import ndimage
        
        try:
            blurred = ndimage.gaussian_filter(rgb_array, sigma=1.0)
            sharpened = rgb_array + factor * (rgb_array - blurred)
            return sharpened
        except ImportError:
            # Fallback if scipy not available
            return rgb_array
    
    def _geometric_ease(self, t: float) -> float:
        """Geometric easing function with mathematical precision."""
        # Smooth step with geometric flavor
        return t * t * t * (t * (t * 6 - 15) + 10)
    
    def _symmetry_dance(self, t: float) -> float:
        """Custom easing for symmetry dance movements."""
        # Three-phase easing matching Tricorn's 3-fold symmetry
        phase = (t * 3) % 1.0
        if phase < 0.33:
            local_t = phase / 0.33
            return local_t * local_t
        elif phase < 0.67:
            local_t = (phase - 0.33) / 0.34
            return 1 - (1 - local_t) * (1 - local_t)
        else:
            local_t = (phase - 0.67) / 0.33
            return 1 - 0.5 * (1 - local_t) * (1 - local_t)
    
    def create_visual_fallback(self):
        """Create geometric fallback showcasing three-fold symmetry."""
        
        # Create three-fold symmetric pattern
        symmetry_center = ORIGIN
        
        # Three main elements at 120-degree intervals
        elements = VGroup()
        
        for i in range(3):
            angle = i * 2 * np.pi / 3
            
            # Create symmetric element
            element = VGroup(
                # Main shape
                RegularPolygon(n=6, radius=1.5, color=BLUE),
                # Inner detail
                Circle(radius=0.8, color=YELLOW, fill_opacity=0.6),
                # Radial lines
                Line(ORIGIN, [1.2, 0, 0], color=WHITE, stroke_width=3),
                Line(ORIGIN, [-1.2, 0, 0], color=WHITE, stroke_width=3),
            )
            
            # Position at symmetry points
            element.rotate(angle)
            element.shift([2.5 * np.cos(angle), 2.5 * np.sin(angle), 0])
            
            elements.add(element)
        
        # Central connecting element
        center_element = Star(
            outer_radius=1.0,
            inner_radius=0.5,
            n=6,
            color=PURPLE,
            fill_opacity=0.8
        )
        
        full_pattern = VGroup(elements, center_element)
        
        # Animated symmetry demonstration
        self.play(Create(center_element, run_time=1.5))
        self.play(Create(elements, run_time=2.0))
        
        # Rotation dance showing symmetry
        for i in range(self.rotation_cycles):
            # 120-degree rotation maintaining symmetry
            self.play(
                Rotate(full_pattern, angle=2*PI/3, run_time=2.0),
                rate_func=self._symmetry_dance
            )
            
            # Color transition between rotations
            new_colors = [RED, GREEN, BLUE, ORANGE, PURPLE, CYAN]
            color_cycle = new_colors[i % len(new_colors)]
            
            self.play(
                elements.animate.set_color(color_cycle),
                run_time=0.5
            )
        
        # Final scale and fade
        self.play(
            full_pattern.animate.scale(1.2),
            run_time=1.0
        )
        self.wait(1.0)
        self.play(FadeOut(full_pattern, run_time=2.0))
    
    def _create_symmetry_path(self) -> ZoomPath:
        """Create symmetry-focused path for Tricorn exploration."""
        
        if TRICORN_PATHS and 'symmetry_dance' in TRICORN_PATHS:
            path = TRICORN_PATHS['symmetry_dance']
            return path
        
        # Fallback: Create symmetry exploration path
        path = ZoomPath("Tricorn Symmetry Dance")
        
        # Symmetry dance waypoints with rotations
        total_rotation = self.rotation_cycles * 2 * np.pi / 3  # Multiple 120-degree turns
        
        path.add_keyframe(0+0j, 1.0, 0.0, rotation=0.0, easing=EasingFunction.EASE_IN_OUT)
        path.add_keyframe(0+0j, 2.0, 0.2, rotation=total_rotation*0.2, easing=EasingFunction.EASE_IN_OUT)
        path.add_keyframe(-0.5+0j, 5.0, 0.4, rotation=total_rotation*0.4, easing=EasingFunction.EASE_IN_OUT)
        path.add_keyframe(-0.8+0.2j, 15.0, 0.6, rotation=total_rotation*0.6, easing=EasingFunction.EXPONENTIAL)
        path.add_keyframe(-0.85+0.15j, 50.0, 0.8, rotation=total_rotation*0.8, easing=EasingFunction.EXPONENTIAL)
        path.add_keyframe(-0.855+0.145j, 200.0, 0.95, rotation=total_rotation, easing=EasingFunction.CIRCULAR)
        
        path.enable_loop_back(0.05)
        return path
    
    def _initialize_calculator(self) -> Optional[FractalCalculator]:
        """Initialize Tricorn calculator."""
        try:
            if FractalCalculator:
                return create_fractal_calculator(
                    fractal_type='tricorn',
                    max_iterations=self.max_iterations,
                    bailout_radius=2.0
                )
        except Exception as e:
            print(f"Failed to initialize calculator: {e}")
        return None
    
    def _initialize_colorizer(self) -> Optional[FractalColorizer]:
        """Initialize colorizer with electric palette for geometric emphasis."""
        try:
            if FractalColorizer:
                return FractalColorizer(
                    palette=ColorPalette.ELECTRIC,
                    gamma=1.0,  # Neutral gamma for electric colors
                    contrast=self.color_intensity
                )
        except Exception as e:
            print(f"Failed to initialize colorizer: {e}")
        return None

# Test version for development
class TestVisualTricornSymmetry(VisualTricornSymmetry):
    """Test version with reduced frames for faster development."""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.symmetry_frames = 12  # Reduced for testing
        self.rotation_cycles = 2   # Fewer cycles for testing
        self.total_duration = 8.0  # Shorter test duration
    
    def construct(self):
        """Quick symmetry test with key rotations."""
        
        if not UTILS_AVAILABLE:
            self.create_visual_fallback()
            return
        
        # Test key symmetry points
        test_rotations = [0.0, 2*PI/3, 4*PI/3]
        test_centers = [0+0j, -0.3+0j, -0.5+0.1j]
        test_zooms = [1.0, 5.0, 15.0]
        
        current_tricorn = None
        
        for i, (center, zoom, rotation) in enumerate(zip(test_centers, test_zooms, test_rotations)):
            tricorn = self.render_tricorn_visual(center, zoom, rotation, i/3.0)
            if tricorn:
                tricorn.scale_to_fit_height(config.frame_height * 0.9)
                tricorn.center()
                
                if current_tricorn is None:
                    self.play(FadeIn(tricorn, run_time=1.0))
                    current_tricorn = tricorn
                else:
                    self.play(Transform(current_tricorn, tricorn, run_time=1.5))
                
                self.wait(0.8)
        
        if current_tricorn:
            self.play(FadeOut(current_tricorn, run_time=1.0))

if __name__ == "__main__":
    print("Pure Visual Tricorn Symmetry Dance Scene")
    print("Full: manim -pqh visual_04_tricorn_symmetry.py VisualTricornSymmetry")
    print("Test: manim -pql visual_04_tricorn_symmetry.py TestVisualTricornSymmetry")