"""
Interactive version of Physics Simulations tutorial with Jupyter widgets.
This file demonstrates how to use interactive widgets with Manim physics simulations.
"""
from manim import *
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from utils.widget_utils import *
import ipywidgets as widgets
from IPython.display import display
import numpy as np

# This would be used in a Jupyter notebook cell
def interactive_physics_simulations_demo():
    """
    Demonstrate interactive physics simulations with widgets.
    This function would be called in a Jupyter notebook to create interactive controls.
    """
    # Create interactive widgets
    pendulum_length_slider = create_slider_widget(
        min_val=1.0, max_val=5.0, step=0.1, value=3.0, description="Pendulum Length"
    )
    
    gravity_slider = create_slider_widget(
        min_val=1.0, max_val=20.0, step=0.5, value=9.8, description="Gravity"
    )
    
    angle_slider = create_slider_widget(
        min_val=0.1, max_val=PI/2, step=0.1, value=PI/4, description="Initial Angle"
    )
    
    bounce_count_slider = create_integer_slider_widget(
        min_val=1, max_val=10, step=1, value=5, description="Bounce Count"
    )
    
    simulation_type_dropdown = create_dropdown_widget(
        options=['Pendulum', 'Bouncing Ball', 'Wave'],
        value='Pendulum',
        description="Simulation"
    )
    
    # Display the widgets
    controller = widgets.VBox([
        widgets.HTML("<h3>Interactive Physics Simulations Controller</h3>"),
        pendulum_length_slider,
        gravity_slider,
        angle_slider,
        bounce_count_slider,
        simulation_type_dropdown
    ])
    
    display(controller)
    
    return {
        'pendulum_length_slider': pendulum_length_slider,
        'gravity_slider': gravity_slider,
        'angle_slider': angle_slider,
        'bounce_count_slider': bounce_count_slider,
        'simulation_type_dropdown': simulation_type_dropdown
    }

class InteractivePhysicsSimulations(Scene):
    """
    An interactive version of the PhysicsSimulations scene that demonstrates
    how parameters could be controlled via widgets.
    """
    def construct(self):
        # Title
        title = Text("Interactive Physics Simulations", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # Explanation text
        explanation = Text(
            "In a Jupyter notebook, you could control\n"
            "these parameters using interactive widgets!",
            font_size=24
        )
        explanation.next_to(title, DOWN, buff=0.5)
        self.play(Write(explanation))
        self.wait(1)
        
        # Create a simple pendulum simulation
        # Pendulum parameters
        length = 3
        gravity = 9.8
        angle = PI / 4  # 45 degrees
        
        # Create pivot point
        pivot = Dot(point=ORIGIN, color=WHITE)
        
        # Create pendulum rod and bob
        rod = Line(ORIGIN, length * DOWN, color=WHITE)
        bob = Dot(point=length * DOWN, color=RED, radius=0.2)
        
        # Group pendulum parts
        pendulum = VGroup(pivot, rod, bob)
        pendulum.shift(UP * 2 + LEFT * 3)
        
        # Add to scene
        self.add(pendulum)
        self.wait(1)
        
        # Animate pendulum swing (simplified)
        def swing_pendulum(mob, alpha):
            # Simple harmonic motion approximation
            current_angle = angle * np.cos(alpha * 2 * PI)
            new_bob_pos = pendulum.get_center() + length * np.array([
                np.sin(current_angle),
                -np.cos(current_angle),
                0
            ])
            rod.put_start_and_end_on(pendulum.get_center(), new_bob_pos)
            bob.move_to(new_bob_pos)
        
        # Create an updater for the pendulum
        pendulum.add_updater(swing_pendulum)
        self.add(pendulum)
        
        # Let it swing for a few seconds
        self.wait(4)
        
        # Remove updater
        pendulum.clear_updaters()
        self.wait(1)
        
        # Create a bouncing ball simulation
        ball = Circle(radius=0.3, color=BLUE, fill_opacity=1)
        ball.shift(RIGHT * 3)
        
        ground = Line(LEFT * 4, RIGHT * 4, color=WHITE).shift(DOWN * 2)
        
        self.play(Create(ground))
        self.play(Create(ball))
        
        # Animate bouncing ball
        bounce_heights = [2, 1.5, 1, 0.5, 0.2]
        for i, height in enumerate(bounce_heights):
            # Move ball up
            self.play(ball.animate.shift(UP * height), rate_func=rush_into, run_time=0.5)
            # Move ball down
            self.play(ball.animate.shift(DOWN * height), rate_func=rush_from, run_time=0.5)
        
        self.wait(2)
        
        # Second part - Wave simulation
        # Create a wave simulation
        # Parameters
        amplitude = 1
        wavelength = 2
        frequency = 1
        
        # Create axes
        axes = Axes(
            x_range=[0, 8, 1],
            y_range=[-2, 2, 1],
            axis_config={"color": BLUE},
        )
        axes_labels = axes.get_axis_labels(x_label="x", y_label="y")
        
        # Create wave function
        def wave_function(x, t=0):
            return amplitude * np.sin(2 * PI * (x / wavelength - frequency * t))
        
        # Create initial wave
        wave = axes.plot(wave_function, color=YELLOW)
        wave_label = Text("Wave Simulation", font_size=24).next_to(axes, UP)
        
        # Display static wave
        self.play(Create(axes), Write(axes_labels), Create(wave), Write(wave_label))
        self.wait(2)
        
        # Animate wave motion
        def update_wave(mob, alpha):
            t = alpha * 2  # Time parameter
            new_wave = axes.plot(lambda x: wave_function(x, t), color=YELLOW)
            mob.become(new_wave)
        
        # Apply the wave animation
        wave.add_updater(update_wave)
        self.add(wave)
        self.wait(4)
        
        # Remove updater and finish
        wave.clear_updaters()
        self.wait(1)
        
        # Show how parameters could be adjusted
        self.play(
            pendulum.animate.set_color(YELLOW),
            ball.animate.set_color(GREEN),
            wave.animate.set_color(RED),
            run_time=1
        )
        
        self.wait(2)
        
        # Final message
        final_text = Text("Try adjusting the widgets above!", font_size=30)
        final_text.next_to(explanation, DOWN, buff=1)
        self.play(Write(final_text))
        self.wait(2)
        
        # Fade out all objects
        self.play(FadeOut(title), FadeOut(explanation), FadeOut(pendulum), 
                  FadeOut(ground), FadeOut(ball), FadeOut(axes),
                  FadeOut(axes_labels), FadeOut(wave), FadeOut(wave_label),
                  FadeOut(final_text))
        self.wait(1)

# Example usage in a Jupyter notebook:
"""
# In a Jupyter notebook cell, you would run:

from manim_tutorials.advanced.04_physics_simulations_interactive import interactive_physics_simulations_demo

# Create the interactive controller
widgets_controller = interactive_physics_simulations_demo()

# Then render the scene
%%manim -pql InteractivePhysicsSimulations

from manim_tutorials.advanced.04_physics_simulations_interactive import InteractivePhysicsSimulations

class InteractivePhysicsSimulations(InteractivePhysicsSimulations):
    def construct(self):
        super().construct()
"""

if __name__ == "__main__":
    # This is just for testing the file can be imported
    print("Interactive Physics Simulations module loaded successfully")