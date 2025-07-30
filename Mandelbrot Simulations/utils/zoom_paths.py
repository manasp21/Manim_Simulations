"""
Predefined zoom paths and trajectory management for fractal animations.

This module provides sophisticated zoom sequence management with smooth
interpolation, loop-back capability, and predefined interesting locations
for various fractal types. Designed for creating mesmerizing fractal
zoom animations that seamlessly return to their starting position.

Features:
- Predefined zoom sequences for famous fractal locations
- Smooth interpolation with multiple easing functions
- Automatic loop-back trajectory generation
- Zoom path optimization for visual appeal
- Mathematical analysis of zoom stability
"""

import numpy as np
from typing import List, Tuple, Dict, Union, Callable, Optional
from dataclasses import dataclass
from enum import Enum
import math

class EasingFunction(Enum):
    """Easing functions for smooth zoom transitions."""
    LINEAR = "linear"
    EASE_IN = "ease_in"
    EASE_OUT = "ease_out"
    EASE_IN_OUT = "ease_in_out"
    EXPONENTIAL = "exponential"
    CIRCULAR = "circular"
    SINE = "sine"
    ELASTIC = "elastic"

@dataclass
class ZoomKeyframe:
    """
    A keyframe in a zoom sequence.
    
    Attributes
    ----------
    center : complex
        Center point in the complex plane
    zoom : float
        Zoom level (1.0 = standard view, higher = more zoomed in)
    time : float
        Time position in the sequence (0.0 to 1.0)
    rotation : float
        Rotation angle in radians
    easing : EasingFunction
        Easing function to use when transitioning to this keyframe
    """
    center: complex
    zoom: float
    time: float = 0.0
    rotation: float = 0.0
    easing: EasingFunction = EasingFunction.EASE_IN_OUT

class ZoomPath:
    """
    Advanced zoom path manager with smooth interpolation and loop-back capability.
    """
    
    def __init__(self, name: str = "Custom Path"):
        """
        Initialize zoom path.
        
        Parameters
        ----------
        name : str
            Name identifier for this zoom path
        """
        self.name = name
        self.keyframes: List[ZoomKeyframe] = []
        self.loop_back_enabled = False
        self.total_duration = 10.0  # Default duration in seconds
        self._easing_functions = self._initialize_easing_functions()
    
    def add_keyframe(self, center: complex, zoom: float, time: float = None,
                    rotation: float = 0.0, easing: EasingFunction = EasingFunction.EASE_IN_OUT):
        """
        Add a keyframe to the zoom path.
        
        Parameters
        ----------
        center : complex
            Center point for this keyframe
        zoom : float
            Zoom level for this keyframe
        time : float, optional
            Time position (0.0 to 1.0). If None, auto-distribute evenly
        rotation : float
            Rotation angle in radians
        easing : EasingFunction
            Easing function for transition to this keyframe
        """
        if time is None:
            time = len(self.keyframes) / max(1, len(self.keyframes))
        
        keyframe = ZoomKeyframe(center, zoom, time, rotation, easing)
        
        # Insert keyframe in chronological order
        inserted = False
        for i, existing_keyframe in enumerate(self.keyframes):
            if existing_keyframe.time > time:
                self.keyframes.insert(i, keyframe)
                inserted = True
                break
        
        if not inserted:
            self.keyframes.append(keyframe)
    
    def enable_loop_back(self, loop_duration_ratio: float = 0.2):
        """
        Enable automatic loop-back to starting position.
        
        Parameters
        ----------
        loop_duration_ratio : float
            Fraction of total duration used for loop-back transition
        """
        self.loop_back_enabled = True
        
        if len(self.keyframes) > 0:
            # Add loop-back keyframe
            start_keyframe = self.keyframes[0]
            loop_time = 1.0 - loop_duration_ratio
            
            self.add_keyframe(
                center=start_keyframe.center,
                zoom=start_keyframe.zoom,
                time=loop_time,
                rotation=start_keyframe.rotation + 2 * np.pi,  # Complete rotation
                easing=EasingFunction.EASE_OUT
            )
    
    def interpolate_at_time(self, t: float) -> Tuple[complex, float, float]:
        """
        Interpolate zoom parameters at given time.
        
        Parameters
        ----------
        t : float
            Time parameter (0.0 to 1.0)
            
        Returns
        -------
        tuple
            (center, zoom, rotation) at time t
        """
        if not self.keyframes:
            return 0+0j, 1.0, 0.0
        
        if len(self.keyframes) == 1:
            kf = self.keyframes[0]
            return kf.center, kf.zoom, kf.rotation
        
        # Clamp time to valid range
        t = np.clip(t, 0.0, 1.0)
        
        # Find surrounding keyframes
        prev_kf = self.keyframes[0]
        next_kf = self.keyframes[-1]
        
        for i in range(len(self.keyframes) - 1):
            if self.keyframes[i].time <= t <= self.keyframes[i + 1].time:
                prev_kf = self.keyframes[i]
                next_kf = self.keyframes[i + 1]
                break
        
        # Calculate local interpolation parameter
        if next_kf.time > prev_kf.time:
            local_t = (t - prev_kf.time) / (next_kf.time - prev_kf.time)
        else:
            local_t = 0.0
        
        # Apply easing function
        easing_func = self._easing_functions[next_kf.easing]
        eased_t = easing_func(local_t)
        
        # Interpolate parameters
        center = self._interpolate_complex(prev_kf.center, next_kf.center, eased_t)
        zoom = self._interpolate_zoom(prev_kf.zoom, next_kf.zoom, eased_t)
        rotation = self._interpolate_angle(prev_kf.rotation, next_kf.rotation, eased_t)
        
        return center, zoom, rotation
    
    def get_path_length(self) -> float:
        """
        Calculate total path length in the complex plane.
        
        Returns
        -------
        float
            Total path length
        """
        if len(self.keyframes) < 2:
            return 0.0
        
        total_length = 0.0
        for i in range(len(self.keyframes) - 1):
            curr = self.keyframes[i]
            next_kf = self.keyframes[i + 1]
            distance = abs(next_kf.center - curr.center)
            total_length += distance
        
        return total_length
    
    def optimize_for_visual_appeal(self, smoothness_factor: float = 0.8):
        """
        Optimize zoom path for maximum visual appeal.
        
        Parameters
        ----------
        smoothness_factor : float
            How much to prioritize smoothness vs. dramatic zooms
        """
        if len(self.keyframes) < 3:
            return
        
        # Analyze zoom progression for optimal dramatic effect
        zoom_values = [kf.zoom for kf in self.keyframes]
        
        # Ensure exponential zoom progression for dramatic effect
        for i in range(1, len(self.keyframes)):
            prev_zoom = self.keyframes[i-1].zoom
            curr_zoom = self.keyframes[i].zoom
            
            if curr_zoom > prev_zoom:
                # Ensure exponential growth
                optimal_zoom = prev_zoom * (2.0 + smoothness_factor)
                self.keyframes[i] = ZoomKeyframe(
                    center=self.keyframes[i].center,
                    zoom=min(curr_zoom, optimal_zoom),
                    time=self.keyframes[i].time,
                    rotation=self.keyframes[i].rotation,
                    easing=self.keyframes[i].easing
                )
    
    def _interpolate_complex(self, c1: complex, c2: complex, t: float) -> complex:
        """Linearly interpolate between two complex numbers."""
        return c1 + t * (c2 - c1)
    
    def _interpolate_zoom(self, z1: float, z2: float, t: float) -> float:
        """Exponentially interpolate between zoom levels for natural progression."""
        log_z1 = np.log(max(z1, 1e-10))
        log_z2 = np.log(max(z2, 1e-10))
        return np.exp(log_z1 + t * (log_z2 - log_z1))
    
    def _interpolate_angle(self, a1: float, a2: float, t: float) -> float:
        """Interpolate angles with proper wraparound."""
        # Ensure shortest path rotation
        diff = a2 - a1
        if diff > np.pi:
            diff -= 2 * np.pi
        elif diff < -np.pi:
            diff += 2 * np.pi
        
        return a1 + t * diff
    
    def _initialize_easing_functions(self) -> Dict[EasingFunction, Callable[[float], float]]:
        """Initialize easing function implementations."""
        return {
            EasingFunction.LINEAR: lambda t: t,
            EasingFunction.EASE_IN: lambda t: t * t,
            EasingFunction.EASE_OUT: lambda t: 1 - (1 - t) * (1 - t),
            EasingFunction.EASE_IN_OUT: lambda t: 3 * t * t - 2 * t * t * t,
            EasingFunction.EXPONENTIAL: lambda t: 0 if t == 0 else 2 ** (10 * (t - 1)),
            EasingFunction.CIRCULAR: lambda t: 1 - np.sqrt(1 - t * t),
            EasingFunction.SINE: lambda t: 1 - np.cos(t * np.pi / 2),
            EasingFunction.ELASTIC: lambda t: -(2 ** (10 * (t - 1))) * np.sin((t - 1.1) * 5 * np.pi)
        }

class PredefinedZoomPaths:
    """
    Collection of predefined zoom paths for famous fractal locations.
    """
    
    @staticmethod
    def mandelbrot_seahorse_valley() -> ZoomPath:
        """
        Zoom sequence into the famous seahorse valley region.
        
        Returns
        -------
        ZoomPath
            Configured zoom path for seahorse valley exploration
        """
        path = ZoomPath("Mandelbrot: Seahorse Valley")
        
        # Start with overview
        path.add_keyframe(0+0j, 1.0, 0.0, easing=EasingFunction.EASE_IN)
        
        # Approach seahorse valley
        path.add_keyframe(-0.7+0.1j, 5.0, 0.2, easing=EasingFunction.EASE_IN_OUT)
        
        # Enter the valley
        path.add_keyframe(-0.7269+0.1889j, 50.0, 0.5, easing=EasingFunction.EASE_IN)
        
        # Deep zoom into fine details
        path.add_keyframe(-0.72691+0.18891j, 500.0, 0.7, easing=EasingFunction.EXPONENTIAL)
        
        # Maximum zoom
        path.add_keyframe(-0.726920+0.188910j, 5000.0, 0.9, easing=EasingFunction.CIRCULAR)
        
        path.enable_loop_back(0.1)
        return path
    
    @staticmethod
    def mandelbrot_lightning() -> ZoomPath:
        """
        Zoom sequence along the negative real axis (lightning-like structures).
        """
        path = ZoomPath("Mandelbrot: Lightning")
        
        path.add_keyframe(0+0j, 1.0, 0.0)
        path.add_keyframe(-1.5+0j, 3.0, 0.15)
        path.add_keyframe(-1.8+0j, 10.0, 0.35)
        path.add_keyframe(-1.85+0j, 50.0, 0.6)
        path.add_keyframe(-1.859+0j, 200.0, 0.8)
        path.add_keyframe(-1.8595+0j, 1000.0, 0.95)
        
        path.enable_loop_back(0.05)
        return path
    
    @staticmethod
    def mandelbrot_spiral_galaxy() -> ZoomPath:
        """
        Zoom into spiral-like structures in the Mandelbrot set.
        """
        path = ZoomPath("Mandelbrot: Spiral Galaxy")
        
        path.add_keyframe(0+0j, 1.0, 0.0, rotation=0.0)
        path.add_keyframe(0.001643721971153+0.822467633298876j, 10.0, 0.25, rotation=np.pi/4)
        path.add_keyframe(0.001643721971153+0.822467633298876j, 100.0, 0.5, rotation=np.pi/2)
        path.add_keyframe(0.001643721971153+0.822467633298876j, 1000.0, 0.75, rotation=3*np.pi/4)
        path.add_keyframe(0.001643721971153+0.822467633298876j, 10000.0, 0.95, rotation=np.pi)
        
        path.enable_loop_back()
        return path
    
    @staticmethod
    def julia_dendrite_morph() -> ZoomPath:
        """
        Zoom path that morphs through different Julia set parameters.
        """
        path = ZoomPath("Julia: Dendrite Morph")
        
        # Start with classic dendrite
        path.add_keyframe(0+0j, 1.0, 0.0)
        path.add_keyframe(0+0j, 2.0, 0.2)
        path.add_keyframe(0+0j, 5.0, 0.4)
        path.add_keyframe(0+0j, 20.0, 0.6)
        path.add_keyframe(0+0j, 100.0, 0.8)
        path.add_keyframe(0+0j, 500.0, 0.95)
        
        path.enable_loop_back()
        return path
    
    @staticmethod
    def burning_ship_journey() -> ZoomPath:
        """
        Zoom sequence exploring the Burning Ship fractal's ship-like structures.
        """
        path = ZoomPath("Burning Ship: Ship Journey")
        
        # Start with overview showing ship silhouette
        path.add_keyframe(-0.5-0.6j, 1.0, 0.0)
        
        # Approach the main ship structure
        path.add_keyframe(-1.0-0.6j, 3.0, 0.2)
        
        # Enter ship details
        path.add_keyframe(-1.7-0.03j, 10.0, 0.4)
        
        # Explore intricate ship details
        path.add_keyframe(-1.775-0.01j, 50.0, 0.6)
        
        # Deep zoom into ship's "rigging"
        path.add_keyframe(-1.7751-0.003j, 200.0, 0.8)
        
        # Maximum detail
        path.add_keyframe(-1.77513-0.0015j, 1000.0, 0.95)
        
        path.enable_loop_back()
        return path
    
    @staticmethod
    def tricorn_symmetry_dance() -> ZoomPath:
        """
        Zoom path highlighting the three-fold symmetry of the Tricorn set.
        """
        path = ZoomPath("Tricorn: Symmetry Dance")
        
        # Start with overview
        path.add_keyframe(0+0j, 1.0, 0.0, rotation=0.0)
        
        # Rotate to show symmetry while zooming
        path.add_keyframe(0+0j, 2.0, 0.2, rotation=2*np.pi/3)
        path.add_keyframe(-0.5+0j, 5.0, 0.4, rotation=4*np.pi/3)
        path.add_keyframe(-0.8+0.2j, 20.0, 0.6, rotation=2*np.pi)
        path.add_keyframe(-0.85+0.15j, 100.0, 0.8, rotation=8*np.pi/3)
        path.add_keyframe(-0.855+0.145j, 500.0, 0.95, rotation=10*np.pi/3)
        
        path.enable_loop_back()
        return path
    
    @staticmethod
    def create_custom_zoom_path(fractal_type: str, zoom_factor: float = 1000.0) -> ZoomPath:
        """
        Create a custom zoom path for any fractal type.
        
        Parameters
        ----------
        fractal_type : str
            Type of fractal ('mandelbrot', 'julia', 'burning_ship', 'tricorn')
        zoom_factor : float
            Maximum zoom level to reach
            
        Returns
        -------
        ZoomPath
            Customized zoom path
        """
        path = ZoomPath(f"Custom {fractal_type.title()} Zoom")
        
        # Default zoom progression
        zoom_levels = [1.0, 5.0, 25.0, 125.0, zoom_factor]
        time_points = np.linspace(0.0, 0.9, len(zoom_levels))
        
        # Fractal-specific center points
        centers = {
            'mandelbrot': [0+0j, -0.5+0j, -0.7+0.1j, -0.72+0.18j, -0.725+0.185j],
            'julia': [0+0j, 0+0j, 0+0j, 0+0j, 0+0j],
            'burning_ship': [-0.5-0.6j, -1.0-0.5j, -1.5-0.1j, -1.7-0.05j, -1.75-0.02j],
            'tricorn': [0+0j, -0.2+0j, -0.5+0.1j, -0.7+0.15j, -0.75+0.12j]
        }
        
        fractal_centers = centers.get(fractal_type, centers['mandelbrot'])
        
        for i, (center, zoom, time) in enumerate(zip(fractal_centers, zoom_levels, time_points)):
            easing = EasingFunction.EASE_IN_OUT if i < len(zoom_levels) - 1 else EasingFunction.EXPONENTIAL
            path.add_keyframe(center, zoom, time, easing=easing)
        
        path.enable_loop_back()
        return path

class ZoomPathAnalyzer:
    """
    Tools for analyzing and optimizing zoom paths.
    """
    
    @staticmethod
    def analyze_path_smoothness(path: ZoomPath, num_samples: int = 100) -> Dict[str, float]:
        """
        Analyze the smoothness of a zoom path.
        
        Parameters
        ----------
        path : ZoomPath
            Zoom path to analyze
        num_samples : int
            Number of samples to use for analysis
            
        Returns
        -------
        dict
            Analysis results including smoothness metrics
        """
        if len(path.keyframes) < 2:
            return {'smoothness_score': 0.0, 'max_acceleration': 0.0}
        
        # Sample path at regular intervals
        times = np.linspace(0.0, 1.0, num_samples)
        positions = []
        zooms = []
        
        for t in times:
            center, zoom, _ = path.interpolate_at_time(t)
            positions.append(center)
            zooms.append(zoom)
        
        # Calculate velocity and acceleration
        velocities = []
        accelerations = []
        
        for i in range(1, len(positions)):
            dt = times[i] - times[i-1]
            velocity = abs(positions[i] - positions[i-1]) / dt
            velocities.append(velocity)
            
            if i > 1:
                acceleration = abs(velocities[i-1] - velocities[i-2]) / dt
                accelerations.append(acceleration)
        
        smoothness_score = 1.0 / (1.0 + np.std(accelerations)) if accelerations else 0.0
        max_acceleration = max(accelerations) if accelerations else 0.0
        
        return {
            'smoothness_score': smoothness_score,
            'max_acceleration': max_acceleration,
            'path_length': path.get_path_length(),
            'zoom_range': max(zooms) / min(zooms) if min(zooms) > 0 else 0.0
        }
    
    @staticmethod
    def suggest_optimizations(path: ZoomPath) -> List[str]:
        """
        Suggest optimizations for a zoom path.
        
        Parameters
        ----------
        path : ZoomPath
            Zoom path to analyze
            
        Returns
        -------
        list
            List of optimization suggestions
        """
        suggestions = []
        analysis = ZoomPathAnalyzer.analyze_path_smoothness(path)
        
        if analysis['smoothness_score'] < 0.5:
            suggestions.append("Consider using smoother easing functions (EASE_IN_OUT)")
        
        if analysis['max_acceleration'] > 100.0:
            suggestions.append("Reduce abrupt changes in zoom speed")
        
        if analysis['zoom_range'] > 10000.0:
            suggestions.append("Consider splitting extreme zoom range into multiple segments")
        
        if len(path.keyframes) < 3:
            suggestions.append("Add more keyframes for smoother interpolation")
        
        return suggestions

# Export commonly used zoom paths
MANDELBROT_PATHS = {
    'seahorse_valley': PredefinedZoomPaths.mandelbrot_seahorse_valley(),
    'lightning': PredefinedZoomPaths.mandelbrot_lightning(),
    'spiral_galaxy': PredefinedZoomPaths.mandelbrot_spiral_galaxy()
}

JULIA_PATHS = {
    'dendrite_morph': PredefinedZoomPaths.julia_dendrite_morph()
}

BURNING_SHIP_PATHS = {
    'ship_journey': PredefinedZoomPaths.burning_ship_journey()
}

TRICORN_PATHS = {
    'symmetry_dance': PredefinedZoomPaths.tricorn_symmetry_dance()
}