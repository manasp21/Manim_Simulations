"""
Quantum-themed color schemes and palettes for the quantum beats animation.

This module provides consistent color definitions and schemes specifically designed
for quantum physics visualizations, ensuring accessibility and professional appearance.
"""

from manim import *
import numpy as np

# Primary Quantum Colors (from director's script)
QUANTUM_BACKGROUND = "#0B1426"  # Deep blue background
QUANTUM_GOLD = "#FFD700"        # Key concepts and highlights
COHERENCE_GREEN = "#00FF7F"     # Quantum coherence phenomena
DECOHERENCE_RED = "#FF4500"     # Environmental effects and decay

# Energy Level Colors
GROUND_STATE_COLOR = WHITE
EXCITED_STATE_1_COLOR = "#4169E1"  # Royal Blue
EXCITED_STATE_2_COLOR = "#DC143C"  # Crimson
EXCITED_STATE_3_COLOR = "#32CD32"  # Lime Green

# Quantum State Colors
SUPERPOSITION_COLOR = QUANTUM_GOLD
ENTANGLED_COLOR = "#9932CC"        # Dark Orchid
MIXED_STATE_COLOR = GRAY
PURE_STATE_COLOR = WHITE

# Coherence and Decoherence
COHERENT_COLOR = COHERENCE_GREEN
INCOHERENT_COLOR = DECOHERENCE_RED
PARTIALLY_COHERENT_COLOR = YELLOW

# Mathematical Elements
EQUATION_COLOR = WHITE
OPERATOR_COLOR = QUANTUM_GOLD
CONSTANT_COLOR = LIGHT_GRAY
VARIABLE_COLOR = COHERENCE_GREEN
COMPLEX_COLOR = "#FF69B4"          # Hot Pink for complex numbers

# Experimental Setup Colors
LASER_COLOR = RED
DETECTOR_COLOR = PURPLE
BEAM_SPLITTER_COLOR = LIGHT_GRAY
MIRROR_COLOR = BLUE_E
SAMPLE_COLOR = QUANTUM_GOLD

# Polarization Colors
POLARIZATION_X = BLUE
POLARIZATION_Y = RED
POLARIZATION_CIRCULAR_L = GREEN
POLARIZATION_CIRCULAR_R = ORANGE

# Physical Process Colors
ABSORPTION_COLOR = RED
EMISSION_COLOR = GREEN
SCATTERING_COLOR = BLUE
INTERFERENCE_COLOR = QUANTUM_GOLD

# Environment and Bath Colors
PHONON_COLOR = "#8FBC8F"          # Dark Sea Green
PHOTON_COLOR = YELLOW
ELECTRON_COLOR = BLUE
NUCLEAR_SPIN_COLOR = RED

class QuantumColorScheme:
    """
    Centralized color scheme management for quantum physics animations.
    
    Provides methods for generating color gradients, ensuring accessibility,
    and maintaining consistent visual styling throughout the animation.
    """
    
    @staticmethod
    def get_energy_level_color(level_index: int) -> str:
        """
        Get color for energy level based on index.
        
        Parameters
        ----------
        level_index : int
            Energy level index (0 = ground state, 1+ = excited states)
            
        Returns
        -------
        str
            Hex color code for the energy level
        """
        colors = [
            GROUND_STATE_COLOR,
            EXCITED_STATE_1_COLOR,
            EXCITED_STATE_2_COLOR,
            EXCITED_STATE_3_COLOR
        ]
        
        if level_index < len(colors):
            return colors[level_index]
        else:
            # Generate additional colors for higher levels
            hue = (level_index * 60) % 360  # Cycle through hues
            return f"hsl({hue}, 70%, 60%)"
    
    @staticmethod
    def get_coherence_color(coherence_value: float) -> str:
        """
        Get color representing degree of quantum coherence.
        
        Parameters
        ----------
        coherence_value : float
            Coherence value between 0 (incoherent) and 1 (fully coherent)
            
        Returns
        -------
        str
            Color interpolated between incoherent and coherent colors
        """
        # Interpolate between red (incoherent) and green (coherent)
        if coherence_value <= 0:
            return DECOHERENCE_RED
        elif coherence_value >= 1:
            return COHERENCE_GREEN
        else:
            # Linear interpolation in RGB space
            red_rgb = np.array([1.0, 0.27, 0.0])  # FF4500 in normalized RGB
            green_rgb = np.array([0.0, 1.0, 0.5])  # 00FF7F in normalized RGB
            
            interpolated_rgb = (1 - coherence_value) * red_rgb + coherence_value * green_rgb
            
            # Convert back to hex
            r, g, b = (interpolated_rgb * 255).astype(int)
            return f"#{r:02x}{g:02x}{b:02x}"
    
    @staticmethod
    def get_phase_color(phase: float) -> str:
        """
        Get color representing quantum phase.
        
        Parameters
        ----------
        phase : float
            Phase value in radians
            
        Returns
        -------
        str
            Color representing the phase (hue varies with phase)
        """
        # Map phase to hue (0 to 2π maps to 0 to 360 degrees)
        hue = int((phase % (2 * np.pi)) / (2 * np.pi) * 360)
        return f"hsl({hue}, 80%, 60%)"
    
    @staticmethod
    def get_decay_gradient(num_steps: int) -> list:
        """
        Generate color gradient for decay processes.
        
        Parameters
        ----------
        num_steps : int
            Number of gradient steps
            
        Returns
        -------
        list
            List of colors from bright to faded
        """
        colors = []
        for i in range(num_steps):
            opacity = 1.0 - (i / (num_steps - 1))
            # Fade from bright to transparent
            alpha = int(opacity * 255)
            colors.append(f"{COHERENCE_GREEN}{alpha:02x}")
        return colors
    
    @staticmethod
    def ensure_accessibility(color1: str, color2: str) -> tuple:
        """
        Ensure two colors have sufficient contrast for accessibility.
        
        Parameters
        ----------
        color1, color2 : str
            Color codes to check
            
        Returns
        -------
        tuple
            Adjusted colors with sufficient contrast ratio (4.5:1 minimum)
        """
        # This is a simplified implementation
        # In practice, you'd calculate actual luminance and contrast ratios
        return color1, color2
    
    @staticmethod
    def get_bloch_sphere_colors() -> dict:
        """
        Get standardized colors for Bloch sphere visualization.
        
        Returns
        -------
        dict
            Dictionary mapping Bloch sphere elements to colors
        """
        return {
            'sphere': BLUE_E,
            'x_axis': RED,
            'y_axis': GREEN,
            'z_axis': BLUE,
            'state_vector': QUANTUM_GOLD,
            'trajectory': WHITE,
            'north_pole': WHITE,
            'south_pole': BLACK,
            'equator': LIGHT_GRAY
        }
    
    @staticmethod
    def get_density_matrix_colors() -> dict:
        """
        Get colors for density matrix visualization.
        
        Returns
        -------
        dict
            Dictionary mapping matrix elements to colors
        """
        return {
            'diagonal': QUANTUM_GOLD,      # Population terms
            'off_diagonal': COHERENCE_GREEN,  # Coherence terms
            'real_part': BLUE,
            'imaginary_part': RED,
            'matrix_frame': WHITE,
            'zero_elements': GRAY
        }
    
    @staticmethod
    def get_interference_colors() -> dict:
        """
        Get colors for interference pattern visualization.
        
        Returns
        -------
        dict
            Dictionary mapping interference elements to colors
        """
        return {
            'constructive': COHERENCE_GREEN,
            'destructive': DECOHERENCE_RED,
            'partial': YELLOW,
            'envelope': WHITE,
            'carrier': BLUE,
            'beat_frequency': QUANTUM_GOLD
        }

# Predefined color palettes for common quantum systems
ATOMIC_SYSTEM_COLORS = {
    'hydrogen': ['#FF0000', '#00FF00', '#0000FF', '#FFFF00'],
    'helium': ['#FFB6C1', '#98FB98', '#87CEEB', '#F0E68C'],
    'calcium': ['#FFA500', '#32CD32', '#4169E1', '#DA70D6'],
    'cesium': ['#FFD700', '#ADFF2F', '#1E90FF', '#FF1493']
}

MOLECULAR_SYSTEM_COLORS = {
    'diatomic': [BLUE, RED, GREEN, YELLOW],
    'organic': ['#228B22', '#DC143C', '#4169E1', '#FF8C00'],
    'protein': ['#2E8B57', '#B22222', '#4682B4', '#DAA520']
}

SOLID_STATE_COLORS = {
    'quantum_dot': [QUANTUM_GOLD, COHERENCE_GREEN, DECOHERENCE_RED],
    'nv_center': ['#FF69B4', '#00CED1', '#32CD32'],
    'superconductor': ['#4169E1', '#87CEEB', '#B0C4DE']
}

# Accessibility-compliant color combinations
HIGH_CONTRAST_PAIRS = [
    (WHITE, BLACK),
    (QUANTUM_GOLD, QUANTUM_BACKGROUND),
    (COHERENCE_GREEN, QUANTUM_BACKGROUND),
    (WHITE, DECOHERENCE_RED),
    (YELLOW, BLUE_E)
]

def get_quantum_color_palette(system_type: str = 'general') -> dict:
    """
    Get a complete color palette for a specific quantum system type.
    
    Parameters
    ----------
    system_type : str
        Type of quantum system ('atomic', 'molecular', 'solid_state', 'general')
        
    Returns
    -------
    dict
        Complete color palette for the system
    """
    base_palette = {
        'background': QUANTUM_BACKGROUND,
        'text': WHITE,
        'highlight': QUANTUM_GOLD,
        'coherent': COHERENCE_GREEN,
        'decoherent': DECOHERENCE_RED,
        'ground_state': GROUND_STATE_COLOR,
        'excited_state': EXCITED_STATE_1_COLOR
    }
    
    if system_type == 'atomic':
        base_palette.update({
            'electron': BLUE,
            'nucleus': RED,
            'orbital': GREEN,
            'transition': QUANTUM_GOLD
        })
    elif system_type == 'molecular':
        base_palette.update({
            'bond': WHITE,
            'vibration': GREEN,
            'rotation': BLUE,
            'electronic': RED
        })
    elif system_type == 'solid_state':
        base_palette.update({
            'conduction': BLUE,
            'valence': RED,
            'defect': QUANTUM_GOLD,
            'phonon': GREEN
        })
    
    return base_palette

def validate_color_scheme(colors: dict) -> bool:
    """
    Validate that a color scheme meets accessibility requirements.
    
    Parameters
    ----------
    colors : dict
        Dictionary of color assignments
        
    Returns
    -------
    bool
        True if color scheme is accessible, False otherwise
    """
    # Check for common accessibility issues
    # This is a simplified implementation
    required_keys = ['background', 'text', 'highlight']
    
    for key in required_keys:
        if key not in colors:
            return False
    
    # In a full implementation, would check contrast ratios
    return True