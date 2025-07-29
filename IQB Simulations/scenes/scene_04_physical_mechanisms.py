"""
Scene 4: Physical Mechanisms and Interference

This scene explores the fundamental quantum mechanical mechanisms behind quantum beats,
contrasting V-system and Λ-system configurations, and demonstrating the difference
between coherent superposition and incoherent mixing.

Duration: 2.5 minutes (150 seconds)
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

class PhysicalMechanisms(Scene):
    """
    Scene 4: Physical mechanisms behind quantum interference in beats.
    
    Demonstrates V-systems, Λ-systems, indistinguishable pathways, and the
    fundamental difference between coherent superposition and incoherent mixing.
    """
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.camera.background_color = QUANTUM_BACKGROUND
        
        # Scene timing parameters (2.5 min = 150 seconds total)
        self.intro_duration = 15.0            # Scene introduction
        self.pathway_interference_duration = 40.0  # Indistinguishable pathways
        self.system_comparison_duration = 35.0     # V-system vs Λ-system
        self.coherence_types_duration = 35.0       # Coherent vs incoherent
        self.interference_demo_duration = 15.0     # Quantum interference demo
        self.conclusion_duration = 10.0            # Conclusion and transition
        
        # Animation parameters
        self.standard_run_time = 2.0
        self.quick_run_time = 1.0
        self.slow_run_time = 3.0
        
    def construct(self):
        """Main scene construction with precise timing."""
        
        # Segment 1: Introduction (0-15s)
        self.create_scene_introduction()
        
        # Segment 2: Indistinguishable Pathways (15-55s)
        self.demonstrate_pathway_interference()
        
        # Segment 3: V-system vs Λ-system (55-90s)
        self.compare_system_configurations()
        
        # Segment 4: Coherent vs Incoherent (90-125s)
        self.contrast_coherence_types()
        
        # Segment 5: Quantum Interference Demo (125-140s)
        self.demonstrate_quantum_interference()
        
        # Segment 6: Conclusion and Transition (140-150s)
        self.conclude_scene()
    
    def create_scene_introduction(self):
        """
        Scene introduction highlighting quantum interference mechanisms.
        
        Sets up the fundamental question of how quantum beats arise mechanistically.
        """
        
        # Scene title
        scene_title = Text(
            "Physical Mechanisms and Interference",
            font_size=48,
            color=QUANTUM_GOLD
        ).to_edge(UP, buff=0.5)
        
        self.play(Write(scene_title, run_time=self.standard_run_time))
        
        # Central question
        central_question = Text(
            "How do quantum beats arise from indistinguishable pathways?",
            font_size=32,
            color=WHITE
        ).center()
        
        self.play(Write(central_question, run_time=self.standard_run_time))
        self.wait(2.0)
        
        # Key mechanism
        mechanism_text = Text(
            "Quantum interference between indistinguishable transition pathways",
            font_size=28,
            color=COHERENCE_GREEN
        ).shift(DOWN * 1.5)
        
        self.play(Write(mechanism_text, run_time=self.standard_run_time))
        self.wait(3.0)
        
        # Clear introduction elements
        intro_elements = VGroup(scene_title, central_question, mechanism_text)
        self.play(FadeOut(intro_elements, run_time=self.quick_run_time))
    
    def demonstrate_pathway_interference(self):
        """
        Demonstrate indistinguishable pathway interference.
        
        Shows how multiple quantum pathways lead to interference patterns.
        """
        
        # Section title
        section_title = Text(
            "Indistinguishable Quantum Pathways",
            font_size=40,
            color=COHERENCE_GREEN
        ).to_edge(UP, buff=0.5)
        
        self.play(Write(section_title, run_time=self.standard_run_time))
        
        # Create pathway diagram
        pathway_diagram = self.create_pathway_visualization()
        pathway_diagram.center()
        
        self.play(Create(pathway_diagram, run_time=self.slow_run_time))
        
        # Mathematical description - improved vertical spacing
        pathway_amplitude = MathTex(
            r'A_{total} = A_1 e^{i\phi_1} + A_2 e^{i\phi_2}',
            font_size=36,
            color=WHITE
        ).to_edge(DOWN, buff=1.8)  # Increased from 1.5
        
        self.play(Write(pathway_amplitude, run_time=self.standard_run_time))
        
        # Intensity with interference
        interference_intensity = MathTex(
            r'|A_{total}|^2 = |A_1|^2 + |A_2|^2 + 2|A_1||A_2|\cos(\phi_2 - \phi_1)',
            font_size=32,
            color=QUANTUM_GOLD
        ).next_to(pathway_amplitude, UP, buff=0.8)  # Increased from 0.5
        
        self.play(Write(interference_intensity, run_time=self.slow_run_time))
        
        # Highlight interference term
        self.play(
            interference_intensity[0][27:].animate.set_color(COHERENCE_GREEN),
            run_time=self.standard_run_time
        )
        
        self.wait(2.0)
        
        # Store pathway elements
        self.pathway_elements = VGroup(
            section_title, pathway_diagram, pathway_amplitude, interference_intensity
        )
    
    def create_pathway_visualization(self):
        """
        Create visualization of indistinguishable quantum pathways.
        
        Shows two interfering pathways with phase differences.
        """
        
        # Initial and final states
        initial_state = Circle(radius=0.3, color=WHITE, fill_opacity=0.8)
        initial_state.shift(LEFT * 4)
        initial_label = MathTex(r'|i\rangle', font_size=28).next_to(initial_state, DOWN)
        
        final_state = Circle(radius=0.3, color=WHITE, fill_opacity=0.8)
        final_state.shift(RIGHT * 4)
        final_label = MathTex(r'|f\rangle', font_size=28).next_to(final_state, DOWN)
        
        # Intermediate states
        intermediate_1 = Circle(radius=0.25, color=COHERENCE_GREEN, fill_opacity=0.7)
        intermediate_1.shift(UP * 1.5)
        inter_1_label = MathTex(r'|1\rangle', font_size=24).next_to(intermediate_1, UP)
        
        intermediate_2 = Circle(radius=0.25, color=DECOHERENCE_RED, fill_opacity=0.7)
        intermediate_2.shift(DOWN * 1.5)
        inter_2_label = MathTex(r'|2\rangle', font_size=24).next_to(intermediate_2, DOWN)
        
        # Pathways
        pathway_1a = Arrow(start=initial_state.get_center(), 
                          end=intermediate_1.get_center(), 
                          color=COHERENCE_GREEN, stroke_width=3)
        pathway_1b = Arrow(start=intermediate_1.get_center(), 
                          end=final_state.get_center(), 
                          color=COHERENCE_GREEN, stroke_width=3)
        
        pathway_2a = Arrow(start=initial_state.get_center(), 
                          end=intermediate_2.get_center(), 
                          color=DECOHERENCE_RED, stroke_width=3)
        pathway_2b = Arrow(start=intermediate_2.get_center(), 
                          end=final_state.get_center(), 
                          color=DECOHERENCE_RED, stroke_width=3)
        
        # Pathway labels - increased spacing for better readability
        path_1_label = MathTex(r'A_1 e^{i\phi_1}', font_size=20, color=COHERENCE_GREEN)
        path_1_label.next_to(intermediate_1, LEFT, buff=0.8)  # Increased from 0.5
        
        path_2_label = MathTex(r'A_2 e^{i\phi_2}', font_size=20, color=DECOHERENCE_RED)
        path_2_label.next_to(intermediate_2, LEFT, buff=0.8)  # Increased from 0.5
        
        return VGroup(
            initial_state, initial_label, final_state, final_label,
            intermediate_1, inter_1_label, intermediate_2, inter_2_label,
            pathway_1a, pathway_1b, pathway_2a, pathway_2b,
            path_1_label, path_2_label
        )
    
    def compare_system_configurations(self):
        """
        Compare V-system and Λ-system energy level configurations.
        
        Shows how different level structures lead to different beat patterns.
        """
        
        # Clear previous elements
        self.play(FadeOut(self.pathway_elements, run_time=self.quick_run_time))
        
        # Section title
        section_title = Text(
            "V-System vs Λ-System Configurations",
            font_size=40,
            color=QUANTUM_GOLD
        ).to_edge(UP, buff=0.5)
        
        self.play(Write(section_title, run_time=self.standard_run_time))
        
        # Create side-by-side comparison
        v_system = self.create_v_system()
        v_system.shift(LEFT * 3.5)
        
        lambda_system = self.create_lambda_system()
        lambda_system.shift(RIGHT * 3.5)
        
        # System labels
        v_label = Text("V-System", font_size=32, color=COHERENCE_GREEN)
        v_label.next_to(v_system, UP, buff=0.5)
        
        lambda_label = Text("Λ-System", font_size=32, color=DECOHERENCE_RED)
        lambda_label.next_to(lambda_system, UP, buff=0.5)
        
        self.play(
            Create(v_system, run_time=self.standard_run_time),
            Create(lambda_system, run_time=self.standard_run_time),
            Write(v_label, run_time=1.5),
            Write(lambda_label, run_time=1.5)
        )
        
        # Hamiltonians - improved spacing and positioning
        v_hamiltonian = MathTex(
            r'\hat{H}_V = \hbar\omega_0|0\rangle\langle 0| + \hbar\omega_1|1\rangle\langle 1| + \hbar\omega_2|2\rangle\langle 2|',
            font_size=22,  # Slightly reduced for better fit
            color=WHITE
        ).next_to(v_system, DOWN, buff=1.2)  # Increased spacing
        
        lambda_hamiltonian = MathTex(
            r'\hat{H}_\Lambda = \hbar\omega_1|1\rangle\langle 1| + \hbar\omega_2|2\rangle\langle 2| + \hbar\omega_0|0\rangle\langle 0|',
            font_size=22,  # Slightly reduced for better fit
            color=WHITE
        ).next_to(lambda_system, DOWN, buff=1.2)  # Increased spacing
        
        self.play(
            Write(v_hamiltonian, run_time=self.slow_run_time),
            Write(lambda_hamiltonian, run_time=self.slow_run_time)
        )
        
        self.wait(2.0)
        
        # Store system elements
        self.system_elements = VGroup(
            section_title, v_system, lambda_system, v_label, lambda_label,
            v_hamiltonian, lambda_hamiltonian
        )
    
    def create_v_system(self):
        """Create V-system energy level diagram."""
        
        # Energy levels - improved alignment and spacing
        level_0 = Line(start=[-1, -1.5, 0], end=[1, -1.5, 0], color=WHITE, stroke_width=4)
        level_1 = Line(start=[-1, 0.5, 0], end=[1, 0.5, 0], color=WHITE, stroke_width=4)
        level_2 = Line(start=[-1, 1.5, 0], end=[1, 1.5, 0], color=WHITE, stroke_width=4)
        
        # Labels - increased spacing for better alignment
        label_0 = MathTex(r'|0\rangle', font_size=28).next_to(level_0, LEFT, buff=0.4)  # Added explicit spacing
        label_1 = MathTex(r'|1\rangle', font_size=28).next_to(level_1, LEFT, buff=0.4)  # Added explicit spacing
        label_2 = MathTex(r'|2\rangle', font_size=28).next_to(level_2, LEFT, buff=0.4)  # Added explicit spacing
        
        # Transitions (V-shape)
        trans_01 = Arrow(start=[0.5, -1.3, 0], end=[0.5, 0.3, 0], 
                        color=COHERENCE_GREEN, stroke_width=3)
        trans_02 = Arrow(start=[-0.5, -1.3, 0], end=[-0.5, 1.3, 0], 
                        color=DECOHERENCE_RED, stroke_width=3)
        
        return VGroup(level_0, level_1, level_2, label_0, label_1, label_2, 
                     trans_01, trans_02)
    
    def create_lambda_system(self):
        """Create Λ-system energy level diagram."""
        
        # Energy levels - improved alignment and spacing
        level_0 = Line(start=[-1, 0, 0], end=[1, 0, 0], color=WHITE, stroke_width=4)
        level_1 = Line(start=[-1, -1.5, 0], end=[1, -1.5, 0], color=WHITE, stroke_width=4)
        level_2 = Line(start=[-1, 1.5, 0], end=[1, 1.5, 0], color=WHITE, stroke_width=4)
        
        # Labels - increased spacing for better alignment
        label_0 = MathTex(r'|0\rangle', font_size=28).next_to(level_0, LEFT, buff=0.4)  # Added explicit spacing
        label_1 = MathTex(r'|1\rangle', font_size=28).next_to(level_1, LEFT, buff=0.4)  # Added explicit spacing
        label_2 = MathTex(r'|2\rangle', font_size=28).next_to(level_2, LEFT, buff=0.4)  # Added explicit spacing
        
        # Transitions (Λ-shape)
        trans_10 = Arrow(start=[0.5, -1.3, 0], end=[0.5, -0.2, 0], 
                        color=COHERENCE_GREEN, stroke_width=3)
        trans_20 = Arrow(start=[-0.5, 1.3, 0], end=[-0.5, 0.2, 0], 
                        color=DECOHERENCE_RED, stroke_width=3)
        
        return VGroup(level_0, level_1, level_2, label_0, label_1, label_2, 
                     trans_10, trans_20)
    
    def contrast_coherence_types(self):
        """
        Contrast coherent superposition vs incoherent mixing.
        
        Shows the fundamental difference between quantum superposition and statistical mixtures.
        """
        
        # Clear previous elements
        self.play(FadeOut(self.system_elements, run_time=self.quick_run_time))
        
        # Section title
        section_title = Text(
            "Coherent vs Incoherent Superposition",
            font_size=40,
            color=COHERENCE_GREEN
        ).to_edge(UP, buff=0.5)
        
        self.play(Write(section_title, run_time=self.standard_run_time))
        
        # Coherent superposition
        coherent_title = Text("Coherent Superposition", font_size=32, color=COHERENCE_GREEN)
        coherent_title.shift(LEFT * 3.5 + UP * 1.5)
        
        coherent_state = MathTex(
            r'|\psi_{coherent}\rangle = \frac{1}{\sqrt{2}}(|1\rangle + |2\rangle)',
            font_size=28,
            color=WHITE
        ).next_to(coherent_title, DOWN, buff=0.5)
        
        # Incoherent mixture
        incoherent_title = Text("Incoherent Mixture", font_size=32, color=DECOHERENCE_RED)
        incoherent_title.shift(RIGHT * 3.5 + UP * 1.5)
        
        incoherent_state = MathTex(
            r'\hat{\rho}_{incoherent} = \frac{1}{2}|1\rangle\langle 1| + \frac{1}{2}|2\rangle\langle 2|',
            font_size=24,
            color=WHITE
        ).next_to(incoherent_title, DOWN, buff=0.5)
        
        self.play(
            Write(coherent_title, run_time=1.5),
            Write(coherent_state, run_time=self.standard_run_time),
            Write(incoherent_title, run_time=1.5),
            Write(incoherent_state, run_time=self.standard_run_time)
        )
        
        # Key differences
        coherent_properties = VGroup(
            Text("• Phase relationships preserved", font_size=20, color=WHITE),
            Text("• Interference possible", font_size=20, color=COHERENCE_GREEN),
            Text("• Quantum beats observable", font_size=20, color=QUANTUM_GOLD),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        coherent_properties.next_to(coherent_state, DOWN, buff=0.5)
        
        incoherent_properties = VGroup(
            Text("• No phase relationships", font_size=20, color=WHITE),
            Text("• No interference", font_size=20, color=DECOHERENCE_RED),
            Text("• No quantum beats", font_size=20, color=GRAY),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        incoherent_properties.next_to(incoherent_state, DOWN, buff=0.5)
        
        for prop in coherent_properties:
            self.play(Write(prop, run_time=1.2))
            self.wait(0.2)
        
        for prop in incoherent_properties:
            self.play(Write(prop, run_time=1.2))
            self.wait(0.2)
        
        # Contrast formula
        contrast_formula = MathTex(
            r'V = \frac{I_{max} - I_{min}}{I_{max} + I_{min}} = 2|\rho_{12}|',
            font_size=32,
            color=QUANTUM_GOLD
        ).to_edge(DOWN, buff=1.0)
        
        self.play(Write(contrast_formula, run_time=self.standard_run_time))
        
        self.wait(2.0)
        
        # Store coherence elements
        self.coherence_elements = VGroup(
            section_title, coherent_title, coherent_state, incoherent_title, incoherent_state,
            coherent_properties, incoherent_properties, contrast_formula
        )
    
    def demonstrate_quantum_interference(self):
        """
        Demonstrate quantum interference pattern formation.
        
        Shows how quantum coherence leads to observable interference patterns.
        """
        
        # Clear previous elements
        self.play(FadeOut(self.coherence_elements, run_time=self.quick_run_time))
        
        # Section title
        section_title = Text(
            "Quantum Interference Pattern",
            font_size=40,
            color=QUANTUM_GOLD
        ).to_edge(UP, buff=0.5)
        
        self.play(Write(section_title, run_time=self.standard_run_time))
        
        # Interference pattern visualization
        interference_pattern = self.create_interference_pattern()
        interference_pattern.center()
        
        self.play(Create(interference_pattern, run_time=self.slow_run_time))
        
        # Mathematical description
        quantum_interference = MathTex(
            r'I_{quantum} = \langle\hat{E}^-\hat{E}^+\rangle = \text{Tr}[\hat{\rho}\hat{E}^-\hat{E}^+]',
            font_size=32,
            color=WHITE
        ).to_edge(DOWN, buff=1.0)
        
        self.play(Write(quantum_interference, run_time=self.standard_run_time))
        
        self.wait(2.0)
        
        # Store interference elements
        self.interference_elements = VGroup(section_title, interference_pattern, quantum_interference)
    
    def create_interference_pattern(self):
        """Create visualization of quantum interference pattern."""
        
        # Create sinusoidal interference pattern
        axes = Axes(
            x_range=[0, 4*PI, PI],
            y_range=[-2, 2, 1],
            x_length=8,
            y_length=3,
            axis_config={"stroke_width": 2, "color": WHITE}
        )
        
        # Interference pattern function
        def interference_func(x):
            return 1.5 * np.cos(x) * np.exp(-0.1 * x)
        
        interference_curve = axes.plot(
            interference_func,
            color=QUANTUM_GOLD,
            stroke_width=4
        )
        
        # Beat envelope
        def envelope_func(x):
            return 1.5 * np.exp(-0.1 * x)
        
        envelope_upper = axes.plot(envelope_func, color=COHERENCE_GREEN, stroke_width=2)
        envelope_lower = axes.plot(lambda x: -envelope_func(x), color=COHERENCE_GREEN, stroke_width=2)
        
        # Labels
        x_label = Text("Time", font_size=24, color=WHITE).next_to(axes.x_axis, RIGHT)
        y_label = Text("Signal Intensity", font_size=24, color=WHITE).next_to(axes.y_axis, UP)
        
        return VGroup(axes, interference_curve, envelope_upper, envelope_lower, x_label, y_label)
    
    def conclude_scene(self):
        """
        Conclude scene with key insights and transition.
        
        Summarizes physical mechanisms and transitions to decoherence effects.
        """
        
        # Clear previous elements
        self.play(FadeOut(self.interference_elements, run_time=self.quick_run_time))
        
        # Key insight
        insight_title = Text(
            "Key Physical Insights",
            font_size=48,
            color=QUANTUM_GOLD
        ).to_edge(UP, buff=1.0)
        
        self.play(Write(insight_title, run_time=self.standard_run_time))
        
        # Main conclusions
        conclusions = VGroup(
            Text("Quantum beats arise from indistinguishable interference pathways", font_size=26, color=WHITE),
            Text("Coherent superposition enables observable quantum interference", font_size=26, color=COHERENCE_GREEN),
            Text("System configuration determines beat pattern characteristics", font_size=26, color=WHITE)
        ).arrange(DOWN, buff=0.8, aligned_edge=LEFT).center()
        
        for conclusion in conclusions:
            self.play(Write(conclusion, run_time=self.standard_run_time))
            self.wait(0.3)
        
        self.wait(1.5)
        
        # Transition preview
        transition_text = Text(
            "Next: Decoherence and Environmental Effects",
            font_size=28,
            color=QUANTUM_GOLD,
            style=ITALIC
        ).to_edge(DOWN, buff=1.0)
        
        self.play(Write(transition_text, run_time=self.standard_run_time))
        self.wait(1.5)
        
        # Final fade out
        conclusion_elements = VGroup(insight_title, conclusions, transition_text)
        self.play(FadeOut(conclusion_elements, run_time=self.standard_run_time))
        
        self.wait(0.5)  # Buffer for scene transition

# Test version for development
class TestPhysicalMechanisms(PhysicalMechanisms):
    """Test version for rapid development and debugging."""
    
    def construct(self):
        """Test construction - build incrementally."""
        # Test introduction first
        self.create_scene_introduction()
        # Test pathway interference
        self.demonstrate_pathway_interference()
        # Test system comparison
        self.compare_system_configurations()
        # Add more segments as they're developed
        # self.contrast_coherence_types()
        # self.demonstrate_quantum_interference()

if __name__ == "__main__":
    # Test the scene independently
    print("Testing Scene 4: Physical Mechanisms and Interference")
    print("Run with: manim -pql scene_04_physical_mechanisms.py TestPhysicalMechanisms")