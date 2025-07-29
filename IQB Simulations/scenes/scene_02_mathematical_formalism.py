"""
Scene 2: Mathematical Formalism and Density Matrix Approach

This scene introduces the mathematical framework for quantum beats using
density matrix formalism, master equation approach, and beat signal derivation.

Duration: 3.5 minutes (210 seconds)
Target Audience: Physics researchers and graduate students
Scientific Level: Advanced graduate/research level
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

class MathematicalFormalism(Scene):
    """
    Scene 2: Mathematical formalism for quantum beats using density matrices.
    
    Introduces density matrix approach, master equation, and beat signal derivation
    with interactive visualizations of quantum coherence dynamics.
    """
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.camera.background_color = QUANTUM_BACKGROUND
        
        # Scene timing parameters (3.5 min = 210 seconds total)
        self.intro_duration = 15.0        # Scene introduction
        self.density_matrix_duration = 45.0   # Density matrix introduction
        self.master_equation_duration = 60.0  # Master equation derivation
        self.beat_signal_duration = 50.0      # Beat signal development
        self.coherence_duration = 25.0        # Coherence interpretation
        self.conclusion_duration = 15.0       # Conclusion and transition
        
        # Animation parameters
        self.standard_run_time = 2.0
        self.quick_run_time = 1.0
        self.slow_run_time = 3.0
        
    def construct(self):
        """Main scene construction with precise timing."""
        
        # Segment 1: Introduction (0-15s)
        self.create_scene_introduction()
        
        # Segment 2: Density Matrix Approach (15-60s)
        self.introduce_density_matrix()
        
        # Segment 3: Master Equation Derivation (60-120s)
        self.derive_master_equation()
        
        # Segment 4: Beat Signal Development (120-170s)
        self.develop_beat_signal()
        
        # Segment 5: Physical Interpretation (170-195s)
        self.interpret_coherence_dynamics()
        
        # Segment 6: Conclusion and Transition (195-210s)
        self.conclude_scene()
    
    def create_scene_introduction(self):
        """
        Scene introduction highlighting mathematical approach.
        
        Establishes the need for density matrix formalism in quantum beats.
        """
        
        # Scene title
        scene_title = Text(
            "Mathematical Formalism and Density Matrix Approach",
            font_size=48,
            color=QUANTUM_GOLD
        ).to_edge(UP, buff=0.5)
        
        self.play(Write(scene_title, run_time=self.standard_run_time))
        
        # Key motivation
        motivation_text = Text(
            "Why do we need density matrices for quantum beats?",
            font_size=32,
            color=WHITE
        ).center()
        
        self.play(Write(motivation_text, run_time=self.standard_run_time))
        self.wait(2.0)
        
        # Answer with key points
        key_points = VGroup(
            Text("• Mixed quantum states require statistical description", font_size=28, color=WHITE),
            Text("• Environmental decoherence needs open system treatment", font_size=28, color=WHITE),
            Text("• Coherence dynamics captured by off-diagonal elements", font_size=28, color=COHERENCE_GREEN)
        ).arrange(DOWN, buff=0.5, aligned_edge=LEFT)
        key_points.shift(DOWN * 0.5)
        
        for point in key_points:
            self.play(Write(point, run_time=1.5))
            self.wait(0.5)
        
        self.wait(2.0)
        
        # Clear introduction elements
        intro_elements = VGroup(scene_title, motivation_text, key_points)
        self.play(FadeOut(intro_elements, run_time=self.quick_run_time))
    
    def introduce_density_matrix(self):
        """
        Introduce density matrix formalism with interactive visualization.
        
        Shows pure vs mixed states and matrix element interpretation.
        """
        
        # Section title
        section_title = Text(
            "Density Matrix Formalism",
            font_size=40,
            color=COHERENCE_GREEN
        ).to_edge(UP, buff=0.5)
        
        self.play(Write(section_title, run_time=self.standard_run_time))
        
        # General density matrix definition
        density_def = MathTex(
            r'\hat{\rho} = \sum_i p_i |\psi_i\rangle\langle\psi_i|',
            font_size=36,
            color=WHITE
        ).shift(UP * 1.5)
        
        self.play(Write(density_def, run_time=self.standard_run_time))
        
        # Two-level system density matrix
        two_level_matrix = MathTex(
            r'\hat{\rho} = \begin{pmatrix} \rho_{11} & \rho_{12} \\ \rho_{21} & \rho_{22} \end{pmatrix}',
            font_size=36,
            color=WHITE
        ).center()
        
        self.play(Write(two_level_matrix, run_time=self.standard_run_time))
        
        # Interactive density matrix visualization
        matrix_visual = self.create_density_matrix_visualization()
        matrix_visual.shift(DOWN * 1.5)
        
        self.play(Create(matrix_visual, run_time=self.slow_run_time))
        
        # Element interpretations
        population_text = Text("Diagonal: Population", font_size=24, color=WHITE)
        population_text.next_to(matrix_visual, LEFT, buff=1.5).shift(UP * 0.8)  # Increased buffer and spacing
        
        coherence_text = Text("Off-diagonal: Coherence", font_size=24, color=COHERENCE_GREEN)
        coherence_text.next_to(matrix_visual, LEFT, buff=1.5).shift(DOWN * 0.8)  # Increased buffer and spacing
        
        self.play(
            Write(population_text, run_time=1.5),
            Write(coherence_text, run_time=1.5)
        )
        
        # Highlight matrix elements
        self.play(
            two_level_matrix[0][6:10].animate.set_color(QUANTUM_GOLD),  # rho_11
            two_level_matrix[0][20:24].animate.set_color(QUANTUM_GOLD), # rho_22
            run_time=self.standard_run_time
        )
        
        self.wait(1.0)
        
        self.play(
            two_level_matrix[0][11:15].animate.set_color(COHERENCE_GREEN), # rho_12
            two_level_matrix[0][16:20].animate.set_color(COHERENCE_GREEN), # rho_21
            run_time=self.standard_run_time
        )
        
        self.wait(2.0)
        
        # Store elements for next section
        self.density_elements = VGroup(
            section_title, density_def, two_level_matrix, 
            matrix_visual, population_text, coherence_text
        )
    
    def create_density_matrix_visualization(self):
        """
        Create interactive density matrix visualization.
        
        Uses simple geometric shapes to avoid LaTeX bracket issues.
        """
        
        # Matrix elements as colored squares
        rho_11 = Rectangle(width=1.2, height=1.2, color=QUANTUM_GOLD, fill_opacity=0.7)
        rho_12 = Rectangle(width=1.2, height=1.2, color=COHERENCE_GREEN, fill_opacity=0.7)
        rho_21 = Rectangle(width=1.2, height=1.2, color=COHERENCE_GREEN, fill_opacity=0.7)
        rho_22 = Rectangle(width=1.2, height=1.2, color=QUANTUM_GOLD, fill_opacity=0.7)
        
        # Labels
        label_11 = MathTex(r'\rho_{11}', font_size=24, color=WHITE)
        label_12 = MathTex(r'\rho_{12}', font_size=24, color=WHITE)
        label_21 = MathTex(r'\rho_{21}', font_size=24, color=WHITE)
        label_22 = MathTex(r'\rho_{22}', font_size=24, color=WHITE)
        
        # Position elements in 2x2 grid
        matrix_elements = VGroup(
            VGroup(rho_11, label_11), VGroup(rho_12, label_12),
            VGroup(rho_21, label_21), VGroup(rho_22, label_22)
        )
        
        for element_group in matrix_elements:
            element_group[1].move_to(element_group[0].get_center())
        
        matrix_elements.arrange_in_grid(rows=2, cols=2, buff=0.4)  # Increased from 0.2 for better spacing
        
        # Simple bracket lines instead of LaTeX brackets
        left_bracket = VGroup(
            Line(start=[-0.2, 1.3, 0], end=[-0.4, 1.3, 0], color=WHITE, stroke_width=3),
            Line(start=[-0.4, 1.3, 0], end=[-0.4, -1.3, 0], color=WHITE, stroke_width=3),
            Line(start=[-0.4, -1.3, 0], end=[-0.2, -1.3, 0], color=WHITE, stroke_width=3)
        )
        
        right_bracket = VGroup(
            Line(start=[0.2, 1.3, 0], end=[0.4, 1.3, 0], color=WHITE, stroke_width=3),
            Line(start=[0.4, 1.3, 0], end=[0.4, -1.3, 0], color=WHITE, stroke_width=3),
            Line(start=[0.4, -1.3, 0], end=[0.2, -1.3, 0], color=WHITE, stroke_width=3)
        )
        
        # Position brackets relative to matrix
        left_bracket.next_to(matrix_elements, LEFT, buff=0.1)
        right_bracket.next_to(matrix_elements, RIGHT, buff=0.1)
        
        return VGroup(left_bracket, matrix_elements, right_bracket)
    
    def derive_master_equation(self):
        """
        Derive the quantum master equation step by step.
        
        Shows Liouville-von Neumann equation and Lindblad form.
        """
        
        # Clear previous elements
        self.play(FadeOut(self.density_elements, run_time=self.quick_run_time))
        
        # Section title
        section_title = Text(
            "Master Equation Derivation",
            font_size=40,
            color=DECOHERENCE_RED
        ).to_edge(UP, buff=0.5)
        
        self.play(Write(section_title, run_time=self.standard_run_time))
        
        # Step 1: Liouville-von Neumann equation
        liouville_eq = MathTex(
            r'\frac{d\hat{\rho}}{dt} = -\frac{i}{\hbar}[\hat{H}, \hat{\rho}]',
            font_size=36,
            color=WHITE
        ).shift(UP * 2.5)  # Increased from UP * 2
        
        self.play(Write(liouville_eq, run_time=self.standard_run_time))
        
        # Step 2: Add dissipation
        master_eq = MathTex(
            r'\frac{d\hat{\rho}}{dt} = -\frac{i}{\hbar}[\hat{H}, \hat{\rho}] + \mathcal{L}_{diss}[\hat{\rho}]',
            font_size=36,
            color=WHITE
        ).shift(UP * 0.8)  # Increased from UP * 0.5
        
        self.play(Write(master_eq, run_time=self.standard_run_time))
        
        # Step 3: Lindblad dissipator
        lindblad_eq = MathTex(
            r'\mathcal{L}_{diss}[\hat{\rho}] = \sum_k \gamma_k \left(\hat{L}_k\hat{\rho}\hat{L}_k^\dagger - \frac{1}{2}\{\hat{L}_k^\dagger\hat{L}_k, \hat{\rho}\}\right)',
            font_size=30,  # Reduced from 32 for better spacing
            color=DECOHERENCE_RED
        ).shift(DOWN * 1.5)  # Increased from DOWN * 1
        
        self.play(Write(lindblad_eq, run_time=self.slow_run_time))
        
        # Two-level system specific form
        two_level_title = Text(
            "Two-Level System:",
            font_size=28,
            color=QUANTUM_GOLD
        ).shift(DOWN * 2.2).to_edge(LEFT, buff=1)
        
        coherence_evolution = MathTex(
            r'\frac{d\rho_{12}}{dt} = -i\omega_{12}\rho_{12} - \Gamma_{12}\rho_{12}',
            font_size=32,
            color=COHERENCE_GREEN
        ).shift(DOWN * 2.8)
        
        self.play(
            Write(two_level_title, run_time=1.5),
            Write(coherence_evolution, run_time=self.standard_run_time)
        )
        
        self.wait(3.0)
        
        # Store master equation elements
        self.master_elements = VGroup(
            section_title, liouville_eq, master_eq, lindblad_eq,
            two_level_title, coherence_evolution
        )
    
    def develop_beat_signal(self):
        """
        Develop the beat signal from coherence dynamics.
        
        Shows how off-diagonal elements lead to observable beating.
        """
        
        # Clear previous elements
        self.play(FadeOut(self.master_elements, run_time=self.quick_run_time))
        
        # Section title
        section_title = Text(
            "Beat Signal Development",
            font_size=40,
            color=QUANTUM_GOLD
        ).to_edge(UP, buff=0.5)
        
        self.play(Write(section_title, run_time=self.standard_run_time))
        
        # Solution to coherence evolution
        coherence_solution = MathTex(
            r'\rho_{12}(t) = \rho_{12}(0) e^{-i\omega_{12}t - \Gamma_{12}t}',
            font_size=36,
            color=COHERENCE_GREEN
        ).shift(UP * 1.5)
        
        self.play(Write(coherence_solution, run_time=self.standard_run_time))
        
        # Beat signal intensity
        beat_intensity = MathTex(
            r'I(t) = \gamma_1 p_1 + \gamma_2 p_2 + 2\text{Re}[\gamma_{12}\rho_{12}(t)]',
            font_size=32,
            color=WHITE
        ).center()
        
        self.play(Write(beat_intensity, run_time=self.standard_run_time))
        
        # Expanded form
        expanded_form = MathTex(
            r'I(t) = I_0 + A e^{-\Gamma_{12}t} \cos(\omega_{12}t + \phi)',
            font_size=36,
            color=QUANTUM_GOLD
        ).shift(DOWN * 1.5)
        
        self.play(Write(expanded_form, run_time=self.standard_run_time))
        
        # Highlight key components
        oscillation_text = Text("Quantum beat oscillation", font_size=24, color=QUANTUM_GOLD)
        oscillation_text.next_to(expanded_form, DOWN, buff=0.5).shift(LEFT * 2)
        
        decay_text = Text("Decoherence envelope", font_size=24, color=DECOHERENCE_RED)  
        decay_text.next_to(expanded_form, DOWN, buff=0.5).shift(RIGHT * 2)
        
        self.play(
            Write(oscillation_text, run_time=1.5),
            Write(decay_text, run_time=1.5)
        )
        
        self.wait(2.0)
        
        # Store beat signal elements
        self.beat_elements = VGroup(
            section_title, coherence_solution, beat_intensity,
            expanded_form, oscillation_text, decay_text
        )
    
    def interpret_coherence_dynamics(self):
        """
        Interpret the physical meaning of coherence dynamics.
        
        Connects mathematical formalism to quantum mechanical intuition.
        """
        
        # Clear previous elements  
        self.play(FadeOut(self.beat_elements, run_time=self.quick_run_time))
        
        # Section title
        section_title = Text(
            "Physical Interpretation",
            font_size=40,
            color=COHERENCE_GREEN
        ).to_edge(UP, buff=0.5)
        
        self.play(Write(section_title, run_time=self.standard_run_time))
        
        # Key interpretations
        interpretations = VGroup(
            Text("• ρ₁₂(t) captures quantum superposition coherence", font_size=28, color=WHITE),
            Text("• Beat frequency ω₁₂ = (E₂ - E₁)/ℏ measures energy separation", font_size=28, color=WHITE),
            Text("• Decay rate Γ₁₂ quantifies environmental decoherence", font_size=28, color=DECOHERENCE_RED),
            Text("• Observable beats reveal quantum coherence directly", font_size=28, color=COHERENCE_GREEN)
        ).arrange(DOWN, buff=0.6, aligned_edge=LEFT).center()
        
        for interpretation in interpretations:
            self.play(Write(interpretation, run_time=1.8))
            self.wait(0.4)
        
        self.wait(2.0)
        
        # Store interpretation elements
        self.interpretation_elements = VGroup(section_title, interpretations)
    
    def conclude_scene(self):
        """
        Conclude scene with key insights and transition.
        
        Summarizes mathematical framework and transitions to next scene.
        """
        
        # Clear previous elements
        self.play(FadeOut(self.interpretation_elements, run_time=self.quick_run_time))
        
        # Key insight
        insight_title = Text(
            "Key Mathematical Insights",
            font_size=48,
            color=QUANTUM_GOLD
        ).to_edge(UP, buff=1.0)
        
        self.play(Write(insight_title, run_time=self.standard_run_time))
        
        # Main conclusions
        conclusions = VGroup(
            Text("Density matrices provide complete quantum description", font_size=32, color=WHITE),
            Text("Master equation governs coherence evolution", font_size=32, color=WHITE),
            Text("Beat signals emerge from off-diagonal dynamics", font_size=32, color=COHERENCE_GREEN)
        ).arrange(DOWN, buff=0.8, aligned_edge=LEFT).center()
        
        for conclusion in conclusions:
            self.play(Write(conclusion, run_time=self.standard_run_time))
            self.wait(0.5)
        
        self.wait(2.0)
        
        # Transition preview
        transition_text = Text(
            "Next: Isotropic vs Anisotropic Systems",
            font_size=28,
            color=QUANTUM_GOLD,
            style=ITALIC
        ).to_edge(DOWN, buff=1.0)
        
        self.play(Write(transition_text, run_time=self.standard_run_time))
        self.wait(2.0)
        
        # Final fade out
        conclusion_elements = VGroup(insight_title, conclusions, transition_text)
        self.play(FadeOut(conclusion_elements, run_time=self.standard_run_time))
        
        self.wait(1.0)  # Buffer for scene transition

# Test version for development
class TestMathematicalFormalism(MathematicalFormalism):
    """Test version for rapid development and debugging."""
    
    def construct(self):
        """Test construction - build incrementally."""
        # Test introduction first
        self.create_scene_introduction()
        # Test density matrix section
        self.introduce_density_matrix()
        # Test master equation section
        self.derive_master_equation()
        # Add more segments as they're developed
        # self.develop_beat_signal()
        # self.interpret_coherence_dynamics()
        # self.conclude_scene()

if __name__ == "__main__":
    # Test the scene independently
    print("Testing Scene 2: Mathematical Formalism")
    print("Run with: manim -pql scene_02_mathematical_formalism.py TestMathematicalFormalism")