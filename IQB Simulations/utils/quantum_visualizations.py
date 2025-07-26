"""
Advanced quantum physics visualization utilities for Manim animations.

This module provides sophisticated 3D visualizations for quantum states, 
Bloch spheres, energy levels, density matrices, and quantum processes
specifically designed for the quantum beats animation.
"""

from manim import *
import numpy as np
from typing import List, Tuple, Optional, Union, Dict
from .color_schemes import QuantumColorScheme, QUANTUM_GOLD, COHERENCE_GREEN, DECOHERENCE_RED
from .latex_formatting import QuantumLatexFormatter

class QuantumBlochSphere(ThreeDScene):
    """
    Advanced Bloch sphere visualization with quantum state evolution.
    
    Provides methods for creating, animating, and manipulating Bloch sphere
    representations of quantum states with proper 3D rendering and state tracking.
    """
    
    def __init__(self, radius: float = 2.0, **kwargs):
        super().__init__(**kwargs)
        self.radius = radius
        self.sphere = None
        self.axes = None
        self.state_vector = None
        self.trajectory_points = []
        
    def create_bloch_sphere(self, opacity: float = 0.3) -> VGroup:
        """
        Create the basic Bloch sphere structure.
        
        Parameters
        ----------
        opacity : float
            Sphere opacity (0-1)
            
        Returns
        -------
        VGroup
            Complete Bloch sphere visualization
        """
        colors = QuantumColorScheme.get_bloch_sphere_colors()
        
        # Create the sphere
        self.sphere = Sphere(
            radius=self.radius,
            resolution=(20, 20),
            u_range=[0, TAU],
            v_range=[0, PI]
        )
        self.sphere.set_color(colors['sphere'])
        self.sphere.set_opacity(opacity)
        
        # Create coordinate axes
        x_axis = Arrow3D(
            start=[-self.radius-0.5, 0, 0],
            end=[self.radius+0.5, 0, 0],
            color=colors['x_axis'],
            thickness=0.02
        )
        y_axis = Arrow3D(
            start=[0, -self.radius-0.5, 0],
            end=[0, self.radius+0.5, 0],
            color=colors['y_axis'],
            thickness=0.02
        )
        z_axis = Arrow3D(
            start=[0, 0, -self.radius-0.5],
            end=[0, 0, self.radius+0.5],
            color=colors['z_axis'],
            thickness=0.02
        )
        
        # Add axis labels
        x_label = MathTex(r"|+\rangle_x", font_size=24).next_to(x_axis.get_end(), RIGHT)
        y_label = MathTex(r"|+\rangle_y", font_size=24).next_to(y_axis.get_end(), UP)
        z_label = MathTex(r"|0\rangle", font_size=24).next_to(z_axis.get_end(), UP)
        
        # Create equatorial circle
        equator = Circle(
            radius=self.radius,
            color=colors['equator'],
            stroke_width=2
        ).rotate(PI/2, axis=RIGHT)
        
        # Add meridians
        meridian1 = Circle(
            radius=self.radius,
            color=colors['equator'],
            stroke_width=1,
            stroke_opacity=0.5
        ).rotate(PI/2, axis=UP)
        
        meridian2 = Circle(
            radius=self.radius,
            color=colors['equator'], 
            stroke_width=1,
            stroke_opacity=0.5
        ).rotate(PI/2, axis=OUT)
        
        self.axes = VGroup(x_axis, y_axis, z_axis, x_label, y_label, z_label)
        
        return VGroup(
            self.sphere, self.axes, equator, meridian1, meridian2
        )
    
    def add_quantum_state(self, theta: float, phi: float, 
                         color: str = None, label: str = None) -> VGroup:
        """
        Add a quantum state vector to the Bloch sphere.
        
        Parameters
        ----------
        theta : float
            Polar angle (0 to π)
        phi : float
            Azimuthal angle (0 to 2π)
        color : str, optional
            Color of the state vector
        label : str, optional
            LaTeX label for the state
            
        Returns
        -------
        VGroup
            State vector and label
        """
        if color is None:
            color = QuantumColorScheme.get_bloch_sphere_colors()['state_vector']
        
        # Convert spherical to Cartesian coordinates
        x = self.radius * np.sin(theta) * np.cos(phi)
        y = self.radius * np.sin(theta) * np.sin(phi)
        z = self.radius * np.cos(theta)
        
        # Create state vector
        self.state_vector = Arrow3D(
            start=[0, 0, 0],
            end=[x, y, z],
            color=color,
            thickness=0.04
        )
        
        # Add state point
        state_point = Sphere(
            radius=0.1,
            color=color
        ).move_to([x, y, z])
        
        state_group = VGroup(self.state_vector, state_point)
        
        # Add label if specified
        if label:
            state_label = MathTex(label, font_size=24, color=color)
            state_label.next_to([x, y, z], direction=normalize([x, y, z]))
            state_group.add(state_label)
        
        return state_group
    
    def animate_state_evolution(self, 
                               theta_func, phi_func, 
                               t_range: Tuple[float, float] = (0, 4),
                               color: str = None) -> Animation:
        """
        Create animation of quantum state evolution on Bloch sphere.
        
        Parameters
        ----------
        theta_func : callable
            Function theta(t) for polar angle evolution
        phi_func : callable
            Function phi(t) for azimuthal angle evolution  
        t_range : tuple
            Time range (start, end)
        color : str, optional
            Color of the trajectory
            
        Returns
        -------
        Animation
            State evolution animation
        """
        if color is None:
            color = COHERENCE_GREEN
        
        def state_updater(mob, dt):
            # Get current time (this is simplified - in practice would track time)
            current_t = self.renderer.time if hasattr(self, 'renderer') else 0
            
            theta = theta_func(current_t)
            phi = phi_func(current_t)
            
            x = self.radius * np.sin(theta) * np.cos(phi)
            y = self.radius * np.sin(theta) * np.sin(phi)
            z = self.radius * np.cos(theta)
            
            # Update state vector
            new_end = [x, y, z]
            mob[0].put_start_and_end_on([0, 0, 0], new_end)
            mob[1].move_to(new_end)
            
            # Add to trajectory
            self.trajectory_points.append(new_end.copy())
        
        return UpdateFromFunc(
            VGroup(self.state_vector, self.state_vector),
            state_updater
        )
    
    def create_coherence_visualization(self, 
                                     coherence_value: float,
                                     phase: float = 0) -> VGroup:
        """
        Visualize quantum coherence on the Bloch sphere.
        
        Parameters
        ----------
        coherence_value : float
            Coherence magnitude (0-1)
        phase : float
            Coherence phase
            
        Returns
        -------
        VGroup
            Coherence visualization elements
        """
        color = QuantumColorScheme.get_coherence_color(coherence_value)
        
        # Create coherence ring around equator
        coherence_ring = Circle(
            radius=self.radius * coherence_value,
            color=color,
            stroke_width=4
        ).rotate(PI/2, axis=RIGHT)
        
        # Add phase indicator
        phase_point = Dot(
            point=[
                self.radius * coherence_value * np.cos(phase),
                self.radius * coherence_value * np.sin(phase),
                0
            ],
            color=color,
            radius=0.08
        )
        
        # Add coherence label
        coherence_label = MathTex(
            rf"|\rho_{{12}}| = {coherence_value:.2f}",
            font_size=20,
            color=color
        ).next_to(coherence_ring, DOWN)
        
        return VGroup(coherence_ring, phase_point, coherence_label)

class QuantumEnergyLevels:
    """
    Visualization utilities for quantum energy level diagrams.
    
    Provides methods for creating energy level diagrams, transitions,
    population dynamics, and coherence evolution.
    """
    
    @staticmethod
    def create_energy_level_diagram(energies: List[float],
                                   labels: List[str] = None,
                                   width: float = 4.0,
                                   height: float = 6.0) -> VGroup:
        """
        Create energy level diagram with specified energies.
        
        Parameters
        ----------
        energies : list
            Energy values for each level
        labels : list, optional
            Labels for each energy level
        width : float
            Width of energy levels
        height : float
            Total height of diagram
            
        Returns
        -------
        VGroup
            Complete energy level diagram
        """
        # Normalize energies to fit in height
        min_energy = min(energies)
        max_energy = max(energies)
        energy_range = max_energy - min_energy
        
        if energy_range == 0:
            energy_range = 1  # Avoid division by zero
        
        levels = VGroup()
        
        for i, energy in enumerate(energies):
            # Calculate vertical position
            y_pos = (energy - min_energy) / energy_range * height - height/2
            
            # Create energy level line
            level_color = QuantumColorScheme.get_energy_level_color(i)
            level_line = Line(
                start=[-width/2, y_pos, 0],
                end=[width/2, y_pos, 0],
                color=level_color,
                stroke_width=4
            )
            
            # Add energy label
            energy_label = MathTex(
                rf"E_{i} = {energy:.2f}\hbar\omega",
                font_size=20,
                color=level_color
            ).next_to(level_line, RIGHT, buff=0.2)
            
            # Add state label if provided
            if labels and i < len(labels):
                state_label = MathTex(
                    rf"|{labels[i]}\rangle",
                    font_size=24,
                    color=level_color
                ).next_to(level_line, LEFT, buff=0.2)
                levels.add(VGroup(level_line, energy_label, state_label))
            else:
                levels.add(VGroup(level_line, energy_label))
        
        return levels
    
    @staticmethod
    def add_transition_arrow(from_level: int, to_level: int,
                            energy_levels: VGroup,
                            transition_type: str = 'emission',
                            label: str = None) -> VGroup:
        """
        Add transition arrow between energy levels.
        
        Parameters
        ----------
        from_level : int
            Index of initial level
        to_level : int
            Index of final level
        energy_levels : VGroup
            Energy level diagram
        transition_type : str
            Type of transition ('emission', 'absorption', 'coherent')
        label : str, optional
            Transition label
            
        Returns
        -------
        VGroup
            Transition arrow and label
        """
        colors = {
            'emission': COHERENCE_GREEN,
            'absorption': DECOHERENCE_RED,
            'coherent': QUANTUM_GOLD
        }
        
        color = colors.get(transition_type, WHITE)
        
        # Get level positions
        from_pos = energy_levels[from_level][0].get_center()
        to_pos = energy_levels[to_level][0].get_center()
        
        # Create transition arrow
        if transition_type == 'emission':
            arrow = Arrow(
                start=from_pos + [0.2, 0, 0],
                end=to_pos + [0.2, 0, 0],
                color=color,
                stroke_width=3,
                tip_length=0.2
            )
        else:  # absorption or coherent
            arrow = Arrow(
                start=to_pos + [-0.2, 0, 0],
                end=from_pos + [-0.2, 0, 0],
                color=color,
                stroke_width=3,
                tip_length=0.2
            )
        
        transition_group = VGroup(arrow)
        
        # Add label if specified
        if label:
            arrow_label = MathTex(label, font_size=18, color=color)
            arrow_label.next_to(arrow, RIGHT, buff=0.1)
            transition_group.add(arrow_label)
        
        return transition_group
    
    @staticmethod
    def create_population_bars(populations: List[float],
                              energy_levels: VGroup,
                              max_width: float = 1.0) -> VGroup:
        """
        Create population bars showing level populations.
        
        Parameters
        ----------
        populations : list
            Population values for each level
        energy_levels : VGroup
            Energy level diagram
        max_width : float
            Maximum width of population bars
            
        Returns
        -------
        VGroup
            Population bar visualization
        """
        max_pop = max(populations) if populations else 1
        bars = VGroup()
        
        for i, pop in enumerate(populations):
            if i < len(energy_levels):
                level_pos = energy_levels[i][0].get_center()
                bar_width = (pop / max_pop) * max_width
                
                bar = Rectangle(
                    width=bar_width,
                    height=0.2,
                    color=QuantumColorScheme.get_energy_level_color(i),
                    fill_opacity=0.7
                )
                bar.next_to(level_pos, LEFT, buff=0.5)
                
                # Add population value label
                pop_label = DecimalNumber(
                    pop,
                    num_decimal_places=3,
                    font_size=16
                ).next_to(bar, LEFT, buff=0.1)
                
                bars.add(VGroup(bar, pop_label))
        
        return bars

class QuantumDensityMatrix:
    """
    Visualization utilities for quantum density matrices.
    
    Provides methods for creating matrix visualizations, coherence evolution,
    and population dynamics representations.
    """
    
    @staticmethod
    def create_density_matrix_grid(matrix_elements: np.ndarray,
                                  show_phase: bool = True,
                                  cell_size: float = 1.0) -> VGroup:
        """
        Create visual representation of density matrix.
        
        Parameters
        ----------
        matrix_elements : ndarray
            Complex matrix elements
        show_phase : bool
            Whether to show phase information
        cell_size : float
            Size of each matrix cell
            
        Returns
        -------
        VGroup
            Density matrix visualization
        """
        n_dim = matrix_elements.shape[0]
        colors = QuantumColorScheme.get_density_matrix_colors()
        
        matrix_group = VGroup()
        
        for i in range(n_dim):
            for j in range(n_dim):
                element = matrix_elements[i, j]
                
                # Cell position
                x_pos = (j - n_dim/2 + 0.5) * cell_size
                y_pos = -(i - n_dim/2 + 0.5) * cell_size
                
                # Choose color based on matrix element type
                if i == j:  # Diagonal (population)
                    color = colors['diagonal']
                    alpha = abs(element)  # Population determines opacity
                else:  # Off-diagonal (coherence)
                    color = colors['off_diagonal']
                    alpha = abs(element) * 2  # Coherence visualization
                
                # Create matrix cell
                cell = Square(
                    side_length=cell_size * 0.9,
                    color=color,
                    fill_opacity=alpha
                ).move_to([x_pos, y_pos, 0])
                
                # Add element value
                if abs(element) > 1e-6:  # Only show non-zero elements
                    if show_phase and not np.isreal(element):
                        # Show magnitude and phase
                        magnitude = abs(element)
                        phase = np.angle(element)
                        value_text = MathTex(
                            rf"{magnitude:.2f}e^{{i{phase:.2f}}}",
                            font_size=12,
                            color=WHITE
                        )
                    else:
                        # Show real value only
                        value_text = MathTex(
                            rf"{abs(element):.3f}",
                            font_size=14,
                            color=WHITE
                        )
                    
                    value_text.move_to(cell.get_center())
                    matrix_group.add(VGroup(cell, value_text))
                else:
                    matrix_group.add(cell)
        
        # Add matrix brackets
        left_bracket = MathTex(r"\begin{pmatrix}", font_size=36)
        right_bracket = MathTex(r"\end{pmatrix}", font_size=36)
        
        left_bracket.next_to(matrix_group, LEFT, buff=0.1)
        right_bracket.next_to(matrix_group, RIGHT, buff=0.1)
        
        return VGroup(matrix_group, left_bracket, right_bracket)
    
    @staticmethod
    def animate_coherence_decay(initial_matrix: np.ndarray,
                               decay_rates: Dict[Tuple[int, int], float],
                               oscillation_frequencies: Dict[Tuple[int, int], float] = None,
                               duration: float = 5.0) -> Animation:
        """
        Create animation of density matrix coherence decay.
        
        Parameters
        ----------
        initial_matrix : ndarray
            Initial density matrix
        decay_rates : dict
            Decay rates for each matrix element
        oscillation_frequencies : dict, optional
            Oscillation frequencies for coherences
        duration : float
            Animation duration
            
        Returns
        -------
        Animation
            Coherence decay animation
        """
        if oscillation_frequencies is None:
            oscillation_frequencies = {}
        
        def matrix_updater(mob, t):
            # Calculate time-evolved matrix elements
            evolved_matrix = initial_matrix.copy()
            
            for (i, j), gamma in decay_rates.items():
                omega = oscillation_frequencies.get((i, j), 0)
                
                # Apply decay and oscillation
                decay_factor = np.exp(-gamma * t)
                oscillation_factor = np.exp(-1j * omega * t)
                
                evolved_matrix[i, j] *= decay_factor * oscillation_factor
                if i != j:  # Ensure hermiticity
                    evolved_matrix[j, i] = np.conj(evolved_matrix[i, j])
            
            # Update visualization (this is simplified)
            # In practice, would update the matrix grid elements
            pass
        
        return UpdateFromAlphaFunc(
            self.create_density_matrix_grid(initial_matrix),
            matrix_updater,
            run_time=duration
        )

class QuantumInterference:
    """
    Visualization utilities for quantum interference phenomena.
    
    Provides methods for wave superposition, beat patterns,
    and interference visualization.
    """
    
    @staticmethod
    def create_wave_superposition(wave_functions: List[callable],
                                 colors: List[str] = None,
                                 x_range: Tuple[float, float] = (-5, 5),
                                 show_envelope: bool = True) -> VGroup:
        """
        Create visualization of wave superposition.
        
        Parameters
        ----------
        wave_functions : list
            List of wave functions to superpose
        colors : list, optional
            Colors for each wave
        x_range : tuple
            X-axis range for plotting
        show_envelope : bool
            Whether to show beat envelope
            
        Returns
        -------
        VGroup
            Wave superposition visualization
        """
        if colors is None:
            colors = [RED, BLUE, GREEN, YELLOW][:len(wave_functions)]
        
        axes = Axes(
            x_range=[x_range[0], x_range[1], 1],
            y_range=[-3, 3, 1],
            tips=False
        )
        
        waves_group = VGroup()
        
        # Plot individual waves
        for i, (wave_func, color) in enumerate(zip(wave_functions, colors)):
            wave_graph = axes.plot(
                wave_func,
                color=color,
                stroke_width=2
            )
            waves_group.add(wave_graph)
        
        # Create superposition
        def superposition(x):
            return sum(wave_func(x) for wave_func in wave_functions)
        
        superposition_graph = axes.plot(
            superposition,
            color=QUANTUM_GOLD,
            stroke_width=4
        )
        
        visualization = VGroup(axes, waves_group, superposition_graph)
        
        # Add envelope if requested
        if show_envelope and len(wave_functions) == 2:
            def envelope_upper(x):
                return abs(superposition(x))
            
            def envelope_lower(x):
                return -abs(superposition(x))
            
            envelope_upper_graph = axes.plot(
                envelope_upper,
                color=WHITE,
                stroke_width=2,
                stroke_opacity=0.7
            )
            
            envelope_lower_graph = axes.plot(
                envelope_lower,
                color=WHITE,
                stroke_width=2,
                stroke_opacity=0.7
            )
            
            visualization.add(envelope_upper_graph, envelope_lower_graph)
        
        return visualization
    
    @staticmethod
    def create_beat_pattern(freq1: float, freq2: float,
                           amplitude1: float = 1.0, amplitude2: float = 1.0,
                           phase1: float = 0, phase2: float = 0,
                           time_range: Tuple[float, float] = (0, 10)) -> VGroup:
        """
        Create quantum beat pattern visualization.
        
        Parameters
        ----------
        freq1, freq2 : float
            Frequencies of the two components
        amplitude1, amplitude2 : float
            Amplitudes of the components
        phase1, phase2 : float
            Initial phases
        time_range : tuple
            Time range for visualization
            
        Returns
        -------
        VGroup
            Beat pattern visualization
        """
        axes = Axes(
            x_range=[time_range[0], time_range[1], 1],
            y_range=[-3, 3, 1],
            axis_config={"include_tip": False}
        )
        
        # Individual components
        def wave1(t):
            return amplitude1 * np.cos(2 * PI * freq1 * t + phase1)
        
        def wave2(t):
            return amplitude2 * np.cos(2 * PI * freq2 * t + phase2)
        
        # Beat pattern
        def beat_signal(t):
            return wave1(t) + wave2(t)
        
        # Beat envelope
        beat_freq = abs(freq2 - freq1) / 2
        def beat_envelope(t):
            return 2 * np.sqrt(amplitude1 * amplitude2) * abs(np.cos(2 * PI * beat_freq * t))
        
        # Create graphs
        wave1_graph = axes.plot(wave1, color=BLUE, stroke_width=1, stroke_opacity=0.6)
        wave2_graph = axes.plot(wave2, color=RED, stroke_width=1, stroke_opacity=0.6)
        beat_graph = axes.plot(beat_signal, color=QUANTUM_GOLD, stroke_width=3)
        envelope_graph = axes.plot(beat_envelope, color=WHITE, stroke_width=2, stroke_opacity=0.8)
        
        # Add beat frequency label
        beat_freq_label = MathTex(
            rf"\Delta f = {beat_freq:.2f} \text{{ Hz}}",
            font_size=24,
            color=WHITE
        ).next_to(axes, UP)
        
        return VGroup(
            axes, wave1_graph, wave2_graph, 
            beat_graph, envelope_graph, beat_freq_label
        )

def test_quantum_visualizations():
    """Test function to verify quantum visualizations work correctly."""
    print("Testing quantum visualization utilities...")
    
    # Test Bloch sphere creation
    bloch = QuantumBlochSphere()
    sphere = bloch.create_bloch_sphere()
    print("✓ Bloch sphere creation successful")
    
    # Test energy levels
    energies = [0, 1, 2, 3]
    labels = ['0', '1', '2', '3']
    levels = QuantumEnergyLevels.create_energy_level_diagram(energies, labels)
    print("✓ Energy level diagram creation successful")
    
    # Test density matrix
    test_matrix = np.array([
        [0.5, 0.3+0.2j],
        [0.3-0.2j, 0.5]
    ])
    matrix_viz = QuantumDensityMatrix.create_density_matrix_grid(test_matrix)
    print("✓ Density matrix visualization successful")
    
    # Test wave interference
    wave1 = lambda x: np.cos(x)
    wave2 = lambda x: np.cos(1.1 * x)
    interference = QuantumInterference.create_wave_superposition([wave1, wave2])
    print("✓ Wave interference visualization successful")
    
    print("All quantum visualization tests passed!")

if __name__ == "__main__":
    test_quantum_visualizations()