"""
Scene 3: Isotropic vs Anisotropic Systems

This scene explores the fundamental distinction between isotropic quantum beats
in atomic systems and anisotropic beats in crystalline materials, demonstrating
the role of spherical tensor decomposition and angular averaging.

Duration: 3.0 minutes (180 seconds)
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

class IsotropicAnisotropic(Scene):
    """
    Scene 3: Isotropic vs Anisotropic quantum beats.
    
    Demonstrates the fundamental distinction between spherically symmetric
    atomic systems and anisotropic crystalline materials, with experimental
    comparisons between Ca atoms and ReS₂ crystals.
    """
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.camera.background_color = QUANTUM_BACKGROUND
        
        # Scene timing parameters (3.0 min = 180 seconds total)
        self.intro_duration = 20.0           # Scene introduction
        self.isotropy_definition_duration = 35.0  # Define isotropy concept
        self.spherical_tensor_duration = 40.0     # Spherical tensor formalism
        self.experimental_comparison_duration = 50.0  # Ca vs ReS₂ comparison
        self.angular_averaging_duration = 20.0    # Angular averaging effects
        self.conclusion_duration = 15.0          # Conclusion and transition
        
        # Animation parameters
        self.standard_run_time = 2.0
        self.quick_run_time = 1.0
        self.slow_run_time = 3.0
        
    def construct(self):
        """Main scene construction with precise timing."""
        
        # Segment 1: Introduction (0-20s)
        self.create_scene_introduction()
        
        # Segment 2: Isotropy Definition (20-55s)
        self.define_isotropy_concept()
        
        # Segment 3: Spherical Tensor Formalism (55-95s)
        self.introduce_spherical_tensors()
        
        # Segment 4: Experimental Comparison (95-145s)
        self.compare_experimental_systems()
        
        # Segment 5: Angular Averaging (145-165s)
        self.demonstrate_angular_averaging()
        
        # Segment 6: Conclusion and Transition (165-180s)
        self.conclude_scene()
    
    def create_scene_introduction(self):
        """
        Scene introduction highlighting isotropic vs anisotropic distinction.
        
        Sets up the fundamental question of directional dependence in quantum beats.
        """
        
        # Scene title
        scene_title = Text(
            "Isotropic vs Anisotropic Systems",
            font_size=48,
            color=QUANTUM_GOLD
        ).to_edge(UP, buff=0.5)
        
        self.play(Write(scene_title, run_time=self.standard_run_time))
        
        # Central question
        central_question = Text(
            "Do quantum beats depend on measurement direction?",
            font_size=36,
            color=WHITE
        ).center()
        
        self.play(Write(central_question, run_time=self.standard_run_time))
        self.wait(2.0)
        
        # Two contrasting answers
        isotropic_answer = Text(
            "Isotropic: Independent of direction",
            font_size=32,
            color=COHERENCE_GREEN
        ).shift(UP * 1.5)
        
        anisotropic_answer = Text(
            "Anisotropic: Direction-dependent",
            font_size=32,
            color=DECOHERENCE_RED
        ).shift(DOWN * 1.5)
        
        self.play(
            Transform(central_question, VGroup(isotropic_answer, anisotropic_answer)),
            run_time=self.standard_run_time
        )
        
        self.wait(3.0)
        
        # Clear introduction elements
        intro_elements = VGroup(scene_title, central_question)
        self.play(FadeOut(intro_elements, run_time=self.quick_run_time))
    
    def define_isotropy_concept(self):
        """
        Define the concept of isotropy in quantum systems.
        
        Introduces spherical symmetry and rotational invariance.
        """
        
        # Section title
        section_title = Text(
            "Isotropy: Spherical Symmetry",
            font_size=40,
            color=COHERENCE_GREEN
        ).to_edge(UP, buff=0.5)
        
        self.play(Write(section_title, run_time=self.standard_run_time))
        
        # Mathematical definition
        isotropy_definition = MathTex(
            r'\langle I(\theta,\phi) \rangle_{\text{orientations}} = \text{constant}',
            font_size=36,
            color=WHITE
        ).shift(UP * 1.5)
        
        self.play(Write(isotropy_definition, run_time=self.standard_run_time))
        
        # Visual representation - 3D sphere
        sphere_visualization = self.create_sphere_visualization()
        sphere_visualization.shift(DOWN * 0.5)
        
        self.play(Create(sphere_visualization, run_time=self.slow_run_time))
        
        # Rotation invariance
        rotation_text = Text(
            "Rotational Invariance → Spherical Averaging",
            font_size=28,
            color=QUANTUM_GOLD
        ).to_edge(DOWN, buff=1.0)
        
        self.play(Write(rotation_text, run_time=self.standard_run_time))
        
        # Demonstrate rotation
        self.play(
            Rotate(sphere_visualization, angle=PI, axis=UP, run_time=2.0),
            rate_func=smooth
        )
        
        self.wait(2.0)
        
        # Store isotropy elements
        self.isotropy_elements = VGroup(
            section_title, isotropy_definition, sphere_visualization, rotation_text
        )
    
    def create_sphere_visualization(self):
        """
        Create 3D sphere visualization for isotropy concept.
        
        Uses basic Manim 3D objects and coordinate arrows.
        """
        
        # Central sphere
        sphere = Sphere(radius=1.5, resolution=(20, 20))
        sphere.set_color(COHERENCE_GREEN)
        sphere.set_opacity(0.3)
        
        # Coordinate axes
        x_axis = Arrow3D(start=ORIGIN, end=[2, 0, 0], color=RED)
        y_axis = Arrow3D(start=ORIGIN, end=[0, 2, 0], color=GREEN)  
        z_axis = Arrow3D(start=ORIGIN, end=[0, 0, 2], color=BLUE)
        
        # Axis labels
        x_label = Text("x", font_size=24, color=RED).next_to([2, 0, 0], RIGHT)
        y_label = Text("y", font_size=24, color=GREEN).next_to([0, 2, 0], UP) 
        z_label = Text("z", font_size=24, color=BLUE).next_to([0, 0, 2], OUT)
        
        # Directional arrows on sphere
        directions = [
            Arrow3D(start=ORIGIN, end=[1.5, 0, 0], color=QUANTUM_GOLD),
            Arrow3D(start=ORIGIN, end=[0, 1.5, 0], color=QUANTUM_GOLD),
            Arrow3D(start=ORIGIN, end=[0, 0, 1.5], color=QUANTUM_GOLD),
            Arrow3D(start=ORIGIN, end=[1.06, 1.06, 0], color=QUANTUM_GOLD),
        ]
        
        return VGroup(
            sphere, x_axis, y_axis, z_axis,
            x_label, y_label, z_label, *directions
        )
    
    def introduce_spherical_tensors(self):
        """
        Introduce spherical tensor decomposition formalism.
        
        Shows how quantum operators decompose in spherical coordinates.
        """
        
        # Clear previous elements
        self.play(FadeOut(self.isotropy_elements, run_time=self.quick_run_time))
        
        # Section title
        section_title = Text(
            "Spherical Tensor Decomposition",
            font_size=40,
            color=QUANTUM_GOLD
        ).to_edge(UP, buff=0.5)
        
        self.play(Write(section_title, run_time=self.standard_run_time))
        
        # General tensor decomposition
        tensor_decomposition = MathTex(
            r'\hat{\rho} = \sum_{k,q} \rho_k^q \hat{T}_k^q',
            font_size=36,
            color=WHITE
        ).shift(UP * 1.5)
        
        self.play(Write(tensor_decomposition, run_time=self.standard_run_time))
        
        # Specific tensor ranks
        tensor_ranks = VGroup(
            MathTex(r'k=0: \text{ Scalar (population)}', font_size=28, color=WHITE),
            MathTex(r'k=1: \text{ Vector (orientation)}', font_size=28, color=COHERENCE_GREEN),
            MathTex(r'k=2: \text{ Tensor (alignment)}', font_size=28, color=DECOHERENCE_RED),
        ).arrange(DOWN, buff=0.5, aligned_edge=LEFT).center()
        
        for rank in tensor_ranks:
            self.play(Write(rank, run_time=1.5))
            self.wait(0.3)
        
        # Polarization tensor
        polarization_tensor = MathTex(
            r'P_{ij}^{(k)} = \sum_{m,m\prime} \rho_{m,m\prime} \langle J,m|T_{ij}^{(k)}|J,m\prime\rangle',
            font_size=32,
            color=QUANTUM_GOLD
        ).to_edge(DOWN, buff=1.0)
        
        self.play(Write(polarization_tensor, run_time=self.slow_run_time))
        
        self.wait(2.0)
        
        # Store tensor elements
        self.tensor_elements = VGroup(
            section_title, tensor_decomposition, tensor_ranks, polarization_tensor
        )
    
    def compare_experimental_systems(self):
        """
        Compare Ca atoms (isotropic) vs ReS₂ crystals (anisotropic).
        
        Shows experimental realizations and their different behaviors.
        """
        
        # Clear previous elements
        self.play(FadeOut(self.tensor_elements, run_time=self.quick_run_time))
        
        # Section title
        section_title = Text(
            "Experimental Systems Comparison",
            font_size=40,
            color=DECOHERENCE_RED
        ).to_edge(UP, buff=0.5)
        
        self.play(Write(section_title, run_time=self.standard_run_time))
        
        # Create side-by-side comparison
        ca_system = self.create_ca_atom_system()
        ca_system.shift(LEFT * 3.5)
        
        res2_system = self.create_res2_crystal_system()
        res2_system.shift(RIGHT * 3.5)
        
        # System labels
        ca_label = Text("Ca Atoms", font_size=32, color=COHERENCE_GREEN)
        ca_label.next_to(ca_system, UP, buff=0.5)
        
        res2_label = Text("ReS₂ Crystal", font_size=32, color=DECOHERENCE_RED)
        res2_label.next_to(res2_system, UP, buff=0.5)
        
        self.play(
            Create(ca_system, run_time=self.standard_run_time),
            Create(res2_system, run_time=self.standard_run_time),
            Write(ca_label, run_time=1.5),
            Write(res2_label, run_time=1.5)
        )
        
        # Key differences
        differences = VGroup(
            Text("Isotropic:", font_size=24, color=COHERENCE_GREEN),
            Text("• Spherical symmetry", font_size=20, color=WHITE),
            Text("• Angular averaging", font_size=20, color=WHITE),
            Text("• Independent of θ,φ", font_size=20, color=WHITE),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        differences.next_to(ca_system, DOWN, buff=0.5)
        
        anisotropic_differences = VGroup(
            Text("Anisotropic:", font_size=24, color=DECOHERENCE_RED),
            Text("• Crystal anisotropy", font_size=20, color=WHITE),
            Text("• Directional beats", font_size=20, color=WHITE),
            Text("• I(θ,φ) modulation", font_size=20, color=WHITE),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        anisotropic_differences.next_to(res2_system, DOWN, buff=0.5)
        
        for diff in differences:
            self.play(Write(diff, run_time=1.2))
            self.wait(0.2)
        
        for diff in anisotropic_differences:
            self.play(Write(diff, run_time=1.2))
            self.wait(0.2)
        
        self.wait(2.0)
        
        # Store comparison elements
        self.comparison_elements = VGroup(
            section_title, ca_system, res2_system, ca_label, res2_label,
            differences, anisotropic_differences
        )
    
    def create_ca_atom_system(self):
        """Create visualization of Ca atom system."""
        
        # Central atom
        atom_core = Circle(radius=0.3, color=COHERENCE_GREEN, fill_opacity=0.8)
        
        # Electron orbitals (spherical)
        orbital_1 = Circle(radius=0.6, color=COHERENCE_GREEN, fill_opacity=0.2)
        orbital_2 = Circle(radius=0.9, color=COHERENCE_GREEN, fill_opacity=0.1)
        
        # Spherical emission pattern
        emission_lines = VGroup(*[
            Line(start=ORIGIN, end=[0.9 * np.cos(i * PI/6), 0.9 * np.sin(i * PI/6), 0], 
                 color=QUANTUM_GOLD, stroke_width=2)
            for i in range(12)
        ])
        
        return VGroup(atom_core, orbital_1, orbital_2, emission_lines)
    
    def create_res2_crystal_system(self):
        """Create visualization of ReS₂ crystal system."""
        
        # Crystal lattice structure
        lattice_points = VGroup(*[
            Dot(point=[0.3*i, 0.3*j, 0], radius=0.05, color=DECOHERENCE_RED)
            for i in range(-2, 3) for j in range(-2, 3)
        ])
        
        # Anisotropic emission pattern
        emission_x = Arrow(start=ORIGIN, end=[1.2, 0, 0], color=QUANTUM_GOLD, stroke_width=4)
        emission_y = Arrow(start=ORIGIN, end=[0, 0.6, 0], color=QUANTUM_GOLD, stroke_width=2)
        
        # Crystal axes labels
        x_crystal = Text("a", font_size=16, color=WHITE).next_to(emission_x, RIGHT)
        y_crystal = Text("b", font_size=16, color=WHITE).next_to(emission_y, UP)
        
        return VGroup(lattice_points, emission_x, emission_y, x_crystal, y_crystal)
    
    def demonstrate_angular_averaging(self):
        """
        Demonstrate angular averaging effects in isotropic systems.
        
        Shows how directional measurements average to isotropy.
        """
        
        # Clear previous elements
        self.play(FadeOut(self.comparison_elements, run_time=self.quick_run_time))
        
        # Section title
        section_title = Text(
            "Angular Averaging in Isotropic Systems",
            font_size=40,
            color=COHERENCE_GREEN
        ).to_edge(UP, buff=0.5)
        
        self.play(Write(section_title, run_time=self.standard_run_time))
        
        # Angular averaging formula
        averaging_formula = MathTex(
            r'\langle I \rangle = \frac{1}{4\pi}\int I(\theta,\phi) d\Omega',
            font_size=36,
            color=WHITE
        ).shift(UP * 1.5)
        
        self.play(Write(averaging_formula, run_time=self.standard_run_time))
        
        # Angular dependence equation
        angular_dependence = MathTex(
            r'I(\theta,\phi) = I_0 [1 + \beta P_2(\cos\theta)]',
            font_size=32,
            color=QUANTUM_GOLD
        ).center()
        
        self.play(Write(angular_dependence, run_time=self.standard_run_time))
        
        # Result of averaging
        averaging_result = MathTex(
            r'\text{Isotropic result: } \langle I \rangle = I_0',
            font_size=32,
            color=COHERENCE_GREEN
        ).shift(DOWN * 1.5)
        
        self.play(Write(averaging_result, run_time=self.standard_run_time))
        
        self.wait(2.0)
        
        # Store averaging elements
        self.averaging_elements = VGroup(
            section_title, averaging_formula, angular_dependence, averaging_result
        )
    
    def conclude_scene(self):
        """
        Conclude scene with key insights and transition.
        
        Summarizes isotropic vs anisotropic distinction and transitions to next scene.
        """
        
        # Clear previous elements
        self.play(FadeOut(self.averaging_elements, run_time=self.quick_run_time))
        
        # Key insight
        insight_title = Text(
            "Key Physical Insights",
            font_size=48,
            color=QUANTUM_GOLD
        ).to_edge(UP, buff=1.0)
        
        self.play(Write(insight_title, run_time=self.standard_run_time))
        
        # Main conclusions
        conclusions = VGroup(
            Text("Isotropic systems: Universal quantum beat behavior", font_size=28, color=COHERENCE_GREEN),
            Text("Anisotropic systems: Direction-dependent beat patterns", font_size=28, color=DECOHERENCE_RED),
            Text("Spherical tensor formalism unifies both cases", font_size=28, color=WHITE)
        ).arrange(DOWN, buff=0.8, aligned_edge=LEFT).center()
        
        for conclusion in conclusions:
            self.play(Write(conclusion, run_time=self.standard_run_time))
            self.wait(0.5)
        
        self.wait(2.0)
        
        # Transition preview
        transition_text = Text(
            "Next: Physical Mechanisms and Interference",
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
class TestIsotropicAnisotropic(IsotropicAnisotropic):
    """Test version for rapid development and debugging."""
    
    def construct(self):
        """Test construction - build incrementally."""
        # Test introduction first
        self.create_scene_introduction()
        # Test isotropy definition
        self.define_isotropy_concept()
        # Add more segments as they're developed
        # self.introduce_spherical_tensors()
        # self.compare_experimental_systems()

if __name__ == "__main__":
    # Test the scene independently
    print("Testing Scene 3: Isotropic vs Anisotropic Systems")
    print("Run with: manim -pql scene_03_isotropic_anisotropic.py TestIsotropicAnisotropic")