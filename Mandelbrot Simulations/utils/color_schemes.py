"""
Advanced color schemes for fractal visualizations.

This module provides sophisticated coloring algorithms that transform
escape-time data into beautiful, mathematically-inspired color palettes.
Designed for high-quality artistic rendering of fractal sets.

Features:
- Multiple artistic color palettes (fire, ice, rainbow, cosmic, etc.)
- Smooth color interpolation algorithms
- Histogram equalization for balanced colors
- Color cycling for animation effects
- Accessibility-compliant high-contrast options
"""

import numpy as np
import colorsys
from typing import Tuple, List, Dict, Union, Callable
from enum import Enum
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

class ColorPalette(Enum):
    """Enumeration of available color palettes."""
    FIRE = "fire"
    ICE = "ice"
    RAINBOW = "rainbow"
    COSMIC = "cosmic"
    FOREST = "forest"
    OCEAN = "ocean"
    SUNSET = "sunset"
    MONOCHROME = "monochrome"
    QUANTUM_GOLD = "quantum_gold"
    ELECTRIC = "electric"
    MAGMA = "magma"
    VIRIDIS = "viridis"
    WHITE_ON_BLACK = "white_on_black"

class FractalColorizer:
    """
    Advanced color scheme generator for fractal visualizations.
    
    Transforms escape-time data into beautiful color representations
    using mathematically-inspired palettes and smooth interpolation.
    """
    
    def __init__(self, palette: Union[ColorPalette, str] = ColorPalette.FIRE,
                 gamma: float = 1.0, contrast: float = 1.0):
        """
        Initialize fractal colorizer.
        
        Parameters
        ----------
        palette : ColorPalette or str
            Color palette to use
        gamma : float
            Gamma correction factor (>1 brightens, <1 darkens)
        contrast : float
            Contrast enhancement factor
        """
        self.palette = ColorPalette(palette) if isinstance(palette, str) else palette
        self.gamma = gamma
        self.contrast = contrast
        self._color_functions = self._initialize_color_functions()
    
    def colorize_escape_data(self, escape_data: np.ndarray, 
                           max_iterations: int = 256,
                           cycle_speed: float = 1.0,
                           use_histogram_equalization: bool = False) -> np.ndarray:
        """
        Convert escape-time data to RGB color array.
        
        Parameters
        ----------
        escape_data : np.ndarray
            2D array of escape counts from fractal calculation
        max_iterations : int
            Maximum iteration count used in fractal calculation
        cycle_speed : float
            Speed of color cycling (for animation)
        use_histogram_equalization : bool
            Whether to apply histogram equalization for balanced colors
            
        Returns
        -------
        np.ndarray
            RGB color array with shape (height, width, 3)
        """
        # Normalize escape data to [0, 1] range
        normalized_data = self._normalize_escape_data(escape_data, max_iterations)
        
        # Apply histogram equalization if requested
        if use_histogram_equalization:
            normalized_data = self._histogram_equalization(normalized_data)
        
        # Apply gamma correction and contrast enhancement
        normalized_data = self._apply_gamma_contrast(normalized_data)
        
        # Generate colors using selected palette
        color_func = self._color_functions[self.palette]
        rgb_array = color_func(normalized_data, cycle_speed)
        
        return rgb_array
    
    def create_palette_preview(self, width: int = 512, height: int = 64) -> np.ndarray:
        """
        Create a preview strip showing the color palette.
        
        Parameters
        ----------
        width : int
            Width of the preview strip
        height : int
            Height of the preview strip
            
        Returns
        -------
        np.ndarray
            RGB array showing color palette gradient
        """
        # Create gradient from 0 to 1
        gradient = np.linspace(0, 1, width)
        gradient_2d = np.tile(gradient, (height, 1))
        
        # Apply color function
        color_func = self._color_functions[self.palette]
        rgb_array = color_func(gradient_2d, 1.0)
        
        return rgb_array
    
    def _normalize_escape_data(self, escape_data: np.ndarray, max_iterations: int) -> np.ndarray:
        """Normalize escape data to [0, 1] range with special handling for set points."""
        normalized = escape_data.copy()
        
        # Points in the set (reached max_iterations) get value 0
        in_set_mask = (escape_data >= max_iterations)
        normalized[in_set_mask] = 0.0
        
        # Points outside the set get normalized escape count
        outside_set_mask = ~in_set_mask
        if np.any(outside_set_mask):
            min_escape = np.min(escape_data[outside_set_mask])
            max_escape = np.max(escape_data[outside_set_mask])
            
            if max_escape > min_escape:
                normalized[outside_set_mask] = (escape_data[outside_set_mask] - min_escape) / (max_escape - min_escape)
            else:
                normalized[outside_set_mask] = 0.5
        
        return normalized
    
    def _histogram_equalization(self, data: np.ndarray) -> np.ndarray:
        """Apply histogram equalization for more balanced color distribution."""
        # Flatten data for histogram calculation
        flat_data = data.flatten()
        
        # Calculate histogram
        hist, bins = np.histogram(flat_data, bins=256, range=(0, 1))
        
        # Calculate cumulative distribution function
        cdf = hist.cumsum()
        cdf = cdf / cdf[-1]  # Normalize to [0, 1]
        
        # Apply equalization
        equalized = np.interp(flat_data, bins[:-1], cdf)
        
        return equalized.reshape(data.shape)
    
    def _apply_gamma_contrast(self, data: np.ndarray) -> np.ndarray:
        """Apply gamma correction and contrast enhancement."""
        # Apply gamma correction
        corrected = np.power(data, self.gamma)
        
        # Apply contrast enhancement
        # Contrast formula: ((value - 0.5) * contrast) + 0.5
        enhanced = ((corrected - 0.5) * self.contrast) + 0.5
        
        # Clamp to [0, 1] range
        return np.clip(enhanced, 0.0, 1.0)
    
    def _initialize_color_functions(self) -> Dict[ColorPalette, Callable]:
        """Initialize color mapping functions for each palette."""
        return {
            ColorPalette.FIRE: self._fire_palette,
            ColorPalette.ICE: self._ice_palette,
            ColorPalette.RAINBOW: self._rainbow_palette,
            ColorPalette.COSMIC: self._cosmic_palette,
            ColorPalette.FOREST: self._forest_palette,
            ColorPalette.OCEAN: self._ocean_palette,
            ColorPalette.SUNSET: self._sunset_palette,
            ColorPalette.MONOCHROME: self._monochrome_palette,
            ColorPalette.QUANTUM_GOLD: self._quantum_gold_palette,
            ColorPalette.ELECTRIC: self._electric_palette,
            ColorPalette.MAGMA: self._magma_palette,
            ColorPalette.VIRIDIS: self._viridis_palette,
            ColorPalette.WHITE_ON_BLACK: self._white_on_black_palette
        }
    
    def _fire_palette(self, data: np.ndarray, cycle_speed: float) -> np.ndarray:
        """Classic fire color palette: black -> red -> orange -> yellow -> white."""
        height, width = data.shape
        rgb = np.zeros((height, width, 3))
        
        # Apply color cycling
        cycled_data = (data + cycle_speed * 0.1) % 1.0
        
        # Fire color mapping
        rgb[:, :, 0] = np.minimum(1.0, cycled_data * 2.0)  # Red channel
        rgb[:, :, 1] = np.maximum(0.0, np.minimum(1.0, (cycled_data - 0.3) * 2.5))  # Green channel
        rgb[:, :, 2] = np.maximum(0.0, np.minimum(1.0, (cycled_data - 0.7) * 3.33))  # Blue channel
        
        # Points in the set (data = 0) are black
        in_set_mask = (data == 0)
        rgb[in_set_mask] = [0, 0, 0]
        
        return rgb
    
    def _ice_palette(self, data: np.ndarray, cycle_speed: float) -> np.ndarray:
        """Ice color palette: black -> blue -> cyan -> white."""
        height, width = data.shape
        rgb = np.zeros((height, width, 3))
        
        # Apply color cycling
        cycled_data = (data + cycle_speed * 0.1) % 1.0
        
        # Ice color mapping
        rgb[:, :, 0] = np.maximum(0.0, np.minimum(1.0, (cycled_data - 0.5) * 2.0))  # Red channel
        rgb[:, :, 1] = np.maximum(0.0, np.minimum(1.0, (cycled_data - 0.3) * 2.5))  # Green channel
        rgb[:, :, 2] = np.minimum(1.0, cycled_data * 1.5)  # Blue channel
        
        # Points in the set are black
        in_set_mask = (data == 0)
        rgb[in_set_mask] = [0, 0, 0]
        
        return rgb
    
    def _rainbow_palette(self, data: np.ndarray, cycle_speed: float) -> np.ndarray:
        """Rainbow color palette using HSV color space."""
        height, width = data.shape
        rgb = np.zeros((height, width, 3))
        
        # Apply color cycling
        cycled_data = (data + cycle_speed * 0.2) % 1.0
        
        # Convert to HSV and then to RGB
        for i in range(height):
            for j in range(width):
                if data[i, j] > 0:  # Not in the set
                    hue = cycled_data[i, j]
                    saturation = 1.0
                    value = 1.0
                    r, g, b = colorsys.hsv_to_rgb(hue, saturation, value)
                    rgb[i, j] = [r, g, b]
        
        return rgb
    
    def _cosmic_palette(self, data: np.ndarray, cycle_speed: float) -> np.ndarray:
        """Cosmic space palette: black -> purple -> blue -> magenta -> white."""
        height, width = data.shape
        rgb = np.zeros((height, width, 3))
        
        # Apply color cycling
        cycled_data = (data + cycle_speed * 0.15) % 1.0
        
        # Cosmic color mapping with non-linear progression
        t = cycled_data
        rgb[:, :, 0] = 0.5 * np.sin(np.pi * t) + 0.5 * t**2  # Red channel
        rgb[:, :, 1] = 0.3 * np.sin(2 * np.pi * t + np.pi/3)  # Green channel  
        rgb[:, :, 2] = np.minimum(1.0, t * 1.5 + 0.3 * np.sin(4 * np.pi * t))  # Blue channel
        
        # Points in the set are black
        in_set_mask = (data == 0)
        rgb[in_set_mask] = [0, 0, 0]
        
        return np.clip(rgb, 0, 1)
    
    def _forest_palette(self, data: np.ndarray, cycle_speed: float) -> np.ndarray:
        """Forest palette: black -> dark green -> light green -> yellow."""
        height, width = data.shape
        rgb = np.zeros((height, width, 3))
        
        # Apply color cycling
        cycled_data = (data + cycle_speed * 0.08) % 1.0
        
        # Forest color mapping
        rgb[:, :, 0] = np.maximum(0.0, np.minimum(1.0, (cycled_data - 0.6) * 2.5))  # Red channel
        rgb[:, :, 1] = np.minimum(1.0, cycled_data * 1.8)  # Green channel
        rgb[:, :, 2] = np.maximum(0.0, np.minimum(0.3, cycled_data * 0.5))  # Blue channel
        
        # Points in the set are black
        in_set_mask = (data == 0)
        rgb[in_set_mask] = [0, 0, 0]
        
        return rgb
    
    def _ocean_palette(self, data: np.ndarray, cycle_speed: float) -> np.ndarray:
        """Ocean palette: black -> dark blue -> turquoise -> white."""
        height, width = data.shape
        rgb = np.zeros((height, width, 3))
        
        # Apply color cycling
        cycled_data = (data + cycle_speed * 0.12) % 1.0
        
        # Ocean color mapping
        rgb[:, :, 0] = np.maximum(0.0, np.minimum(1.0, (cycled_data - 0.7) * 3.33))  # Red channel
        rgb[:, :, 1] = np.maximum(0.0, np.minimum(1.0, (cycled_data - 0.4) * 1.67))  # Green channel
        rgb[:, :, 2] = np.minimum(1.0, cycled_data * 1.5)  # Blue channel
        
        # Points in the set are black
        in_set_mask = (data == 0)
        rgb[in_set_mask] = [0, 0, 0]
        
        return rgb
    
    def _sunset_palette(self, data: np.ndarray, cycle_speed: float) -> np.ndarray:
        """Sunset palette: black -> purple -> orange -> yellow -> white."""
        height, width = data.shape
        rgb = np.zeros((height, width, 3))
        
        # Apply color cycling
        cycled_data = (data + cycle_speed * 0.1) % 1.0
        
        # Sunset color mapping with smooth transitions
        t = cycled_data
        rgb[:, :, 0] = np.minimum(1.0, 0.8 + 0.2 * np.sin(np.pi * t))  # Red channel
        rgb[:, :, 1] = 0.5 * t + 0.3 * np.sin(2 * np.pi * t)  # Green channel
        rgb[:, :, 2] = 0.3 * t + 0.2 * np.cos(np.pi * t)  # Blue channel
        
        # Points in the set are black
        in_set_mask = (data == 0)
        rgb[in_set_mask] = [0, 0, 0]
        
        return np.clip(rgb, 0, 1)
    
    def _monochrome_palette(self, data: np.ndarray, cycle_speed: float) -> np.ndarray:
        """High-contrast monochrome palette for accessibility."""
        height, width = data.shape
        rgb = np.zeros((height, width, 3))
        
        # Simple grayscale with enhanced contrast
        intensity = data ** 0.5  # Square root for better contrast
        rgb[:, :, 0] = intensity
        rgb[:, :, 1] = intensity
        rgb[:, :, 2] = intensity
        
        # Points in the set are black
        in_set_mask = (data == 0)
        rgb[in_set_mask] = [0, 0, 0]
        
        return rgb
    
    def _quantum_gold_palette(self, data: np.ndarray, cycle_speed: float) -> np.ndarray:
        """Quantum-inspired gold palette matching IQB project colors."""
        height, width = data.shape
        rgb = np.zeros((height, width, 3))
        
        # Apply color cycling
        cycled_data = (data + cycle_speed * 0.1) % 1.0
        
        # Quantum gold color progression
        # Base colors: quantum background (#0B1426) -> quantum gold (#FFD700)
        base_r, base_g, base_b = 0.043, 0.078, 0.149  # Quantum background RGB
        gold_r, gold_g, gold_b = 1.0, 0.843, 0.0     # Quantum gold RGB
        
        # Smooth interpolation with non-linear progression
        t = cycled_data ** 0.7  # Slight gamma for more golden appearance
        rgb[:, :, 0] = base_r + t * (gold_r - base_r)
        rgb[:, :, 1] = base_g + t * (gold_g - base_g)
        rgb[:, :, 2] = base_b + t * (gold_b - base_b)
        
        # Points in the set use quantum background color
        in_set_mask = (data == 0)
        rgb[in_set_mask] = [base_r, base_g, base_b]
        
        return rgb
    
    def _electric_palette(self, data: np.ndarray, cycle_speed: float) -> np.ndarray:
        """Electric palette with bright, energetic colors."""
        height, width = data.shape
        rgb = np.zeros((height, width, 3))
        
        # Apply color cycling
        cycled_data = (data + cycle_speed * 0.25) % 1.0
        
        # Electric color mapping with oscillations
        t = cycled_data
        rgb[:, :, 0] = 0.5 + 0.5 * np.sin(6 * np.pi * t)  # Red channel
        rgb[:, :, 1] = 0.7 * t + 0.3 * np.sin(8 * np.pi * t + np.pi/4)  # Green channel
        rgb[:, :, 2] = 0.8 + 0.2 * np.cos(4 * np.pi * t)  # Blue channel
        
        # Points in the set are black
        in_set_mask = (data == 0)
        rgb[in_set_mask] = [0, 0, 0]
        
        return np.clip(rgb, 0, 1)
    
    def _magma_palette(self, data: np.ndarray, cycle_speed: float) -> np.ndarray:
        """Magma-inspired palette: black -> purple -> magenta -> yellow."""
        height, width = data.shape
        rgb = np.zeros((height, width, 3))
        
        # Apply color cycling
        cycled_data = (data + cycle_speed * 0.1) % 1.0
        
        # Magma color progression (inspired by matplotlib's magma)
        t = cycled_data
        rgb[:, :, 0] = np.minimum(1.0, -0.002136 + t * (2.176514 + t * (-2.689460 + t * 1.515094)))
        rgb[:, :, 1] = np.minimum(1.0, 0.000515 + t * (0.924472 + t * (-2.324622 + t * 1.399748)))
        rgb[:, :, 2] = np.minimum(1.0, -0.005772 + t * (1.012426 + t * (-0.834229 + t * -0.172270)))
        
        # Points in the set are black
        in_set_mask = (data == 0)
        rgb[in_set_mask] = [0, 0, 0]
        
        return np.clip(rgb, 0, 1)
    
    def _viridis_palette(self, data: np.ndarray, cycle_speed: float) -> np.ndarray:
        """Viridis-inspired palette: purple -> blue -> green -> yellow."""
        height, width = data.shape
        rgb = np.zeros((height, width, 3))
        
        # Apply color cycling
        cycled_data = (data + cycle_speed * 0.1) % 1.0
        
        # Viridis color progression (inspired by matplotlib's viridis)
        t = cycled_data
        rgb[:, :, 0] = np.minimum(1.0, 0.267004 + t * (-0.127568 + t * (0.929718 + t * (-0.567931))))
        rgb[:, :, 1] = np.minimum(1.0, 0.004874 + t * (1.424076 + t * (-0.781372 + t * 0.352501)))
        rgb[:, :, 2] = np.minimum(1.0, 0.329415 + t * (0.515757 + t * (-0.702646 + t * (-0.142200))))
        
        # Points in the set are black
        in_set_mask = (data == 0)
        rgb[in_set_mask] = [0, 0, 0]
        
        return np.clip(rgb, 0, 1)
    
    def _white_on_black_palette(self, data: np.ndarray, cycle_speed: float) -> np.ndarray:
        """Pure white-on-black palette for classic mathematical visualization.
        
        Creates the traditional mathematical representation where:
        - Points in the Mandelbrot set (non-escaping): pure black (0,0,0)
        - Points outside the set (escaping): pure white (1,1,1)
        
        This produces the iconic mathematical visualization with the Mandelbrot
        set appearing as a black silhouette against a white background.
        """
        height, width = data.shape
        rgb = np.zeros((height, width, 3))
        
        # Points in the set (data == 0) are pure white
        in_set_mask = (data == 0)
        rgb[in_set_mask] = [1.0, 1.0, 1.0]  # Pure white
        
        # Points outside the set (data > 0) remain black (already initialized to 0)
        # This creates the dramatic white-on-black visualization
        
        return rgb

class AnimatedColorCycler:
    """
    Manages color cycling for animated fractal sequences.
    """
    
    def __init__(self, base_colorizer: FractalColorizer, cycle_period: float = 10.0):
        """
        Initialize animated color cycler.
        
        Parameters
        ----------
        base_colorizer : FractalColorizer
            Base colorizer to animate
        cycle_period : float
            Time in seconds for one complete color cycle
        """
        self.base_colorizer = base_colorizer
        self.cycle_period = cycle_period
        self.start_time = 0.0
    
    def get_colors_at_time(self, escape_data: np.ndarray, time: float, **kwargs) -> np.ndarray:
        """
        Get colors for escape data at specific time.
        
        Parameters
        ----------
        escape_data : np.ndarray
            Escape time data from fractal calculation
        time : float
            Current animation time
        **kwargs
            Additional arguments for colorization
            
        Returns
        -------
        np.ndarray
            RGB color array at the specified time
        """
        # Calculate cycle position
        cycle_position = (time - self.start_time) / self.cycle_period
        cycle_speed = cycle_position % 1.0
        
        return self.base_colorizer.colorize_escape_data(
            escape_data, cycle_speed=cycle_speed, **kwargs
        )
    
    def reset_cycle(self, start_time: float = 0.0):
        """Reset the color cycle to start at specified time."""
        self.start_time = start_time

# Utility functions for color analysis and optimization
def analyze_color_distribution(rgb_array: np.ndarray) -> Dict[str, float]:
    """
    Analyze color distribution in an RGB array.
    
    Parameters
    ----------
    rgb_array : np.ndarray
        RGB color array with shape (height, width, 3)
        
    Returns
    -------
    dict
        Statistics about color distribution
    """
    # Convert to HSV for better analysis
    height, width, _ = rgb_array.shape
    rgb_flat = rgb_array.reshape(-1, 3)
    
    # Calculate statistics
    stats = {
        'mean_brightness': np.mean(np.max(rgb_flat, axis=1)),
        'color_variance': np.var(rgb_flat),
        'dominant_hue': 0.0,  # Would require HSV conversion
        'contrast_ratio': np.ptp(rgb_flat),  # Peak-to-peak range
        'color_diversity': len(np.unique(rgb_flat.view(np.void), axis=0))
    }
    
    return stats

def create_palette_comparison(palettes: List[ColorPalette], width: int = 512) -> np.ndarray:
    """
    Create a comparison image showing multiple color palettes.
    
    Parameters
    ----------
    palettes : list
        List of ColorPalette enums to compare
    width : int
        Width of each palette strip
        
    Returns
    -------
    np.ndarray
        Combined RGB array showing all palettes
    """
    height_per_palette = 32
    total_height = len(palettes) * height_per_palette
    combined = np.zeros((total_height, width, 3))
    
    for i, palette in enumerate(palettes):
        colorizer = FractalColorizer(palette)
        palette_strip = colorizer.create_palette_preview(width, height_per_palette)
        
        start_row = i * height_per_palette
        end_row = start_row + height_per_palette
        combined[start_row:end_row] = palette_strip
    
    return combined

# Export commonly used color configurations
DEFAULT_COLORIZER = FractalColorizer(ColorPalette.FIRE)
QUANTUM_COLORIZER = FractalColorizer(ColorPalette.QUANTUM_GOLD, gamma=0.8, contrast=1.2)
ARTISTIC_COLORIZER = FractalColorizer(ColorPalette.COSMIC, gamma=1.2, contrast=1.1)
ACCESSIBILITY_COLORIZER = FractalColorizer(ColorPalette.MONOCHROME, contrast=2.0)
WHITE_ON_BLACK_COLORIZER = FractalColorizer(ColorPalette.WHITE_ON_BLACK, gamma=1.0, contrast=1.0)