"""
Pre-formatted mathematical expressions for the quantum beats animation.

This module contains all key equations, formulas, and mathematical expressions
used throughout the animation, organized by scene and topic for easy reference.
All expressions are formatted using proper LaTeX notation for quantum mechanics.
"""

from manim import *
from typing import Dict, List, Union
import numpy as np

class QuantumBeatExpressions:
    """
    Centralized repository of mathematical expressions for quantum beats.
    
    Contains all equations from theoretical foundations through experimental
    applications, formatted with consistent LaTeX styling.
    """
    
    # =================================================================
    # SCENE 1: Classical vs Quantum Beating
    # =================================================================
    
    CLASSICAL_BEATING = {
        'classical_superposition': r'y(t) = A_1 \cos(\omega_1 t) + A_2 \cos(\omega_2 t)',
        
        'classical_beat_envelope': r'y(t) = 2A \cos\left(\frac{\omega_1 - \omega_2}{2}t\right) \cos\left(\frac{\omega_1 + \omega_2}{2}t\right)',
        
        'classical_beat_frequency': r'\Omega_{beat} = |\omega_1 - \omega_2|',
        
        'quantum_state_superposition': r'|\psi\rangle = c_1 |1\rangle + c_2 |2\rangle',
        
        'quantum_energy_difference': r'\Delta\omega = \frac{E_2 - E_1}{\hbar}',
        
        'quantum_beat_origin': r'\text{Quantum beats} \leftarrow \text{Coherent superposition of energy eigenstates}',
        
        'energy_eigenvalue_equation': r'\hat{H}|n\rangle = E_n|n\rangle',
        
        'time_evolution_superposition': r'|\psi(t)\rangle = c_1 e^{-iE_1 t/\hbar}|1\rangle + c_2 e^{-iE_2 t/\hbar}|2\rangle'
    }
    
    # =================================================================
    # SCENE 2: Mathematical Formalism and Density Matrix
    # =================================================================
    
    DENSITY_MATRIX_FORMALISM = {
        'density_matrix_definition': r'\hat{\rho} = \sum_i p_i |\psi_i\rangle\langle\psi_i|',
        
        'pure_state_density_matrix': r'\hat{\rho} = |\psi\rangle\langle\psi|',
        
        'two_level_density_matrix': r'\hat{\rho} = \begin{pmatrix} \rho_{11} & \rho_{12} \\ \rho_{21} & \rho_{22} \end{pmatrix}',
        
        'population_elements': r'\rho_{ii} = \text{population of state } |i\rangle',
        
        'coherence_elements': r'\rho_{ij} = \text{coherence between states } |i\rangle \text{ and } |j\rangle',
        
        'master_equation': r'\frac{\partial\hat{\rho}}{\partial t} = -\frac{i}{\hbar}[\hat{H}, \hat{\rho}] + \mathcal{L}_{diss}[\hat{\rho}]',
        
        'lindblad_dissipator': r'\mathcal{L}_{diss}[\hat{\rho}] = \sum_k \gamma_k \left(\hat{L}_k\hat{\rho}\hat{L}_k^\dagger - \frac{1}{2}\{\hat{L}_k^\dagger\hat{L}_k, \hat{\rho}\}\right)',
        
        'coherence_evolution': r'\frac{d\rho_{12}}{dt} = -i\omega_{12}\rho_{12} - \Gamma_{12}\rho_{12}',
        
        'population_evolution': r'\frac{dp_i}{dt} = -\gamma_i p_i + \sum_{j>i} \gamma_{ji} p_j',
        
        'off_diagonal_decay': r'\rho_{12}(t) = \rho_{12}(0) e^{-i\omega_{12}t - \Gamma_{12}t}',
        
        'beat_signal_intensity': r'I(t) = \gamma_1 p_1 + \gamma_2 p_2 + 2\text{Re}[\gamma_{12}\rho_{12}(t)]',
        
        'quantum_coherence_measure': r'C_{12} = |\rho_{12}| = |\langle 1|\hat{\rho}|2\rangle|'
    }
    
    # =================================================================
    # SCENE 3: Isotropic vs Anisotropic Systems
    # =================================================================
    
    ISOTROPIC_ANISOTROPIC = {
        'isotropic_condition': r'\text{Isotropic: } \langle I(t)\rangle_{\text{orientations}} = \text{constant}',
        
        'spherical_tensor_decomposition': r'\hat{\rho} = \sum_{k,q} \rho_k^q \hat{T}_k^q',
        
        'zeeman_hamiltonian': r'\hat{H}_Z = \mu_B g_J \hat{\mathbf{J}} \cdot \mathbf{B}',
        
        'magnetic_sublevel_coherence': r'\rho_{m,m\prime} = \langle J,m|\hat{\rho}|J,m\prime\rangle',
        
        'zeeman_beat_frequency': r'\omega_{m,m\prime} = \frac{\mu_B g_J B}{\hbar}(m - m\prime)',
        
        'polarization_tensor': r'P_{ij}^{(k)} = \sum_{m,m\prime} \rho_{m,m\prime} \langle J,m|T_{ij}^{(k)}|J,m\prime\rangle',
        
        'calcium_rydberg_states': r'|nS_{1/2}, m_j\rangle \text{ vs } |nP_{1/2}, m_j\rangle',
        
        'res2_crystal_anisotropy': r'\hat{H}_{\text{crystal}} = \sum_{i} \Delta_i |i\rangle\langle i|',
        
        'angular_dependence': r'I(\theta,\phi) = I_0 [1 + \beta P_2(\cos\theta)]',
        
        'spherical_averaging': r'\langle I \rangle = \frac{1}{4\pi}\int I(\theta,\phi) d\Omega'
    }
    
    # =================================================================
    # SCENE 4: Physical Mechanisms and Interference
    # =================================================================
    
    PHYSICAL_MECHANISMS = {
        'v_system_hamiltonian': r'\hat{H}_V = \hbar\omega_0|0\rangle\langle 0| + \hbar\omega_1|1\rangle\langle 1| + \hbar\omega_2|2\rangle\langle 2|',
        
        'lambda_system_hamiltonian': r'\hat{H}_\Lambda = \hbar\omega_1|1\rangle\langle 1| + \hbar\omega_2|2\rangle\langle 2| + \hbar\omega_0|0\rangle\langle 0|',
        
        'dipole_interaction': r'\hat{H}_{int} = -\vec{\mu} \cdot \vec{E} = -\sum_{i,j} \mu_{ij} E(t) (|i\rangle\langle j| + |j\rangle\langle i|)',
        
        'pathway_interference': r'A_{total} = A_1 e^{i\phi_1} + A_2 e^{i\phi_2}',
        
        'indistinguishable_pathways': r'|\text{final}\rangle = \alpha|\text{path 1}\rangle + \beta|\text{path 2}\rangle',
        
        'coherent_superposition': r'|\psi_{coherent}\rangle = \frac{1}{\sqrt{2}}(|1\rangle + |2\rangle)',
        
        'incoherent_mixture': r'\hat{\rho}_{incoherent} = \frac{1}{2}|1\rangle\langle 1| + \frac{1}{2}|2\rangle\langle 2|',
        
        'quantum_interference_contrast': r'V = \frac{I_{max} - I_{min}}{I_{max} + I_{min}} = 2|\rho_{12}|',
        
        'classical_interference_pattern': r'I_{classical} = I_1 + I_2 + 2\sqrt{I_1 I_2}\cos(\Delta\phi)',
        
        'quantum_interference_pattern': r'I_{quantum} = \langle\hat{E}^-\hat{E}^+\rangle = \text{Tr}[\hat{\rho}\hat{E}^-\hat{E}^+]'
    }
    
    # =================================================================
    # SCENE 5: Decoherence and Dephasing Effects
    # =================================================================
    
    DECOHERENCE_EFFECTS = {
        'system_bath_hamiltonian': r'\hat{H}_{total} = \hat{H}_S + \hat{H}_B + \hat{H}_{SB}',
        
        'system_bath_interaction': r'\hat{H}_{SB} = \sum_\alpha \hat{S}_\alpha \otimes \hat{B}_\alpha',
        
        'born_markov_approximation': r'\text{Born-Markov: } \tau_B \ll \tau_S \text{ and } \text{weak coupling}',
        
        'relaxation_rates': r'T_1^{-1} = \text{longitudinal relaxation rate}',
        
        'dephasing_rates': r'T_2^{-1} = \frac{1}{2}T_1^{-1} + T_2^{*-1}',
        
        'pure_dephasing': r'T_2^{*-1} = \text{pure dephasing rate}',
        
        'coherence_decay_general': r'\rho_{ij}(t) = \rho_{ij}(0) e^{-\Gamma_{ij} t} e^{-i\omega_{ij} t}',
        
        'decoherence_rate_formula': r'\Gamma_{ij} = \frac{\gamma_i + \gamma_j}{2} + \gamma_{ij}^{pure}',
        
        'environmental_spectral_density': r'J(\omega) = \sum_k g_k^2 \delta(\omega - \omega_k)',
        
        'phonon_decoherence': r'\gamma_{phonon} = \frac{2\pi}{\hbar} |g_{ph}|^2 n(\omega) \delta(\omega - \omega_{ph})',
        
        'photon_decoherence': r'\gamma_{photon} = \frac{2\pi}{\hbar} |g_{ph}|^2 [n(\omega) + 1]',
        
        'spin_bath_coupling': r'\hat{H}_{spin-bath} = \sum_k A_k \hat{S}_z \hat{I}_k^z',
        
        'coherence_envelope': r'|\rho_{12}(t)| = |\rho_{12}(0)| e^{-\Gamma_{12} t}',
        
        'platform_specific_timescales': r'T_2^{atom} > T_2^{solid} > T_2^{molecule}'
    }
    
    # =================================================================
    # SCENE 6: Experimental Detection and Measurement
    # =================================================================
    
    EXPERIMENTAL_DETECTION = {
        'pump_probe_signal': r'S(\tau) = \int_0^\infty I(t) I_{probe}(t+\tau) dt',
        
        'time_resolved_fluorescence': r'I(t) = I_0 \sum_i p_i e^{-\gamma_i t} [1 + V_i \cos(\omega_i t + \phi_i)]',
        
        'heterodyne_detection': r'I_{het}(t) = |E_s(t) + E_{LO} e^{i\omega_{LO}t}|^2',
        
        'homodyne_detection': r'I_{hom}(t) = |E_s(t) + E_{LO}|^2 = I_s + I_{LO} + 2\sqrt{I_s I_{LO}}\cos(\phi)',
        
        'quantum_efficiency': r'\eta = \frac{\text{detected photons}}{\text{incident photons}}',
        
        'shot_noise_limit': r'\Delta N = \sqrt{\langle N \rangle}',
        
        'signal_to_noise_ratio': r'SNR = \frac{S}{\sqrt{S + B}}',
        
        'detection_probability': r'P_{det} = 1 - e^{-\eta N_{photons}}',
        
        'timing_resolution': r'\Delta t_{res} = \frac{1}{\sqrt{N_{counts}} \cdot \text{bandwidth}}',
        
        'femtosecond_pulse_duration': r'\tau_{pulse} \sim 10-100 \text{ fs}',
        
        'spectral_bandwidth': r'\Delta\omega \cdot \Delta t \geq \frac{1}{2}',
        
        'autocorrelation_function': r'g^{(2)}(\tau) = \frac{\langle I(t)I(t+\tau)\rangle}{\langle I(t)\rangle^2}'
    }
    
    # =================================================================
    # SCENE 7: Interpretational Issues and Measurement
    # =================================================================
    
    INTERPRETATIONAL_ISSUES = {
        'measurement_problem': r'\text{Measurement: } |\psi\rangle \rightarrow |measurement\ outcome\rangle',
        
        'wave_function_collapse': r'|\psi\rangle = \sum_i c_i|i\rangle \xrightarrow{measurement} |j\rangle',
        
        'born_rule': r'P(j) = |\langle j|\psi\rangle|^2 = |c_j|^2',
        
        'quantum_to_classical_transition': r'\text{Quantum} \xrightarrow{\text{decoherence}} \text{Classical}',
        
        'decoherence_timescale': r't_{dec} \ll t_{observation}',
        
        'many_worlds_interpretation': r'|\psi\rangle_{total} = \sum_i |outcome_i\rangle_{system} \otimes |observer_i\rangle',
        
        'consistent_histories': r'P(history) = |\langle final|...|intermediate|...|initial\rangle|^2',
        
        'measurement_back_action': r'\hat{\rho}_{after} = \sum_m M_m \hat{\rho}_{before} M_m^\dagger',
        
        'quantum_zeno_effect': r'\text{Frequent measurements} \rightarrow \text{frozen evolution}',
        
        'complementarity_principle': r'\text{Wave-particle duality} \leftrightarrow \Delta x \cdot \Delta p \geq \frac{\hbar}{2}',
        
        'fundamental_limits': r'\text{Measurement precision} \propto \frac{1}{\sqrt{N_{particles}}}',
        
        'entanglement_role': r'|\psi\rangle_{AB} \neq |\psi\rangle_A \otimes |\psi\rangle_B'
    }
    
    # =================================================================
    # SCENE 8: Future Directions and Applications
    # =================================================================
    
    FUTURE_APPLICATIONS = {
        'atomic_clock_precision': r'\frac{\Delta f}{f} \sim 10^{-18} \text{ (fractional uncertainty)}',
        
        'quantum_sensing_advantage': r'\text{Sensitivity} \propto N^{-1/2} \text{ (classical)} \text{ vs } N^{-1} \text{ (quantum)}',
        
        'ramsey_interrogation': r'P = \frac{1}{2}[1 + \cos(\omega_0 T + \phi)]',
        
        'quantum_metrology_scaling': r'\Delta\phi \geq \frac{1}{\sqrt{N}} \text{ (SQL)} \text{ vs } \Delta\phi \geq \frac{1}{N} \text{ (HL)}',
        
        'biological_coherence_timescale': r'T_2^{bio} \sim 10^2 - 10^6 \text{ fs}',
        
        'quantum_transport_efficiency': r'\eta_{quantum} > \eta_{classical} \text{ for } T_2 > \tau_{transport}',
        
        'quantum_information_fidelity': r'F = \text{Tr}[\sqrt{\sqrt{\rho_{ideal}}\rho_{actual}\sqrt{\rho_{ideal}}}]',
        
        'quantum_error_correction_threshold': r'p_{error} < p_{threshold} \approx 10^{-4}',
        
        'quantum_supremacy_condition': r'T_{classical} > T_{universe} \text{ and } T_{quantum} < T_{feasible}',
        
        'entanglement_distribution_rate': r'R_{ent} = \frac{\eta^2 e^{-L/L_{att}}}{2\tau_{rep}}',
        
        'quantum_networking_fidelity': r'F_{network} = \prod_{links} F_{link}',
        
        'future_precision_goal': r'\frac{\Delta f}{f} \sim 10^{-19} \text{ (next generation atomic clocks)}'
    }
    
    # =================================================================
    # SUPPORTING MATHEMATICAL FUNCTIONS
    # =================================================================
    
    @staticmethod
    def create_equation_with_number(equation: str, number: str, **kwargs) -> VGroup:
        """
        Create numbered equation with consistent formatting.
        
        Parameters
        ----------
        equation : str
            LaTeX equation string
        number : str
            Equation number
        **kwargs
            Additional MathTex arguments
            
        Returns
        -------
        VGroup
            Formatted numbered equation
        """
        default_kwargs = {'font_size': 32, 'color': WHITE}
        default_kwargs.update(kwargs)
        
        equation_tex = MathTex(equation, **default_kwargs)
        equation_number = MathTex(f"({number})", font_size=24, color=LIGHT_GRAY)
        
        # Position equation number to the right
        equation_number.next_to(equation_tex, RIGHT, buff=1.0)
        
        return VGroup(equation_tex, equation_number)
    
    @staticmethod
    def create_equation_derivation(steps: List[str], **kwargs) -> VGroup:
        """
        Create step-by-step equation derivation.
        
        Parameters
        ----------
        steps : list
            List of equation steps in order
        **kwargs
            Additional formatting arguments
            
        Returns
        -------
        VGroup
            Formatted derivation steps
        """
        default_kwargs = {'font_size': 28, 'color': WHITE}
        default_kwargs.update(kwargs)
        
        derivation_steps = VGroup()
        
        for i, step in enumerate(steps):
            step_eq = MathTex(step, **default_kwargs)
            
            if i > 0:
                # Add equals sign or arrow
                if '\\rightarrow' in step or '\\Rightarrow' in step:
                    connector = MathTex('\\Rightarrow', font_size=24, color=YELLOW)
                else:
                    connector = MathTex('=', font_size=24, color=YELLOW)
                
                connector.next_to(derivation_steps[-1], DOWN, buff=0.2)
                step_eq.next_to(connector, DOWN, buff=0.2)
                derivation_steps.add(connector)
            
            derivation_steps.add(step_eq)
        
        return derivation_steps
    
    @staticmethod
    def create_highlighted_equation(equation: str, highlight_parts: List[str], 
                                   highlight_color: str = QUANTUM_GOLD, **kwargs) -> MathTex:
        """
        Create equation with highlighted terms.
        
        Parameters
        ----------
        equation : str
            LaTeX equation string
        highlight_parts : list
            Parts of equation to highlight
        highlight_color : str
            Color for highlighting
        **kwargs
            Additional MathTex arguments
            
        Returns
        -------
        MathTex
            Equation with highlighted terms
        """
        default_kwargs = {'font_size': 32, 'color': WHITE}
        default_kwargs.update(kwargs)
        
        equation_tex = MathTex(equation, **default_kwargs)
        
        # Highlight specified parts
        for part in highlight_parts:
            try:
                equation_tex.set_color_by_tex(part, highlight_color)
            except:
                # If tex matching fails, skip this highlight
                pass
        
        return equation_tex
    
    @staticmethod
    def create_equation_with_explanation(equation: str, explanation: str, **kwargs) -> VGroup:
        """
        Create equation paired with explanatory text.
        
        Parameters
        ----------
        equation : str
            LaTeX equation string
        explanation : str
            Plain text explanation
        **kwargs
            Additional formatting arguments
            
        Returns
        -------
        VGroup
            Equation and explanation together
        """
        equation_kwargs = kwargs.get('equation_kwargs', {'font_size': 32, 'color': WHITE})
        text_kwargs = kwargs.get('text_kwargs', {'font_size': 20, 'color': LIGHT_GRAY})
        
        equation_tex = MathTex(equation, **equation_kwargs)
        explanation_text = Text(explanation, **text_kwargs)
        
        explanation_text.next_to(equation_tex, DOWN, buff=0.5)
        
        return VGroup(equation_tex, explanation_text)
    
    @staticmethod
    def get_all_expressions_by_scene() -> Dict[str, Dict[str, str]]:
        """
        Get all mathematical expressions organized by scene.
        
        Returns
        -------
        dict
            Dictionary mapping scene names to expression dictionaries
        """
        return {
            'scene_1_classical_vs_quantum': QuantumBeatExpressions.CLASSICAL_BEATING,
            'scene_2_mathematical_formalism': QuantumBeatExpressions.DENSITY_MATRIX_FORMALISM,
            'scene_3_isotropic_anisotropic': QuantumBeatExpressions.ISOTROPIC_ANISOTROPIC,
            'scene_4_physical_mechanisms': QuantumBeatExpressions.PHYSICAL_MECHANISMS,
            'scene_5_decoherence_effects': QuantumBeatExpressions.DECOHERENCE_EFFECTS,
            'scene_6_experimental_detection': QuantumBeatExpressions.EXPERIMENTAL_DETECTION,
            'scene_7_interpretational_issues': QuantumBeatExpressions.INTERPRETATIONAL_ISSUES,
            'scene_8_future_applications': QuantumBeatExpressions.FUTURE_APPLICATIONS
        }
    
    @staticmethod
    def search_expressions(keyword: str) -> List[Tuple[str, str, str]]:
        """
        Search for expressions containing a keyword.
        
        Parameters
        ----------
        keyword : str
            Search keyword
            
        Returns
        -------
        list
            List of (scene, expression_name, expression) tuples
        """
        results = []
        all_expressions = QuantumBeatExpressions.get_all_expressions_by_scene()
        
        for scene, expressions in all_expressions.items():
            for name, expression in expressions.items():
                if keyword.lower() in expression.lower() or keyword.lower() in name.lower():
                    results.append((scene, name, expression))
        
        return results

# Convenience functions for quick access to common equation types
def get_beat_frequency_equation() -> str:
    """Get the fundamental beat frequency equation."""
    return QuantumBeatExpressions.CLASSICAL_BEATING['quantum_energy_difference']

def get_master_equation() -> str:
    """Get the quantum master equation."""
    return QuantumBeatExpressions.DENSITY_MATRIX_FORMALISM['master_equation']

def get_coherence_decay_equation() -> str:
    """Get the coherence decay equation."""
    return QuantumBeatExpressions.DENSITY_MATRIX_FORMALISM['off_diagonal_decay']

def get_decoherence_rate_equation() -> str:
    """Get the decoherence rate formula."""
    return QuantumBeatExpressions.DECOHERENCE_EFFECTS['decoherence_rate_formula']

def test_mathematical_expressions():
    """Test function to verify mathematical expressions work correctly."""
    print("Testing mathematical expressions...")
    
    # Test basic equation creation
    eq = QuantumBeatExpressions.create_equation_with_number(
        get_beat_frequency_equation(), "1"
    )
    print("✓ Numbered equation creation successful")
    
    # Test derivation steps
    steps = [
        get_beat_frequency_equation(),
        r'\omega_{beat} = \Delta\omega',
        r'\omega_{beat} = \frac{E_2 - E_1}{\hbar}'
    ]
    derivation = QuantumBeatExpressions.create_equation_derivation(steps)
    print("✓ Equation derivation creation successful")
    
    # Test highlighted equation
    highlighted = QuantumBeatExpressions.create_highlighted_equation(
        get_master_equation(), ['\\hat{H}', '\\hat{\\rho}']
    )
    print("✓ Highlighted equation creation successful")
    
    # Test expression search
    results = QuantumBeatExpressions.search_expressions('coherence')
    print(f"✓ Expression search found {len(results)} results")
    
    print("All mathematical expression tests passed!")

if __name__ == "__main__":
    test_mathematical_expressions()