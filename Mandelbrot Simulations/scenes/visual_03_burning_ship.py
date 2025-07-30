"""
Visual Scene 3: Burning Ship Voyage (50 seconds)

Pure visual journey through the Burning Ship fractal's unique ship-like
structures. No text, just mesmerizing exploration of nautical fractal forms.

Visual Flow:
- Overview of complete "ship" silhouette
- Voyage into main ship structure  
- Exploration of detailed "rigging" and "sails"
- Deep zoom into microscopic ship details
- Ocean color palette emphasizing nautical theme
- Smooth return to overview
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
    from utils.zoom_paths import BURNING_SHIP_PATHS, ZoomPath, EasingFunction, ZoomKeyframe
    UTILS_AVAILABLE = True
except ImportError as e:
    print(f"Import error: {e}")
    UTILS_AVAILABLE = False

class VisualBurningShipVoyage(Scene):
    """
    Pure visual Burning Ship exploration with nautical voyage theme.
    
    50-second journey through ship-like fractal structures.
    """
    
    def __init__(self, **kwargs):
        """Initialize visual-only Burning Ship voyage scene."""
        super().__init__(**kwargs)
        self.camera.background_color = "#001122"  # Deep ocean blue
        
        # Visual parameters
        self.total_duration = 50.0
        self.voyage_frames = 100  # 2 fps for smooth 50-second animation
        self.transition_smoothness = 0.85
        
        # High-quality rendering parameters optimized for Burning Ship
        self.base_resolution = 950
        self.max_iterations = 512  # Higher for detailed ship structures
        self.color_intensity = 1.1
        
        # Initialize fractal tools
        self.fractal_calculator = self._initialize_calculator()
        self.colorizer = self._initialize_colorizer()
        self.voyage_path = self._create_voyage_path()
        
    def construct(self):
        """Pure visual construction - nautical voyage through Burning Ship."""
        
        if not UTILS_AVAILABLE or not self.fractal_calculator:
            self.create_visual_fallback()
            return
        
        # Create the mesmerizing ship voyage sequence
        self.create_burning_ship_voyage()
    
    def create_burning_ship_voyage(self):
        """
        Create pure visual voyage through Burning Ship fractal.
        """
        
        # Generate voyage waypoints for smooth navigation
        frame_times = np.linspace(0.0, 1.0, self.voyage_frames)
        
        # Start with ship overview
        initial_center, initial_zoom, _ = self.voyage_path.interpolate_at_time(0.0)
        current_ship = self.render_burning_ship_visual(
            center=initial_center,
            zoom=initial_zoom,
            color_time=0.0
        )
        
        if current_ship:
            # Scale for cinematic presentation
            current_ship.scale_to_fit_height(config.frame_height * 0.95)
            current_ship.center()
            
            # Ocean-like entrance with wave effect
            self.play(
                FadeIn(current_ship, run_time=2.5),
                rate_func=self._wave_function
            )
            
            # Navigate through ship structures
            for i, t in enumerate(frame_times[1:], 1):
                center, zoom, rotation = self.voyage_path.interpolate_at_time(t)
                
                # Render next waypoint
                next_ship = self.render_burning_ship_visual(
                    center=center,
                    zoom=zoom,
                    color_time=t,
                    rotation=rotation
                )
                
                if next_ship:
                    next_ship.scale_to_fit_height(config.frame_height * 0.95)
                    next_ship.center()
                    
                    # Variable navigation speed based on zoom level
                    if zoom < 5:
                        navigation_time = 0.8  # Slower for overview navigation
                    elif zoom < 50:
                        navigation_time = 0.6  # Medium for approaching structures
                    elif zoom < 500:
                        navigation_time = 0.4  # Faster for detailed exploration
                    else:
                        navigation_time = 0.3  # Fastest for microscopic detail
                    
                    # Smooth voyage transition with slight wave motion
                    self.play(
                        Transform(current_ship, next_ship, run_time=navigation_time),
                        rate_func=self._smooth_voyage
                    )
                    
                    # Pause for appreciation at major ship structures
                    if zoom in [1.0, 10.0, 100.0, 1000.0]:
                        self.wait(0.6)
            
            # Final contemplation at deepest detail
            self.wait(1.2)
            
            # Ocean-like departure
            self.play(
                FadeOut(current_ship, run_time=2.5),
                rate_func=self._wave_function
            )
        
        else:
            self.create_visual_fallback()
    
    def render_burning_ship_visual(self, center: complex, zoom: float, 
                                  color_time: float, rotation: float = 0.0) -> Optional[ImageMobject]:
        """
        Render pure visual Burning Ship frame with nautical emphasis.
        
        Parameters
        ----------
        center : complex
            Center point in complex plane
        zoom : float
            Zoom level for navigation
        color_time : float
            Time parameter for color animation (0.0 to 1.0)
        rotation : float
            Rotation angle for dynamic viewing
            
        Returns
        -------
        Optional[ImageMobject]
            High-quality visual Burning Ship frame
        """
        try:
            # Fixed resolution for consistent image sizes in Transform
            resolution = self.base_resolution
            
            # Calculate Burning Ship data
            ship_data = self.fractal_calculator.burning_ship(
                width=resolution,
                height=resolution,
                center=center,
                zoom=zoom
            )
            
            # Apply ocean coloring with voyage-synchronized effects
            rgb_array = self.colorizer.colorize_escape_data(
                ship_data,
                max_iterations=self.max_iterations,
                cycle_speed=color_time * 1.5 + zoom * 0.0005,  # Subtle ocean motion
                use_histogram_equalization=True
            )
            
            # Enhance nautical visual qualities
            rgb_array = self._enhance_nautical_visuals(rgb_array, zoom, color_time)
            
            # Convert to PIL Image
            rgb_uint8 = (np.clip(rgb_array, 0, 1) * 255).astype(np.uint8)
            pil_image = Image.fromarray(rgb_uint8)
            
            # Apply slight rotation for dynamic voyage feel
            if abs(rotation) > 0.01:
                pil_image = pil_image.rotate(
                    np.degrees(rotation), 
                    resample=Image.BICUBIC,
                    fillcolor=(0, 17, 34)  # Ocean background color
                )
            
            # Save with voyage-themed filename
            temp_filename = f"/tmp/burning_ship_voyage_{abs(hash((center, zoom, color_time))) % 100000}.png"
            pil_image.save(temp_filename, optimize=True, quality=95)
            
            return ImageMobject(temp_filename)
            
        except Exception as e:
            print(f"Burning Ship rendering error: {e}")
            return None
    
    def _enhance_nautical_visuals(self, rgb_array: np.ndarray, zoom: float, time: float) -> np.ndarray:
        """
        Enhance visuals with nautical/oceanic effects.
        """
        # Ocean-like contrast enhancement
        depth_factor = 1.0 + min(0.2, zoom / 5000.0)  # Deeper contrast at high zoom
        enhanced = ((rgb_array - 0.5) * depth_factor) + 0.5
        
        # Add subtle "underwater" blue tint at deep zooms
        if zoom > 100:
            blue_tint = min(0.1, (zoom - 100) / 10000.0)
            enhanced[:, :, 2] += blue_tint  # Enhance blue channel
        
        # Ocean wave-like saturation modulation
        wave_phase = time * 2 * np.pi
        saturation_wave = 1.1 + 0.1 * np.sin(wave_phase)
        enhanced = self._modulate_saturation(enhanced, saturation_wave)
        
        return np.clip(enhanced, 0.0, 1.0)
    
    def _modulate_saturation(self, rgb_array: np.ndarray, saturation_factor: float) -> np.ndarray:
        """Apply wave-like saturation modulation for ocean effect."""
        gray = 0.299 * rgb_array[:, :, 0] + 0.587 * rgb_array[:, :, 1] + 0.114 * rgb_array[:, :, 2]
        
        # Apply saturation modulation
        modulated = rgb_array.copy()
        for c in range(3):
            modulated[:, :, c] = gray + saturation_factor * (rgb_array[:, :, c] - gray)
        
        return modulated
    
    def _wave_function(self, t: float) -> float:
        """Custom easing function that mimics ocean wave motion."""
        # Combination of smooth step and gentle wave
        smooth_t = t * t * (3.0 - 2.0 * t)  # Smooth step
        wave_t = smooth_t + 0.1 * np.sin(smooth_t * 4 * np.pi) * (1 - smooth_t)
        return np.clip(wave_t, 0.0, 1.0)
    
    def _smooth_voyage(self, t: float) -> float:
        """Smooth voyage easing with slight acceleration/deceleration."""
        # Custom easing for ship navigation feeling
        if t < 0.3:
            return 2 * t * t  # Accelerate
        elif t < 0.7:
            return 1 - 2 * (1 - t) * (1 - t)  # Cruise
        else:
            return 1 - 0.5 * (1 - t) * (1 - t)  # Gentle deceleration
    
    def create_visual_fallback(self):
        """Create nautical-themed fallback if rendering fails."""
        
        # Create stylized ship silhouette
        ship_hull = Ellipse(width=4.0, height=1.5, color=BLUE_E, fill_opacity=0.8)
        ship_hull.shift(DOWN * 0.5)
        
        # Ship masts
        main_mast = Line(start=[0, 0, 0], end=[0, 3, 0], color=BROWN, stroke_width=6)
        fore_mast = Line(start=[-1.5, 0, 0], end=[-1.5, 2.5, 0], color=BROWN, stroke_width=4)
        
        # Simple sails
        main_sail = Polygon(
            [-0.3, 0.5, 0], [0.3, 0.5, 0], [0.2, 2.5, 0], [-0.2, 2.5, 0],
            color=WHITE, fill_opacity=0.9, stroke_color=GRAY
        )
        
        fore_sail = Polygon(
            [-1.8, 0.3, 0], [-1.2, 0.3, 0], [-1.3, 2.0, 0], [-1.7, 2.0, 0],
            color=WHITE, fill_opacity=0.9, stroke_color=GRAY
        )
        
        # Ocean waves
        waves = VGroup()
        for i in range(-3, 4):
            wave = ParametricFunction(
                lambda t: np.array([t, 0.2 * np.sin(3 * t + i), 0]),
                t_range=[-4, 4, 0.1],
                color=BLUE,
                stroke_width=3
            ).shift(DOWN * (2 + i * 0.1))
            waves.add(wave)
        
        # Complete ship
        ship = VGroup(ship_hull, main_mast, fore_mast, main_sail, fore_sail)
        ship.center()
        
        # Ocean scene
        ocean_scene = VGroup(waves, ship)
        
        # Animated sequence
        self.play(Create(waves, run_time=2.0), rate_func=self._wave_function)
        self.play(FadeIn(ship, run_time=2.0))
        
        # Gentle ocean motion
        for _ in range(6):
            self.play(
                ship.animate.shift(UP * 0.1).shift(LEFT * 0.05),
                waves.animate.shift(RIGHT * 0.1),
                run_time=1.0,
                rate_func=self._wave_function
            )
            self.play(
                ship.animate.shift(DOWN * 0.1).shift(RIGHT * 0.05),
                waves.animate.shift(LEFT * 0.1),
                run_time=1.0,
                rate_func=self._wave_function
            )
        
        self.wait(1.0)
        self.play(FadeOut(ocean_scene, run_time=2.0))
    
    def _create_voyage_path(self) -> ZoomPath:
        """Create optimized voyage path through Burning Ship structures."""
        
        if BURNING_SHIP_PATHS and 'ship_journey' in BURNING_SHIP_PATHS:
            path = BURNING_SHIP_PATHS['ship_journey']
            path.enable_loop_back(0.1)
            return path
        
        # Fallback: Create ship voyage path
        path = ZoomPath("Burning Ship Voyage")
        
        # Voyage waypoints focusing on ship-like structures
        path.add_keyframe(-0.5-0.6j, 1.0, 0.0, easing=EasingFunction.EASE_IN_OUT)       # Ship overview
        path.add_keyframe(-1.0-0.5j, 3.0, 0.15, easing=EasingFunction.EASE_IN_OUT)      # Approach main body
        path.add_keyframe(-1.7-0.03j, 15.0, 0.35, easing=EasingFunction.EASE_IN_OUT)    # Enter ship details
        path.add_keyframe(-1.775-0.01j, 75.0, 0.55, easing=EasingFunction.EXPONENTIAL)  # Detailed rigging
        path.add_keyframe(-1.7751-0.003j, 300.0, 0.75, easing=EasingFunction.EXPONENTIAL) # Ship's "rigging"
        path.add_keyframe(-1.77513-0.0015j, 1500.0, 0.90, easing=EasingFunction.CIRCULAR) # Microscopic detail
        
        path.enable_loop_back(0.08)  # Smooth return voyage
        return path
    
    def _initialize_calculator(self) -> Optional[FractalCalculator]:
        """Initialize Burning Ship calculator with higher iterations."""
        try:
            if FractalCalculator:
                return create_fractal_calculator(
                    fractal_type='burning_ship',
                    max_iterations=self.max_iterations,
                    bailout_radius=2.0
                )
        except Exception as e:
            print(f"Failed to initialize calculator: {e}")
        return None
    
    def _initialize_colorizer(self) -> Optional[FractalColorizer]:
        """Initialize colorizer with ocean palette."""
        try:
            if FractalColorizer:
                return FractalColorizer(
                    palette=ColorPalette.OCEAN,
                    gamma=0.85,  # Slightly darker for ocean depth
                    contrast=self.color_intensity
                )
        except Exception as e:
            print(f"Failed to initialize colorizer: {e}")
        return None

# Test version for development
class TestVisualBurningShipVoyage(VisualBurningShipVoyage):
    """Test version with reduced frames for faster development."""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.voyage_frames = 20  # Reduced for testing
        self.total_duration = 10.0  # Shorter test duration
    
    def construct(self):
        """Quick voyage test with key waypoints."""
        
        if not UTILS_AVAILABLE:
            self.create_visual_fallback()
            return
        
        # Test key voyage points
        test_centers = [-0.5-0.6j, -1.0-0.5j, -1.7-0.03j]
        test_zooms = [1.0, 15.0, 75.0]
        
        current_ship = None
        
        for i, (center, zoom) in enumerate(zip(test_centers, test_zooms)):
            ship = self.render_burning_ship_visual(center, zoom, i/3.0)
            if ship:
                ship.scale_to_fit_height(config.frame_height * 0.9)
                ship.center()
                
                if current_ship is None:
                    self.play(FadeIn(ship, run_time=1.0))
                    current_ship = ship
                else:
                    self.play(Transform(current_ship, ship, run_time=2.0))
                
                self.wait(1.0)
        
        if current_ship:
            self.play(FadeOut(current_ship, run_time=1.5))

if __name__ == "__main__":
    print("Pure Visual Burning Ship Voyage Scene")
    print("Full: manim -pqh visual_03_burning_ship.py VisualBurningShipVoyage")
    print("Test: manim -pql visual_03_burning_ship.py TestVisualBurningShipVoyage")