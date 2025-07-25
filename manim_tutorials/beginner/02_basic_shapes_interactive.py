"""
Interactive version of Basic Shapes tutorial with Jupyter widgets.
This file demonstrates how to use interactive widgets with basic geometric shapes.
"""
from manim import *
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from utils.widget_utils import *
import ipywidgets as widgets
from IPython.display import display

# This would be used in a Jupyter notebook cell
def interactive_basic_shapes_demo():
    """
    Demonstrate interactive basic shapes with widgets.
    This function would be called in a Jupyter notebook to create interactive controls.
    """
    # Create interactive widgets
    circle_color_picker = create_color_picker_widget(
        color="#FF69B4", description="Circle Color"
    )
    
    square_color_picker = create_color_picker_widget(
        color="#1E90FF", description="Square Color"
    )
    
    triangle_color_picker = create_color_picker_widget(
        color="#32CD32", description="Triangle Color"
    )
    
    rectangle_color_picker = create_color_picker_widget(
        color="#FFD700", description="Rectangle Color"
    )
    
    ellipse_color_picker = create_color_picker_widget(
        color="#FF8C00", description="Ellipse Color"
    )
    
    opacity_slider = create_slider_widget(
        min_val=0.1, max_val=1.0, step=0.1, value=0.5, description="Shape Opacity"
    )
    
    # Display the widgets
    controller = widgets.VBox([
        widgets.HTML("<h3>Interactive Basic Shapes Controller</h3>"),
        circle_color_picker,
        square_color_picker,
        triangle_color_picker,
        rectangle_color_picker,
        ellipse_color_picker,
        opacity_slider
    ])
    
    display(controller)
    
    return {
        'circle_color_picker': circle_color_picker,
        'square_color_picker': square_color_picker,
        'triangle_color_picker': triangle_color_picker,
        'rectangle_color_picker': rectangle_color_picker,
        'ellipse_color_picker': ellipse_color_picker,
        'opacity_slider': opacity_slider
    }

class InteractiveBasicShapes(Scene):
    """
    An interactive version of the BasicShapes scene that demonstrates
    how parameters could be controlled via widgets.
    """
    def construct(self):
        # Title
        title = Text("Interactive Basic Shapes", font_size=36)
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
        
        # Create various shapes
        circle = Circle()
        square = Square()
        triangle = Triangle()
        rectangle = Rectangle(height=2, width=3)
        ellipse = Ellipse()
        
        # Set colors for each shape
        circle.set_fill(PINK, opacity=0.5)
        square.set_fill(BLUE, opacity=0.5)
        triangle.set_fill(GREEN, opacity=0.5)
        rectangle.set_fill(YELLOW, opacity=0.5)
        ellipse.set_fill(ORANGE, opacity=0.5)
        
        # Position the shapes
        circle.shift(LEFT * 3)
        square.shift(LEFT)
        triangle.shift(RIGHT)
        rectangle.shift(RIGHT * 3)
        ellipse.shift(DOWN * 2)
        
        # Add shapes to the scene
        self.play(Create(circle))
        self.play(Create(square))
        self.play(Create(triangle))
        self.play(Create(rectangle))
        self.play(Create(ellipse))
        
        # Wait for a moment
        self.wait(2)
        
        # Show how parameters could be adjusted
        self.play(
            circle.animate.set_fill(RED),
            square.animate.set_fill(PURPLE),
            triangle.animate.set_fill(YELLOW),
            rectangle.animate.set_fill(BLUE),
            ellipse.animate.set_fill(PINK),
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
                  FadeOut(square), FadeOut(triangle), FadeOut(rectangle), 
                  FadeOut(ellipse), FadeOut(final_text))
        self.wait(1)

# Example usage in a Jupyter notebook:
"""
# In a Jupyter notebook cell, you would run:

from manim_tutorials.beginner.02_basic_shapes_interactive import interactive_basic_shapes_demo

# Create the interactive controller
widgets_controller = interactive_basic_shapes_demo()

# Then render the scene
%%manim -pql InteractiveBasicShapes

from manim_tutorials.beginner.02_basic_shapes_interactive import InteractiveBasicShapes

class InteractiveBasicShapes(InteractiveBasicShapes):
    def construct(self):
        super().construct()
"""

if __name__ == "__main__":
    # This is just for testing the file can be imported
    print("Interactive Basic Shapes module loaded successfully")