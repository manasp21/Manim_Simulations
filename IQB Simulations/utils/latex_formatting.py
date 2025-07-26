"""
Standardized LaTeX formatting for quantum mechanical equations and expressions.

This module provides consistent formatting for quantum physics notation, operators,
mathematical expressions, and complex derivations used throughout the animation.
"""

from manim import *
import numpy as np
from typing import Dict, List, Union, Optional

class QuantumLatexFormatter:
    """
    Centralized LaTeX formatting for quantum mechanical expressions.
    
    Provides standardized formatting for operators, states, equations, and
    mathematical derivations commonly used in quantum physics.
    """
    
    # Standard quantum mechanical operators
    OPERATORS = {
        'hamiltonian': r'\hat{H}',
        'density_matrix': r'\hat{\rho}',
        'pauli_x': r'\hat{\sigma}_x',
        'pauli_y': r'\hat{\sigma}_y', 
        'pauli_z': r'\hat{\sigma}_z',
        'pauli_plus': r'\hat{\sigma}_+',
        'pauli_minus': r'\hat{\sigma}_-',
        'creation': r'\hat{a}^\dagger',
        'annihilation': r'\hat{a}',
        'number': r'\hat{n}',
        'position': r'\hat{x}',
        'momentum': r'\hat{p}',
        'angular_momentum': r'\hat{L}',
        'spin': r'\hat{S}',
        'electric_field': r'\hat{E}',
        'magnetic_field': r'\hat{B}'
    }
    
    # Physical constants and parameters
    CONSTANTS = {
        'hbar': r'\hbar',
        'planck': r'h',
        'speed_of_light': r'c',
        'electron_charge': r'e',
        'electron_mass': r'm_e',
        'proton_mass': r'm_p',
        'bohr_radius': r'a_0',
        'fine_structure': r'\alpha',
        'boltzmann': r'k_B',
        'permeability': r'\mu_0',
        'permittivity': r'\varepsilon_0'
    }
    
    # Greek letters commonly used in quantum mechanics
    GREEK_LETTERS = {
        'alpha': r'\alpha',
        'beta': r'\beta', 
        'gamma': r'\gamma',
        'delta': r'\delta',
        'epsilon': r'\varepsilon',
        'zeta': r'\zeta',
        'eta': r'\eta',
        'theta': r'\theta',
        'iota': r'\iota',
        'kappa': r'\kappa',
        'lambda': r'\lambda',
        'mu': r'\mu',
        'nu': r'\nu',
        'xi': r'\xi',
        'pi': r'\pi',
        'rho': r'\rho',
        'sigma': r'\sigma',
        'tau': r'\tau',
        'upsilon': r'\upsilon',
        'phi': r'\varphi',
        'chi': r'\chi',
        'psi': r'\psi',
        'omega': r'\omega',
        'Gamma': r'\Gamma',
        'Delta': r'\Delta',
        'Theta': r'\Theta',
        'Lambda': r'\Lambda',
        'Xi': r'\Xi',
        'Pi': r'\Pi',
        'Sigma': r'\Sigma',
        'Upsilon': r'\Upsilon',
        'Phi': r'\Phi',
        'Psi': r'\Psi',
        'Omega': r'\Omega'
    }
    
    @staticmethod
    def quantum_state(state: str, subscript: Optional[str] = None) -> str:
        """
        Format quantum state in Dirac notation.
        
        Parameters
        ----------
        state : str
            State label (e.g., '0', '1', 'up', 'down')
        subscript : str, optional
            Subscript for the state
            
        Returns
        -------
        str
            Formatted LaTeX string for the quantum state
        """
        if subscript:
            return rf'|{state}\rangle_{{{subscript}}}'
        else:
            return rf'|{state}\rangle'
    
    @staticmethod
    def bra_state(state: str, subscript: Optional[str] = None) -> str:
        """
        Format bra state in Dirac notation.
        
        Parameters
        ----------
        state : str
            State label
        subscript : str, optional
            Subscript for the state
            
        Returns
        -------
        str
            Formatted LaTeX string for the bra state
        """
        if subscript:
            return rf'\langle{state}|_{{{subscript}}}'
        else:
            return rf'\langle{state}|'
    
    @staticmethod
    def expectation_value(operator: str, state: str) -> str:
        """
        Format expectation value notation.
        
        Parameters
        ----------
        operator : str
            Operator (will be formatted with hat)
        state : str
            State for expectation value
            
        Returns
        -------
        str
            Formatted expectation value
        """
        return rf'\langle{state}|\hat{{{operator}}}|{state}\rangle'
    
    @staticmethod
    def matrix_element(operator: str, bra_state: str, ket_state: str) -> str:
        """
        Format matrix element notation.
        
        Parameters
        ----------
        operator : str
            Operator name
        bra_state : str
            Bra state
        ket_state : str
            Ket state
            
        Returns
        -------
        str
            Formatted matrix element
        """
        return rf'\langle{bra_state}|\hat{{{operator}}}|{ket_state}\rangle'
    
    @staticmethod
    def commutator(op1: str, op2: str) -> str:
        """
        Format commutator bracket.
        
        Parameters
        ----------
        op1, op2 : str
            Operator names
            
        Returns
        -------
        str
            Formatted commutator
        """
        return rf'[\hat{{{op1}}}, \hat{{{op2}}}]'
    
    @staticmethod
    def anticommutator(op1: str, op2: str) -> str:
        """
        Format anticommutator bracket.
        
        Parameters
        ----------
        op1, op2 : str
            Operator names
            
        Returns
        -------
        str
            Formatted anticommutator
        """
        return rf'\{{\hat{{{op1}}}, \hat{{{op2}}}\}}'
    
    @staticmethod
    def time_evolution(time_var: str = 't') -> str:
        """
        Format time evolution operator.
        
        Parameters
        ----------
        time_var : str
            Time variable symbol
            
        Returns
        -------
        str
            Formatted time evolution operator
        """
        return rf'e^{{-i\hat{{H}}{time_var}/\hbar}}'
    
    @staticmethod
    def density_matrix_element(i: Union[int, str], j: Union[int, str]) -> str:
        """
        Format density matrix element.
        
        Parameters
        ----------
        i, j : int or str
            Matrix indices
            
        Returns
        -------
        str
            Formatted density matrix element
        """
        return rf'\rho_{{{i}{j}}}'
    
    @staticmethod
    def coherence_term(i: Union[int, str], j: Union[int, str], 
                      time_dep: bool = True, time_var: str = 't') -> str:
        """
        Format quantum coherence term.
        
        Parameters
        ----------
        i, j : int or str
            State indices
        time_dep : bool
            Whether to include time dependence
        time_var : str
            Time variable
            
        Returns
        -------
        str
            Formatted coherence term
        """
        if time_dep:
            return rf'\rho_{{{i}{j}}}({time_var})'
        else:
            return rf'\rho_{{{i}{j}}}'
    
    @staticmethod 
    def master_equation(dissipator: bool = True) -> str:
        """
        Format master equation.
        
        Parameters
        ----------
        dissipator : bool
            Whether to include dissipator terms
            
        Returns
        -------
        str
            Formatted master equation
        """
        base = r'\frac{d\hat{\rho}}{dt} = -\frac{i}{\hbar}[\hat{H}, \hat{\rho}]'
        
        if dissipator:
            base += rf' + \mathcal{{L}}_{{diss}}[\hat{{\rho}}]'
        
        return base
    
    @staticmethod
    def lindblad_dissipator(jump_op: str = 'L') -> str:
        """
        Format Lindblad dissipator.
        
        Parameters
        ----------
        jump_op : str
            Jump operator symbol
            
        Returns
        -------
        str
            Formatted Lindblad dissipator
        """
        return (rf'\mathcal{{L}}_{{diss}}[\hat{{\rho}}] = \sum_i \gamma_i \left('
                rf'\hat{{{jump_op}}}_i \hat{{\rho}} \hat{{{jump_op}}}_i^\dagger - '
                rf'\frac{{1}}{{2}} \{{\hat{{{jump_op}}}_i^\dagger \hat{{{jump_op}}}_i, \hat{{\rho}}\}}'
                rf'\right)')
    
    @staticmethod
    def beat_signal_intensity(detailed: bool = False) -> str:
        """
        Format quantum beat signal intensity.
        
        Parameters
        ----------
        detailed : bool
            Whether to show detailed form with all terms
            
        Returns
        -------
        str
            Formatted beat intensity equation
        """
        if detailed:
            return (rf'I(t) = \gamma_1 p_1 e^{{-\gamma_1 t}} + \gamma_2 p_2 e^{{-\gamma_2 t}} + '
                   rf'2\sqrt{{\gamma_1 \gamma_2 p_1 p_2}} e^{{-\Gamma_{{12}} t}} '
                   rf'\cos(\Delta t - \phi)')
        else:
            return rf'I(t) = I_1(t) + I_2(t) + I_{{beat}}(t)'
    
    @staticmethod
    def superposition_state(coeffs: List[str], states: List[str], 
                           time_dep: bool = False, time_var: str = 't') -> str:
        """
        Format superposition state.
        
        Parameters
        ----------
        coeffs : list
            Coefficient symbols
        states : list  
            State labels
        time_dep : bool
            Whether to include time dependence
        time_var : str
            Time variable
            
        Returns
        -------
        str
            Formatted superposition state
        """
        terms = []
        for coeff, state in zip(coeffs, states):
            if time_dep:
                term = rf'{coeff} e^{{-i\omega_{{{state}}} {time_var}}} |{state}\rangle'
            else:
                term = rf'{coeff} |{state}\rangle'
            terms.append(term)
        
        return rf'|\psi\rangle = ' + ' + '.join(terms)
    
    @staticmethod
    def bloch_vector() -> str:
        """Format Bloch vector representation."""
        return rf'\vec{{r}} = \langle \hat{{\vec{{\sigma}}}} \rangle = (r_x, r_y, r_z)'
    
    @staticmethod
    def fidelity(rho1: str = r'\rho_1', rho2: str = r'\rho_2') -> str:
        """
        Format quantum fidelity.
        
        Parameters
        ----------
        rho1, rho2 : str
            Density matrix symbols
            
        Returns
        -------
        str
            Formatted fidelity expression
        """
        return rf'F({rho1}, {rho2}) = \text{{Tr}}\left(\sqrt{{\sqrt{{{rho1}}} {rho2} \sqrt{{{rho1}}}}}\right)'
    
    @staticmethod
    def von_neumann_entropy(rho: str = r'\rho') -> str:
        """
        Format von Neumann entropy.
        
        Parameters
        ----------
        rho : str
            Density matrix symbol
            
        Returns
        -------
        str
            Formatted entropy expression
        """
        return rf'S({rho}) = -\text{{Tr}}({rho} \log {rho})'
    
    @staticmethod
    def create_equation_array(equations: List[str], align_char: str = '=') -> str:
        """
        Create aligned equation array.
        
        Parameters
        ----------
        equations : list
            List of equation strings
        align_char : str
            Character to align on
            
        Returns
        -------
        str
            Formatted equation array
        """
        formatted_eqs = []
        for eq in equations:
            # Replace alignment character with LaTeX alignment
            formatted_eq = eq.replace(align_char, f'&{align_char}')
            formatted_eqs.append(formatted_eq)
        
        return r'\begin{align}' + r'\\'.join(formatted_eqs) + r'\end{align}'
    
    @staticmethod
    def create_matrix(elements: List[List[str]], bracket_type: str = 'pmatrix') -> str:
        """
        Create formatted matrix.
        
        Parameters
        ----------
        elements : list of lists
            Matrix elements
        bracket_type : str
            Type of brackets ('pmatrix', 'bmatrix', 'vmatrix', etc.)
            
        Returns
        -------
        str
            Formatted matrix
        """
        rows = []
        for row in elements:
            rows.append(' & '.join(row))
        
        matrix_content = r' \\ '.join(rows)
        return rf'\begin{{{bracket_type}}} {matrix_content} \end{{{bracket_type}}}'

# Predefined common expressions for quantum beats
QUANTUM_BEAT_EXPRESSIONS = {
    'hamiltonian_v_system': (
        rf'\hat{{H}} = \hbar\omega_0 |0\rangle\langle 0| + \hbar\omega_1 |1\rangle\langle 1| + '
        rf'\hbar\omega_2 |2\rangle\langle 2|'
    ),
    
    'beat_frequency': r'\Delta = \omega_2 - \omega_1 = \frac{E_2 - E_1}{\hbar}',
    
    'coherence_decay': r'\rho_{12}(t) = \rho_{12}(0) e^{-i\Delta t - \Gamma_{12} t}',
    
    'decoherence_rate': r'\Gamma_{12} = \frac{\gamma_1 + \gamma_2}{2}',
    
    'beat_visibility': r'V = \frac{2\sqrt{p_1 p_2}}{p_1 + p_2}',
    
    'rotating_frame': r'\tilde{H} = \hat{H} - \hbar\omega_L \sum_i |i\rangle\langle i|',
    
    'dipole_interaction': (
        r'\hat{H}_{int} = -\vec{\mu} \cdot \vec{E} = -\sum_{i,j} \mu_{ij} E(t) '
        r'(|i\rangle\langle j| + |j\rangle\langle i|)'
    ),
    
    'population_dynamics': (
        r'\frac{dp_i}{dt} = -\gamma_i p_i + \sum_{j>i} \gamma_{ji} p_j'
    ),
    
    'coherence_dynamics': (
        r'\frac{d\rho_{ij}}{dt} = -i\omega_{ij} \rho_{ij} - \Gamma_{ij} \rho_{ij}'
    )
}

def create_quantum_equation(equation_key: str, **kwargs) -> MathTex:
    """
    Create a formatted MathTex object for common quantum equations.
    
    Parameters
    ----------
    equation_key : str
        Key for predefined equation
    **kwargs
        Additional arguments for MathTex
        
    Returns
    -------
    MathTex
        Formatted equation object
    """
    if equation_key in QUANTUM_BEAT_EXPRESSIONS:
        equation_str = QUANTUM_BEAT_EXPRESSIONS[equation_key]
    else:
        raise ValueError(f"Unknown equation key: {equation_key}")
    
    # Set default styling
    default_kwargs = {
        'font_size': 36,
        'color': WHITE
    }
    default_kwargs.update(kwargs)
    
    return MathTex(equation_str, **default_kwargs)

def format_complex_number(real: float, imag: float, 
                         precision: int = 2, 
                         exponential: bool = False) -> str:
    """
    Format complex number for LaTeX display.
    
    Parameters
    ----------
    real, imag : float
        Real and imaginary parts
    precision : int
        Decimal precision
    exponential : bool
        Whether to use exponential notation
        
    Returns
    -------
    str
        Formatted complex number string
    """
    if exponential:
        if imag >= 0:
            return rf'{real:.{precision}e} + {imag:.{precision}e}i'
        else:
            return rf'{real:.{precision}e} - {abs(imag):.{precision}e}i'
    else:
        if imag >= 0:
            return rf'{real:.{precision}f} + {imag:.{precision}f}i'
        else:
            return rf'{real:.{precision}f} - {abs(imag):.{precision}f}i'

def test_latex_formatting():
    """Test function to verify LaTeX formatting works correctly."""
    formatter = QuantumLatexFormatter()
    
    # Test basic quantum state
    print("Quantum state:", formatter.quantum_state('psi', 'n'))
    
    # Test superposition
    coeffs = ['c_1', 'c_2'] 
    states = ['0', '1']
    print("Superposition:", formatter.superposition_state(coeffs, states, time_dep=True))
    
    # Test matrix element
    print("Matrix element:", formatter.matrix_element('H', '1', '2'))
    
    # Test beat equation
    print("Beat signal:", formatter.beat_signal_intensity(detailed=True))
    
    print("LaTeX formatting test completed successfully!")

if __name__ == "__main__":
    test_latex_formatting()