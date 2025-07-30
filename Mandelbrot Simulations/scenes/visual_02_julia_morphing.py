"""
Visual Scene 2: Julia Set Morphing Gallery (45 seconds)

Pure visual exploration of Julia set parameter space with smooth morphing
between famous Julia set configurations. No text, just mathematical beauty.

Visual Flow:
- Smooth parameter morphing through Julia space
- Famous Julia sets: Dendrite → Douady Rabbit → San Marco → Siegel Disk
- Cosmic color palette with synchronized color cycling
- Seamless loop back to starting parameter
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
    from utils.fractal_algorithms import FractalCalculator, create_fractal_calculator, JULIA_PARAMETERS
    from utils.color_schemes import FractalColorizer, ColorPalette
    UTILS_AVAILABLE = True
except ImportError as e:
    print(f"Import error: {e}")
    UTILS_AVAILABLE = False
    JULIA_PARAMETERS = None

class VisualJuliaMorphing(Scene):
    """
    Pure visual Julia set morphing with smooth parameter transitions.
    
    45-second journey through Julia parameter space showing morphing fractals.
    """
    
    def __init__(self, **kwargs):
        """Initialize visual-only Julia morphing scene."""
        super().__init__(**kwargs)
        self.camera.background_color = "#000000"  # Pure black background
        
        # Visual parameters
        self.total_duration = 45.0
        self.morph_frames = 90  # 2 fps for smooth 45-second animation
        self.transition_smoothness = 0.9
        
        # High-quality rendering parameters
        self.base_resolution = 900
        self.max_iterations = 384
        self.color_intensity = 1.3
        
        # Julia set parameters for morphing sequence
        self.julia_sequence = self._create_julia_sequence()
        
        # Initialize fractal tools
        self.fractal_calculator = self._initialize_calculator()
        self.colorizer = self._initialize_colorizer()
        
    def construct(self):
        """Pure visual construction - smooth Julia set morphing."""
        
        if not UTILS_AVAILABLE or not self.fractal_calculator:
            self.create_visual_fallback()
            return
        
        # Create the mesmerizing morphing sequence
        self.create_julia_morphing_sequence()
    
    def create_julia_morphing_sequence(self):
        """
        Create pure visual morphing sequence between Julia parameters.
        """
        
        # Generate time points for smooth morphing
        frame_times = np.linspace(0.0, 1.0, self.morph_frames)
        
        # Start with first Julia set
        initial_param = self._interpolate_julia_parameter(0.0)
        current_julia = self.render_julia_visual(
            parameter=initial_param,
            color_time=0.0
        )
        
        if current_julia:
            # Scale to full screen for maximum visual impact
            current_julia.scale_to_fit_height(config.frame_height * 0.95)
            current_julia.center()
            
            # Smooth entry
            self.play(FadeIn(current_julia, run_time=1.5), rate_func=smooth)
            
            # Execute morphing sequence
            for i, t in enumerate(frame_times[1:], 1):
                # Interpolate Julia parameter
                julia_param = self._interpolate_julia_parameter(t)
                
                # Render next frame
                next_julia = self.render_julia_visual(
                    parameter=julia_param,
                    color_time=t
                )
                
                if next_julia:
                    next_julia.scale_to_fit_height(config.frame_height * 0.95)
                    next_julia.center()
                    
                    # Variable transition speed for visual interest
                    if t < 0.2 or t > 0.8:
                        transition_time = 0.6  # Slower at beginning and end
                    else:
                        transition_time = 0.4  # Faster in middle for dramatic effect
                    
                    # Smooth morph between Julia sets
                    self.play(
                        Transform(current_julia, next_julia, run_time=transition_time),
                        rate_func=smooth
                    )
                    
                    # Brief pause at key parameter values for appreciation
                    if self._is_famous_julia_point(julia_param):
                        self.wait(0.8)
            
            # Final pause before fade out
            self.wait(1.0)
            
            # Smooth fade out
            self.play(FadeOut(current_julia, run_time=1.5), rate_func=smooth)
        
        else:
            self.create_visual_fallback()
    
    def render_julia_visual(self, parameter: complex, color_time: float) -> Optional[ImageMobject]:
        """
        Render pure visual Julia set frame.
        
        Parameters
        ----------
        parameter : complex
            Julia set parameter c
        color_time : float
            Time parameter for color animation (0.0 to 1.0)
            
        Returns
        -------
        Optional[ImageMobject]
            High-quality visual Julia frame
        """
        try:
            # Fixed resolution for consistent image sizes in Transform
            resolution = self.base_resolution
            
            # Calculate Julia set data
            julia_data = self.fractal_calculator.julia_set(
                width=resolution,
                height=resolution,
                c=parameter,
                center=0+0j,  # Fixed center for parameter morphing
                zoom=1.2  # Slight zoom for better view
            )
            
            # Apply cosmic coloring with parameter-synchronized cycling
            rgb_array = self.colorizer.colorize_escape_data(
                julia_data,
                max_iterations=self.max_iterations,
                cycle_speed=color_time * 2.0 + abs(parameter) * 5.0,
                use_histogram_equalization=True
            )
            
            # Enhance visual quality based on parameter
            rgb_array = self._enhance_julia_visuals(rgb_array, parameter)
            
            # Convert to PIL Image
            rgb_uint8 = (np.clip(rgb_array, 0, 1) * 255).astype(np.uint8)
            pil_image = Image.fromarray(rgb_uint8)
            
            # Save with unique filename
            temp_filename = f"/tmp/julia_visual_{abs(hash((parameter, color_time))) % 100000}.png"
            pil_image.save(temp_filename, optimize=True, quality=95)
            
            return ImageMobject(temp_filename)
            
        except Exception as e:
            print(f"Julia rendering error: {e}")
            return None
    
    def _interpolate_julia_parameter(self, t: float) -> complex:
        """
        Interpolate smoothly between Julia parameters.
        
        Parameters
        ----------
        t : float
            Time parameter (0.0 to 1.0)
            
        Returns
        -------
        complex
            Interpolated Julia parameter
        """
        # Scale time to sequence length
        sequence_t = t * (len(self.julia_sequence) - 1)
        
        # Find surrounding keyframes
        index = int(sequence_t)
        local_t = sequence_t - index
        
        if index >= len(self.julia_sequence) - 1:
            return self.julia_sequence[-1]
        
        # Smooth interpolation between parameters
        param1 = self.julia_sequence[index]
        param2 = self.julia_sequence[index + 1]
        
        # Use smooth easing for natural morphing
        eased_t = self._smooth_step(local_t)
        
        return param1 + eased_t * (param2 - param1)
    
    def _smooth_step(self, t: float) -> float:
        """Smooth step function for natural parameter interpolation."""
        return t * t * (3.0 - 2.0 * t)
    
    def _is_famous_julia_point(self, param: complex) -> bool:
        """Check if parameter is close to a famous Julia set."""
        famous_params = [
            -0.7 + 0.27015j,  # Dendrite
            -0.4 + 0.6j,      # Douady Rabbit
            -0.8 + 0.156j,    # San Marco
            -0.391 - 0.587j,  # Siegel Disk
            -0.194 + 0.6557j  # Fatou Dust
        ]
        
        threshold = 0.05
        return any(abs(param - famous) < threshold for famous in famous_params)
    
    def _enhance_julia_visuals(self, rgb_array: np.ndarray, parameter: complex) -> np.ndarray:
        """
        Enhance Julia visual quality based on parameter characteristics.
        """
        # Adjust contrast based on parameter position
        param_magnitude = abs(parameter)
        contrast_factor = 1.1 + min(0.4, param_magnitude * 0.3)
        enhanced = ((rgb_array - 0.5) * contrast_factor) + 0.5
        
        # Saturation boost varies with parameter angle
        param_angle = np.angle(parameter)
        saturation_boost = 1.2 + 0.3 * np.sin(param_angle * 2)
        
        # Apply saturation enhancement
        enhanced = self._boost_saturation(enhanced, saturation_boost)
        
        return np.clip(enhanced, 0.0, 1.0)
    
    def _boost_saturation(self, rgb_array: np.ndarray, boost_factor: float) -> np.ndarray:
        """Boost color saturation for visual appeal."""
        # Simple saturation boost via luminance preservation
        luminance = 0.299 * rgb_array[:, :, 0] + 0.587 * rgb_array[:, :, 1] + 0.114 * rgb_array[:, :, 2]
        
        # Boost each channel while preserving luminance
        boosted = rgb_array.copy()
        for c in range(3):
            boosted[:, :, c] = luminance + boost_factor * (rgb_array[:, :, c] - luminance)
        
        return boosted
    
    def create_visual_fallback(self):
        """Create aesthetic fallback if Julia rendering fails."""
        
        # Create morphing geometric shapes as placeholder
        shapes = VGroup()
        
        # Base shapes that will morph
        initial_shapes = [
            Circle(radius=2.0, color=PURPLE),
            Square(side_length=3.0, color=BLUE),
            RegularPolygon(n=6, radius=2.5, color=GREEN),
            Star(outer_radius=2.2, color=YELLOW),
        ]
        
        for shape in initial_shapes:
            shape.set_fill(opacity=0.6)
            shape.set_stroke(width=2)
            shapes.add(shape)
        
        shapes.arrange_in_grid(rows=2, cols=2, buff=0.5)
        shapes.center()
        
        # Morphing animation sequence
        self.play(Create(shapes, run_time=2.0))
        
        # Smooth morphing transformations
        for i in range(8):
            # Rotate and scale variations
            new_shapes = shapes.copy()
            for j, shape in enumerate(new_shapes):
                angle = (i * j * PI) / 4
                scale = 0.7 + 0.3 * np.sin(i + j)
                shape.rotate(angle).scale(scale)
                
                # Color cycling
                hue = (i * 0.1 + j * 0.15) % 1.0
                shape.set_color(Color(hue=hue))
            
            self.play(
                Transform(shapes, new_shapes, run_time=1.5),
                rate_func=smooth
            )
            self.wait(0.3)
        
        self.wait(1.0)
        self.play(FadeOut(shapes, run_time=2.0))
    
    def _create_julia_sequence(self) -> List[complex]:
        """Create sequence of Julia parameters for morphing."""
        
        if JULIA_PARAMETERS:
            # Use predefined famous Julia parameters
            sequence = [
                JULIA_PARAMETERS.get('dendrite', -0.7 + 0.27015j),
                JULIA_PARAMETERS.get('douady_rabbit', -0.4 + 0.6j),
                JULIA_PARAMETERS.get('san_marco', -0.8 + 0.156j),
                JULIA_PARAMETERS.get('siegel_disk', -0.391 - 0.587j),
                JULIA_PARAMETERS.get('fatou_dust', -0.194 + 0.6557j),
            ]
            
            # Add back to start for seamless loop
            sequence.append(sequence[0])
            return sequence
        
        # Fallback sequence for visual appeal
        return [
            -0.7 + 0.27015j,  # Dendrite
            -0.4 + 0.6j,      # Douady Rabbit  
            -0.8 + 0.156j,    # San Marco
            -0.391 - 0.587j,  # Siegel Disk
            -0.194 + 0.6557j, # Fatou Dust
            -0.7 + 0.27015j   # Loop back
        ]
    
    def _initialize_calculator(self) -> Optional[FractalCalculator]:
        """Initialize Julia set calculator."""
        try:
            if FractalCalculator:
                return create_fractal_calculator(
                    fractal_type='julia',
                    max_iterations=self.max_iterations,
                    bailout_radius=2.0
                )
        except Exception as e:
            print(f"Failed to initialize calculator: {e}")
        return None
    
    def _initialize_colorizer(self) -> Optional[FractalColorizer]:
        """Initialize colorizer with cosmic palette."""
        try:
            if FractalColorizer:
                return FractalColorizer(
                    palette=ColorPalette.COSMIC,
                    gamma=0.9,
                    contrast=self.color_intensity
                )
        except Exception as e:
            print(f"Failed to initialize colorizer: {e}")
        return None

# Test version for development
class TestVisualJuliaMorphing(VisualJuliaMorphing):
    """Test version with reduced frames for faster development."""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.morph_frames = 15  # Reduced for testing
        self.total_duration = 8.0  # Shorter test duration
    
    def construct(self):
        """Quick test with key Julia parameters."""
        
        if not UTILS_AVAILABLE:
            self.create_visual_fallback()
            return
        
        # Test with just key parameters
        test_params = [
            -0.7 + 0.27015j,  # Dendrite
            -0.4 + 0.6j,      # Douady Rabbit
            -0.8 + 0.156j     # San Marco
        ]
        
        current_julia = None
        
        for i, param in enumerate(test_params):
            julia = self.render_julia_visual(param, i/3.0)
            if julia:
                julia.scale_to_fit_height(config.frame_height * 0.9)
                julia.center()
                
                if current_julia is None:
                    self.play(FadeIn(julia, run_time=1.0))
                    current_julia = julia
                else:
                    self.play(Transform(current_julia, julia, run_time=2.0))
                
                self.wait(1.0)
        
        if current_julia:
            self.play(FadeOut(current_julia, run_time=1.0))

if __name__ == "__main__":
    print("Pure Visual Julia Set Morphing Scene")
    print("Full: manim -pqh visual_02_julia_morphing.py VisualJuliaMorphing")
    print("Test: manim -pql visual_02_julia_morphing.py TestVisualJuliaMorphing")