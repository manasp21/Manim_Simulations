"""
Interactive version of Colors and Styling tutorial with Jupyter widgets.
This file demonstrates how to use interactive widgets with Manim styling scenes.
"""
from manim import *
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from utils.widget_utils import *
import ipywidgets as widgets
from IPython.display import display

# This would be used in a Jupyter notebook cell
def interactive_colors_styling_demo():
    """
    Demonstrate interactive colors and styling with widgets.
    This function would be called in a Jupyter notebook to create interactive controls.
    """
    # Create interactive widgets
    circle1_color_picker = create_color_picker_widget(
        color="#FF0000", description="Circle 1 Color"
    )
    
    circle2_color_picker = create_color_picker_widget(
        color="#00FF00", description="Circle 2 Color"
    )
    
    circle3_color_picker = create_color_picker_widget(
        color="#0000FF", description="Circle 3 Color"
    )
    
    square1_stroke_slider = create_integer_slider_widget(
        min_val=1, max_val=20, step=1, value=5, description="Square 1 Stroke"
    )
    
    square2_stroke_slider = create_integer_slider_widget(
        min_val=1, max_val=20, step=1, value=10, description="Square 2 Stroke"
    )
    
    opacity_slider = create_slider_widget(
        min_val=0.1, max_val=1.0, step=0.1, value=0.5, description="Fill Opacity"
    )
    
    # Display the widgets
    controller = widgets.VBox([
        widgets.HTML("<h3>Interactive Colors and Styling Controller</h3>"),
        circle1_color_picker,
        circle2_color_picker,
        circle3_color_picker,
        square1_stroke_slider,
        square2_stroke_slider,
        opacity_slider
    ])
    
    display(controller)
    
    return {
        'circle1_color_picker': circle1_color_picker,
        'circle2_color_picker': circle2_color_picker,
        'circle3_color_picker': circle3_color_picker,
        'square1_stroke_slider': square1_stroke_slider,
        'square2_stroke_slider': square2_stroke_slider,
        'opacity_slider': opacity_slider
    }

class InteractiveColorsAndStyling(Scene):
    """
    An interactive version of the ColorsAndStyling scene that demonstrates
    how parameters could be controlled via widgets.
    """
    def construct(self):
        # Title
        title = Text("Interactive Colors and Styling", font_size=36)
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
        
        # Create circles with different colors
        circle1 = Circle(radius=1, color=RED)
        circle1.set_fill(RED, opacity=0.5)
        
        circle2 = Circle(radius=1, color=GREEN)
        circle2.set_fill(GREEN, opacity=0.5)
        
        circle3 = Circle(radius=1, color=BLUE)
        circle3.set_fill(BLUE, opacity=0.5)
        
        # Position the circles
        circle1.shift(LEFT * 2)
        circle3.shift(RIGHT * 2)
        
        # Create squares with different stroke widths
        square1 = Square(side_length=1, color=YELLOW)
        square1.set_fill(YELLOW, opacity=0.5)
        square1.set_stroke(width=5)
        
        square2 = Square(side_length=1, color=PURPLE)
        square2.set_fill(PURPLE, opacity=0.5)
        square2.set_stroke(width=10)
        
        # Position the squares below the circles
        square1.shift(DOWN * 2 + LEFT)
        square2.shift(DOWN * 2 + RIGHT)
        
        # Display all objects
        self.play(Create(circle1), Create(circle2), Create(circle3))
        self.play(Create(square1), Create(square2))
        self.wait(2)
        
        # Show how parameters could be adjusted
        self.play(
            circle1.animate.set_fill(ORANGE).set_stroke(ORANGE),
            circle2.animate.set_fill(PINK).set_stroke(PINK),
            circle3.animate.set_fill(WHITE).set_stroke(WHITE),
            square1.animate.set_stroke(width=15),
            square2.animate.set_stroke(width=3),
            run_time=2
        )
        
        self.wait(2)
        
        # Final message
        final_text = Text("Try adjusting the widgets above!", font_size=30)
        final_text.next_to(explanation, DOWN, buff=1)
        self.play(Write(final_text))
        self.wait(2)
        
        # Fade out all objects
        self.play(FadeOut(title), FadeOut(explanation), FadeOut(circle1), 
                  FadeOut(circle2), FadeOut(circle3), FadeOut(square1), 
                  FadeOut(square2), FadeOut(final_text))
        self.wait(1)

# Example usage in a Jupyter notebook:
"""
# In a Jupyter notebook cell, you would run:

from manim_tutorials.beginner.05_colors_and_styling_interactive import interactive_colors_styling_demo

# Create the interactive controller
widgets_controller = interactive_colors_styling_demo()

# Then render the scene
%%manim -pql InteractiveColorsAndStyling

from manim_tutorials.beginner.05_colors_and_styling_interactive import InteractiveColorsAndStyling

class InteractiveColorsAndStyling(InteractiveColorsAndStyling):
    def construct(self):
        super().construct()
"""

if __name__ == "__main__":
    # This is just for testing the file can be imported
    print("Interactive Colors and Styling module loaded successfully")