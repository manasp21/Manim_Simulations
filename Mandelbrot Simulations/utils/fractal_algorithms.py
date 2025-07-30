"""
Fractal mathematical algorithms for Mandelbrot Simulations.

This module provides optimized implementations of escape-time algorithms
for various fractal types including Mandelbrot, Julia, Burning Ship, and Tricorn sets.
All algorithms are designed for high-performance rendering in Manim animations.

Key features:
- Vectorized numpy operations for performance
- Smooth coloring using fractional escape counts
- Multiple fractal family support
- Configurable iteration limits and bailout radii
"""

import numpy as np
from typing import Tuple, Union, Callable, Dict, Any, List, Optional

# Try to import numba for performance, fall back to regular numpy if not available
try:
    import numba
    from numba import jit, vectorize, float64, complex128, int32
    NUMBA_AVAILABLE = True
except ImportError:
    print("Numba not available - using fallback numpy implementations")
    NUMBA_AVAILABLE = False
    # Create dummy decorators for compatibility
    def jit(*args, **kwargs):
        def decorator(func):
            return func
        return decorator

class FractalCalculator:
    """
    High-performance fractal calculation engine.
    
    Provides optimized algorithms for computing escape-time fractals
    with smooth coloring and multiple fractal type support.
    """
    
    def __init__(self, max_iterations: int = 256, bailout_radius: float = 2.0):
        """
        Initialize fractal calculator.
        
        Parameters
        ----------
        max_iterations : int
            Maximum number of iterations before considering point as in the set
        bailout_radius : float
            Radius at which point is considered to have escaped to infinity
        """
        self.max_iterations = max_iterations
        self.bailout_radius = bailout_radius
        self.bailout_squared = bailout_radius ** 2
    
    def mandelbrot_set(self, width: int, height: int, 
                      center: complex = 0+0j, zoom: float = 1.0) -> np.ndarray:
        """
        Calculate the classic Mandelbrot set.
        
        The Mandelbrot set is defined as the set of complex numbers c
        for which the iteration z_{n+1} = z_n^2 + c remains bounded.
        
        Parameters
        ----------
        width, height : int
            Dimensions of the output array
        center : complex
            Center point of the view
        zoom : float
            Zoom level (higher = more zoomed in)
            
        Returns
        -------
        np.ndarray
            2D array of escape counts with smooth coloring
        """
        # Create coordinate arrays
        x_min = center.real - 2.0 / zoom
        x_max = center.real + 2.0 / zoom
        y_min = center.imag - 2.0 / zoom
        y_max = center.imag + 2.0 / zoom
        
        x = np.linspace(x_min, x_max, width)
        y = np.linspace(y_min, y_max, height)
        
        # Create complex plane
        X, Y = np.meshgrid(x, y)
        C = X + 1j * Y
        
        # Calculate escape times using optimized algorithm
        return self._mandelbrot_escape_count(C)
    
    def mandelbrot_set_with_distance_estimation(self, width: int, height: int,
                                              center: complex = 0+0j, zoom: float = 1.0) -> Tuple[np.ndarray, np.ndarray]:
        """
        Calculate Mandelbrot set with distance estimation for boundary enhancement.
        
        Distance estimation highlights fractal boundaries by calculating the approximate
        distance to the Mandelbrot set boundary, making self-similar structures more visible.
        
        Parameters
        ----------
        width, height : int
            Dimensions of the output array
        center : complex
            Center point of the view
        zoom : float
            Zoom level (higher = more zoomed in)
            
        Returns
        -------
        tuple
            (escape_data, distance_data) - escape counts and distance estimation arrays
        """
        # Create coordinate arrays
        x_min = center.real - 2.0 / zoom
        x_max = center.real + 2.0 / zoom
        y_min = center.imag - 2.0 / zoom
        y_max = center.imag + 2.0 / zoom
        
        x = np.linspace(x_min, x_max, width)
        y = np.linspace(y_min, y_max, height)
        
        # Create complex plane
        X, Y = np.meshgrid(x, y)
        C = X + 1j * Y
        
        # Calculate escape times and distance estimation
        return self._mandelbrot_distance_estimation(C)
    
    def julia_set(self, width: int, height: int, c: complex,
                  center: complex = 0+0j, zoom: float = 1.0) -> np.ndarray:
        """
        Calculate a Julia set for given parameter c.
        
        Julia sets use a fixed parameter c and vary the starting point z_0.
        The iteration is the same: z_{n+1} = z_n^2 + c
        
        Parameters
        ----------
        width, height : int
            Dimensions of the output array
        c : complex
            Julia set parameter
        center : complex
            Center point of the view
        zoom : float
            Zoom level
            
        Returns
        -------
        np.ndarray
            2D array of escape counts with smooth coloring
        """
        # Create coordinate arrays for starting points
        x_min = center.real - 2.0 / zoom
        x_max = center.real + 2.0 / zoom
        y_min = center.imag - 2.0 / zoom
        y_max = center.imag + 2.0 / zoom
        
        x = np.linspace(x_min, x_max, width)
        y = np.linspace(y_min, y_max, height)
        
        # Create complex plane for starting points
        X, Y = np.meshgrid(x, y)
        Z = X + 1j * Y
        
        # Calculate escape times using Julia algorithm
        return self._julia_escape_count(Z, c)
    
    def burning_ship(self, width: int, height: int,
                    center: complex = -0.5-0.6j, zoom: float = 1.0) -> np.ndarray:
        """
        Calculate the Burning Ship fractal.
        
        Uses the iteration: z_{n+1} = (|Re(z_n)| + i|Im(z_n)|)^2 + c
        This creates the distinctive "ship" appearance.
        
        Parameters
        ----------
        width, height : int
            Dimensions of the output array
        center : complex
            Center point of the view (default optimized for ship structure)
        zoom : float
            Zoom level
            
        Returns
        -------
        np.ndarray
            2D array of escape counts with smooth coloring
        """
        # Create coordinate arrays
        x_min = center.real - 2.0 / zoom
        x_max = center.real + 2.0 / zoom
        y_min = center.imag - 2.0 / zoom
        y_max = center.imag + 2.0 / zoom
        
        x = np.linspace(x_min, x_max, width)
        y = np.linspace(y_min, y_max, height)
        
        # Create complex plane
        X, Y = np.meshgrid(x, y)
        C = X + 1j * Y
        
        # Calculate escape times using Burning Ship algorithm
        return self._burning_ship_escape_count(C)
    
    def tricorn_set(self, width: int, height: int,
                   center: complex = 0+0j, zoom: float = 1.0) -> np.ndarray:
        """
        Calculate the Tricorn (Mandelbar) set.
        
        Uses the iteration: z_{n+1} = z_n*^2 + c (conjugate of z_n squared)
        This creates a fractal with three-fold symmetry.
        
        Parameters
        ----------
        width, height : int
            Dimensions of the output array
        center : complex
            Center point of the view
        zoom : float
            Zoom level
            
        Returns
        -------
        np.ndarray
            2D array of escape counts with smooth coloring
        """
        # Create coordinate arrays
        x_min = center.real - 2.0 / zoom
        x_max = center.real + 2.0 / zoom
        y_min = center.imag - 2.0 / zoom
        y_max = center.imag + 2.0 / zoom
        
        x = np.linspace(x_min, x_max, width)
        y = np.linspace(y_min, y_max, height)
        
        # Create complex plane
        X, Y = np.meshgrid(x, y)
        C = X + 1j * Y
        
        # Calculate escape times using Tricorn algorithm
        return self._tricorn_escape_count(C)
    
    @staticmethod
    def _mandelbrot_escape_count(C):
        """
        Mandelbrot escape count calculation with smooth coloring.
        
        Uses numpy operations with fallback for non-Numba environments.
        """
        if NUMBA_AVAILABLE:
            return FractalCalculator._mandelbrot_escape_count_numba(C)
        else:
            return FractalCalculator._mandelbrot_escape_count_numpy(C)
    
    @staticmethod
    def _mandelbrot_escape_count_numpy(C):
        """Numpy fallback implementation."""
        height, width = C.shape
        result = np.zeros((height, width), dtype=np.float64)
        
        for i in range(height):
            for j in range(width):
                c = C[i, j]
                z = 0.0 + 0.0j
                iteration = 0
                
                # Main iteration loop
                while iteration < 256 and abs(z) <= 2.0:
                    z = z * z + c
                    iteration += 1
                
                # Smooth coloring using fractional escape count
                if iteration < 256:
                    # Add fractional part for smooth coloring
                    if abs(z) > 1:
                        smooth_count = iteration + 1 - np.log2(np.log2(abs(z)))
                        result[i, j] = smooth_count
                    else:
                        result[i, j] = iteration
                else:
                    result[i, j] = 256.0  # Point is in the set
                    
        return result
    
    @staticmethod
    def _mandelbrot_escape_count_numba(C):
        """Numba-optimized implementation (if available)."""
        @jit(nopython=True, parallel=True)
        def _numba_mandelbrot(C):
            height, width = C.shape
            result = np.zeros((height, width), dtype=np.float64)
            
            for i in numba.prange(height):
                for j in numba.prange(width):
                    c = C[i, j]
                    z = 0.0 + 0.0j
                    iteration = 0
                    
                    # Main iteration loop
                    while iteration < 256 and abs(z) <= 2.0:
                        z = z * z + c
                        iteration += 1
                    
                    # Smooth coloring using fractional escape count
                    if iteration < 256:
                        smooth_count = iteration + 1 - np.log2(np.log2(abs(z)))
                        result[i, j] = smooth_count
                    else:
                        result[i, j] = 256.0  # Point is in the set
                        
            return result
        
        return _numba_mandelbrot(C)
    
    @staticmethod
    def _julia_escape_count(Z, c):
        """
        Julia set escape count calculation.
        """
        if NUMBA_AVAILABLE:
            return FractalCalculator._julia_escape_count_numba(Z, c)
        else:
            return FractalCalculator._julia_escape_count_numpy(Z, c)
    
    @staticmethod
    def _julia_escape_count_numpy(Z, c):
        """Numpy fallback implementation for Julia sets."""
        height, width = Z.shape
        result = np.zeros((height, width), dtype=np.float64)
        
        for i in range(height):
            for j in range(width):
                z = Z[i, j]
                iteration = 0
                
                # Main iteration loop
                while iteration < 256 and abs(z) <= 2.0:
                    z = z * z + c
                    iteration += 1
                
                # Smooth coloring
                if iteration < 256:
                    if abs(z) > 1:
                        smooth_count = iteration + 1 - np.log2(np.log2(abs(z)))
                        result[i, j] = smooth_count
                    else:
                        result[i, j] = iteration
                else:
                    result[i, j] = 256.0
                    
        return result
    
    @staticmethod
    def _julia_escape_count_numba(Z, c):
        """Numba-optimized Julia implementation."""
        @jit(nopython=True, parallel=True)
        def _numba_julia(Z, c):
            height, width = Z.shape
            result = np.zeros((height, width), dtype=np.float64)
            
            for i in numba.prange(height):
                for j in numba.prange(width):
                    z = Z[i, j]
                    iteration = 0
                    
                    # Main iteration loop
                    while iteration < 256 and abs(z) <= 2.0:
                        z = z * z + c
                        iteration += 1
                    
                    # Smooth coloring
                    if iteration < 256:
                        smooth_count = iteration + 1 - np.log2(np.log2(abs(z)))
                        result[i, j] = smooth_count
                    else:
                        result[i, j] = 256.0
                        
            return result
        
        return _numba_julia(Z, c)
    
    @staticmethod
    def _burning_ship_escape_count(C):
        """
        Burning Ship escape count calculation.
        """
        if NUMBA_AVAILABLE:
            return FractalCalculator._burning_ship_escape_count_numba(C)
        else:
            return FractalCalculator._burning_ship_escape_count_numpy(C)
    
    @staticmethod
    def _burning_ship_escape_count_numpy(C):
        """Numpy fallback implementation for Burning Ship."""
        height, width = C.shape
        result = np.zeros((height, width), dtype=np.float64)
        
        for i in range(height):
            for j in range(width):
                c = C[i, j]
                z = 0.0 + 0.0j
                iteration = 0
                
                # Main iteration loop with absolute value modification
                while iteration < 256 and abs(z) <= 2.0:
                    # Burning Ship formula: z = (|Re(z)| + i|Im(z)|)^2 + c
                    z = complex(abs(z.real), abs(z.imag))**2 + c
                    iteration += 1
                
                # Smooth coloring
                if iteration < 256:
                    if abs(z) > 1:
                        smooth_count = iteration + 1 - np.log2(np.log2(abs(z)))
                        result[i, j] = smooth_count
                    else:
                        result[i, j] = iteration
                else:
                    result[i, j] = 256.0
                    
        return result
    
    @staticmethod
    def _burning_ship_escape_count_numba(C):
        """Numba-optimized Burning Ship implementation."""
        @jit(nopython=True, parallel=True)
        def _numba_burning_ship(C):
            height, width = C.shape
            result = np.zeros((height, width), dtype=np.float64)
            
            for i in numba.prange(height):
                for j in numba.prange(width):
                    c = C[i, j]
                    z = 0.0 + 0.0j
                    iteration = 0
                    
                    # Main iteration loop with absolute value modification
                    while iteration < 256 and abs(z) <= 2.0:
                        # Burning Ship formula: z = (|Re(z)| + i|Im(z)|)^2 + c
                        z = complex(abs(z.real), abs(z.imag))**2 + c
                        iteration += 1
                    
                    # Smooth coloring
                    if iteration < 256:
                        smooth_count = iteration + 1 - np.log2(np.log2(abs(z)))
                        result[i, j] = smooth_count
                    else:
                        result[i, j] = 256.0
                        
            return result
        
        return _numba_burning_ship(C)
    
    @staticmethod
    def _tricorn_escape_count(C):
        """
        Tricorn set escape count calculation.
        """
        if NUMBA_AVAILABLE:
            return FractalCalculator._tricorn_escape_count_numba(C)
        else:
            return FractalCalculator._tricorn_escape_count_numpy(C)
    
    @staticmethod
    def _tricorn_escape_count_numpy(C):
        """Numpy fallback implementation for Tricorn set."""
        height, width = C.shape
        result = np.zeros((height, width), dtype=np.float64)
        
        for i in range(height):
            for j in range(width):
                c = C[i, j]
                z = 0.0 + 0.0j
                iteration = 0
                
                # Main iteration loop with conjugate
                while iteration < 256 and abs(z) <= 2.0:
                    # Tricorn formula: z = conj(z)^2 + c
                    z = np.conj(z)**2 + c
                    iteration += 1
                
                # Smooth coloring
                if iteration < 256:
                    if abs(z) > 1:
                        smooth_count = iteration + 1 - np.log2(np.log2(abs(z)))
                        result[i, j] = smooth_count
                    else:
                        result[i, j] = iteration
                else:
                    result[i, j] = 256.0
                    
        return result
    
    @staticmethod
    def _tricorn_escape_count_numba(C):
        """Numba-optimized Tricorn implementation."""
        @jit(nopython=True, parallel=True)
        def _numba_tricorn(C):
            height, width = C.shape
            result = np.zeros((height, width), dtype=np.float64)
            
            for i in numba.prange(height):
                for j in numba.prange(width):
                    c = C[i, j]
                    z = 0.0 + 0.0j
                    iteration = 0
                    
                    # Main iteration loop with conjugate
                    while iteration < 256 and abs(z) <= 2.0:
                        # Tricorn formula: z = conj(z)^2 + c
                        z = np.conj(z)**2 + c
                        iteration += 1
                    
                    # Smooth coloring
                    if iteration < 256:
                        smooth_count = iteration + 1 - np.log2(np.log2(abs(z)))
                        result[i, j] = smooth_count
                    else:
                        result[i, j] = 256.0
                        
            return result
        
        return _numba_tricorn(C)
    
    @staticmethod
    def _mandelbrot_distance_estimation(C):
        """
        Calculate Mandelbrot set with distance estimation for enhanced boundary visibility.
        
        Distance estimation provides approximate distance to the fractal boundary,
        which helps highlight self-similar structures by emphasizing edges.
        """
        if NUMBA_AVAILABLE:
            return FractalCalculator._mandelbrot_distance_estimation_numba(C)
        else:
            return FractalCalculator._mandelbrot_distance_estimation_numpy(C)
    
    @staticmethod
    def _mandelbrot_distance_estimation_numpy(C):
        """Numpy implementation of Mandelbrot distance estimation."""
        height, width = C.shape
        escape_data = np.zeros((height, width), dtype=np.float64)
        distance_data = np.zeros((height, width), dtype=np.float64)
        
        for i in range(height):
            for j in range(width):
                c = C[i, j]
                z = 0.0 + 0.0j
                dz = 0.0 + 0.0j  # Derivative for distance estimation
                iteration = 0
                
                # Main iteration loop with derivative tracking
                while iteration < 256 and abs(z) <= 2.0:
                    # Update derivative: dz = 2*z*dz + 1
                    dz = 2.0 * z * dz + 1.0
                    # Update z: z = z^2 + c
                    z = z * z + c
                    iteration += 1
                
                # Calculate escape data with smooth coloring
                if iteration < 256:
                    if abs(z) > 1:
                        smooth_count = iteration + 1 - np.log2(np.log2(abs(z)))
                        escape_data[i, j] = smooth_count
                        
                        # Distance estimation: d = |z|*ln|z| / |dz|
                        if abs(dz) > 0:
                            distance = abs(z) * np.log(abs(z)) / abs(dz)
                            distance_data[i, j] = distance
                        else:
                            distance_data[i, j] = 0.0
                    else:
                        escape_data[i, j] = iteration
                        distance_data[i, j] = 0.0
                else:
                    escape_data[i, j] = 256.0
                    distance_data[i, j] = 0.0  # Inside the set
        
        return escape_data, distance_data
    
    @staticmethod
    def _mandelbrot_distance_estimation_numba(C):
        """Numba-optimized Mandelbrot distance estimation."""
        @jit(nopython=True, parallel=True)
        def _numba_distance_estimation(C):
            height, width = C.shape
            escape_data = np.zeros((height, width), dtype=np.float64)
            distance_data = np.zeros((height, width), dtype=np.float64)
            
            for i in numba.prange(height):
                for j in numba.prange(width):
                    c = C[i, j]
                    z = 0.0 + 0.0j
                    dz = 0.0 + 0.0j  # Derivative for distance estimation
                    iteration = 0
                    
                    # Main iteration loop with derivative tracking
                    while iteration < 256 and abs(z) <= 2.0:
                        # Update derivative: dz = 2*z*dz + 1
                        dz = 2.0 * z * dz + 1.0
                        # Update z: z = z^2 + c
                        z = z * z + c
                        iteration += 1
                    
                    # Calculate escape data with smooth coloring
                    if iteration < 256:
                        smooth_count = iteration + 1 - np.log2(np.log2(abs(z)))
                        escape_data[i, j] = smooth_count
                        
                        # Distance estimation: d = |z|*ln|z| / |dz|
                        if abs(dz) > 0:
                            distance = abs(z) * np.log(abs(z)) / abs(dz)
                            distance_data[i, j] = distance
                        else:
                            distance_data[i, j] = 0.0
                    else:
                        escape_data[i, j] = iteration
                        distance_data[i, j] = 0.0
            
            return escape_data, distance_data
        
        return _numba_distance_estimation(C)

class ZoomPath:
    """
    Manages smooth zoom sequences with loop-back capability.
    """
    
    def __init__(self, start_center: complex, start_zoom: float):
        """
        Initialize zoom path.
        
        Parameters
        ----------
        start_center : complex
            Starting center point
        start_zoom : float
            Starting zoom level
        """
        self.start_center = start_center
        self.start_zoom = start_zoom
        self.keyframes = [(start_center, start_zoom)]
    
    def add_keyframe(self, center: complex, zoom: float):
        """Add a keyframe to the zoom path."""
        self.keyframes.append((center, zoom))
    
    def close_loop(self):
        """Add the starting position as the final keyframe for seamless looping."""
        self.keyframes.append((self.start_center, self.start_zoom))
    
    def interpolate(self, t: float) -> Tuple[complex, float]:
        """
        Interpolate position and zoom at parameter t ∈ [0, 1].
        
        Parameters
        ----------
        t : float
            Interpolation parameter (0 = start, 1 = end)
            
        Returns
        -------
        tuple
            (center, zoom) at parameter t
        """
        if len(self.keyframes) < 2:
            return self.keyframes[0]
        
        # Find surrounding keyframes
        scaled_t = t * (len(self.keyframes) - 1)
        index = int(scaled_t)
        local_t = scaled_t - index
        
        if index >= len(self.keyframes) - 1:
            return self.keyframes[-1]
        
        # Interpolate between keyframes
        center1, zoom1 = self.keyframes[index]
        center2, zoom2 = self.keyframes[index + 1]
        
        # Linear interpolation for center
        center = center1 + local_t * (center2 - center1)
        
        # Exponential interpolation for zoom (looks more natural)
        log_zoom1 = np.log(zoom1)
        log_zoom2 = np.log(zoom2)
        zoom = np.exp(log_zoom1 + local_t * (log_zoom2 - log_zoom1))
        
        return center, zoom

# Predefined interesting zoom paths for different fractals
MANDELBROT_ZOOM_PATHS = {
    'seahorse_valley': ZoomPath(-0.7269 + 0.1889j, 1.0),
    'lightning': ZoomPath(-1.8 + 0.0j, 1.0),
    'spiral': ZoomPath(0.001643721971153 + 0.822467633298876j, 1.0),
    'mini_mandelbrot': ZoomPath(-0.16070135 + 1.0375665j, 1.0)
}

JULIA_PARAMETERS = {
    'dendrite': -0.7 + 0.27015j,
    'douady_rabbit': -0.4 + 0.6j,
    'san_marco': -0.8 + 0.156j,
    'siegel_disk': -0.391 - 0.587j,
    'fatou_dust': -0.194 + 0.6557j
}

# Performance optimization utilities
class PerformanceOptimizer:
    """
    Utilities for optimizing fractal calculations.
    """
    
    @staticmethod
    def adaptive_quality(zoom_level: float, base_resolution: int = 800) -> int:
        """
        Determine optimal resolution based on zoom level.
        
        At higher zoom levels, we can use lower resolution without
        losing visual quality due to the mathematical structure.
        
        Parameters
        ----------
        zoom_level : float
            Current zoom level
        base_resolution : int
            Base resolution for zoom level 1.0
            
        Returns
        -------
        int
            Optimal resolution for current zoom level
        """
        # Use logarithmic scaling to maintain detail
        scale_factor = min(2.0, max(0.5, 1.0 + 0.1 * np.log10(zoom_level)))
        return int(base_resolution * scale_factor)
    
    @staticmethod
    def estimate_computation_time(width: int, height: int, max_iterations: int) -> float:
        """
        Estimate computation time for given parameters.
        
        Useful for progress indicators and optimization decisions.
        
        Parameters
        ----------
        width, height : int
            Image dimensions
        max_iterations : int
            Maximum iterations
            
        Returns
        -------
        float
            Estimated computation time in seconds
        """
        # Empirical formula based on typical hardware
        pixels = width * height
        operations = pixels * max_iterations
        operations_per_second = 1e8  # Approximate for modern CPU
        
        return operations / operations_per_second

class AspectRatioManager:
    """
    Manages 16:10 aspect ratio configuration for Manim and fractal viewports.
    """
    
    # Standard 16:10 resolutions
    RESOLUTIONS_16_10 = {
        'low': (1280, 800),
        'medium': (1680, 1050), 
        'high': (1920, 1200),
        'ultra': (2560, 1600)
    }
    
    @staticmethod
    def configure_manim_16_10(quality: str = 'high'):
        """
        Configure Manim for 16:10 aspect ratio.
        
        Parameters
        ----------
        quality : str
            Resolution quality ('low', 'medium', 'high', 'ultra')
        """
        try:
            from manim import config
            width, height = AspectRatioManager.RESOLUTIONS_16_10[quality]
            config.pixel_width = width
            config.pixel_height = height
            config.aspect_ratio = width / height
            print(f"✅ Configured Manim for 16:10 aspect ratio: {width}x{height}")
        except ImportError:
            print("⚠️  Manim config not available - aspect ratio will be set per scene")
        except KeyError:
            print(f"❌ Unknown quality '{quality}' - using 'high'")
            AspectRatioManager.configure_manim_16_10('high')
    
    @staticmethod
    def get_fractal_viewport(center: complex, zoom: float, aspect_ratio: float = 1.6) -> Tuple[float, float, float, float]:
        """
        Calculate fractal viewport bounds for 16:10 aspect ratio.
        
        Parameters
        ----------
        center : complex
            Center point of the view
        zoom : float
            Zoom level
        aspect_ratio : float
            Aspect ratio (1.6 for 16:10)
            
        Returns
        -------
        tuple
            (x_min, x_max, y_min, y_max) viewport bounds
        """
        # Calculate viewport size
        height_range = 2.0 / zoom
        width_range = height_range * aspect_ratio
        
        # Calculate bounds
        x_min = center.real - width_range / 2
        x_max = center.real + width_range / 2
        y_min = center.imag - height_range / 2
        y_max = center.imag + height_range / 2
        
        return x_min, x_max, y_min, y_max

class SmoothZoomEngine:
    """
    Advanced smooth zoom engine for continuous fractal navigation.
    
    Eliminates jump cuts by generating smooth progressive zoom sequences
    with configurable zoom rates and adaptive quality.
    """
    
    def __init__(self, fractal_calculator: FractalCalculator):
        """
        Initialize smooth zoom engine.
        
        Parameters
        ----------
        fractal_calculator : FractalCalculator
            Fractal calculation engine
        """
        self.fractal_calculator = fractal_calculator
        self.aspect_ratio = 1.6  # 16:10 ratio
    
    def generate_smooth_zoom_sequence(self, start_center: complex, start_zoom: float,
                                    end_center: complex, end_zoom: float,
                                    duration_seconds: float = 3.0, fps: int = 30,
                                    width: int = 800, height: int = 500) -> List[np.ndarray]:
        """
        Generate smooth zoom sequence between two points.
        
        Parameters
        ----------
        start_center, end_center : complex
            Start and end center points
        start_zoom, end_zoom : float
            Start and end zoom levels
        duration_seconds : float
            Duration of zoom sequence
        fps : int
            Frames per second
        width, height : int
            Image dimensions (should maintain 16:10 ratio)
            
        Returns
        -------
        List[np.ndarray]
            List of fractal data arrays for smooth animation
        """
        total_frames = int(duration_seconds * fps)
        frames = []
        
        print(f"🎬 Generating {total_frames} frames for smooth zoom")
        print(f"   From: center={start_center}, zoom={start_zoom:,.0f}x")
        print(f"   To: center={end_center}, zoom={end_zoom:,.0f}x")
        
        for frame_idx in range(total_frames):
            # Calculate interpolation parameter (0 to 1)
            t = frame_idx / (total_frames - 1) if total_frames > 1 else 0
            
            # Apply easing function for natural zoom feel
            t_eased = self._smooth_step(t)
            
            # Interpolate center point (linear)
            current_center = start_center + t_eased * (end_center - start_center)
            
            # Interpolate zoom level (exponential for natural feel)
            log_start = np.log(start_zoom)
            log_end = np.log(end_zoom)
            current_zoom = np.exp(log_start + t_eased * (log_end - log_start))
            
            # Calculate adaptive iterations based on zoom level
            iterations = self._calculate_adaptive_iterations(current_zoom)
            
            # Generate fractal data with 16:10 aspect ratio
            fractal_data = self._generate_16_10_fractal_frame(
                current_center, current_zoom, width, height, iterations
            )
            
            frames.append(fractal_data)
            
            if frame_idx % 10 == 0:
                print(f"   🔄 Frame {frame_idx+1}/{total_frames}: zoom={current_zoom:,.0f}x, iterations={iterations}")
        
        print("✅ Smooth zoom sequence generated successfully")
        return frames
    
    def generate_multi_location_zoom(self, locations: List[Tuple[complex, float, str]],
                                   transition_duration: float = 2.0, pause_duration: float = 1.0,
                                   fps: int = 30, width: int = 800, height: int = 500) -> List[Tuple[np.ndarray, str]]:
        """
        Generate smooth zoom sequence through multiple locations.
        
        Parameters
        ----------
        locations : List[Tuple[complex, float, str]]
            List of (center, zoom, description) tuples
        transition_duration : float
            Duration of transition between locations
        pause_duration : float
            Duration to pause at each location
        fps : int
            Frames per second
        width, height : int
            Image dimensions
            
        Returns
        -------
        List[Tuple[np.ndarray, str]]
            List of (fractal_data, description) tuples
        """
        all_frames = []
        
        print(f"🌟 Generating multi-location smooth zoom through {len(locations)} locations")
        
        for i in range(len(locations)):
            center, zoom, description = locations[i]
            
            print(f"\n📍 Location {i+1}/{len(locations)}: {description}")
            print(f"   Center: {center}, Zoom: {zoom:,.0f}x")
            
            # Generate frames for current location (pause frames)
            pause_frames = int(pause_duration * fps)
            iterations = self._calculate_adaptive_iterations(zoom)
            
            for _ in range(pause_frames):
                fractal_data = self._generate_16_10_fractal_frame(
                    center, zoom, width, height, iterations
                )
                all_frames.append((fractal_data, description))
            
            # Generate transition to next location (if not last)
            if i < len(locations) - 1:
                next_center, next_zoom, _ = locations[i + 1]
                
                transition_frames = self.generate_smooth_zoom_sequence(
                    center, zoom, next_center, next_zoom,
                    duration_seconds=transition_duration, fps=fps,
                    width=width, height=height
                )
                
                # Add transition frames (skip first frame to avoid duplication)
                for frame_data in transition_frames[1:]:
                    all_frames.append((frame_data, f"Zooming to {locations[i+1][2]}"))
        
        print(f"\n✅ Generated {len(all_frames)} total frames for multi-location journey")
        return all_frames
    
    def _smooth_step(self, t: float) -> float:
        """Apply smooth step function for natural easing."""
        # Smooth step function: 3t² - 2t³
        return 3 * t * t - 2 * t * t * t
    
    def _calculate_adaptive_iterations(self, zoom: float) -> int:
        """Calculate optimal iteration count based on zoom level."""
        base_iterations = 256
        zoom_factor = max(1.0, np.log10(zoom))  
        adaptive_iterations = int(base_iterations + zoom_factor * 100)
        return min(adaptive_iterations, 2048)  # Cap at 2048 for performance
    
    def _generate_16_10_fractal_frame(self, center: complex, zoom: float, 
                                    width: int, height: int, iterations: int) -> np.ndarray:
        """Generate single fractal frame with 16:10 aspect ratio."""
        # Use AspectRatioManager for proper viewport
        x_min, x_max, y_min, y_max = AspectRatioManager.get_fractal_viewport(
            center, zoom, aspect_ratio=self.aspect_ratio
        )
        
        # Generate coordinate arrays
        x = np.linspace(x_min, x_max, width)
        y = np.linspace(y_min, y_max, height)
        X, Y = np.meshgrid(x, y)
        C = X + 1j * Y
        
        # Calculate fractal with adaptive iterations
        original_iterations = self.fractal_calculator.max_iterations
        self.fractal_calculator.max_iterations = iterations
        
        fractal_data = self.fractal_calculator._mandelbrot_escape_count(C)
        
        # Restore original iterations
        self.fractal_calculator.max_iterations = original_iterations
        
        return fractal_data

def create_fractal_calculator(fractal_type: str = 'mandelbrot', **kwargs) -> FractalCalculator:
    """
    Factory function for creating optimized fractal calculators.
    
    Parameters
    ----------
    fractal_type : str
        Type of fractal ('mandelbrot', 'julia', 'burning_ship', 'tricorn')
    **kwargs
        Additional parameters for the calculator
        
    Returns
    -------
    FractalCalculator
        Configured fractal calculator instance
    """
    # Default parameters optimized for each fractal type
    defaults = {
        'mandelbrot': {'max_iterations': 256, 'bailout_radius': 2.0},
        'julia': {'max_iterations': 256, 'bailout_radius': 2.0},
        'burning_ship': {'max_iterations': 512, 'bailout_radius': 2.0},
        'tricorn': {'max_iterations': 256, 'bailout_radius': 2.0}
    }
    
    config = defaults.get(fractal_type, defaults['mandelbrot'])
    config.update(kwargs)
    
    return FractalCalculator(**config)