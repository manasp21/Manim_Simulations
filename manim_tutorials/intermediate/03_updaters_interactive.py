"""
Interactive version of Updaters tutorial with Jupyter widgets.
This file demonstrates how to use interactive widgets with Manim updater scenes.
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
def interactive_updaters_demo():
    """
    Demonstrate interactive updaters with widgets.
    This function would be called in a Jupyter notebook to create interactive controls.
    """
    # Create interactive widgets
    speed_slider = create_slider_widget(
        min_val=0.1, max_val=5.0, step=0.1, value=2.0, description="Animation Speed"
    )
    
    rotation_speed_slider = create_slider_widget(
        min_val=0.1, max_val=2.0, step=0.1, value=0.2, description="Rotation Speed"
    )
    
    dot_size_slider = create_slider_widget(
        min_val=0.1, max_val=2.0, step=0.1, value=1.0, description="Dot Size"
    )
    
    path_size_slider = create_slider_widget(
        min_val=1.0, max_val=5.0, step=0.1, value=2.0, description="Path Size"
    )
    
    dot_color_picker = create_color_picker_widget(
        color="#FF0000", description="Dot Color"
    )
    
    path_color_picker = create_color_picker_widget(
        color="#0000FF", description="Path Color"
    )
    
    # Display the widgets
    controller = widgets.VBox([
        widgets.HTML("<h3>Interactive Updaters Controller</h3>"),
        speed_slider,
        rotation_speed_slider,
        dot_size_slider,
        path_size_slider,
        dot_color_picker,
        path_color_picker
    ])
    
    display(controller)
    
    return {
        'speed_slider': speed_slider,
        'rotation_speed_slider': rotation_speed_slider,
        'dot_size_slider': dot_size_slider,
        'path_size_slider': path_size_slider,
        'dot_color_picker': dot_color_picker,
        'path_color_picker': path_color_picker
    }

class InteractiveUpdaters(Scene):
    """
    An interactive version of the Updaters scene that demonstrates
    how parameters could be controlled via widgets.
    """
    def construct(self):
        # Title
        title = Text("Interactive Updaters", font_size=36)
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
        
        # Create a moving dot
        dot = Dot(color=RED)
        
        # Create a text that follows the dot
        label = Text("Moving Dot", font_size=24)
        label.add_updater(lambda m: m.next_to(dot, UP))
        
        # Add objects to scene
        self.add(dot, label)
        
        # Move the dot in a square path
        self.play(dot.animate.shift(RIGHT * 2), run_time=2)
        self.play(dot.animate.shift(UP * 2), run_time=2)
        self.play(dot.animate.shift(LEFT * 2), run_time=2)
        self.play(dot.animate.shift(DOWN * 2), run_time=2)
        
        # Remove the updater
        label.clear_updaters()
        self.wait(1)
        
        # Create a rotating square with a dot
        square = Square(color=BLUE)
        dot2 = Dot(color=YELLOW)
        dot2.move_to(square.get_right())
        
        # Define updater for dot2 to move with square
        dot2.add_updater(lambda d: d.move_to(square.get_right()))
        
        self.play(Create(square))
        self.add(dot2)
        
        # Rotate the square
        self.play(Rotate(square, PI * 2), run_time=4)
        self.wait(1)
        
        # Remove updater and move dot independently
        dot2.clear_updaters()
        self.play(dot2.animate.shift(UP * 2))
        self.wait(2)
        
        # Show how parameters could be adjusted
        self.play(
            dot.animate.scale(1.5).set_color(YELLOW),
            dot2.animate.scale(1.5).set_color(GREEN),
            square.animate.set_color(PURPLE),
            run_time=2
        )
        
        self.wait(2)
        
        # Final message
        final_text = Text("Try adjusting the widgets above!", font_size=30)
        final_text.next_to(explanation, DOWN, buff=1)
        self.play(Write(final_text))
        self.wait(2)
        
        # Fade out all objects
        self.play(FadeOut(title), FadeOut(explanation), FadeOut(dot), 
                  FadeOut(label), FadeOut(square), FadeOut(dot2), FadeOut(final_text))
        self.wait(1)

# Example usage in a Jupyter notebook:
"""
# In a Jupyter notebook cell, you would run:

from manim_tutorials.intermediate.03_updaters_interactive import interactive_updaters_demo

# Create the interactive controller
widgets_controller = interactive_updaters_demo()

# Then render the scene
%%manim -pql InteractiveUpdaters

from manim_tutorials.intermediate.03_updaters_interactive import InteractiveUpdaters

class InteractiveUpdaters(InteractiveUpdaters):
    def construct(self):
        super().construct()
"""

if __name__ == "__main__":
    # This is just for testing the file can be imported
    print("Interactive Updaters module loaded successfully")