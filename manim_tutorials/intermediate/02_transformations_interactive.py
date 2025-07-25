"""
Interactive version of Transformations tutorial with Jupyter widgets.
This file demonstrates how to use interactive widgets with Manim transformation scenes.
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
def interactive_transformations_demo():
    """
    Demonstrate interactive transformations with widgets.
    This function would be called in a Jupyter notebook to create interactive controls.
    """
    # Create interactive widgets
    scale_slider = create_slider_widget(
        min_val=0.1, max_val=3.0, step=0.1, value=2.0, description="Scale Factor"
    )
    
    rotation_slider = create_slider_widget(
        min_val=0, max_val=2*PI, step=0.1, value=PI/4, description="Rotation Angle"
    )
    
    move_x_slider = create_slider_widget(
        min_val=-5, max_val=5, step=0.1, value=2, description="Move X"
    )
    
    move_y_slider = create_slider_widget(
        min_val=-5, max_val=5, step=0.1, value=2, description="Move Y"
    )
    
    shape1_color_picker = create_color_picker_widget(
        color="#0000FF", description="Shape 1 Color"
    )
    
    shape2_color_picker = create_color_picker_widget(
        color="#00FF00", description="Shape 2 Color"
    )
    
    shape3_color_picker = create_color_picker_widget(
        color="#FF0000", description="Shape 3 Color"
    )
    
    # Display the widgets
    controller = widgets.VBox([
        widgets.HTML("<h3>Interactive Transformations Controller</h3>"),
        scale_slider,
        rotation_slider,
        move_x_slider,
        move_y_slider,
        shape1_color_picker,
        shape2_color_picker,
        shape3_color_picker
    ])
    
    display(controller)
    
    return {
        'scale_slider': scale_slider,
        'rotation_slider': rotation_slider,
        'move_x_slider': move_x_slider,
        'move_y_slider': move_y_slider,
        'shape1_color_picker': shape1_color_picker,
        'shape2_color_picker': shape2_color_picker,
        'shape3_color_picker': shape3_color_picker
    }

class InteractiveTransformations(Scene):
    """
    An interactive version of the Transformations scene that demonstrates
    how parameters could be controlled via widgets.
    """
    def construct(self):
        # Title
        title = Text("Interactive Transformations", font_size=36)
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
        
        # Create initial shapes
        circle = Circle(fill_color=BLUE, fill_opacity=0.5)
        square = Square(fill_color=GREEN, fill_opacity=0.5)
        triangle = Triangle(fill_color=RED, fill_opacity=0.5)
        
        # Position the shapes
        circle.shift(LEFT * 3)
        triangle.shift(RIGHT * 3)
        
        # Display initial shapes
        self.play(Create(circle), Create(square), Create(triangle))
        self.wait(1)
        
        # Apply transformations
        # Scale the circle
        self.play(circle.animate.scale(2))
        self.wait(1)
        
        # Rotate the square
        self.play(square.animate.rotate(PI/4))
        self.wait(1)
        
        # Move the triangle
        self.play(triangle.animate.shift(UP * 2))
        self.wait(1)
        
        # Complex transformation - morph square to circle
        circle2 = Circle(radius=1, fill_color=YELLOW, fill_opacity=0.5)
        circle2.shift(RIGHT * 3)
        
        self.play(Transform(square, circle2))
        self.wait(1)
        
        # Apply multiple transformations at once
        self.play(
            circle.animate.shift(DOWN * 2).set_color(PURPLE),
            triangle.animate.shift(DOWN * 2).rotate(PI/2),
            square.animate.shift(DOWN * 2).scale(0.5)
        )
        self.wait(2)
        
        # Show how parameters could be adjusted
        self.play(
            circle.animate.scale(1.5).set_color(ORANGE),
            square.animate.set_color(BLUE),
            triangle.animate.set_color(YELLOW),
            run_time=2
        )
        
        self.wait(2)
        
        # Final message
        final_text = Text("Try adjusting the widgets above!", font_size=30)
        final_text.next_to(explanation, DOWN, buff=1)
        self.play(Write(final_text))
        self.wait(2)
        
        # Fade out all objects
        self.play(FadeOut(title), FadeOut(explanation), FadeOut(circle), 
                  FadeOut(square), FadeOut(triangle), FadeOut(final_text))
        self.wait(1)

# Example usage in a Jupyter notebook:
"""
# In a Jupyter notebook cell, you would run:

from manim_tutorials.intermediate.02_transformations_interactive import interactive_transformations_demo

# Create the interactive controller
widgets_controller = interactive_transformations_demo()

# Then render the scene
%%manim -pql InteractiveTransformations

from manim_tutorials.intermediate.02_transformations_interactive import InteractiveTransformations

class InteractiveTransformations(InteractiveTransformations):
    def construct(self):
        super().construct()
"""

if __name__ == "__main__":
    # This is just for testing the file can be imported
    print("Interactive Transformations module loaded successfully")