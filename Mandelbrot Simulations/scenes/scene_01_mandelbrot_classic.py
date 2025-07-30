"""
Scene 1: Classic Mandelbrot Set with Deep Zoom Animation

This scene showcases the iconic Mandelbrot set with a mesmerizing deep zoom
sequence that explores the infinite complexity at the boundary of the set.
Features smooth loop-back animation returning to the original view.

Mathematical Foundation:
The Mandelbrot set consists of complex numbers c for which the iteration
z_{n+1} = z_n^2 + c (starting with z_0 = 0) remains bounded.

Key Features:
- High-resolution Mandelbrot set rendering
- Deep zoom into seahorse valley region  
- Smooth color transitions and escape-time coloring
- Educational mathematical annotations
- Seamless loop-back to starting position
"""

from manim import *
import numpy as np
import sys
import os
from typing import Tuple, Optional
from PIL import Image

# Add project root to path for imports
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)

try:
    from utils.fractal_algorithms import FractalCalculator, create_fractal_calculator
    from utils.color_schemes import FractalColorizer, ColorPalette, QUANTUM_COLORIZER
    from utils.zoom_paths import MANDELBROT_PATHS, ZoomPath, EasingFunction
    from scenes.scene_template import FractalSceneTemplate
except ImportError as e:
    print(f"Import error: {e}")
    # Use fallback imports
    FractalCalculator = None
    FractalColorizer = None
    QUANTUM_COLORIZER = None
    MANDELBROT_PATHS = {}

class ClassicMandelbrotSet(Scene):
    """
    Classic Mandelbrot set visualization with deep zoom animation.
    
    Demonstrates the beauty and infinite complexity of the Mandelbrot set
    through high-quality rendering and smooth zoom sequences.
    """
    
    def __init__(self, **kwargs):
        """Initialize Mandelbrot scene with optimized settings."""
        super().__init__(**kwargs)
        self.camera.background_color = "#0B1426"  # Deep space blue
        
        # Scene timing parameters
        self.intro_duration = 8.0
        self.zoom_sequence_duration = 35.0
        self.conclusion_duration = 7.0
        
        # Animation parameters
        self.standard_run_time = 2.5
        self.quick_run_time = 1.0
        self.zoom_frame_rate = 30  # Frames for zoom animation
        
        # Mandelbrot calculation parameters
        self.base_resolution = 800
        self.max_iterations = 256
        self.bailout_radius = 2.0
        
        # Initialize Mandelbrot tools
        self.fractal_calculator = self._initialize_calculator()
        self.colorizer = self._initialize_colorizer()
        self.zoom_path = self._initialize_zoom_path()
        
        # Colors
        self.mandelbrot_gold = "#FFD700"
        self.fractal_cyan = "#00FFFF"
        self.set_color = "#FFFFFF"
        
    def construct(self):
        """Main scene construction showcasing Mandelbrot set."""
        
        # Introduction: Mathematical foundation
        self.introduce_mandelbrot_mathematics()
        
        # Main sequence: Zoom animation with educational annotations
        self.demonstrate_mandelbrot_zoom()
        
        # Conclusion: Mathematical insights and significance
        self.conclude_with_mathematical_insights()
    
    def introduce_mandelbrot_mathematics(self):
        """
        Introduce the Mandelbrot set with mathematical rigor.
        """
        
        # Title sequence
        title = Text(
            "The Mandelbrot Set",
            font_size=56,
            color=self.mandelbrot_gold,
            font="Arial Bold"
        ).to_edge(UP, buff=0.8)
        
        subtitle = Text(
            "Infinite Complexity from Simple Rules",
            font_size=32,
            color=self.fractal_cyan,
            font="Arial Italic"
        ).next_to(title, DOWN, buff=0.3)
        
        self.play(
            Write(title, run_time=2.0),
            Write(subtitle, run_time=2.0, lag_ratio=0.5)
        )
        self.wait(1.5)
        
        # Core mathematical definition
        definition_text = Text(
            "For each complex number c, iterate:",
            font_size=28,
            color=WHITE
        ).shift(UP * 1.0)
        
        mandelbrot_equation = MathTex(
            r'z_0 = 0',
            r'\\\\',
            r'z_{n+1} = z_n^2 + c',
            font_size=44,
            color=WHITE
        ).center()
        
        condition_text = Text(
            "If |z_n| remains bounded → c is in the Mandelbrot set",
            font_size=26,
            color=self.fractal_cyan
        ).shift(DOWN * 1.2)
        
        self.play(Write(definition_text, run_time=self.standard_run_time))
        self.play(Write(mandelbrot_equation, run_time=self.standard_run_time))
        self.play(Write(condition_text, run_time=self.standard_run_time))
        self.wait(2.0)
        
        # Example calculation
        example_title = Text(
            "Example: c = -1",
            font_size=28,
            color=self.mandelbrot_gold
        ).shift(UP * 2.0)
        
        calculation_steps = VGroup(
            MathTex(r'z_0 = 0', font_size=32),
            MathTex(r'z_1 = 0^2 + (-1) = -1', font_size=32),
            MathTex(r'z_2 = (-1)^2 + (-1) = 0', font_size=32),
            MathTex(r'z_3 = 0^2 + (-1) = -1', font_size=32),
            MathTex(r'\text{Pattern: } 0 \to -1 \to 0 \to -1 \to \ldots', font_size=28, color=self.fractal_cyan)
        ).arrange(DOWN, buff=0.4).shift(DOWN * 0.5)
        
        conclusion = Text(
            "Bounded sequence → c = -1 is in the Mandelbrot set",
            font_size=24,
            color=self.mandelbrot_gold
        ).shift(DOWN * 2.8)
        
        # Clear previous content
        intro_elements = VGroup(title, subtitle, definition_text, mandelbrot_equation, condition_text)
        self.play(FadeOut(intro_elements, run_time=1.0))
        
        # Show example
        self.play(Write(example_title, run_time=1.0))
        
        for step in calculation_steps:
            self.play(Write(step, run_time=0.8))
            self.wait(0.3)
        
        self.play(Write(conclusion, run_time=1.5))
        self.wait(2.0)
        
        # Clear example
        example_elements = VGroup(example_title, calculation_steps, conclusion)
        self.play(FadeOut(example_elements, run_time=1.0))
    
    def demonstrate_mandelbrot_zoom(self):
        """
        Main demonstration: Mandelbrot set with deep zoom animation.
        """
        
        # Section title
        zoom_title = Text(
            "Exploring Infinite Detail",
            font_size=40,
            color=self.mandelbrot_gold
        ).to_edge(UP, buff=0.5)
        
        self.play(Write(zoom_title, run_time=1.5))
        
        # Create initial overview of Mandelbrot set
        overview_mandelbrot = self.render_mandelbrot_frame(
            center=0+0j,
            zoom=1.0,
            resolution=600
        )
        
        if overview_mandelbrot:
            overview_mandelbrot.scale(0.8).center()
            
            # Add coordinate annotations
            annotations = self.create_coordinate_annotations()
            
            self.play(
                FadeIn(overview_mandelbrot, run_time=3.0),
                Create(annotations, run_time=2.0)
            )
            self.wait(2.0)
            
            # Zoom sequence with smooth transitions
            self.execute_zoom_sequence(overview_mandelbrot, zoom_title, annotations)
        else:
            # Fallback if rendering fails
            self.show_mandelbrot_fallback()
    
    def execute_zoom_sequence(self, initial_mandelbrot, title, annotations):
        """
        Execute the main zoom sequence with smooth interpolation.
        """
        
        if not self.zoom_path:
            # Fallback zoom sequence
            self.simple_zoom_sequence(initial_mandelbrot)
            return
        
        # Get zoom sequence parameters
        num_frames = 25
        time_points = np.linspace(0.0, 1.0, num_frames)
        
        current_mandelbrot = initial_mandelbrot
        
        # Zoom information display
        zoom_info = Text(
            "Zoom: 1.0x",
            font_size=24,
            color=self.fractal_cyan
        ).to_edge(DOWN + RIGHT, buff=0.5)
        
        location_info = Text(
            "Location: Overview",
            font_size=20,
            color=WHITE
        ).next_to(zoom_info, UP, buff=0.2)
        
        self.play(
            Write(zoom_info, run_time=0.5),
            Write(location_info, run_time=0.5)
        )
        
        # Execute zoom frames
        for i, t in enumerate(time_points[1:], 1):
            # Get zoom parameters at time t
            center, zoom, rotation = self.zoom_path.interpolate_at_time(t)
            
            # Render new frame
            new_mandelbrot = self.render_mandelbrot_frame(
                center=center,
                zoom=zoom,
                resolution=max(400, int(600 - zoom/100))  # Adaptive resolution
            )
            
            if new_mandelbrot:
                new_mandelbrot.scale(0.8).center()
                
                # Update zoom information
                new_zoom_info = Text(
                    f"Zoom: {zoom:.1f}x",
                    font_size=24,
                    color=self.fractal_cyan
                ).to_edge(DOWN + RIGHT, buff=0.5)
                
                # Get location description
                location_desc = self.get_location_description(center, zoom)
                new_location_info = Text(
                    f"Location: {location_desc}",
                    font_size=20,
                    color=WHITE
                ).next_to(new_zoom_info, UP, buff=0.2)
                
                # Smooth transition
                transition_time = 1.5 if i < 10 else 1.0  # Slower at beginning
                
                self.play(
                    Transform(current_mandelbrot, new_mandelbrot, run_time=transition_time),
                    Transform(zoom_info, new_zoom_info, run_time=0.3),
                    Transform(location_info, new_location_info, run_time=0.3),
                    rate_func=smooth
                )
                
                # Brief pause for dramatic effect at key zoom levels
                if zoom in [10.0, 100.0, 1000.0]:
                    self.wait(0.8)
        
        # Final pause at maximum zoom
        self.wait(2.0)
        
        # Clean up
        final_elements = VGroup(title, current_mandelbrot, annotations, zoom_info, location_info)
        self.play(FadeOut(final_elements, run_time=2.0))
    
    def simple_zoom_sequence(self, mandelbrot_image):
        """Fallback simple zoom sequence if advanced path fails."""
        # Simple 3-step zoom
        zoom_centers = [0+0j, -0.5+0j, -0.7+0.1j]
        zoom_levels = [1.0, 5.0, 25.0]
        
        current_image = mandelbrot_image
        
        for center, zoom in zip(zoom_centers[1:], zoom_levels[1:]):
            new_image = self.render_mandelbrot_frame(center, zoom, 400)
            if new_image:
                new_image.scale(0.8).center()
                self.play(Transform(current_image, new_image, run_time=2.0))
                self.wait(1.0)
    
    def conclude_with_mathematical_insights(self):
        """
        Conclude with mathematical insights about the Mandelbrot set.
        """
        
        # Key insights title
        insights_title = Text(
            "Mathematical Significance",
            font_size=44,
            color=self.mandelbrot_gold
        ).to_edge(UP, buff=0.8)
        
        self.play(Write(insights_title, run_time=2.0))
        
        # Core insights
        insights = VGroup(
            Text("• Infinite complexity from simple iteration", font_size=28, color=WHITE),
            Text("• Self-similarity at all scales", font_size=28, color=WHITE),
            Text("• Boundary between order and chaos", font_size=28, color=WHITE),
            Text("• Connection to complex dynamics theory", font_size=28, color=WHITE)
        ).arrange(DOWN, buff=0.5, aligned_edge=LEFT).center()
        
        for insight in insights:
            self.play(Write(insight, run_time=1.2))
            self.wait(0.3)
        
        self.wait(2.0)
        
        # Historical note
        historical_note = Text(
            "Named after Benoit Mandelbrot (1980)",
            font_size=24,
            color=self.fractal_cyan,
            font="Arial Italic"
        ).next_to(insights, DOWN, buff=1.0)
        
        self.play(Write(historical_note, run_time=1.5))
        self.wait(1.5)
        
        # Transition to next scene
        transition_text = Text(
            "Next: Julia Sets - The Mandelbrot's Companions",
            font_size=26,
            color=self.mandelbrot_gold,
            font="Arial Italic"
        ).to_edge(DOWN, buff=0.8)
        
        self.play(Write(transition_text, run_time=1.5))
        self.wait(2.0)
        
        # Final fade out
        conclusion_elements = VGroup(insights_title, insights, historical_note, transition_text)
        self.play(FadeOut(conclusion_elements, run_time=2.0))
        
        self.wait(1.0)
    
    def render_mandelbrot_frame(self, center: complex, zoom: float, resolution: int) -> Optional[ImageMobject]:
        """
        Render a single Mandelbrot set frame.
        
        Parameters
        ----------
        center : complex
            Center point in complex plane
        zoom : float
            Zoom level
        resolution : int
            Image resolution
            
        Returns
        -------
        ImageMobject or None
            Rendered Mandelbrot frame
        """
        if not self.fractal_calculator:
            return None
        
        try:
            # Calculate Mandelbrot data
            mandelbrot_data = self.fractal_calculator.mandelbrot_set(
                width=resolution,
                height=resolution,
                center=center,
                zoom=zoom
            )
            
            # Apply coloring
            if self.colorizer:
                rgb_array = self.colorizer.colorize_escape_data(
                    mandelbrot_data,
                    max_iterations=self.max_iterations,
                    cycle_speed=zoom * 0.01  # Subtle color cycling based on zoom
                )
            else:
                # Fallback grayscale
                normalized = mandelbrot_data / self.max_iterations
                rgb_array = np.stack([normalized, normalized, normalized], axis=-1)
            
            # Convert to PIL Image and save temporarily
            rgb_uint8 = (np.clip(rgb_array, 0, 1) * 255).astype(np.uint8)
            pil_image = Image.fromarray(rgb_uint8)
            
            # Save with unique filename based on parameters
            temp_filename = f"/tmp/mandelbrot_{abs(hash((center, zoom, resolution))) % 10000}.png"
            pil_image.save(temp_filename)
            
            return ImageMobject(temp_filename)
            
        except Exception as e:
            print(f"Mandelbrot rendering error: {e}")
            return None
    
    def create_coordinate_annotations(self) -> VGroup:
        """Create coordinate system annotations for the Mandelbrot set."""
        
        # Real axis label
        real_axis = Text(
            "Real Axis",
            font_size=20,
            color=WHITE
        ).shift(DOWN * 2.5 + RIGHT * 1.5)
        
        # Imaginary axis label  
        imag_axis = Text(
            "Imaginary\\nAxis",
            font_size=20,
            color=WHITE
        ).shift(UP * 1.5 + LEFT * 3.5)
        
        # Key points
        origin_dot = Dot(ORIGIN, color=self.mandelbrot_gold, radius=0.05)
        origin_label = Text(
            "0",
            font_size=16,
            color=self.mandelbrot_gold
        ).next_to(origin_dot, DOWN + RIGHT, buff=0.1)
        
        # Set boundary indication
        boundary_text = Text(
            "Set Boundary",
            font_size=18,
            color=self.fractal_cyan
        ).shift(UP * 2.8 + LEFT * 2.0)
        
        return VGroup(real_axis, imag_axis, origin_dot, origin_label, boundary_text)
    
    def get_location_description(self, center: complex, zoom: float) -> str:
        """Get descriptive name for current location."""
        
        # Famous locations in the Mandelbrot set
        if abs(center - (-0.7269 + 0.1889j)) < 0.1 / zoom:
            return "Seahorse Valley"
        elif abs(center - (-1.8 + 0j)) < 0.2 / zoom:
            return "Lightning"
        elif abs(center - (0.001643721971153 + 0.822467633298876j)) < 0.1 / zoom:
            return "Spiral Region"
        elif abs(center) < 0.5 / zoom:
            return "Main Body"
        elif center.real < -1.5:
            return "Western Tendrils"
        elif abs(center.imag) > 0.5:
            return "Northern/Southern Regions"
        else:
            return "Deep Zoom"
    
    def show_mandelbrot_fallback(self):
        """Show fallback visualization if rendering fails."""
        
        # Create simple geometric representation
        main_body = Circle(radius=1.0, color=self.set_color, fill_opacity=0.8)
        bulb = Circle(radius=0.3, color=self.set_color, fill_opacity=0.8).shift(LEFT * 1.3)
        
        mandelbrot_approx = VGroup(main_body, bulb).center()
        
        fallback_text = Text(
            "Mandelbrot Set\\n(Simplified View)",
            font_size=24,
            color=self.fractal_cyan
        ).next_to(mandelbrot_approx, DOWN, buff=0.5)
        
        self.play(
            Create(mandelbrot_approx, run_time=2.0),
            Write(fallback_text, run_time=1.5)
        )
        self.wait(3.0)
        
        self.play(FadeOut(VGroup(mandelbrot_approx, fallback_text), run_time=1.5))
    
    def _initialize_calculator(self) -> Optional[FractalCalculator]:
        """Initialize Mandelbrot calculator with error handling."""
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
        """Initialize colorizer with quantum-inspired palette."""
        try:
            if FractalColorizer:
                return QUANTUM_COLORIZER or FractalColorizer(ColorPalette.FIRE)
        except Exception as e:
            print(f"Failed to initialize colorizer: {e}")
        return None
    
    def _initialize_zoom_path(self) -> Optional[ZoomPath]:
        """Initialize zoom path for seahorse valley exploration."""
        try:
            if MANDELBROT_PATHS:
                path = MANDELBROT_PATHS.get('seahorse_valley')
                if path:
                    return path
        except Exception as e:
            print(f"Failed to initialize zoom path: {e}")
        return None

# Test version for development
class TestMandelbrotClassic(ClassicMandelbrotSet):
    """Test version with simplified rendering for development."""
    
    def construct(self):
        """Simplified test construction."""
        
        # Test introduction only
        self.introduce_mandelbrot_mathematics()
        
        # Simple test rendering
        test_frame = self.render_mandelbrot_frame(0+0j, 1.0, 200)
        if test_frame:
            test_frame.scale(0.5).center()
            self.play(FadeIn(test_frame, run_time=2.0))
            self.wait(2.0)

if __name__ == "__main__":
    print("Classic Mandelbrot Set Scene")
    print("Run with: manim -pql scene_01_mandelbrot_classic.py ClassicMandelbrotSet")
    print("Test with: manim -pql scene_01_mandelbrot_classic.py TestMandelbrotClassic")