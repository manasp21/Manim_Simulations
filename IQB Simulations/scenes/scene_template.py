"""
Scene Template for Quantum Beats Animation

This template provides a working structure for implementing additional scenes
based on the successfully debugged Scene 1. Use this as a starting point for
new scenes to avoid LaTeX and import errors.

Key Learnings from Scene 1:
- Use direct LaTeX strings instead of dictionary lookups for mathematical expressions
- Implement simple VGroup-based visualizations instead of complex utility classes
- Include proper try/except blocks for import handling
- Use consistent color scheme and styling
"""

from manim import *
import numpy as np
import sys
import os

# Add project root to path for imports
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)

try:
    from utils.color_schemes import (
        QUANTUM_BACKGROUND, QUANTUM_GOLD, COHERENCE_GREEN, DECOHERENCE_RED,
        QuantumColorScheme
    )
    from utils.latex_formatting import (
        QuantumLatexFormatter
    )
    from utils.quantum_visualizations import (
        QuantumBlochSphere, QuantumEnergyLevels, QuantumInterference
    )
    from assets.mathematical_expressions import QuantumBeatExpressions
    from assets.narration_scripts import QuantumBeatsNarration
except ImportError as e:
    print(f"Import error: {e}")
    # Fallback color definitions if imports fail
    QUANTUM_BACKGROUND = "#0B1426"
    QUANTUM_GOLD = "#FFD700"
    COHERENCE_GREEN = "#00FF7F" 
    DECOHERENCE_RED = "#FF4500"

class SceneTemplate(Scene):
    """
    Template scene class with proven working patterns.
    
    Copy this class and modify for new scenes. The structure follows
    the successful pattern from Scene 1.
    """
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.camera.background_color = QUANTUM_BACKGROUND
        
        # Scene timing parameters (adjust for each scene)
        self.intro_duration = 8.0
        self.main_content_duration = 60.0
        self.conclusion_duration = 12.0
        
        # Animation parameters
        self.standard_run_time = 2.0
        self.quick_run_time = 1.0
        self.slow_run_time = 3.0
        
    def construct(self):
        """Main scene construction with timing structure."""
        
        # Segment 1: Introduction
        self.create_scene_introduction()
        
        # Segment 2: Main Content (customize for each scene)
        self.demonstrate_main_concepts()
        
        # Segment 3: Conclusion and Transition
        self.conclude_scene()
    
    def create_scene_introduction(self):
        """
        Create scene introduction with title and overview.
        
        Use this pattern for consistent scene openings.
        """
        
        # Scene title
        scene_title = Text(
            "Scene Title Here",  # Replace with actual title
            font_size=48,
            color=QUANTUM_GOLD
        ).to_edge(UP, buff=0.5)
        
        self.play(Write(scene_title, run_time=self.standard_run_time))
        
        # Scene overview or key concept introduction
        overview_text = Text(
            "Overview or key concept description",  # Replace with content
            font_size=32,
            color=WHITE
        ).center()
        
        self.play(Write(overview_text, run_time=self.standard_run_time))
        self.wait(2.0)
        
        # Clear introduction elements
        intro_elements = VGroup(scene_title, overview_text)
        self.play(FadeOut(intro_elements, run_time=self.quick_run_time))
    
    def demonstrate_main_concepts(self):
        """
        Main content demonstration section.
        
        Customize this method for each scene's specific content.
        """
        
        # Section title
        section_title = Text(
            "Main Concept",  # Replace with section title
            font_size=40,
            color=COHERENCE_GREEN
        ).to_edge(UP, buff=0.5)
        
        self.play(Write(section_title, run_time=self.standard_run_time))
        
        # Create mathematical equation - use direct LaTeX strings
        main_equation = MathTex(
            r'\text{Replace with actual equation}',  # Replace with content
            font_size=36,
            color=WHITE
        ).center()
        
        self.play(Write(main_equation, run_time=self.standard_run_time))
        
        # Create simple visualization using basic Manim objects
        visualization = self.create_simple_visualization()
        visualization.shift(DOWN * 1.5)
        
        self.play(Create(visualization, run_time=self.slow_run_time))
        
        self.wait(2.0)
        
        # Store elements for cleanup
        self.main_elements = VGroup(section_title, main_equation, visualization)
    
    def create_simple_visualization(self):
        """
        Create visualization using basic Manim objects.
        
        Avoid complex utility classes that may have import issues.
        Use VGroup to combine simple geometric objects.
        """
        
        # Example: Simple energy level diagram
        level_1 = Line(start=[-2, -1, 0], end=[2, -1, 0], color=WHITE, stroke_width=4)
        level_2 = Line(start=[-2, 1, 0], end=[2, 1, 0], color=WHITE, stroke_width=4)
        
        label_1 = MathTex(r'|1\rangle', font_size=28).next_to(level_1, LEFT, buff=0.3)
        label_2 = MathTex(r'|2\rangle', font_size=28).next_to(level_2, LEFT, buff=0.3)
        
        # Simple arrow for transitions
        transition_arrow = Arrow(
            start=[0, -0.8, 0], 
            end=[0, 0.8, 0], 
            color=QUANTUM_GOLD,
            stroke_width=3
        )
        
        arrow_label = MathTex(r'\hbar\omega', font_size=24, color=QUANTUM_GOLD)
        arrow_label.next_to(transition_arrow, RIGHT, buff=0.2)
        
        return VGroup(level_1, level_2, label_1, label_2, transition_arrow, arrow_label)
    
    def conclude_scene(self):
        """
        Conclude scene with key insights and transition.
        
        Use this pattern for consistent scene endings.
        """
        
        # Clear main elements
        self.play(FadeOut(self.main_elements, run_time=self.standard_run_time))
        
        # Key insight
        insight_title = Text(
            "Key Insight",
            font_size=48,
            color=QUANTUM_GOLD
        ).to_edge(UP, buff=1.0)
        
        self.play(Write(insight_title, run_time=self.standard_run_time))
        
        # Main conclusion
        conclusion_text = Text(
            "Main conclusion or key takeaway message",  # Replace with content
            font_size=32,
            color=WHITE
        ).center()
        
        self.play(Write(conclusion_text, run_time=self.standard_run_time))
        self.wait(2.0)
        
        # Transition preview
        transition_text = Text(
            "Next: Preview of following scene",  # Replace with content
            font_size=28,
            color=QUANTUM_GOLD,
            style=ITALIC
        ).to_edge(DOWN, buff=1.0)
        
        self.play(Write(transition_text, run_time=self.standard_run_time))
        self.wait(2.0)
        
        # Final fade out
        conclusion_elements = VGroup(insight_title, conclusion_text, transition_text)
        self.play(FadeOut(conclusion_elements, run_time=self.standard_run_time))
        
        self.wait(1.0)  # Buffer for scene transition

# Quick test version for development
class TestSceneTemplate(SceneTemplate):
    """Test version for rapid development and debugging."""
    
    def construct(self):
        """Quick test construction for development."""
        # Test just the introduction for rapid iteration
        self.create_scene_introduction()

# =============================================================================
# DEVELOPMENT WORKFLOW GUIDELINES
# =============================================================================

"""
DEVELOPMENT WORKFLOW FOR NEW SCENES:

1. SETUP:
   - Copy this template to new scene file (e.g., scene_02_density_matrix.py)
   - Replace class name and customize timing parameters
   - Update scene title and content placeholders

2. MATHEMATICAL EXPRESSIONS:
   - Use direct LaTeX strings: MathTex(r'\hat{H} = \hbar\omega |1\rangle\langle 1|')
   - Avoid dictionary lookups from mathematical_expressions.py until fully tested
   - Test LaTeX compilation with simple equations first

3. VISUALIZATIONS:
   - Use basic Manim objects: Line, Circle, Arrow, Rectangle, etc.
   - Combine with VGroup for complex visualizations
   - Avoid custom utility classes until core functionality works

4. TESTING STRATEGY:
   - Create TestScene class for rapid iteration
   - Test individual segments before combining
   - Use -pql flag for fast development rendering
   - Test LaTeX equations individually if compilation fails

5. COLOR SCHEME:
   - QUANTUM_GOLD (#FFD700): Key concepts and highlights
   - COHERENCE_GREEN (#00FF7F): Quantum coherence phenomena  
   - DECOHERENCE_RED (#FF4500): Environmental effects and decay
   - WHITE: Standard equations and text
   - QUANTUM_BACKGROUND (#0B1426): Scene background

6. TIMING GUIDELINES:
   - Scene 1: 2.5 min (150 seconds) ✓ WORKING
   - Scene 2: 3.5 min (210 seconds) - Mathematical Formalism
   - Scene 3: 3.0 min (180 seconds) - Isotropic vs Anisotropic
   - Scene 4: 2.5 min (150 seconds) - Physical Mechanisms
   - Scene 5: 2.5 min (150 seconds) - Decoherence Effects
   - Scene 6: 2.0 min (120 seconds) - Experimental Detection
   - Scene 7: 2.5 min (150 seconds) - Interpretational Issues
   - Scene 8: 2.0 min (120 seconds) - Future Directions

7. QUALITY ASSURANCE:
   - Test rendering with: manim -pql scenes/scene_XX.py SceneClassName
   - Verify LaTeX compilation for all mathematical expressions
   - Check timing aligns with target duration
   - Ensure consistent visual style and color scheme

8. COMMON PITFALLS TO AVOID:
   - Complex utility class dependencies (use simple objects first)
   - Dictionary-based LaTeX expressions (use direct strings)
   - Missing import fallbacks (always include try/except blocks)
   - Inconsistent timing and pacing across scenes
"""

if __name__ == "__main__":
    # Test the template independently
    print("Testing Scene Template")
    print("Run with: manim -pql scene_template.py SceneTemplate")