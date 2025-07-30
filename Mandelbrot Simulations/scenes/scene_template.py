"""
Scene Template for Mandelbrot Simulations.

This template provides a proven structure for implementing fractal scenes
based on the successful patterns from IQB Simulations. Use this as a 
starting point for new fractal scenes to ensure consistency and avoid errors.

Key Features:
- High-performance fractal rendering with Manim integration
- Smooth animation timing and transitions
- Consistent visual styling and color schemes
- Error handling and fallback mechanisms
- Educational content structure with mathematical rigor

Usage:
    Copy this template and modify for specific fractal types.
    Follow the established patterns for consistent development.
"""

from manim import *
import numpy as np
import sys
import os
from typing import Tuple, Optional, Dict, Any

# Add project root to path for imports
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)

try:
    from utils.fractal_algorithms import FractalCalculator, create_fractal_calculator
    from utils.color_schemes import FractalColorizer, ColorPalette, QUANTUM_COLORIZER
    from utils.zoom_paths import ZoomPath, PredefinedZoomPaths, EasingFunction
    UTILS_AVAILABLE = True
except ImportError as e:
    print(f"Import error: {e}")
    # Fallback mode - basic functionality without advanced features
    FractalCalculator = None
    FractalColorizer = None
    QUANTUM_COLORIZER = None
    ZoomPath = None
    PredefinedZoomPaths = None
    EasingFunction = None
    UTILS_AVAILABLE = False

# Color scheme (fallback if imports fail)
FRACTAL_BACKGROUND = "#0B1426"  # Deep space blue
FRACTAL_GOLD = "#FFD700"        # Mathematical highlights
FRACTAL_CYAN = "#00FFFF"        # Fractal boundaries
FRACTAL_MAGENTA = "#FF00FF"     # Special points
FRACTAL_WHITE = "#FFFFFF"       # Text and equations

class FractalSceneTemplate(Scene):
    """
    Template scene class for fractal visualizations.
    
    Provides consistent structure, timing, and visual styling
    for all fractal animation scenes.
    """
    
    def __init__(self, **kwargs):
        """Initialize fractal scene with standard settings."""
        super().__init__(**kwargs)
        self.camera.background_color = FRACTAL_BACKGROUND
        
        # Scene timing parameters
        self.intro_duration = 6.0
        self.main_content_duration = 45.0
        self.conclusion_duration = 9.0
        
        # Animation parameters
        self.standard_run_time = 2.0
        self.quick_run_time = 1.0
        self.slow_run_time = 3.0
        self.fractal_render_time = 8.0
        
        # Fractal calculation parameters
        self.fractal_resolution = 800
        self.max_iterations = 256
        self.quality_multiplier = 1.0
        
        # Initialize fractal tools
        self.fractal_calculator = self._initialize_fractal_calculator()
        self.colorizer = self._initialize_colorizer()
        self.zoom_path = None
        
    def construct(self):
        """Main scene construction following proven template structure."""
        
        # Segment 1: Introduction with mathematical foundation
        self.create_fractal_introduction()
        
        # Segment 2: Interactive fractal demonstration
        self.demonstrate_fractal_generation()
        
        # Segment 3: Advanced features (zoom, color, animation)
        self.showcase_advanced_features()
        
        # Segment 4: Mathematical insights and conclusion
        self.conclude_with_insights()
    
    def create_fractal_introduction(self):
        """
        Create scene introduction with fractal mathematics.
        
        Standard pattern for fractal scene openings including:
        - Scene title with mathematical context
        - Core equation presentation
        - Brief conceptual overview
        """
        
        # Scene title
        scene_title = Text(
            "Fractal Scene Template",  # Replace with specific fractal name
            font_size=48,
            color=FRACTAL_GOLD
        ).to_edge(UP, buff=0.5)
        
        self.play(Write(scene_title, run_time=self.standard_run_time))
        
        # Mathematical foundation equation
        fractal_equation = MathTex(
            r'z_{n+1} = z_n^2 + c',  # Replace with specific fractal equation
            font_size=40,
            color=FRACTAL_WHITE
        ).center()
        
        self.play(Write(fractal_equation, run_time=self.standard_run_time))
        self.wait(1.5)
        
        # Conceptual explanation
        explanation = Text(
            "Replace with fractal-specific explanation",  # Customize for each fractal
            font_size=28,
            color=FRACTAL_CYAN
        ).next_to(fractal_equation, DOWN, buff=1.0)
        
        self.play(Write(explanation, run_time=self.standard_run_time))
        self.wait(2.0)
        
        # Store introduction elements for cleanup
        self.intro_elements = VGroup(scene_title, fractal_equation, explanation)
        
        # Clear introduction
        self.play(FadeOut(self.intro_elements, run_time=self.quick_run_time))
    
    def demonstrate_fractal_generation(self):
        """
        Main fractal demonstration section.
        
        Shows the fractal generation process with real-time visualization.
        This is the core content section - customize for specific fractals.
        """
        
        # Section title
        demo_title = Text(
            "Fractal Generation",
            font_size=36,
            color=FRACTAL_GOLD
        ).to_edge(UP, buff=0.5)
        
        self.play(Write(demo_title, run_time=self.standard_run_time))
        
        # Create fractal visualization area
        fractal_frame = Rectangle(
            width=6, height=6,
            color=FRACTAL_WHITE,
            stroke_width=2
        ).center()
        
        self.play(Create(fractal_frame, run_time=self.quick_run_time))
        
        # Generate fractal data (placeholder - implement in specific scenes)
        fractal_image = self.generate_fractal_visualization()
        fractal_image.move_to(fractal_frame.get_center())
        fractal_image.scale_to_fit_width(fractal_frame.width * 0.95)
        
        # Animate fractal appearance
        self.play(
            FadeIn(fractal_image, run_time=self.fractal_render_time),
            rate_func=smooth
        )
        
        # Add mathematical annotations
        annotations = self.create_fractal_annotations()
        self.play(Create(annotations, run_time=self.standard_run_time))
        
        self.wait(2.0)
        
        # Store main demonstration elements
        self.demo_elements = VGroup(demo_title, fractal_frame, fractal_image, annotations)
    
    def showcase_advanced_features(self):
        """
        Showcase advanced fractal features.
        
        Demonstrates zoom sequences, color variations, and animation effects.
        """
        
        # Clear previous demonstration
        self.play(FadeOut(self.demo_elements, run_time=self.quick_run_time))
        
        # Advanced features title
        advanced_title = Text(
            "Advanced Features",
            font_size=36,
            color=FRACTAL_MAGENTA
        ).to_edge(UP, buff=0.5)
        
        self.play(Write(advanced_title, run_time=self.standard_run_time))
        
        # Feature 1: Zoom Animation
        zoom_demo = self.create_zoom_demonstration()
        self.play(Create(zoom_demo, run_time=self.slow_run_time))
        self.wait(1.0)
        
        # Feature 2: Color Palette Variation
        color_demo = self.create_color_demonstration()
        self.play(
            Transform(zoom_demo, color_demo, run_time=self.standard_run_time)
        )
        self.wait(1.0)
        
        # Feature 3: Parameter Animation (if applicable)
        param_demo = self.create_parameter_demonstration()
        self.play(
            Transform(zoom_demo, param_demo, run_time=self.standard_run_time)
        )
        self.wait(2.0)
        
        # Store advanced features elements
        self.advanced_elements = VGroup(advanced_title, zoom_demo)
    
    def conclude_with_insights(self):
        """
        Conclude scene with mathematical insights and connections.
        
        Standard conclusion pattern emphasizing educational value.
        """
        
        # Clear advanced features
        self.play(FadeOut(self.advanced_elements, run_time=self.quick_run_time))
        
        # Key insight title
        insight_title = Text(
            "Mathematical Insights",
            font_size=40,
            color=FRACTAL_GOLD
        ).to_edge(UP, buff=1.0)
        
        self.play(Write(insight_title, run_time=self.standard_run_time))
        
        # Main mathematical insight (customize for each fractal)
        insight_text = Text(
            "Replace with fractal-specific mathematical insight",
            font_size=30,
            color=FRACTAL_WHITE
        ).center()
        
        self.play(Write(insight_text, run_time=self.standard_run_time))
        self.wait(2.0)
        
        # Connection to broader mathematics
        connection_text = Text(
            "Connection to broader mathematical concepts",
            font_size=24,
            color=FRACTAL_CYAN,
            font="Arial Italic"
        ).next_to(insight_text, DOWN, buff=1.0)
        
        self.play(Write(connection_text, run_time=self.standard_run_time))
        self.wait(2.0)
        
        # Transition preview (for multi-scene sequences)
        transition_text = Text(
            "Next: [Preview of following scene]",
            font_size=24,
            color=FRACTAL_MAGENTA,
            font="Arial Italic"
        ).to_edge(DOWN, buff=1.0)
        
        self.play(Write(transition_text, run_time=self.standard_run_time))
        self.wait(1.5)
        
        # Final fade out
        conclusion_elements = VGroup(insight_title, insight_text, connection_text, transition_text)
        self.play(FadeOut(conclusion_elements, run_time=self.standard_run_time))
        
        self.wait(1.0)  # Buffer for scene transition
    
    def generate_fractal_visualization(self) -> ImageMobject:
        """
        Generate fractal visualization using high-performance algorithms.
        
        Override this method in specific fractal scenes to implement
        the actual fractal calculation and rendering.
        
        Returns
        -------
        ImageMobject
            Rendered fractal image for Manim display
        """
        if self.fractal_calculator is None:
            # Fallback: Simple placeholder
            return self.create_placeholder_fractal()
        
        # Template implementation - replace in specific scenes
        try:
            # Calculate fractal data
            fractal_data = self.fractal_calculator.mandelbrot_set(
                width=self.fractal_resolution,
                height=self.fractal_resolution,
                center=0+0j,
                zoom=1.0
            )
            
            # Convert to RGB using colorizer
            if self.colorizer:
                rgb_array = self.colorizer.colorize_escape_data(
                    fractal_data,
                    max_iterations=self.max_iterations
                )
            else:
                # Fallback grayscale
                rgb_array = self.create_grayscale_fractal(fractal_data)
            
            # Convert to Manim ImageMobject
            # Note: This requires converting numpy array to PIL Image
            from PIL import Image
            
            # Convert to uint8 and create PIL Image
            rgb_uint8 = (rgb_array * 255).astype(np.uint8)
            pil_image = Image.fromarray(rgb_uint8)
            
            # Create temporary file for Manim
            temp_path = "/tmp/fractal_temp.png"
            pil_image.save(temp_path)
            
            return ImageMobject(temp_path)
            
        except Exception as e:
            print(f"Fractal generation error: {e}")
            return self.create_placeholder_fractal()
    
    def create_placeholder_fractal(self) -> Rectangle:
        """Create a placeholder when fractal generation fails."""
        placeholder = Rectangle(
            width=4, height=4,
            color=FRACTAL_CYAN,
            fill_opacity=0.3
        )
        
        placeholder_text = Text(
            "Fractal\\nPlaceholder",
            font_size=24,
            color=FRACTAL_WHITE
        ).move_to(placeholder.get_center())
        
        return VGroup(placeholder, placeholder_text)
    
    def create_grayscale_fractal(self, fractal_data: np.ndarray) -> np.ndarray:
        """Create simple grayscale visualization from fractal data."""
        normalized = fractal_data / np.max(fractal_data)
        rgb_array = np.stack([normalized, normalized, normalized], axis=-1)
        return rgb_array
    
    def create_fractal_annotations(self) -> VGroup:
        """
        Create mathematical annotations for the fractal.
        
        Override in specific scenes to add relevant annotations.
        """
        # Template annotations - customize for each fractal
        annotation1 = MathTex(
            r'\text{Set points: } |z_n| \leq R',
            font_size=24,
            color=FRACTAL_WHITE
        )
        
        annotation2 = MathTex(
            r'\text{Escape points: } |z_n| > R',
            font_size=24,
            color=FRACTAL_CYAN
        )
        
        annotations = VGroup(annotation1, annotation2)
        annotations.arrange(DOWN, buff=0.3)
        annotations.to_edge(RIGHT, buff=1.0)
        
        return annotations
    
    def create_zoom_demonstration(self) -> VGroup:
        """Create zoom sequence demonstration."""
        # Simple zoom visualization placeholder
        zoom_circles = VGroup()
        
        for i in range(3):
            circle = Circle(
                radius=2 - i * 0.5,
                color=FRACTAL_GOLD,
                stroke_width=2
            )
            zoom_circles.add(circle)
        
        zoom_label = Text(
            "Zoom Sequence",
            font_size=20,
            color=FRACTAL_WHITE
        ).next_to(zoom_circles, DOWN, buff=0.5)
        
        return VGroup(zoom_circles, zoom_label)
    
    def create_color_demonstration(self) -> VGroup:
        """Create color palette demonstration."""
        # Simple color strip
        color_strip = Rectangle(
            width=4, height=1,
            fill_opacity=1.0
        )
        color_strip.set_color_by_gradient(BLUE, PURPLE, RED, ORANGE, YELLOW)
        
        color_label = Text(
            "Color Palettes",
            font_size=20,
            color=FRACTAL_WHITE
        ).next_to(color_strip, DOWN, buff=0.3)
        
        return VGroup(color_strip, color_label)
    
    def create_parameter_demonstration(self) -> VGroup:
        """Create parameter variation demonstration."""
        # Simple parameter visualization
        param_shapes = VGroup()
        
        for i in range(3):
            shape = RegularPolygon(
                n=4 + i * 2,
                radius=0.8,
                color=FRACTAL_MAGENTA,
                stroke_width=2
            ).shift(LEFT * 2 + RIGHT * i * 2)
            param_shapes.add(shape)
        
        param_label = Text(
            "Parameter Variation",
            font_size=20,
            color=FRACTAL_WHITE
        ).next_to(param_shapes, DOWN, buff=0.5)
        
        return VGroup(param_shapes, param_label)
    
    def _initialize_fractal_calculator(self) -> Optional[FractalCalculator]:
        """Initialize fractal calculator with error handling."""
        try:
            if FractalCalculator:
                return create_fractal_calculator(
                    fractal_type='mandelbrot',
                    max_iterations=self.max_iterations
                )
        except Exception as e:
            print(f"Failed to initialize fractal calculator: {e}")
        
        return None
    
    def _initialize_colorizer(self) -> Optional[FractalColorizer]:
        """Initialize color scheme with error handling."""
        try:
            if FractalColorizer:
                return QUANTUM_COLORIZER or FractalColorizer(ColorPalette.FIRE)
        except Exception as e:
            print(f"Failed to initialize colorizer: {e}")
        
        return None

# Quick test version for development
class TestFractalTemplate(FractalSceneTemplate):
    """Test version for rapid development and debugging."""
    
    def construct(self):
        """Simplified construction for testing."""
        # Test just the introduction for rapid iteration
        self.create_fractal_introduction()
        
        # Add simple fractal visualization test
        test_visual = self.generate_fractal_visualization()
        test_visual.scale(0.5).center()
        
        self.play(FadeIn(test_visual, run_time=2.0))
        self.wait(2.0)

# =============================================================================
# DEVELOPMENT WORKFLOW GUIDELINES
# =============================================================================

"""
DEVELOPMENT WORKFLOW FOR FRACTAL SCENES:

1. SETUP:
   - Copy this template to new scene file (e.g., scene_01_mandelbrot_classic.py)
   - Replace class name and customize fractal-specific parameters
   - Update scene title and mathematical equations

2. FRACTAL IMPLEMENTATION:
   - Override generate_fractal_visualization() method
   - Implement specific fractal algorithm (Mandelbrot, Julia, etc.)
   - Configure appropriate color scheme and zoom parameters

3. MATHEMATICAL CONTENT:
   - Update fractal equations using direct LaTeX strings
   - Customize annotations for specific fractal properties
   - Add relevant mathematical insights in conclusion

4. TESTING STRATEGY:
   - Use TestFractalTemplate class for rapid iteration
   - Test fractal generation separately before animation
   - Verify color schemes and zoom sequences independently

5. PERFORMANCE OPTIMIZATION:
   - Adjust fractal_resolution based on zoom level
   - Use appropriate max_iterations for fractal type
   - Profile fractal calculation performance

6. QUALITY ASSURANCE:
   - Test rendering with: manim -pql scenes/scene_XX.py ClassName
   - Verify mathematical accuracy of fractal algorithms
   - Check timing aligns with target duration
   - Ensure consistent visual style

7. INTEGRATION:
   - Test scene transitions between fractal types
   - Verify zoom sequences loop back smoothly
   - Check color palette consistency across scenes

PERFORMANCE GUIDELINES:
- Mandelbrot: resolution 800x800, max_iterations 256
- Julia: resolution 800x800, max_iterations 256
- Burning Ship: resolution 600x600, max_iterations 512
- Tricorn: resolution 800x800, max_iterations 256

TIMING STANDARDS:
- Introduction: 6 seconds
- Main content: 45 seconds  
- Advanced features: 20 seconds
- Conclusion: 9 seconds
- Total: ~80 seconds per scene
"""

if __name__ == "__main__":
    # Test the template independently
    print("Testing Fractal Scene Template")
    print("Run with: manim -pql scene_template.py FractalSceneTemplate")