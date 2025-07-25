"""
Interactive version of Getting Started tutorial with Jupyter widgets.
This file demonstrates how to use interactive widgets with basic Manim scenes.
"""
from manim import *
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from utils.widget_utils import *
import ipywidgets as widgets
from IPython.display import display

# This would be used in a Jupyter notebook cell
def interactive_getting_started_demo():
    """
    Demonstrate interactive getting started example with widgets.
    This function would be called in a Jupyter notebook to create interactive controls.
    """
    # Create interactive widgets
    circle_color_picker = create_color_picker_widget(
        color="#FF69B4", description="Circle Color"
    )
    
    circle_opacity_slider = create_slider_widget(
        min_val=0.1, max_val=1.0, step=0.1, value=0.5, description="Circle Opacity"
    )
    
    text_content_textbox = create_text_widget(
        value="Hello, Manim!", description="Text Content"
    )
    
    text_color_picker = create_color_picker_widget(
        color="#FFFFFF", description="Text Color"
    )
    
    wait_duration_slider = create_slider_widget(
        min_val=1, max_val=5, step=0.5, value=2, description="Wait Duration"
    )
    
    # Display the widgets
    controller = widgets.VBox([
        widgets.HTML("<h3>Interactive Getting Started Controller</h3>"),
        circle_color_picker,
        circle_opacity_slider,
        text_content_textbox,
        text_color_picker,
        wait_duration_slider
    ])
    
    display(controller)
    
    return {
        'circle_color_picker': circle_color_picker,
        'circle_opacity_slider': circle_opacity_slider,
        'text_content_textbox': text_content_textbox,
        'text_color_picker': text_color_picker,
        'wait_duration_slider': wait_duration_slider
    }

class InteractiveGettingStarted(Scene):
    """
    An interactive version of the GettingStarted scene that demonstrates
    how parameters could be controlled via widgets.
    """
    def construct(self):
        # Title
        title = Text("Interactive Getting Started", font_size=36)
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
        
        # Create a simple circle
        circle = Circle()
        circle.set_fill(PINK, opacity=0.5)
        
        # Create text
        text = Text("Hello, Manim!")
        
        # Position the text below the circle
        text.next_to(circle, DOWN)
        
        # Add the circle and text to the scene
        self.play(Create(circle))
        self.play(Write(text))
        
        # Wait for a moment
        self.wait(2)
        
        # Show how parameters could be adjusted
        self.play(
            circle.animate.set_fill(BLUE).set_stroke(BLUE),
            text.animate.set_color(YELLOW),
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
                  FadeOut(text), FadeOut(final_text))
        self.wait(1)

# Example usage in a Jupyter notebook:
"""
# In a Jupyter notebook cell, you would run:

from manim_tutorials.beginner.01_getting_started_interactive import interactive_getting_started_demo

# Create the interactive controller
widgets_controller = interactive_getting_started_demo()

# Then render the scene
%%manim -pql InteractiveGettingStarted

from manim_tutorials.beginner.01_getting_started_interactive import InteractiveGettingStarted

class InteractiveGettingStarted(InteractiveGettingStarted):
    def construct(self):
        super().construct()
"""

if __name__ == "__main__":
    # This is just for testing the file can be imported
    print("Interactive Getting Started module loaded successfully")