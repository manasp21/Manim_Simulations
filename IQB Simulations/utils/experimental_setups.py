"""
Experimental setup visualization utilities for quantum beats experiments.

This module provides 3D models and animations of laboratory equipment, optical
setups, and detection systems commonly used in quantum coherence experiments.
"""

from manim import *
import numpy as np
from typing import List, Tuple, Optional, Dict, Union
from .color_schemes import (
    LASER_COLOR, DETECTOR_COLOR, BEAM_SPLITTER_COLOR, MIRROR_COLOR, 
    SAMPLE_COLOR, QUANTUM_GOLD, COHERENCE_GREEN
)
from .latex_formatting import QuantumLatexFormatter

class OpticalComponent:
    """
    Base class for optical components in quantum experiments.
    
    Provides common functionality for creating, positioning, and animating
    optical elements like lasers, mirrors, detectors, etc.
    """
    
    def __init__(self, position: np.ndarray = ORIGIN, rotation: float = 0):
        self.position = position
        self.rotation = rotation
        self.mobject = None
        self.label = None
    
    def create_component(self) -> VGroup:
        """Create the visual representation of the component."""
        raise NotImplementedError("Subclasses must implement create_component")
    
    def add_label(self, text: str, direction: np.ndarray = UP, **kwargs) -> MathTex:
        """Add a label to the component."""
        default_kwargs = {'font_size': 18, 'color': WHITE}
        default_kwargs.update(kwargs)
        
        self.label = MathTex(text, **default_kwargs)
        self.label.next_to(self.mobject, direction, buff=0.2)
        return self.label
    
    def get_visualization(self) -> VGroup:
        """Get complete visualization including component and label."""
        if self.mobject is None:
            self.mobject = self.create_component()
        
        viz = VGroup(self.mobject)
        if self.label is not None:
            viz.add(self.label)
        
        return viz

class LaserSource(OpticalComponent):
    """
    Laser source visualization with beam and specifications.
    
    Creates realistic laser representation with adjustable parameters
    for different laser types (CW, pulsed, femtosecond).
    """
    
    def __init__(self, laser_type: str = 'cw', wavelength: float = 632.8, 
                 power: float = 1.0, **kwargs):
        super().__init__(**kwargs)
        self.laser_type = laser_type
        self.wavelength = wavelength  # nm
        self.power = power  # mW
    
    def create_component(self) -> VGroup:
        """Create laser source visualization."""
        # Laser body
        laser_body = Rectangle(
            width=1.5, height=0.8,
            color=LASER_COLOR,
            fill_opacity=0.8
        ).move_to(self.position)
        
        # Laser aperture
        aperture = Circle(
            radius=0.15,
            color=WHITE,
            fill_opacity=1.0
        ).move_to(laser_body.get_right() + [-0.1, 0, 0])
        
        # Beam visualization
        beam_points = [
            laser_body.get_right(),
            laser_body.get_right() + [3, 0, 0]
        ]
        
        beam = Line(
            start=beam_points[0],
            end=beam_points[1],
            color=LASER_COLOR,
            stroke_width=8,
            stroke_opacity=0.6
        )
        
        # Add beam divergence for realism
        beam_cone = Polygon(
            beam_points[0],
            beam_points[1] + [0, 0.1, 0],
            beam_points[1] + [0, -0.1, 0],
            color=LASER_COLOR,
            fill_opacity=0.2,
            stroke_width=0
        )
        
        laser_group = VGroup(laser_body, aperture, beam, beam_cone)
        laser_group.rotate(self.rotation)
        
        return laser_group
    
    def create_pulsed_beam_animation(self, duration: float = 2.0) -> AnimationGroup:
        """Create animation showing pulsed laser operation."""
        if self.mobject is None:
            self.mobject = self.create_component()
        
        beam = self.mobject[2]  # Beam is the third element
        
        def pulse_updater(mob, t):
            # Create pulse pattern
            pulse_freq = 2.0  # Hz
            intensity = (np.sin(2 * PI * pulse_freq * t) + 1) / 2
            mob.set_opacity(0.2 + 0.6 * intensity)
        
        return UpdateFromAlphaFunc(beam, pulse_updater, run_time=duration)
    
    def get_specifications(self) -> VGroup:
        """Get laser specifications text."""
        specs = VGroup()
        
        # Wavelength
        wavelength_text = MathTex(
            rf"\lambda = {self.wavelength:.1f} \text{{ nm}}",
            font_size=16, color=WHITE
        )
        
        # Power
        power_text = MathTex(
            rf"P = {self.power:.1f} \text{{ mW}}",
            font_size=16, color=WHITE
        )
        
        # Type
        type_text = Text(
            f"Type: {self.laser_type.upper()}",
            font_size=16, color=WHITE
        )
        
        specs.add(wavelength_text, power_text, type_text)
        specs.arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        
        return specs

class PhotoDetector(OpticalComponent):
    """
    Photodetector visualization with quantum efficiency and response.
    
    Creates various detector types including PMTs, avalanche photodiodes,
    and CCD cameras with appropriate specifications.
    """
    
    def __init__(self, detector_type: str = 'pmt', 
                 quantum_efficiency: float = 0.3,
                 dark_count_rate: float = 100, **kwargs):
        super().__init__(**kwargs)
        self.detector_type = detector_type
        self.quantum_efficiency = quantum_efficiency
        self.dark_count_rate = dark_count_rate  # Hz
    
    def create_component(self) -> VGroup:
        """Create photodetector visualization."""
        if self.detector_type == 'pmt':
            # PMT tube
            detector_body = Circle(
                radius=0.6,
                color=DETECTOR_COLOR,
                fill_opacity=0.7
            ).move_to(self.position)
            
            # PMT window
            window = Circle(
                radius=0.4,
                color=BLUE_E,
                fill_opacity=0.3
            ).move_to(self.position)
            
            # PMT base
            base = Rectangle(
                width=0.8, height=0.3,
                color=GRAY,
                fill_opacity=0.8
            ).next_to(detector_body, DOWN, buff=0)
            
        elif self.detector_type == 'apd':
            # Avalanche photodiode
            detector_body = Square(
                side_length=0.8,
                color=DETECTOR_COLOR,
                fill_opacity=0.7
            ).move_to(self.position)
            
            window = Square(
                side_length=0.4,
                color=BLUE_E,
                fill_opacity=0.3
            ).move_to(self.position)
            
            base = Rectangle(
                width=1.0, height=0.2,
                color=GRAY,
                fill_opacity=0.8
            ).next_to(detector_body, DOWN, buff=0)
            
        elif self.detector_type == 'ccd':
            # CCD camera
            detector_body = Rectangle(
                width=1.2, height=0.8,
                color=DETECTOR_COLOR,
                fill_opacity=0.7
            ).move_to(self.position)
            
            window = Rectangle(
                width=0.6, height=0.4,
                color=BLUE_E,
                fill_opacity=0.3
            ).move_to(self.position)
            
            base = Rectangle(
                width=1.2, height=0.3,
                color=GRAY,
                fill_opacity=0.8
            ).next_to(detector_body, DOWN, buff=0)
        
        else:
            # Generic detector
            detector_body = Circle(
                radius=0.5,
                color=DETECTOR_COLOR,
                fill_opacity=0.7
            ).move_to(self.position)
            window = detector_body
            base = Rectangle(width=0.6, height=0.2, color=GRAY, fill_opacity=0.8)
        
        detector_group = VGroup(detector_body, window, base)
        detector_group.rotate(self.rotation)
        
        return detector_group
    
    def create_detection_animation(self, photon_positions: List[np.ndarray],
                                  detection_probability: float = 0.8) -> AnimationGroup:
        """Create animation showing photon detection events."""
        animations = []
        
        for pos in photon_positions:
            # Photon approach
            photon = Dot(color=YELLOW, radius=0.05).move_to(pos)
            
            if np.random.random() < detection_probability:
                # Successful detection
                approach = photon.animate.move_to(self.position)
                flash = Flash(self.position, color=WHITE, flash_radius=0.5)
                
                animations.extend([approach, flash])
            else:
                # Missed detection
                approach = photon.animate.move_to(self.position)
                fade = FadeOut(photon)
                
                animations.extend([approach, fade])
        
        return AnimationGroup(*animations, lag_ratio=0.3)

class BeamSplitter(OpticalComponent):
    """
    Beam splitter visualization with reflection and transmission paths.
    
    Models various beam splitter types including cube beam splitters,
    pellicle beam splitters, and polarizing beam splitters.
    """
    
    def __init__(self, split_ratio: Tuple[float, float] = (0.5, 0.5),
                 polarizing: bool = False, **kwargs):
        super().__init__(**kwargs)
        self.split_ratio = split_ratio  # (reflection, transmission)
        self.polarizing = polarizing
    
    def create_component(self) -> VGroup:
        """Create beam splitter visualization."""
        # Main body (cube or pellicle)
        if self.polarizing:
            bs_body = Square(
                side_length=0.8,
                color=BEAM_SPLITTER_COLOR,
                fill_opacity=0.6
            ).move_to(self.position)
            
            # Polarization indicator
            pol_indicator = MathTex(r"PBS", font_size=12, color=WHITE)
            pol_indicator.move_to(bs_body.get_center())
            
        else:
            bs_body = Square(
                side_length=0.8,
                color=BEAM_SPLITTER_COLOR,
                fill_opacity=0.4
            ).move_to(self.position)
            pol_indicator = VGroup()  # Empty group
        
        # Diagonal splitting line
        diagonal = Line(
            start=bs_body.get_corner(DOWN + LEFT),
            end=bs_body.get_corner(UP + RIGHT),
            color=WHITE,
            stroke_width=2
        )
        
        bs_group = VGroup(bs_body, diagonal, pol_indicator)
        bs_group.rotate(self.rotation)
        
        return bs_group
    
    def split_beam(self, input_beam_start: np.ndarray, 
                   input_beam_end: np.ndarray) -> Tuple[VGroup, VGroup]:
        """
        Create reflected and transmitted beam paths.
        
        Parameters
        ----------
        input_beam_start, input_beam_end : ndarray
            Start and end points of input beam
            
        Returns
        -------
        tuple
            (reflected_beam, transmitted_beam) as VGroup objects
        """
        # Calculate beam directions
        input_direction = normalize(input_beam_end - input_beam_start)
        
        # Reflected beam (90° rotation)
        reflected_direction = np.array([-input_direction[1], input_direction[0], 0])
        reflected_start = self.position
        reflected_end = reflected_start + 2 * reflected_direction
        
        reflected_beam = Line(
            start=reflected_start,
            end=reflected_end,
            color=LASER_COLOR,
            stroke_width=6,
            stroke_opacity=self.split_ratio[0]
        )
        
        # Transmitted beam (continues straight)
        transmitted_start = self.position
        transmitted_end = transmitted_start + 2 * input_direction
        
        transmitted_beam = Line(
            start=transmitted_start,
            end=transmitted_end,
            color=LASER_COLOR,
            stroke_width=6,
            stroke_opacity=self.split_ratio[1]
        )
        
        # Add power labels
        reflected_label = MathTex(
            rf"{self.split_ratio[0]*100:.0f}\%",
            font_size=14, color=WHITE
        ).next_to(reflected_beam.get_center(), UP, buff=0.1)
        
        transmitted_label = MathTex(
            rf"{self.split_ratio[1]*100:.0f}\%",
            font_size=14, color=WHITE
        ).next_to(transmitted_beam.get_center(), UP, buff=0.1)
        
        reflected_group = VGroup(reflected_beam, reflected_label)
        transmitted_group = VGroup(transmitted_beam, transmitted_label)
        
        return reflected_group, transmitted_group

class MirrorOptical(OpticalComponent):
    """
    Optical mirror visualization with reflection path calculation.
    
    Models different mirror types including flat mirrors, curved mirrors,
    and dichroic mirrors with wavelength-dependent properties.
    """
    
    def __init__(self, mirror_type: str = 'flat', curvature: float = 0, 
                 reflectivity: float = 0.99, **kwargs):
        super().__init__(**kwargs)
        self.mirror_type = mirror_type
        self.curvature = curvature
        self.reflectivity = reflectivity
    
    def create_component(self) -> VGroup:
        """Create mirror visualization."""
        if self.mirror_type == 'flat':
            mirror_surface = Line(
                start=[-0.6, 0, 0],
                end=[0.6, 0, 0],
                color=MIRROR_COLOR,
                stroke_width=8
            ).move_to(self.position)
            
            # Mirror backing
            backing = Rectangle(
                width=1.2, height=0.2,
                color=GRAY,
                fill_opacity=0.8
            ).next_to(mirror_surface, DOWN, buff=0.05)
            
        elif self.mirror_type == 'curved':
            # Curved mirror surface
            if self.curvature > 0:  # Concave
                mirror_surface = Arc(
                    radius=1/abs(self.curvature),
                    angle=PI/3,
                    color=MIRROR_COLOR,
                    stroke_width=8
                ).move_to(self.position)
            else:  # Convex
                mirror_surface = Arc(
                    radius=1/abs(self.curvature),
                    angle=-PI/3,
                    color=MIRROR_COLOR,
                    stroke_width=8
                ).move_to(self.position)
            
            backing = Arc(
                radius=1/abs(self.curvature) + 0.1,
                angle=PI/3 if self.curvature > 0 else -PI/3,
                color=GRAY,
                stroke_width=4
            ).move_to(self.position)
            
        else:  # dichroic or specialized
            mirror_surface = Line(
                start=[-0.6, 0, 0],
                end=[0.6, 0, 0],
                color=PURPLE,  # Different color for dichroic
                stroke_width=8
            ).move_to(self.position)
            
            backing = Rectangle(
                width=1.2, height=0.2,
                color=GRAY,
                fill_opacity=0.8
            ).next_to(mirror_surface, DOWN, buff=0.05)
        
        mirror_group = VGroup(mirror_surface, backing)
        mirror_group.rotate(self.rotation)
        
        return mirror_group
    
    def reflect_beam(self, incident_beam_start: np.ndarray,
                    incident_beam_end: np.ndarray) -> VGroup:
        """
        Calculate and create reflected beam path.
        
        Parameters
        ----------
        incident_beam_start, incident_beam_end : ndarray
            Incident beam path
            
        Returns
        -------
        VGroup
            Reflected beam visualization
        """
        # Calculate incident direction
        incident_direction = normalize(incident_beam_end - incident_beam_start)
        
        # Mirror normal (assuming vertical mirror for simplicity)
        if self.mirror_type == 'flat':
            normal = np.array([0, 1, 0])
        else:
            # For curved mirrors, use surface normal at intersection point
            normal = np.array([0, 1, 0])  # Simplified
        
        # Calculate reflected direction using law of reflection
        reflected_direction = incident_direction - 2 * np.dot(incident_direction, normal) * normal
        
        # Create reflected beam
        reflected_start = self.position
        reflected_end = reflected_start + 2 * reflected_direction
        
        reflected_beam = Line(
            start=reflected_start,
            end=reflected_end,
            color=LASER_COLOR,
            stroke_width=6,
            stroke_opacity=self.reflectivity
        )
        
        return VGroup(reflected_beam)

class AtomicSample(OpticalComponent):
    """
    Atomic sample visualization with energy levels and population dynamics.
    
    Models various atomic systems including vapor cells, ion traps,
    and ultracold atomic ensembles with quantum state visualization.
    """
    
    def __init__(self, sample_type: str = 'vapor_cell',
                 atom_species: str = 'Rb87', 
                 temperature: float = 300, **kwargs):
        super().__init__(**kwargs)
        self.sample_type = sample_type
        self.atom_species = atom_species
        self.temperature = temperature  # Kelvin
    
    def create_component(self) -> VGroup:
        """Create atomic sample visualization."""
        if self.sample_type == 'vapor_cell':
            # Vapor cell container
            cell_body = Rectangle(
                width=2.0, height=1.0,
                color=SAMPLE_COLOR,
                fill_opacity=0.3,
                stroke_width=2
            ).move_to(self.position)
            
            # Atomic vapor inside
            atoms = VGroup()
            for _ in range(20):
                atom_pos = self.position + np.random.uniform(-0.8, 0.8, 3)
                atom_pos[2] = 0  # Keep in 2D
                atom = Dot(
                    point=atom_pos,
                    color=COHERENCE_GREEN,
                    radius=0.03
                )
                atoms.add(atom)
            
            # Cell windows
            left_window = Line(
                start=cell_body.get_left() + [0, -0.4, 0],
                end=cell_body.get_left() + [0, 0.4, 0],
                color=BLUE_E,
                stroke_width=4
            )
            
            right_window = Line(
                start=cell_body.get_right() + [0, -0.4, 0],
                end=cell_body.get_right() + [0, 0.4, 0],
                color=BLUE_E,
                stroke_width=4
            )
            
            sample_group = VGroup(cell_body, atoms, left_window, right_window)
            
        elif self.sample_type == 'ion_trap':
            # Ion trap electrodes
            trap_radius = 0.8
            electrodes = VGroup()
            
            for i in range(4):
                angle = i * PI/2
                electrode_pos = self.position + trap_radius * np.array([np.cos(angle), np.sin(angle), 0])
                electrode = Rectangle(
                    width=0.3, height=0.2,
                    color=GOLD,
                    fill_opacity=0.8
                ).move_to(electrode_pos)
                electrodes.add(electrode)
            
            # Trapped ions
            ions = VGroup()
            for i in range(5):
                ion_pos = self.position + [(i-2)*0.15, 0, 0]
                ion = Dot(
                    point=ion_pos,
                    color=QUANTUM_GOLD,
                    radius=0.05
                )
                ions.add(ion)
            
            sample_group = VGroup(electrodes, ions)
            
        elif self.sample_type == 'mot':  # Magneto-optical trap
            # MOT coils
            coil_radius = 1.2
            coils = VGroup()
            
            # Anti-Helmholtz coils
            coil1 = Circle(
                radius=coil_radius,
                color=RED,
                stroke_width=4
            ).move_to(self.position + [0, 0.6, 0])
            
            coil2 = Circle(
                radius=coil_radius,
                color=BLUE,
                stroke_width=4
            ).move_to(self.position + [0, -0.6, 0])
            
            coils.add(coil1, coil2)
            
            # Trapped atomic cloud
            cloud = Circle(
                radius=0.3,
                color=COHERENCE_GREEN,
                fill_opacity=0.5
            ).move_to(self.position)
            
            sample_group = VGroup(coils, cloud)
        
        else:
            # Generic sample
            sample_group = Circle(
                radius=0.5,
                color=SAMPLE_COLOR,
                fill_opacity=0.3
            ).move_to(self.position)
        
        return sample_group
    
    def create_fluorescence_animation(self, duration: float = 3.0) -> AnimationGroup:
        """Create animation showing atomic fluorescence."""
        if self.mobject is None:
            self.mobject = self.create_component()
        
        animations = []
        
        # Create random fluorescence events
        for _ in range(20):
            delay = np.random.uniform(0, duration)
            photon_start = self.position + np.random.uniform(-0.5, 0.5, 3)
            photon_start[2] = 0
            
            photon_direction = normalize(np.random.uniform(-1, 1, 3))
            photon_direction[2] = 0
            photon_end = photon_start + 2 * photon_direction
            
            photon = Dot(color=COHERENCE_GREEN, radius=0.02)
            photon.move_to(photon_start)
            
            emission = Succession(
                Wait(delay),
                Flash(photon_start, color=COHERENCE_GREEN, flash_radius=0.2),
                photon.animate.move_to(photon_end),
                FadeOut(photon)
            )
            
            animations.append(emission)
        
        return AnimationGroup(*animations, lag_ratio=0.1)

class PumpProbeSetup:
    """
    Complete pump-probe spectroscopy setup with synchronized pulses.
    
    Creates comprehensive experimental arrangement including pump laser,
    probe laser, delay stage, sample, and detection system.
    """
    
    def __init__(self, pump_wavelength: float = 800, probe_wavelength: float = 400):
        self.pump_wavelength = pump_wavelength
        self.probe_wavelength = probe_wavelength
        self.components = {}
        self.setup_geometry()
    
    def setup_geometry(self):
        """Define positions and orientations of all components."""
        # Pump laser
        self.components['pump_laser'] = LaserSource(
            laser_type='femtosecond',
            wavelength=self.pump_wavelength,
            power=10,
            position=[-6, 2, 0]
        )
        
        # Probe laser
        self.components['probe_laser'] = LaserSource(
            laser_type='femtosecond', 
            wavelength=self.probe_wavelength,
            power=1,
            position=[-6, -2, 0]
        )
        
        # Beam splitters for beam steering
        self.components['bs1'] = BeamSplitter(
            split_ratio=(0.5, 0.5),
            position=[-3, 2, 0],
            rotation=PI/4
        )
        
        self.components['bs2'] = BeamSplitter(
            split_ratio=(0.1, 0.9),
            position=[-1, 0, 0],
            rotation=PI/4
        )
        
        # Delay stage (moveable mirror)
        self.components['delay_mirror'] = MirrorOptical(
            mirror_type='flat',
            reflectivity=0.99,
            position=[-3, -2, 0],
            rotation=PI/4
        )
        
        # Sample
        self.components['sample'] = AtomicSample(
            sample_type='vapor_cell',
            atom_species='Rb87',
            position=[0, 0, 0]
        )
        
        # Detection system
        self.components['detector'] = PhotoDetector(
            detector_type='pmt',
            quantum_efficiency=0.3,
            position=[3, 0, 0]
        )
        
        # Additional optics
        self.components['focusing_mirror'] = MirrorOptical(
            mirror_type='curved',
            curvature=0.5,
            position=[1.5, 0, 0],
            rotation=PI/4
        )
    
    def create_complete_setup(self) -> VGroup:
        """Create visualization of complete pump-probe setup."""
        setup_group = VGroup()
        
        # Add all components
        for name, component in self.components.items():
            viz = component.get_visualization()
            component.add_label(name.replace('_', ' ').title())
            setup_group.add(viz)
        
        # Add beam paths
        beam_paths = self.create_beam_paths()
        setup_group.add(beam_paths)
        
        # Add timing diagram
        timing_diagram = self.create_timing_diagram()
        timing_diagram.to_edge(DOWN)
        setup_group.add(timing_diagram)
        
        return setup_group
    
    def create_beam_paths(self) -> VGroup:
        """Create visualization of optical beam paths."""
        paths = VGroup()
        
        # Pump beam path
        pump_path = Line(
            start=self.components['pump_laser'].position + [1.5, 0, 0],
            end=self.components['bs1'].position,
            color=RED,
            stroke_width=4
        )
        paths.add(pump_path)
        
        # Probe beam path with delay
        probe_path1 = Line(
            start=self.components['probe_laser'].position + [1.5, 0, 0],
            end=self.components['delay_mirror'].position,
            color=BLUE,
            stroke_width=4
        )
        
        probe_path2 = Line(
            start=self.components['delay_mirror'].position,
            end=self.components['bs2'].position,
            color=BLUE,
            stroke_width=4
        )
        
        paths.add(probe_path1, probe_path2)
        
        # Combined beam to sample
        combined_path = Line(
            start=self.components['bs2'].position,
            end=self.components['sample'].position,
            color=PURPLE,
            stroke_width=6
        )
        paths.add(combined_path)
        
        # Detection path
        detection_path = Line(
            start=self.components['sample'].position + [0.5, 0, 0],
            end=self.components['detector'].position,
            color=COHERENCE_GREEN,
            stroke_width=4
        )
        paths.add(detection_path)
        
        return paths
    
    def create_timing_diagram(self) -> VGroup:
        """Create timing diagram showing pump-probe sequence."""
        timing = VGroup()
        
        # Time axis
        time_axis = NumberLine(
            x_range=[0, 10, 1],
            length=8,
            include_numbers=True,
            numbers_to_exclude=[0]
        )
        
        time_label = MathTex(r"t \text{ (ps)}", font_size=20)
        time_label.next_to(time_axis, RIGHT)
        
        # Pump pulse
        pump_pulse = Rectangle(
            width=0.2, height=0.5,
            color=RED,
            fill_opacity=0.8
        ).move_to(time_axis.number_to_point(1) + [0, 1, 0])
        
        pump_label = MathTex(r"\text{Pump}", font_size=16, color=RED)
        pump_label.next_to(pump_pulse, UP)
        
        # Probe pulse (delayed)
        probe_delay = 3  # ps
        probe_pulse = Rectangle(
            width=0.2, height=0.5,
            color=BLUE,
            fill_opacity=0.8
        ).move_to(time_axis.number_to_point(1 + probe_delay) + [0, 0.5, 0])
        
        probe_label = MathTex(r"\text{Probe}", font_size=16, color=BLUE)
        probe_label.next_to(probe_pulse, UP)
        
        # Signal response
        signal_points = [
            time_axis.number_to_point(1 + probe_delay) + [0, -0.5, 0],
            time_axis.number_to_point(1 + probe_delay + 2) + [0, -1, 0],
            time_axis.number_to_point(10) + [0, -0.5, 0]
        ]
        
        signal_curve = VMobject()
        signal_curve.set_points_smoothly(signal_points)
        signal_curve.set_color(COHERENCE_GREEN)
        signal_curve.set_stroke_width(3)
        
        signal_label = MathTex(r"\text{Signal}", font_size=16, color=COHERENCE_GREEN)
        signal_label.next_to(signal_points[1], DOWN)
        
        timing.add(
            time_axis, time_label,
            pump_pulse, pump_label,
            probe_pulse, probe_label,
            signal_curve, signal_label
        )
        
        return timing
    
    def animate_pulse_sequence(self, delay_time: float = 2.0) -> AnimationGroup:
        """Create animation of pump-probe pulse sequence."""
        animations = []
        
        # Pump pulse propagation
        pump_flash = Flash(
            self.components['pump_laser'].position,
            color=RED,
            flash_radius=0.3
        )
        
        # Probe pulse propagation (delayed)
        probe_flash = Succession(
            Wait(delay_time),
            Flash(
                self.components['probe_laser'].position,
                color=BLUE,
                flash_radius=0.3
            )
        )
        
        # Sample fluorescence response
        sample_response = Succession(
            Wait(delay_time + 0.5),
            self.components['sample'].create_fluorescence_animation(duration=1.0)
        )
        
        # Detection signal
        detection_flash = Succession(
            Wait(delay_time + 1.0),
            Flash(
                self.components['detector'].position,
                color=COHERENCE_GREEN,
                flash_radius=0.5
            )
        )
        
        animations.extend([pump_flash, probe_flash, sample_response, detection_flash])
        
        return AnimationGroup(*animations, lag_ratio=0.1)

def test_experimental_setups():
    """Test function to verify experimental setup utilities work correctly."""
    print("Testing experimental setup utilities...")
    
    # Test laser source
    laser = LaserSource(laser_type='femtosecond', wavelength=800, power=10)
    laser_viz = laser.get_visualization()
    print("✓ Laser source creation successful")
    
    # Test photodetector
    detector = PhotoDetector(detector_type='pmt', quantum_efficiency=0.3)
    detector_viz = detector.get_visualization()
    print("✓ Photodetector creation successful")
    
    # Test beam splitter
    bs = BeamSplitter(split_ratio=(0.7, 0.3), polarizing=True)
    bs_viz = bs.get_visualization()
    print("✓ Beam splitter creation successful")
    
    # Test atomic sample
    sample = AtomicSample(sample_type='vapor_cell', atom_species='Rb87')
    sample_viz = sample.get_visualization()
    print("✓ Atomic sample creation successful")
    
    # Test complete pump-probe setup
    pump_probe = PumpProbeSetup(pump_wavelength=800, probe_wavelength=400)
    setup_viz = pump_probe.create_complete_setup()
    print("✓ Pump-probe setup creation successful")
    
    print("All experimental setup tests passed!")

if __name__ == "__main__":
    test_experimental_setups()