"""
Scene 1: Opening and Classical vs Quantum Beating

This scene introduces the fundamental concepts of quantum beats by first
demonstrating classical wave beating, then revealing the quantum mechanical
origins of the phenomenon through energy eigenstate superposition.

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

class ClassicalVsQuantumIntro(Scene):
    """
    Opening scene introducing classical vs quantum beating phenomena.
    
    This scene establishes the fundamental distinction between classical
    wave interference and quantum mechanical energy eigenstate superposition
    that gives rise to quantum beats.
    """
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.camera.background_color = QUANTUM_BACKGROUND
        
        # Scene timing parameters
        self.title_duration = 8.0
        self.classical_demo_duration = 20.0
        self.quantum_intro_duration = 30.0
        self.comparison_duration = 25.0
        self.conclusion_duration = 17.0
        
        # Animation parameters
        self.wave_amplitude = 1.5
        self.wave_frequency_1 = 1.0
        self.wave_frequency_2 = 1.2
        self.beat_frequency = abs(self.wave_frequency_2 - self.wave_frequency_1)
        
    def construct(self):
        """Main scene construction with precise timing."""
        
        # Segment 1: Title and Introduction (0-8s)
        self.create_title_sequence()
        
        # Segment 2: Classical Wave Beating (8-28s) 
        self.demonstrate_classical_beating()
        
        # Segment 3: Quantum System Introduction (28-58s)
        self.introduce_quantum_system()
        
        # Segment 4: Quantum vs Classical Comparison (58-83s)
        self.compare_quantum_classical()
        
        # Segment 5: Conclusion and Transition (83-100s)
        self.conclude_scene()
    
    def create_title_sequence(self):
        """
        Create professional title sequence with particle effects.
        
        Synchronized with narration: "Quantum beats represent one of the most
        fundamental and fascinating phenomena in quantum mechanics..."
        """
        
        # Main title with quantum styling
        main_title = Text(
            "Isotropic Quantum Beats",
            font_size=72,
            color=QUANTUM_GOLD,
            weight=BOLD
        ).to_edge(UP, buff=1.5)
        
        # Subtitle with scientific context
        subtitle = Text(
            "A Comprehensive Visual Journey Through Quantum Interference Phenomena",
            font_size=32,
            color=WHITE
        ).next_to(main_title, DOWN, buff=0.5)
        
        # Create particle effect background
        particles = self.create_quantum_particles(50)
        
        # Animate title entrance
        self.play(
            AnimationGroup(
                *[FadeIn(particle, run_time=np.random.uniform(0.5, 2.0)) 
                  for particle in particles],
                lag_ratio=0.05
            ),
            run_time=2.0
        )
        
        self.play(
            Write(main_title, run_time=2.0),
            FadeIn(subtitle, run_time=2.0)
        )
        
        # Hold title with particle animation
        self.play(
            *[particle.animate.shift(
                0.1 * np.random.uniform(-1, 1, 3) + [0, 0, 0]
            ) for particle in particles],
            run_time=2.0
        )
        
        # Fade out title elements
        self.play(
            FadeOut(main_title, run_time=1.0),
            FadeOut(subtitle, run_time=1.0),
            *[FadeOut(particle, run_time=1.0) for particle in particles]
        )
        
        self.wait(1.0)  # Buffer for narration sync
    
    def create_quantum_particles(self, num_particles):
        """Create background particle effects for title sequence."""
        particles = VGroup()
        
        for _ in range(num_particles):
            # Random position on screen
            pos = np.array([
                np.random.uniform(-7, 7),
                np.random.uniform(-4, 4),
                0
            ])
            
            # Particle visualization
            particle = Dot(
                point=pos,
                radius=np.random.uniform(0.02, 0.08),
                color=np.random.choice([
                    QUANTUM_GOLD, COHERENCE_GREEN, WHITE, BLUE_E
                ]),
                fill_opacity=np.random.uniform(0.3, 0.8)
            )
            
            particles.add(particle)
        
        return particles
    
    def demonstrate_classical_beating(self):
        """
        Demonstrate classical wave beating with mathematical derivation.
        
        Shows two sinusoidal waves, their superposition, and the resulting
        beat pattern with envelope modulation.
        """
        
        # Section title
        section_title = Text(
            "Classical Wave Beating",
            font_size=48,
            color=COHERENCE_GREEN
        ).to_edge(UP, buff=0.5)
        
        self.play(Write(section_title, run_time=1.5))
        
        # Create coordinate system for wave visualization
        axes = Axes(
            x_range=[0, 8, 1],
            y_range=[-3, 3, 1],
            x_length=10,
            y_length=4,
            axis_config={
                "color": WHITE,
                "stroke_width": 2,
                "include_tip": False
            }
        ).shift(DOWN * 1)
        
        # Axis labels
        x_label = MathTex(r"t", font_size=36).next_to(axes.x_axis, RIGHT)
        y_label = MathTex(r"y(t)", font_size=36).next_to(axes.y_axis, UP)
        
        self.play(
            Create(axes, run_time=2.0),
            Write(x_label, run_time=1.0),
            Write(y_label, run_time=1.0)
        )
        
        # Define wave functions
        def wave1(t):
            return self.wave_amplitude * np.cos(2 * PI * self.wave_frequency_1 * t)
        
        def wave2(t):
            return self.wave_amplitude * np.cos(2 * PI * self.wave_frequency_2 * t)
        
        def superposition(t):
            return wave1(t) + wave2(t)
        
        def beat_envelope(t):
            return 2 * self.wave_amplitude * abs(np.cos(PI * self.beat_frequency * t))
        
        # Create wave graphs
        wave1_graph = axes.plot(
            wave1,
            color=BLUE,
            stroke_width=3
        )
        
        wave2_graph = axes.plot(
            wave2,
            color=RED,
            stroke_width=3
        )
        
        # Show individual waves first
        wave1_label = MathTex(
            rf"y_1(t) = A\cos(2\pi f_1 t)",
            font_size=28,
            color=BLUE
        ).to_corner(UL, buff=1)
        
        wave2_label = MathTex(
            rf"y_2(t) = A\cos(2\pi f_2 t)",
            font_size=28,
            color=RED
        ).next_to(wave1_label, DOWN, buff=0.3)
        
        self.play(
            Create(wave1_graph, run_time=2.0),
            Write(wave1_label, run_time=1.5)
        )
        
        self.play(
            Create(wave2_graph, run_time=2.0),
            Write(wave2_label, run_time=1.5)
        )
        
        self.wait(1.0)
        
        # Show superposition
        superposition_graph = axes.plot(
            superposition,
            color=QUANTUM_GOLD,
            stroke_width=4
        )
        
        superposition_label = MathTex(
            rf"y(t) = y_1(t) + y_2(t)",
            font_size=28,
            color=QUANTUM_GOLD
        ).next_to(wave2_label, DOWN, buff=0.3)
        
        # Mathematical derivation of beat pattern
        beat_derivation = VGroup(
            MathTex(
                rf"y(t) = A[\cos(2\pi f_1 t) + \cos(2\pi f_2 t)]",
                font_size=24
            ),
            MathTex(
                rf"= 2A\cos\left(2\pi\frac{{f_1-f_2}}{{2}}t\right)\cos\left(2\pi\frac{{f_1+f_2}}{{2}}t\right)",
                font_size=24
            ),
            MathTex(
                rf"\Omega_{{beat}} = |f_2 - f_1|",
                font_size=28,
                color=QUANTUM_GOLD
            )
        ).arrange(DOWN, buff=0.2).to_corner(UR, buff=0.5)
        
        self.play(
            Create(superposition_graph, run_time=2.5),
            Write(superposition_label, run_time=1.5)
        )
        
        # Show beat envelope
        envelope_upper = axes.plot(
            beat_envelope,
            color=WHITE,
            stroke_width=2,
            stroke_opacity=0.8
        )
        
        envelope_lower = axes.plot(
            lambda t: -beat_envelope(t),
            color=WHITE,
            stroke_width=2,
            stroke_opacity=0.8
        )
        
        self.play(
            Create(envelope_upper, run_time=2.0),
            Create(envelope_lower, run_time=2.0),
            Write(beat_derivation[0], run_time=2.0)
        )
        
        self.play(
            Write(beat_derivation[1], run_time=2.5),
            Write(beat_derivation[2], run_time=1.5)
        )
        
        self.wait(2.0)
        
        # Clear classical demonstration
        classical_elements = VGroup(
            section_title, axes, x_label, y_label,
            wave1_graph, wave2_graph, superposition_graph,
            envelope_upper, envelope_lower,
            wave1_label, wave2_label, superposition_label,
            beat_derivation
        )
        
        self.play(FadeOut(classical_elements, run_time=2.0))
    
    def introduce_quantum_system(self):
        """
        Introduce quantum mechanical energy eigenstate system.
        
        Shows energy level diagram, quantum superposition states,
        and the fundamental quantum beat frequency formula.
        """
        
        # Section title
        section_title = Text(
            "Quantum Mechanical Origin",
            font_size=48,
            color=QUANTUM_GOLD
        ).to_edge(UP, buff=0.5)
        
        self.play(Write(section_title, run_time=1.5))
        
        # Energy level diagram - simplified version
        level_0 = Line(start=[-5, -1.5, 0], end=[-3, -1.5, 0], color=WHITE, stroke_width=4)
        level_1 = Line(start=[-5, 0, 0], end=[-3, 0, 0], color=WHITE, stroke_width=4)
        level_2 = Line(start=[-5, 1.5, 0], end=[-3, 1.5, 0], color=WHITE, stroke_width=4)
        
        label_0 = MathTex(r'|0\rangle', font_size=32).next_to(level_0, LEFT, buff=0.3)
        label_1 = MathTex(r'|1\rangle', font_size=32).next_to(level_1, LEFT, buff=0.3)
        label_2 = MathTex(r'|2\rangle', font_size=32).next_to(level_2, LEFT, buff=0.3)
        
        energy_levels = VGroup(level_0, level_1, level_2, label_0, label_1, label_2)
        
        self.play(Create(energy_levels, run_time=3.0))
        
        # Energy eigenvalue equation
        eigenvalue_eq = MathTex(
            r'\hat{H}|n\rangle = E_n|n\rangle',
            font_size=36,
            color=WHITE
        ).next_to(energy_levels, RIGHT, buff=1.5).shift(UP * 1.5)
        
        self.play(Write(eigenvalue_eq, run_time=2.0))
        
        # Quantum superposition state
        superposition_eq = MathTex(
            r'|\psi\rangle = c_1 |1\rangle + c_2 |2\rangle',
            font_size=36,
            color=WHITE
        ).next_to(eigenvalue_eq, DOWN, buff=1.0)
        
        self.play(Write(superposition_eq, run_time=2.5))
        
        # Time evolution of superposition
        time_evolution_eq = MathTex(
            r'|\psi(t)\rangle = c_1 e^{-iE_1 t/\hbar}|1\rangle + c_2 e^{-iE_2 t/\hbar}|2\rangle',
            font_size=32,
            color=COHERENCE_GREEN
        ).next_to(superposition_eq, DOWN, buff=0.8)
        
        self.play(Write(time_evolution_eq, run_time=3.0))
        
        # Highlight the oscillatory terms
        self.play(
            time_evolution_eq.animate.set_color_by_tex("e^{-iE_1 t/\\hbar}", QUANTUM_GOLD),
            time_evolution_eq.animate.set_color_by_tex("e^{-iE_2 t/\\hbar}", QUANTUM_GOLD),
            run_time=2.0
        )
        
        # Quantum beat frequency derivation
        beat_freq_title = Text(
            "Quantum Beat Frequency",
            font_size=32,
            color=WHITE
        ).next_to(time_evolution_eq, DOWN, buff=1.0)
        
        beat_freq_eq = MathTex(
            r'\Delta\omega = \frac{E_2 - E_1}{\hbar}',
            font_size=40,
            color=QUANTUM_GOLD
        ).next_to(beat_freq_title, DOWN, buff=0.5)
        
        self.play(
            Write(beat_freq_title, run_time=1.5),
            Write(beat_freq_eq, run_time=2.0)
        )
        
        # Add transition arrows showing energy difference
        # TODO: Fix QuantumEnergyLevels.add_transition_arrow - commenting out temporarily  
        # transition_arrow = QuantumEnergyLevels.add_transition_arrow(
        #     from_level=2,
        #     to_level=1,
        #     energy_levels=energy_levels,
        #     transition_type='emission',
        #     label=r'\\Delta\\omega = \\frac{E_2 - E_1}{\\hbar}'
        # )
        # 
        # self.play(Create(transition_arrow, run_time=2.0))
        
        # Temporary placeholder arrow
        simple_arrow = Arrow(
            start=[-3.5, 0.5, 0], 
            end=[-3.5, -0.5, 0], 
            color=QUANTUM_GOLD,
            stroke_width=3
        )
        arrow_label = MathTex(r'\Delta E = E_2 - E_1', font_size=24, color=QUANTUM_GOLD)
        arrow_label.next_to(simple_arrow, RIGHT, buff=0.2)
        
        transition_group = VGroup(simple_arrow, arrow_label)
        self.play(Create(transition_group, run_time=2.0))
        
        # Emphasize the fundamental difference
        emphasis_text = Text(
            "Energy eigenstate coherence ≠ Classical wave interference",
            font_size=28,
            color=DECOHERENCE_RED,
            weight=BOLD
        ).to_edge(DOWN, buff=1.0)
        
        self.play(Write(emphasis_text, run_time=2.5))
        
        self.wait(3.0)
        
        # Store quantum elements for next section
        self.quantum_elements = VGroup(
            section_title, energy_levels, eigenvalue_eq,
            superposition_eq, time_evolution_eq,
            beat_freq_title, beat_freq_eq, transition_group,
            emphasis_text
        )
    
    def compare_quantum_classical(self):
        """
        Side-by-side comparison of classical and quantum beating.
        
        Shows the fundamental differences in mechanism, mathematics,
        and physical interpretation.
        """
        
        # Clear previous elements
        self.play(FadeOut(self.quantum_elements, run_time=2.0))
        
        # Comparison title
        comparison_title = Text(
            "Classical vs Quantum Beating",
            font_size=48,
            color=WHITE
        ).to_edge(UP, buff=0.5)
        
        self.play(Write(comparison_title, run_time=1.5))
        
        # Create comparison table
        comparison_table = self.create_comparison_table()
        comparison_table.shift(DOWN * 0.5)
        
        self.play(Create(comparison_table, run_time=4.0))
        
        # Add visual demonstrations
        classical_viz = self.create_classical_visualization().shift(LEFT * 3 + DOWN * 2)
        quantum_viz = self.create_quantum_visualization().shift(RIGHT * 3 + DOWN * 2)
        
        self.play(
            Create(classical_viz, run_time=3.0),
            Create(quantum_viz, run_time=3.0)
        )
        
        # Highlight key differences
        key_difference = Text(
            "Quantum beats reveal coherence between energy eigenstates",
            font_size=32,
            color=QUANTUM_GOLD,
            weight=BOLD
        ).to_edge(DOWN, buff=0.5)
        
        self.play(Write(key_difference, run_time=3.0))
        
        self.wait(4.0)
        
        # Store comparison elements
        self.comparison_elements = VGroup(
            comparison_title, comparison_table,
            classical_viz, quantum_viz, key_difference
        )
    
    def create_comparison_table(self):
        """Create visual comparison table between classical and quantum."""
        
        # Table headers
        classical_header = Text("Classical Beating", font_size=32, color=BLUE)
        quantum_header = Text("Quantum Beating", font_size=32, color=QUANTUM_GOLD)
        
        headers = VGroup(classical_header, quantum_header).arrange(RIGHT, buff=4.0)
        
        # Table rows
        rows = [
            ("Wave superposition", "Energy eigenstate superposition"),
            ("Amplitude modulation", "Coherence oscillation"),
            ("ω₂ - ω₁", "(E₂ - E₁)/ℏ"),
            ("Intensity variation", "Population dynamics"),
            ("Classical interference", "Quantum coherence")
        ]
        
        table_rows = VGroup()
        
        for classical_text, quantum_text in rows:
            classical_cell = Text(classical_text, font_size=24, color=WHITE)
            quantum_cell = Text(quantum_text, font_size=24, color=WHITE)
            
            row = VGroup(classical_cell, quantum_cell).arrange(RIGHT, buff=4.0)
            table_rows.add(row)
        
        table_rows.arrange(DOWN, buff=0.4)
        
        # Combine headers and rows
        full_table = VGroup(headers, table_rows).arrange(DOWN, buff=0.8)
        
        # Add separator line
        separator = Line(
            start=[-3, 0, 0],
            end=[3, 0, 0],
            color=WHITE,
            stroke_width=2
        ).next_to(headers, DOWN, buff=0.4)
        
        return VGroup(full_table, separator)
    
    def create_classical_visualization(self):
        """Create simplified classical wave visualization."""
        
        # Small axes for classical demo
        axes = Axes(
            x_range=[0, 4, 1],
            y_range=[-1, 1, 0.5],
            x_length=3,
            y_length=1.5,
            axis_config={"stroke_width": 1, "color": GRAY}
        )
        
        # Simple beat pattern
        beat_pattern = axes.plot(
            lambda t: np.cos(8*t) * np.cos(t),
            color=BLUE,
            stroke_width=2
        )
        
        classical_label = Text("Wave Amplitude", font_size=16, color=BLUE)
        classical_label.next_to(axes, DOWN, buff=0.2)
        
        return VGroup(axes, beat_pattern, classical_label)
    
    def create_quantum_visualization(self):
        """Create simplified quantum coherence visualization."""
        
        # Energy level representation
        level1 = Line(start=[-1, -0.5, 0], end=[1, -0.5, 0], color=WHITE, stroke_width=3)
        level2 = Line(start=[-1, 0.5, 0], end=[1, 0.5, 0], color=WHITE, stroke_width=3)
        
        # Coherence visualization (oscillating connection)
        coherence_line = DashedLine(
            start=[0, -0.5, 0],
            end=[0, 0.5, 0],
            color=QUANTUM_GOLD,
            stroke_width=2
        )
        
        # Labels
        level1_label = MathTex("|1\\rangle", font_size=20).next_to(level1, LEFT)
        level2_label = MathTex("|2\\rangle", font_size=20).next_to(level2, LEFT)
        coherence_label = MathTex("\\rho_{12}", font_size=16, color=QUANTUM_GOLD)
        coherence_label.next_to(coherence_line, RIGHT, buff=0.1)
        
        quantum_label = Text("Quantum Coherence", font_size=16, color=QUANTUM_GOLD)
        quantum_label.next_to(level1, DOWN, buff=0.5)
        
        return VGroup(
            level1, level2, coherence_line,
            level1_label, level2_label, coherence_label,
            quantum_label
        )
    
    def conclude_scene(self):
        """
        Conclude the scene with key insights and transition.
        
        Summarizes the fundamental distinction and prepares transition
        to mathematical formalism in Scene 2.
        """
        
        # Clear comparison elements
        self.play(FadeOut(self.comparison_elements, run_time=2.0))
        
        # Conclusion statement
        conclusion_title = Text(
            "Key Insight",
            font_size=48,
            color=QUANTUM_GOLD
        ).to_edge(UP, buff=1.0)
        
        self.play(Write(conclusion_title, run_time=1.5))
        
        # Main conclusion points
        conclusions = VGroup(
            Text(
                "• Quantum beats arise from coherent superposition of energy eigenstates",
                font_size=32,
                color=WHITE
            ),
            Text(
                "• Beat frequency directly measures energy level separations",
                font_size=32,
                color=WHITE
            ),
            Text(
                "• Phenomenon reveals quantum coherence with no classical analog",
                font_size=32,
                color=WHITE
            ),
            Text(
                "• Mathematical description requires density matrix formalism",
                font_size=32,
                color=COHERENCE_GREEN
            )
        ).arrange(DOWN, buff=0.5, aligned_edge=LEFT).center()
        
        # Animate conclusions sequentially
        for i, conclusion in enumerate(conclusions):
            self.play(Write(conclusion, run_time=2.0))
            if i < len(conclusions) - 1:
                self.wait(0.5)
        
        self.wait(2.0)
        
        # Transition preview
        transition_text = Text(
            "Next: Mathematical Formalism and Density Matrix Approach",
            font_size=28,
            color=QUANTUM_GOLD,
            style=ITALIC
        ).to_edge(DOWN, buff=1.0)
        
        self.play(Write(transition_text, run_time=2.0))
        
        self.wait(2.0)
        
        # Final fade out
        all_elements = VGroup(conclusion_title, conclusions, transition_text)
        self.play(FadeOut(all_elements, run_time=2.0))
        
        self.wait(1.0)  # Buffer for scene transition

# Testing scene independently
class TestClassicalVsQuantum(ClassicalVsQuantumIntro):
    """Test version of Scene 1 for development and debugging."""
    
    def construct(self):
        """Quick test construction for development."""
        self.create_title_sequence()
        # Add other test segments as needed

if __name__ == "__main__":
    # Test the scene independently
    print("Testing Scene 1: Classical vs Quantum Beating")
    print("Run with: manim -pql scene_01_classical_vs_quantum.py ClassicalVsQuantumIntro")