"""
Interactive version of Custom Animations tutorial with Jupyter widgets.
This file demonstrates how to use interactive widgets with Manim custom animations.
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
def interactive_custom_animations_demo():
    """
    Demonstrate interactive custom animations with widgets.
    This function would be called in a Jupyter notebook to create interactive controls.
    """
    # Create interactive widgets
    color_count_slider = create_integer_slider_widget(
        min_val=2, max_val=10, step=1, value=6, description="Color Count"
    )
    
    revolutions_slider = create_slider_widget(
        min_val=1, max_val=10, step=0.5, value=3.0, description="Revolutions"
    )
    
    scale_factor_slider = create_slider_widget(
        min_val=1.0, max_val=3.0, step=0.1, value=1.5, description="Scale Factor"
    )
    
    animation_type_dropdown = create_dropdown_widget(
        options=['Color Cycle', 'Spiral Motion', 'Pulse'],
        value='Color Cycle',
        description="Animation Type"
    )
    
    # Display the widgets
    controller = widgets.VBox([
        widgets.HTML("<h3>Interactive Custom Animations Controller</h3>"),
        color_count_slider,
        revolutions_slider,
        scale_factor_slider,
        animation_type_dropdown
    ])
    
    display(controller)
    
    return {
        'color_count_slider': color_count_slider,
        'revolutions_slider': revolutions_slider,
        'scale_factor_slider': scale_factor_slider,
        'animation_type_dropdown': animation_type_dropdown
    }

class InteractiveCustomAnimations(Scene):
    """
    An interactive version of the CustomAnimations scene that demonstrates
    how parameters could be controlled via widgets.
    """
    def construct(self):
        # Title
        title = Text("Interactive Custom Animations", font_size=36)
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
        
        # Create a custom animation class
        class ColorCycle(Animation):
            def __init__(self, mobject, colors, **kwargs):
                self.colors = colors
                super().__init__(mobject, **kwargs)
            
            def interpolate_mobject(self, alpha):
                # Calculate which color to use based on alpha
                index = int(alpha * len(self.colors)) % len(self.colors)
                self.mobject.set_color(self.colors[index])
        
        # Create a shape to apply the custom animation to
        square = Square(fill_color=RED, fill_opacity=0.8)
        
        # Define a list of colors to cycle through
        colors = [RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE]
        
        # Apply the custom animation
        self.play(ColorCycle(square, colors, run_time=3))
        self.wait(1)
        
        # Create another custom animation - spiral motion
        class SpiralMotion(Animation):
            def __init__(self, mobject, revolutions=2, **kwargs):
                self.revolutions = revolutions
                super().__init__(mobject, **kwargs)
            
            def interpolate_mobject(self, alpha):
                # Calculate spiral position
                angle = alpha * self.revolutions * 2 * PI
                radius = 1 - alpha  # Spiral inward
                x = radius * np.cos(angle)
                y = radius * np.sin(angle)
                self.mobject.move_to([x, y, 0])
        
        # Create a dot for the spiral animation
        dot = Dot(color=YELLOW)
        
        # Apply the spiral animation
        self.play(SpiralMotion(dot, revolutions=3, run_time=4))
        self.wait(2)
        
        # Create a third custom animation - pulse effect
        class Pulse(Animation):
            def __init__(self, mobject, scale_factor=1.5, **kwargs):
                self.scale_factor = scale_factor
                super().__init__(mobject, **kwargs)
            
            def interpolate_mobject(self, alpha):
                # Calculate scale based on alpha (pulse effect)
                scale = 1 + (self.scale_factor - 1) * np.sin(alpha * PI)
                self.mobject.set_width(self.mobject.width * scale / (1 + (self.scale_factor - 1) * np.sin((alpha - 0.01) * PI)))
        
        # Create a shape for the pulse animation
        circle = Circle(radius=1, fill_color=BLUE, fill_opacity=0.5)
        
        # Apply the pulse animation
        self.play(Pulse(circle, scale_factor=2, run_time=2))
        self.play(Pulse(circle, scale_factor=2, run_time=2))
        self.wait(2)
        
        # Show how parameters could be adjusted
        self.play(
            circle.animate.set_color(YELLOW),
            square.animate.set_color(GREEN),
            dot.animate.set_color(RED),
            run_time=1
        )
        
        self.wait(2)
        
        # Final message
        final_text = Text("Try adjusting the widgets above!", font_size=30)
        final_text.next_to(explanation, DOWN, buff=1)
        self.play(Write(final_text))
        self.wait(2)
        
        # Fade out all objects
        self.play(FadeOut(title), FadeOut(explanation), FadeOut(square), 
                  FadeOut(dot), FadeOut(circle), FadeOut(final_text))
        self.wait(1)

# Example usage in a Jupyter notebook:
"""
# In a Jupyter notebook cell, you would run:

from manim_tutorials.advanced.02_custom_animations_interactive import interactive_custom_animations_demo

# Create the interactive controller
widgets_controller = interactive_custom_animations_demo()

# Then render the scene
%%manim -pql InteractiveCustomAnimations

from manim_tutorials.advanced.02_custom_animations_interactive import InteractiveCustomAnimations

class InteractiveCustomAnimations(InteractiveCustomAnimations):
    def construct(self):
        super().construct()
"""

if __name__ == "__main__":
    # This is just for testing the file can be imported
    print("Interactive Custom Animations module loaded successfully")