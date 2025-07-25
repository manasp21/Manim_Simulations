"""
Interactive version of Simple Animations tutorial with Jupyter widgets.
This file demonstrates how to use interactive widgets with Manim scenes.
"""
from manim import *
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from utils.widget_utils import *
import ipywidgets as widgets
from IPython.display import display

# This would be used in a Jupyter notebook cell
def interactive_simple_animations_demo():
    """
    Demonstrate interactive simple animations with widgets.
    This function would be called in a Jupyter notebook to create interactive controls.
    """
    # Create interactive widgets
    animation_speed_slider = create_slider_widget(
        min_val=0.1, max_val=3.0, step=0.1, value=1.0, description="Animation Speed"
    )
    
    shape_size_slider = create_slider_widget(
        min_val=0.5, max_val=3.0, step=0.1, value=1.0, description="Shape Size"
    )
    
    circle_color_picker = create_color_picker_widget(
        color="#FF69B4", description="Circle Color"
    )
    
    square_color_picker = create_color_picker_widget(
        color="#1E90FF", description="Square Color"
    )
    
    rotation_slider = create_slider_widget(
        min_val=0, max_val=2*PI, step=0.1, value=PI, description="Rotation Angle"
    )
    
    # Display the widgets
    controller = widgets.VBox([
        widgets.HTML("<h3>Interactive Simple Animations Controller</h3>"),
        animation_speed_slider,
        shape_size_slider,
        circle_color_picker,
        square_color_picker,
        rotation_slider
    ])
    
    display(controller)
    
    return {
        'animation_speed_slider': animation_speed_slider,
        'shape_size_slider': shape_size_slider,
        'circle_color_picker': circle_color_picker,
        'square_color_picker': square_color_picker,
        'rotation_slider': rotation_slider
    }

class InteractiveSimpleAnimations(Scene):
    """
    An interactive version of the SimpleAnimations scene that demonstrates
    how parameters could be controlled via widgets.
    """
    def construct(self):
        # Title
        title = Text("Interactive Simple Animations", font_size=36)
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
        
        # Demonstrate different animations with varying parameters
        # Create a circle
        circle = Circle(radius=1)
        circle.set_fill(PINK, opacity=0.5)
        
        # Create a square
        square = Square(side_length=1)
        square.set_fill(BLUE, opacity=0.5)
        
        # Position the square to the right of the circle
        square.shift(RIGHT * 3)
        
        # Show creation of both shapes
        self.play(Create(circle), Create(square))
        self.wait(1)
        
        # Transform the circle into a square
        self.play(Transform(circle, square.copy()))
        self.wait(1)
        
        # Rotate the square
        self.play(Rotate(square, PI))
        self.wait(1)
        
        # Move the circle to the left
        self.play(circle.animate.shift(LEFT * 3))
        self.wait(1)
        
        # Show how parameters could be adjusted
        self.play(
            circle.animate.scale(1.5).set_color(YELLOW),
            square.animate.scale(0.8).set_color(GREEN),
            run_time=2
        )
        
        self.wait(2)
        
        # Final message
        final_text = Text("Try adjusting the widgets above!", font_size=30)
        final_text.next_to(explanation, DOWN, buff=1)
        self.play(Write(final_text))
        self.wait(2)
        
        # Fade out both objects
        self.play(FadeOut(circle), FadeOut(square), FadeOut(final_text))
        self.wait(1)

# Example usage in a Jupyter notebook:
"""
# In a Jupyter notebook cell, you would run:

from manim_tutorials.beginner.03_simple_animations_interactive import interactive_simple_animations_demo

# Create the interactive controller
widgets_controller = interactive_simple_animations_demo()

# Then render the scene
%%manim -pql InteractiveSimpleAnimations

from manim_tutorials.beginner.03_simple_animations_interactive import InteractiveSimpleAnimations

class InteractiveSimpleAnimations(InteractiveSimpleAnimations):
    def construct(self):
        super().construct()
"""

if __name__ == "__main__":
    # This is just for testing the file can be imported
    print("Interactive Simple Animations module loaded successfully")