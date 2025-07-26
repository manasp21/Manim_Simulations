"""
Narration scripts for the quantum beats animation with precise timing.

This module contains the complete narration text for all scenes, synchronized
with visual elements and mathematical derivations. Each script includes timing
markers, emphasis points, and scientific accuracy requirements.
"""

from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass
import re

@dataclass
class NarrationSegment:
    """
    Individual narration segment with timing and metadata.
    
    Attributes
    ----------
    text : str
        Narration text content
    start_time : float
        Start time in seconds
    duration : float
        Segment duration in seconds
    emphasis_words : list
        Words to emphasize in narration
    sync_elements : list
        Visual elements to synchronize with
    voice_style : str
        Narration style ('normal', 'emphasis', 'technical')
    """
    text: str
    start_time: float
    duration: float
    emphasis_words: List[str] = None
    sync_elements: List[str] = None
    voice_style: str = 'normal'
    
    def __post_init__(self):
        if self.emphasis_words is None:
            self.emphasis_words = []
        if self.sync_elements is None:
            self.sync_elements = []

class QuantumBeatsNarration:
    """
    Complete narration system for the quantum beats animation.
    
    Manages all scene narrations with precise timing, scientific accuracy,
    and synchronization with visual elements and mathematical derivations.
    """
    
    # =================================================================
    # SCENE 1: Opening and Classical vs Quantum Beating (2.5 minutes)
    # =================================================================
    
    SCENE_1_NARRATION = [
        NarrationSegment(
            text="Quantum beats represent one of the most fundamental and fascinating phenomena in quantum mechanics, arising from the coherent superposition of quantum states with different energies.",
            start_time=0.0,
            duration=8.0,
            emphasis_words=['quantum beats', 'coherent superposition', 'quantum states'],
            sync_elements=['title_animation', 'particle_effects'],
            voice_style='emphasis'
        ),
        
        NarrationSegment(
            text="To understand quantum beats, we first examine classical beating between two oscillating waves with slightly different frequencies.",
            start_time=8.0,
            duration=6.0,
            emphasis_words=['classical beating', 'oscillating waves', 'different frequencies'],
            sync_elements=['classical_wave_demo'],
            voice_style='normal'
        ),
        
        NarrationSegment(
            text="When two classical waves with frequencies omega-one and omega-two interfere, they produce a beat pattern with envelope frequency equal to the difference of the original frequencies.",
            start_time=14.0,
            duration=8.0,
            emphasis_words=['interfere', 'beat pattern', 'envelope frequency'],
            sync_elements=['classical_superposition_equation', 'beat_envelope_visualization'],
            voice_style='technical'
        ),
        
        NarrationSegment(
            text="The mathematical description shows the characteristic amplitude modulation that creates the familiar beating sound in acoustics.",
            start_time=22.0,
            duration=6.0,
            emphasis_words=['amplitude modulation', 'beating sound'],
            sync_elements=['amplitude_modulation_graph'],
            voice_style='normal'
        ),
        
        NarrationSegment(
            text="Quantum beats arise from a fundamentally different mechanism: the coherent superposition of atomic or molecular energy eigenstates.",
            start_time=28.0,
            duration=8.0,
            emphasis_words=['fundamentally different', 'coherent superposition', 'energy eigenstates'],
            sync_elements=['quantum_energy_levels', 'energy_eigenvalue_equation'],
            voice_style='emphasis'
        ),
        
        NarrationSegment(
            text="Consider a quantum system prepared in a superposition of two energy eigenstates. The time evolution of this superposition naturally leads to oscillatory behavior.",
            start_time=36.0,
            duration=8.0,
            emphasis_words=['superposition', 'time evolution', 'oscillatory behavior'],
            sync_elements=['quantum_superposition_state', 'time_evolution_animation'],
            voice_style='technical'
        ),
        
        NarrationSegment(
            text="The beat frequency in quantum systems equals the energy difference between the participating states divided by Planck's constant h-bar.",
            start_time=44.0,
            duration=7.0,
            emphasis_words=['beat frequency', 'energy difference', "Planck's constant"],
            sync_elements=['quantum_beat_frequency_equation'],
            voice_style='technical'
        ),
        
        NarrationSegment(
            text="This fundamental relationship connects the observed oscillation directly to the quantum mechanical energy spectrum of the system.",
            start_time=51.0,
            duration=7.0,
            emphasis_words=['fundamental relationship', 'quantum mechanical', 'energy spectrum'],
            sync_elements=['energy_spectrum_visualization'],
            voice_style='normal'
        ),
        
        NarrationSegment(
            text="Unlike classical beats, quantum beats reveal information about quantum coherence, energy level structures, and the fundamental nature of quantum superposition.",
            start_time=58.0,
            duration=9.0,
            emphasis_words=['quantum coherence', 'energy level structures', 'quantum superposition'],
            sync_elements=['quantum_vs_classical_comparison'],
            voice_style='emphasis'
        ),
        
        NarrationSegment(
            text="The observation of quantum beats thus provides a direct window into the quantum world, allowing us to probe coherence phenomena that have no classical analog.",
            start_time=67.0,
            duration=8.0,
            emphasis_words=['direct window', 'quantum world', 'coherence phenomena', 'no classical analog'],
            sync_elements=['quantum_beats_conclusion'],
            voice_style='emphasis'
        )
    ]
    
    # =================================================================
    # SCENE 2: Mathematical Formalism and Density Matrix (3.5 minutes)
    # =================================================================
    
    SCENE_2_NARRATION = [
        NarrationSegment(
            text="The mathematical description of quantum beats requires the density matrix formalism, which provides a complete framework for describing both pure and mixed quantum states.",
            start_time=75.0,
            duration=9.0,
            emphasis_words=['density matrix formalism', 'pure and mixed', 'quantum states'],
            sync_elements=['density_matrix_introduction'],
            voice_style='technical'
        ),
        
        NarrationSegment(
            text="For a quantum system in a pure state psi, the density matrix is constructed as the outer product of the state vector with its complex conjugate.",
            start_time=84.0,
            duration=8.0,
            emphasis_words=['pure state', 'density matrix', 'outer product', 'complex conjugate'],
            sync_elements=['pure_state_density_matrix_equation'],
            voice_style='technical'
        ),
        
        NarrationSegment(
            text="Consider a two-level system with states one and two. The density matrix becomes a two-by-two matrix with diagonal elements representing state populations and off-diagonal elements representing quantum coherences.",
            start_time=92.0,
            duration=12.0,
            emphasis_words=['two-level system', 'diagonal elements', 'state populations', 'off-diagonal elements', 'quantum coherences'],
            sync_elements=['two_level_density_matrix', 'matrix_elements_visualization'],
            voice_style='technical'
        ),
        
        NarrationSegment(
            text="The diagonal elements rho-i-i give the probability of finding the system in state i, while the off-diagonal coherence terms rho-i-j contain the quantum interference information.",
            start_time=104.0,
            duration=10.0,
            emphasis_words=['diagonal elements', 'probability', 'off-diagonal coherence', 'quantum interference'],
            sync_elements=['population_coherence_explanation'],
            voice_style='normal'
        ),
        
        NarrationSegment(
            text="The time evolution of the density matrix is governed by the quantum master equation, which includes both unitary evolution under the Hamiltonian and dissipative effects from the environment.",
            start_time=114.0,
            duration=11.0,
            emphasis_words=['time evolution', 'master equation', 'unitary evolution', 'Hamiltonian', 'dissipative effects'],
            sync_elements=['master_equation_derivation'],
            voice_style='technical'
        ),
        
        NarrationSegment(
            text="The Lindblad form of the dissipator describes how environmental coupling leads to decoherence and population relaxation through quantum jump operators.",
            start_time=125.0,
            duration=9.0,
            emphasis_words=['Lindblad form', 'environmental coupling', 'decoherence', 'quantum jump operators'],
            sync_elements=['lindblad_dissipator_equation'],
            voice_style='technical'
        ),
        
        NarrationSegment(
            text="For quantum beats, the crucial dynamics occur in the off-diagonal coherence elements, which oscillate at the energy difference frequency while decaying due to decoherence.",
            start_time=134.0,
            duration=10.0,
            emphasis_words=['off-diagonal coherence', 'oscillate', 'energy difference frequency', 'decaying', 'decoherence'],
            sync_elements=['coherence_evolution_equation', 'oscillation_decay_animation'],
            voice_style='emphasis'
        ),
        
        NarrationSegment(
            text="The beat signal intensity can be expressed as the sum of individual state contributions plus an interference term proportional to the real part of the coherence.",
            start_time=144.0,
            duration=10.0,
            emphasis_words=['beat signal intensity', 'individual state contributions', 'interference term', 'real part', 'coherence'],
            sync_elements=['beat_signal_equation', 'intensity_decomposition'],
            voice_style='technical'
        ),
        
        NarrationSegment(
            text="This mathematical framework reveals that quantum beats directly measure the magnitude and phase of quantum coherence, providing a powerful probe of quantum mechanical phenomena.",
            start_time=154.0,
            duration=10.0,
            emphasis_words=['magnitude and phase', 'quantum coherence', 'powerful probe', 'quantum mechanical phenomena'],
            sync_elements=['coherence_measurement_visualization'],
            voice_style='emphasis'
        ),
        
        NarrationSegment(
            text="The density matrix approach thus provides both conceptual clarity and computational power for understanding complex multi-level systems and their coherence dynamics.",
            start_time=164.0,
            duration=9.0,
            emphasis_words=['conceptual clarity', 'computational power', 'multi-level systems', 'coherence dynamics'],
            sync_elements=['density_matrix_conclusion'],
            voice_style='normal'
        )
    ]
    
    # =================================================================
    # SCENE 3: Isotropic vs Anisotropic Distinction (3.0 minutes)
    # =================================================================
    
    SCENE_3_NARRATION = [
        NarrationSegment(
            text="A fundamental distinction in quantum beat phenomena is between isotropic and anisotropic systems, which differ dramatically in their dependence on spatial orientation and light polarization.",
            start_time=173.0,
            duration=11.0,
            emphasis_words=['fundamental distinction', 'isotropic', 'anisotropic', 'spatial orientation', 'light polarization'],
            sync_elements=['isotropic_anisotropic_intro'],
            voice_style='emphasis'
        ),
        
        NarrationSegment(
            text="Isotropic quantum beats arise from spherically symmetric systems where the beat signal remains constant regardless of the observation direction or polarization of the light.",
            start_time=184.0,
            duration=10.0,
            emphasis_words=['spherically symmetric', 'beat signal', 'observation direction', 'polarization'],
            sync_elements=['spherical_symmetry_visualization'],
            voice_style='technical'
        ),
        
        NarrationSegment(
            text="The mathematical description uses spherical tensor decomposition to separate the angular-dependent and angular-independent contributions to the density matrix.",
            start_time=194.0,
            duration=9.0,
            emphasis_words=['spherical tensor decomposition', 'angular-dependent', 'angular-independent', 'density matrix'],
            sync_elements=['spherical_tensor_equation'],
            voice_style='technical'
        ),
        
        NarrationSegment(
            text="In magnetic fields, Zeeman sublevel coherences between different magnetic quantum numbers create beat frequencies proportional to the magnetic field strength.",
            start_time=203.0,
            duration=10.0,
            emphasis_words=['Zeeman sublevel coherences', 'magnetic quantum numbers', 'beat frequencies', 'magnetic field strength'],
            sync_elements=['zeeman_hamiltonian', 'magnetic_sublevel_diagram'],
            voice_style='technical'
        ),
        
        NarrationSegment(
            text="The Zeeman beat frequency equals the product of the Bohr magneton, the Landé g-factor, and the magnetic field strength, divided by Planck's constant.",
            start_time=213.0,
            duration=9.0,
            emphasis_words=['Zeeman beat frequency', 'Bohr magneton', 'Landé g-factor', 'magnetic field strength'],
            sync_elements=['zeeman_beat_frequency_equation'],
            voice_style='technical'
        ),
        
        NarrationSegment(
            text="Experimental examples include calcium Rydberg atoms, where beats between S and P states remain isotropic due to the spherical averaging over atomic orientations.",
            start_time=222.0,
            duration=10.0,
            emphasis_words=['calcium Rydberg atoms', 'S and P states', 'spherical averaging', 'atomic orientations'],
            sync_elements=['calcium_rydberg_visualization'],
            voice_style='normal'
        ),
        
        NarrationSegment(
            text="In contrast, anisotropic systems like ReS2 crystals show strong angular dependence because the crystal structure breaks spherical symmetry.",
            start_time=232.0,
            duration=9.0,
            emphasis_words=['anisotropic systems', 'ReS2 crystals', 'angular dependence', 'crystal structure', 'breaks spherical symmetry'],
            sync_elements=['res2_crystal_structure', 'anisotropy_visualization'],
            voice_style='normal'
        ),
        
        NarrationSegment(
            text="The angular dependence follows a second-order Legendre polynomial in the cosine of the angle, with the anisotropy parameter beta determining the strength of the orientation effect.",
            start_time=241.0,
            duration=11.0,
            emphasis_words=['angular dependence', 'Legendre polynomial', 'anisotropy parameter', 'orientation effect'],
            sync_elements=['angular_dependence_equation', 'legendre_polynomial_plot'],
            voice_style='technical'
        ),
        
        NarrationSegment(
            text="Spherical averaging over all possible orientations converts anisotropic signals back to their isotropic components, revealing the underlying quantum mechanical structure.",
            start_time=252.0,
            duration=10.0,
            emphasis_words=['spherical averaging', 'all possible orientations', 'isotropic components', 'quantum mechanical structure'],
            sync_elements=['spherical_averaging_equation'],
            voice_style='technical'
        ),
        
        NarrationSegment(
            text="This distinction between isotropic and anisotropic behavior provides crucial information about system symmetries and the nature of the quantum states involved in the beating process.",
            start_time=262.0,
            duration=11.0,
            emphasis_words=['crucial information', 'system symmetries', 'quantum states', 'beating process'],
            sync_elements=['symmetry_analysis_conclusion'],
            voice_style='emphasis'
        )
    ]
    
    # =================================================================
    # SCENE 4: Physical Mechanisms and Interference (2.5 minutes)
    # =================================================================
    
    SCENE_4_NARRATION = [
        NarrationSegment(
            text="The physical origin of quantum beats lies in quantum interference between indistinguishable pathways that connect the same initial and final states through different intermediate levels.",
            start_time=273.0,
            duration=11.0,
            emphasis_words=['quantum interference', 'indistinguishable pathways', 'intermediate levels'],
            sync_elements=['pathway_interference_intro'],
            voice_style='emphasis'
        ),
        
        NarrationSegment(
            text="In V-type level systems, two excited states decay to a common ground state, creating interference between the decay pathways that manifests as quantum beats in the fluorescence.",
            start_time=284.0,
            duration=10.0,
            emphasis_words=['V-type level systems', 'common ground state', 'decay pathways', 'fluorescence'],
            sync_elements=['v_system_diagram', 'v_system_hamiltonian'],
            voice_style='technical'
        ),
        
        NarrationSegment(
            text="Lambda systems show the complementary behavior, where a common excited state can decay to two different ground states, again producing beat patterns through pathway interference.",
            start_time=294.0,
            duration=10.0,
            emphasis_words=['Lambda systems', 'common excited state', 'different ground states', 'pathway interference'],
            sync_elements=['lambda_system_diagram', 'lambda_system_hamiltonian'],
            voice_style='technical'
        ),
        
        NarrationSegment(
            text="The key requirement for quantum beats is that the interfering pathways must be quantum mechanically indistinguishable - any information that could distinguish the paths destroys the coherence.",
            start_time=304.0,
            duration=11.0,
            emphasis_words=['quantum mechanically indistinguishable', 'distinguish the paths', 'destroys the coherence'],
            sync_elements=['indistinguishability_principle'],
            voice_style='emphasis'
        ),
        
        NarrationSegment(
            text="Coherent superposition states produce interference with high visibility, while incoherent mixtures of the same states show no beat modulation.",
            start_time=315.0,
            duration=9.0,
            emphasis_words=['coherent superposition', 'high visibility', 'incoherent mixtures', 'no beat modulation'],
            sync_elements=['coherent_vs_incoherent_comparison'],
            voice_style='technical'
        ),
        
        NarrationSegment(
            text="The quantum interference contrast is directly proportional to the magnitude of the off-diagonal density matrix element, providing a direct measure of quantum coherence.",
            start_time=324.0,
            duration=10.0,
            emphasis_words=['interference contrast', 'off-diagonal density matrix', 'measure of quantum coherence'],
            sync_elements=['interference_contrast_equation'],
            voice_style='technical'
        ),
        
        NarrationSegment(
            text="This differs fundamentally from classical interference, where the contrast depends on the relative intensities and phase relationships of classical electromagnetic fields.",
            start_time=334.0,
            duration=9.0,
            emphasis_words=['differs fundamentally', 'classical interference', 'relative intensities', 'electromagnetic fields'],
            sync_elements=['classical_vs_quantum_interference'],
            voice_style='normal'
        ),
        
        NarrationSegment(
            text="Quantum beats thus reveal the fundamentally quantum mechanical nature of matter-light interactions and the role of quantum coherence in atomic and molecular processes.",
            start_time=343.0,
            duration=10.0,
            emphasis_words=['fundamentally quantum mechanical', 'matter-light interactions', 'quantum coherence'],
            sync_elements=['quantum_nature_conclusion'],
            voice_style='emphasis'
        )
    ]
    
    # =================================================================
    # SCENE 5: Decoherence and Dephasing Effects (2.5 minutes)
    # =================================================================
    
    SCENE_5_NARRATION = [
        NarrationSegment(
            text="Quantum beats are inevitably affected by decoherence processes that arise from the coupling of the quantum system to its surrounding environment.",
            start_time=353.0,
            duration=9.0,
            emphasis_words=['decoherence processes', 'coupling', 'surrounding environment'],
            sync_elements=['decoherence_introduction'],
            voice_style='normal'
        ),
        
        NarrationSegment(
            text="The total Hamiltonian includes the system, the environment or bath, and the system-bath interaction that leads to information leakage and coherence loss.",
            start_time=362.0,
            duration=10.0,
            emphasis_words=['total Hamiltonian', 'system-bath interaction', 'information leakage', 'coherence loss'],
            sync_elements=['system_bath_hamiltonian'],
            voice_style='technical'
        ),
        
        NarrationSegment(
            text="Under the Born-Markov approximation, where the bath correlation time is much shorter than the system dynamics, we obtain exponential decay of quantum coherences.",
            start_time=372.0,
            duration=11.0,
            emphasis_words=['Born-Markov approximation', 'bath correlation time', 'exponential decay', 'quantum coherences'],
            sync_elements=['born_markov_conditions', 'exponential_decay_animation'],
            voice_style='technical'
        ),
        
        NarrationSegment(
            text="Three fundamental timescales characterize the decoherence process: T1 for longitudinal relaxation, T2 for transverse dephasing, and T2-star for additional pure dephasing effects.",
            start_time=383.0,
            duration=12.0,
            emphasis_words=['T1', 'longitudinal relaxation', 'T2', 'transverse dephasing', 'T2-star', 'pure dephasing'],
            sync_elements=['relaxation_timescales', 'bloch_sphere_decay'],
            voice_style='technical'
        ),
        
        NarrationSegment(
            text="The coherence decay rate is given by the average of the individual state decay rates plus additional pure dephasing contributions from environmental fluctuations.",
            start_time=395.0,
            duration=10.0,
            emphasis_words=['coherence decay rate', 'individual state decay', 'pure dephasing', 'environmental fluctuations'],
            sync_elements=['decoherence_rate_formula'],
            voice_style='technical'
        ),
        
        NarrationSegment(
            text="Different physical platforms exhibit vastly different coherence timescales: isolated atoms maintain coherence for microseconds, while solid-state systems typically show nanosecond or shorter coherence times.",
            start_time=405.0,
            duration=12.0,
            emphasis_words=['different platforms', 'coherence timescales', 'isolated atoms', 'microseconds', 'solid-state systems', 'nanosecond'],
            sync_elements=['platform_comparison_chart'],
            voice_style='normal'
        ),
        
        NarrationSegment(
            text="Environmental coupling mechanisms include phonon interactions in solids, photon emission and absorption, magnetic field fluctuations, and collisions in atomic vapors.",
            start_time=417.0,
            duration=11.0,
            emphasis_words=['phonon interactions', 'photon emission', 'magnetic field fluctuations', 'collisions', 'atomic vapors'],
            sync_elements=['coupling_mechanisms_visualization'],
            voice_style='technical'
        ),
        
        NarrationSegment(
            text="The beat signal envelope decays exponentially with the coherence lifetime, allowing quantum beats to serve as a sensitive probe of environmental decoherence effects.",
            start_time=428.0,
            duration=10.0,
            emphasis_words=['envelope decays', 'coherence lifetime', 'sensitive probe', 'environmental decoherence'],
            sync_elements=['envelope_decay_measurement'],
            voice_style='emphasis'
        ),
        
        NarrationSegment(
            text="Understanding and controlling decoherence is crucial for quantum technologies, as it sets fundamental limits on quantum information processing and quantum sensing applications.",
            start_time=438.0,
            duration=10.0,
            emphasis_words=['controlling decoherence', 'quantum technologies', 'fundamental limits', 'quantum sensing'],
            sync_elements=['decoherence_control_conclusion'],
            voice_style='emphasis'
        )
    ]
    
    # =================================================================
    # SCENE 6: Experimental Detection and Measurement (2.0 minutes)
    # =================================================================
    
    SCENE_6_NARRATION = [
        NarrationSegment(
            text="Experimental detection of quantum beats requires sophisticated time-resolved spectroscopy techniques capable of measuring coherence dynamics on timescales from femtoseconds to microseconds.",
            start_time=448.0,
            duration=11.0,
            emphasis_words=['time-resolved spectroscopy', 'coherence dynamics', 'femtoseconds to microseconds'],
            sync_elements=['experimental_overview'],
            voice_style='technical'
        ),
        
        NarrationSegment(
            text="Pump-probe spectroscopy uses ultrashort laser pulses to prepare coherent superposition states and then probe their evolution with precisely controlled time delays.",
            start_time=459.0,
            duration=10.0,
            emphasis_words=['pump-probe spectroscopy', 'ultrashort laser pulses', 'coherent superposition', 'time delays'],
            sync_elements=['pump_probe_setup', 'timing_diagram'],
            voice_style='technical'
        ),
        
        NarrationSegment(
            text="The pump pulse creates the initial coherence through multiphoton transitions, while the delayed probe pulse reads out the coherence state through stimulated emission or absorption.",
            start_time=469.0,
            duration=11.0,
            emphasis_words=['pump pulse', 'initial coherence', 'multiphoton transitions', 'probe pulse', 'stimulated emission'],
            sync_elements=['pump_probe_mechanism'],
            voice_style='technical'
        ),
        
        NarrationSegment(
            text="Time-resolved fluorescence detection captures the beat modulation directly in the spontaneous emission intensity as a function of time after the excitation pulse.",
            start_time=480.0,
            duration=10.0,
            emphasis_words=['time-resolved fluorescence', 'beat modulation', 'spontaneous emission', 'excitation pulse'],
            sync_elements=['fluorescence_detection_animation'],
            voice_style='technical'
        ),
        
        NarrationSegment(
            text="Heterodyne and homodyne detection techniques provide phase-sensitive measurements by mixing the signal field with a local oscillator, enabling complete characterization of the quantum coherence.",
            start_time=490.0,
            duration=12.0,
            emphasis_words=['heterodyne', 'homodyne', 'phase-sensitive measurements', 'local oscillator', 'complete characterization'],
            sync_elements=['heterodyne_detection_setup'],
            voice_style='technical'
        ),
        
        NarrationSegment(
            text="Modern femtosecond laser systems with pulse durations below 100 femtoseconds enable the study of ultrafast coherence dynamics in molecules and condensed matter systems.",
            start_time=502.0,
            duration=10.0,
            emphasis_words=['femtosecond laser systems', '100 femtoseconds', 'ultrafast coherence dynamics', 'condensed matter'],
            sync_elements=['femtosecond_laser_visualization'],
            voice_style='normal'
        ),
        
        NarrationSegment(
            text="The experimental challenge lies in achieving sufficient signal-to-noise ratio while maintaining the temporal resolution needed to observe the beat oscillations before decoherence destroys them.",
            start_time=512.0,
            duration=11.0,
            emphasis_words=['signal-to-noise ratio', 'temporal resolution', 'beat oscillations', 'decoherence destroys'],
            sync_elements=['experimental_challenges'],
            voice_style='emphasis'
        ),
        
        NarrationSegment(
            text="These experimental techniques have enabled the observation of quantum beats in systems ranging from simple atoms to complex biological molecules, opening new windows into quantum dynamics.",
            start_time=523.0,
            duration=10.0,
            emphasis_words=['simple atoms', 'complex biological molecules', 'new windows', 'quantum dynamics'],
            sync_elements=['experimental_applications_overview'],
            voice_style='normal'
        )
    ]
    
    # =================================================================
    # SCENE 7: Interpretational Issues and Measurement (2.5 minutes)
    # =================================================================
    
    SCENE_7_NARRATION = [
        NarrationSegment(
            text="Quantum beats raise profound questions about the nature of quantum measurement and the interpretation of quantum mechanical phenomena that continue to challenge our understanding of reality.",
            start_time=533.0,
            duration=11.0,
            emphasis_words=['profound questions', 'quantum measurement', 'interpretation', 'challenge our understanding'],
            sync_elements=['interpretational_introduction'],
            voice_style='emphasis'
        ),
        
        NarrationSegment(
            text="The measurement problem asks how the definite outcomes we observe emerge from quantum superposition states that seem to contain multiple simultaneous realities.",
            start_time=544.0,
            duration=10.0,
            emphasis_words=['measurement problem', 'definite outcomes', 'superposition states', 'multiple simultaneous realities'],
            sync_elements=['measurement_problem_visualization'],
            voice_style='emphasis'
        ),
        
        NarrationSegment(
            text="Wave function collapse, as described by the Born rule, provides statistical predictions but offers no mechanism for how or when the collapse occurs during measurement.",
            start_time=554.0,
            duration=10.0,
            emphasis_words=['wave function collapse', 'Born rule', 'statistical predictions', 'no mechanism'],
            sync_elements=['wave_function_collapse_animation'],
            voice_style='technical'
        ),
        
        NarrationSegment(
            text="Different interpretations of quantum mechanics - from Copenhagen to many-worlds to consistent histories - offer radically different pictures of what quantum beats actually represent.",
            start_time=564.0,
            duration=11.0,
            emphasis_words=['different interpretations', 'Copenhagen', 'many-worlds', 'consistent histories', 'radically different'],
            sync_elements=['interpretation_comparison'],
            voice_style='normal'
        ),
        
        NarrationSegment(
            text="The quantum-to-classical transition occurs when decoherence timescales become much shorter than observation timescales, effectively destroying quantum interference.",
            start_time=575.0,
            duration=10.0,
            emphasis_words=['quantum-to-classical transition', 'decoherence timescales', 'observation timescales', 'destroying quantum interference'],
            sync_elements=['decoherence_transition_animation'],
            voice_style='technical'
        ),
        
        NarrationSegment(
            text="Measurement back-action necessarily disturbs the quantum system, raising questions about the role of the observer and the limits of simultaneous measurement of non-commuting observables.",
            start_time=585.0,
            duration=12.0,
            emphasis_words=['measurement back-action', 'disturbs the quantum system', 'role of the observer', 'non-commuting observables'],
            sync_elements=['measurement_backaction_visualization'],
            voice_style='technical'
        ),
        
        NarrationSegment(
            text="The quantum Zeno effect demonstrates that frequent measurements can freeze quantum evolution, highlighting the intimate connection between measurement and dynamics.",
            start_time=597.0,
            duration=10.0,
            emphasis_words=['quantum Zeno effect', 'frequent measurements', 'freeze quantum evolution', 'measurement and dynamics'],
            sync_elements=['quantum_zeno_demonstration'],
            voice_style='normal'
        ),
        
        NarrationSegment(
            text="Complementarity and uncertainty principles set fundamental limits on what can be simultaneously known about quantum systems, with quantum beats probing these fundamental boundaries.",
            start_time=607.0,
            duration=11.0,
            emphasis_words=['complementarity', 'uncertainty principles', 'fundamental limits', 'fundamental boundaries'],
            sync_elements=['complementarity_visualization'],
            voice_style='emphasis'
        ),
        
        NarrationSegment(
            text="These interpretational challenges remind us that quantum mechanics, despite its predictive success, continues to pose deep questions about the nature of physical reality itself.",
            start_time=618.0,
            duration=10.0,
            emphasis_words=['interpretational challenges', 'predictive success', 'deep questions', 'physical reality'],
            sync_elements=['interpretational_conclusion'],
            voice_style='emphasis'
        )
    ]
    
    # =================================================================
    # SCENE 8: Current Research and Future Directions (2.0 minutes)
    # =================================================================
    
    SCENE_8_NARRATION = [
        NarrationSegment(
            text="Quantum beats have evolved from fundamental physics curiosities to enabling technologies for some of the most precise measurements ever achieved by humanity.",
            start_time=628.0,
            duration=9.0,
            emphasis_words=['enabling technologies', 'most precise measurements', 'achieved by humanity'],
            sync_elements=['precision_measurement_intro'],
            voice_style='emphasis'
        ),
        
        NarrationSegment(
            text="Modern atomic clocks exploit quantum beat phenomena to achieve fractional frequency uncertainties of one part in 10^18, redefining our concept of time itself.",
            start_time=637.0,
            duration=10.0,
            emphasis_words=['atomic clocks', 'fractional frequency uncertainties', '10^18', 'redefining time'],
            sync_elements=['atomic_clock_precision', 'frequency_uncertainty_visualization'],
            voice_style='technical'
        ),
        
        NarrationSegment(
            text="Quantum sensing applications leverage the sensitivity of quantum coherence to external fields, achieving detection limits orders of magnitude beyond classical sensors.",
            start_time=647.0,
            duration=10.0,
            emphasis_words=['quantum sensing', 'external fields', 'detection limits', 'orders of magnitude beyond'],
            sync_elements=['quantum_sensing_comparison'],
            voice_style='technical'
        ),
        
        NarrationSegment(
            text="In biological systems, recent evidence suggests that quantum coherence and beating phenomena may play crucial roles in photosynthesis, avian navigation, and neural processes.",
            start_time=657.0,
            duration=11.0,
            emphasis_words=['biological systems', 'quantum coherence', 'photosynthesis', 'avian navigation', 'neural processes'],
            sync_elements=['biological_quantum_coherence'],
            voice_style='normal'
        ),
        
        NarrationSegment(
            text="Quantum information processing relies on maintaining and manipulating quantum coherence for computation and communication, with quantum beats serving as both resource and diagnostic tool.",
            start_time=668.0,
            duration=11.0,
            emphasis_words=['quantum information processing', 'maintaining coherence', 'computation and communication', 'diagnostic tool'],
            sync_elements=['quantum_computing_visualization'],
            voice_style='technical'
        ),
        
        NarrationSegment(
            text="Future developments promise even greater precision, with next-generation atomic clocks targeting uncertainties of one part in 10^19 and beyond.",
            start_time=679.0,
            duration=9.0,
            emphasis_words=['greater precision', 'next-generation', '10^19 and beyond'],
            sync_elements=['future_precision_goals'],
            voice_style='normal'
        ),
        
        NarrationSegment(
            text="Quantum networks will distribute entangled states across global distances, with quantum beats helping to verify and maintain the quality of these quantum connections.",
            start_time=688.0,
            duration=10.0,
            emphasis_words=['quantum networks', 'entangled states', 'global distances', 'quantum connections'],
            sync_elements=['quantum_network_visualization'],
            voice_style='technical'
        ),
        
        NarrationSegment(
            text="The study of quantum beats thus represents both a window into fundamental physics and a pathway to revolutionary technologies that will reshape our technological civilization.",
            start_time=698.0,
            duration=11.0,
            emphasis_words=['window into fundamental physics', 'revolutionary technologies', 'reshape our civilization'],
            sync_elements=['future_conclusion'],
            voice_style='emphasis'
        ),
        
        NarrationSegment(
            text="As we continue to probe the boundaries between quantum and classical worlds, quantum beats remain one of our most powerful tools for understanding and harnessing the mysteries of quantum mechanics.",
            start_time=709.0,
            duration=12.0,
            emphasis_words=['boundaries', 'quantum and classical worlds', 'powerful tools', 'mysteries of quantum mechanics'],
            sync_elements=['final_conclusion', 'fade_to_credits'],
            voice_style='emphasis'
        )
    ]
    
    # =================================================================
    # UTILITY METHODS
    # =================================================================
    
    @classmethod
    def get_complete_narration(cls) -> List[NarrationSegment]:
        """
        Get complete narration script for all scenes.
        
        Returns
        -------
        list
            All narration segments in chronological order
        """
        all_segments = []
        all_segments.extend(cls.SCENE_1_NARRATION)
        all_segments.extend(cls.SCENE_2_NARRATION)
        all_segments.extend(cls.SCENE_3_NARRATION)
        all_segments.extend(cls.SCENE_4_NARRATION)
        all_segments.extend(cls.SCENE_5_NARRATION)
        all_segments.extend(cls.SCENE_6_NARRATION)
        all_segments.extend(cls.SCENE_7_NARRATION)
        all_segments.extend(cls.SCENE_8_NARRATION)
        
        return all_segments
    
    @classmethod
    def get_scene_narration(cls, scene_number: int) -> List[NarrationSegment]:
        """
        Get narration for a specific scene.
        
        Parameters
        ----------
        scene_number : int
            Scene number (1-8)
            
        Returns
        -------
        list
            Narration segments for the specified scene
        """
        scene_map = {
            1: cls.SCENE_1_NARRATION,
            2: cls.SCENE_2_NARRATION,
            3: cls.SCENE_3_NARRATION,
            4: cls.SCENE_4_NARRATION,
            5: cls.SCENE_5_NARRATION,
            6: cls.SCENE_6_NARRATION,
            7: cls.SCENE_7_NARRATION,
            8: cls.SCENE_8_NARRATION
        }
        
        return scene_map.get(scene_number, [])
    
    @classmethod
    def get_total_duration(cls) -> float:
        """
        Calculate total narration duration.
        
        Returns
        -------
        float
            Total duration in seconds
        """
        all_segments = cls.get_complete_narration()
        if not all_segments:
            return 0.0
        
        return max(seg.start_time + seg.duration for seg in all_segments)
    
    @classmethod
    def get_emphasis_words(cls) -> List[str]:
        """
        Get all words marked for emphasis across all scenes.
        
        Returns
        -------
        list
            Unique emphasis words
        """
        all_segments = cls.get_complete_narration()
        emphasis_words = set()
        
        for segment in all_segments:
            emphasis_words.update(segment.emphasis_words)
        
        return sorted(list(emphasis_words))
    
    @classmethod
    def search_narration(cls, keyword: str) -> List[Tuple[int, NarrationSegment]]:
        """
        Search for segments containing a keyword.
        
        Parameters
        ----------
        keyword : str
            Search keyword
            
        Returns
        -------
        list
            List of (segment_index, segment) tuples matching the keyword
        """
        results = []
        all_segments = cls.get_complete_narration()
        
        for i, segment in enumerate(all_segments):
            if (keyword.lower() in segment.text.lower() or 
                keyword.lower() in ' '.join(segment.emphasis_words).lower()):
                results.append((i, segment))
        
        return results
    
    @classmethod
    def create_timing_script(cls) -> str:
        """
        Create a timing script for audio production.
        
        Returns
        -------
        str
            Formatted timing script
        """
        script_lines = []
        script_lines.append("QUANTUM BEATS ANIMATION - NARRATION TIMING SCRIPT")
        script_lines.append("=" * 60)
        script_lines.append("")
        
        scene_segments = [
            ("Scene 1: Classical vs Quantum Beating", cls.SCENE_1_NARRATION),
            ("Scene 2: Mathematical Formalism", cls.SCENE_2_NARRATION),
            ("Scene 3: Isotropic vs Anisotropic", cls.SCENE_3_NARRATION),
            ("Scene 4: Physical Mechanisms", cls.SCENE_4_NARRATION),
            ("Scene 5: Decoherence Effects", cls.SCENE_5_NARRATION),
            ("Scene 6: Experimental Detection", cls.SCENE_6_NARRATION),
            ("Scene 7: Interpretational Issues", cls.SCENE_7_NARRATION),
            ("Scene 8: Future Directions", cls.SCENE_8_NARRATION)
        ]
        
        for scene_title, segments in scene_segments:
            script_lines.append(f"\n{scene_title}")
            script_lines.append("-" * len(scene_title))
            
            for segment in segments:
                time_str = f"{segment.start_time:.1f}s - {segment.start_time + segment.duration:.1f}s"
                script_lines.append(f"\n[{time_str}] ({segment.voice_style.upper()})")
                
                # Format text with emphasis markers
                text = segment.text
                for word in segment.emphasis_words:
                    text = text.replace(word, f"**{word}**")
                
                script_lines.append(text)
                
                if segment.sync_elements:
                    script_lines.append(f"SYNC: {', '.join(segment.sync_elements)}")
        
        total_duration = cls.get_total_duration()
        script_lines.append(f"\n\nTOTAL DURATION: {total_duration:.1f} seconds ({total_duration/60:.1f} minutes)")
        
        return "\n".join(script_lines)

def test_narration_scripts():
    """Test function to verify narration scripts work correctly."""
    print("Testing narration scripts...")
    
    # Test complete narration retrieval
    complete_narration = QuantumBeatsNarration.get_complete_narration()
    print(f"✓ Complete narration has {len(complete_narration)} segments")
    
    # Test scene-specific narration
    scene1_narration = QuantumBeatsNarration.get_scene_narration(1)
    print(f"✓ Scene 1 has {len(scene1_narration)} segments")
    
    # Test total duration calculation
    total_duration = QuantumBeatsNarration.get_total_duration()
    print(f"✓ Total duration: {total_duration:.1f} seconds ({total_duration/60:.1f} minutes)")
    
    # Test emphasis words extraction
    emphasis_words = QuantumBeatsNarration.get_emphasis_words()
    print(f"✓ Found {len(emphasis_words)} unique emphasis words")
    
    # Test keyword search
    results = QuantumBeatsNarration.search_narration('quantum coherence')
    print(f"✓ Found {len(results)} segments mentioning 'quantum coherence'")
    
    # Test timing script generation
    timing_script = QuantumBeatsNarration.create_timing_script()
    print(f"✓ Generated timing script with {len(timing_script.split('\\n'))} lines")
    
    print("All narration script tests passed!")

if __name__ == "__main__":
    test_narration_scripts()