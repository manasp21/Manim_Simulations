"""
Interactive version of Custom Mobjects tutorial with Jupyter widgets.
This file demonstrates how to use interactive widgets with Manim custom mobject scenes.
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
def interactive_custom_mobjects_demo():
    """
    Demonstrate interactive custom mobjects with widgets.
    This function would be called in a Jupyter notebook to create interactive controls.
    """
    # Create interactive widgets
    star_size_slider = create_slider_widget(
        min_val=0.5, max_val=3.0, step=0.1, value=1.0, description="Star Size"
    )
    
    heart_size_slider = create_slider_widget(
        min_val=0.5, max_val=3.0, step=0.1, value=1.0, description="Heart Size"
    )
    
    star_points_slider = create_integer_slider_widget(
        min_val=3, max_val=10, step=1, value=5, description="Star Points"
    )
    
    star_color_picker = create_color_picker_widget(
        color="#FFFF00", description="Star Color"
    )
    
    heart_color_picker = create_color_picker_widget(
        color="#FF0000", description="Heart Color"
    )
    
    fill_opacity_slider = create_slider_widget(
        min_val=0.1, max_val=1.0, step=0.1, value=0.7, description="Fill Opacity"
    )
    
    # Display the widgets
    controller = widgets.VBox([
        widgets.HTML("<h3>Interactive Custom Mobjects Controller</h3>"),
        star_size_slider,
        heart_size_slider,
        star_points_slider,
        star_color_picker,
        heart_color_picker,
        fill_opacity_slider
    ])
    
    display(controller)
    
    return {
        'star_size_slider': star_size_slider,
        'heart_size_slider': heart_size_slider,
        'star_points_slider': star_points_slider,
        'star_color_picker': star_color_picker,
        'heart_color_picker': heart_color_picker,
        'fill_opacity_slider': fill_opacity_slider
    }

class InteractiveCustomMobjects(Scene):
    """
    An interactive version of the CustomMobjects scene that demonstrates
    how parameters could be controlled via widgets.
    """
    def construct(self):
        # Title
        title = Text("Interactive Custom Mobjects", font_size=36)
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
        
        # Create a custom mobject - a star
        class Star(VMobject):
            def __init__(self, **kwargs):
                super().__init__(**kwargs)
                self.create_star()
            
            def create_star(self):
                # Create points for a 5-pointed star
                points = []
                for i in range(10):
                    angle = i * PI / 5
                    radius = 1 if i % 2 == 0 else 0.4
                    x = radius * np.cos(angle)
                    y = radius * np.sin(angle)
                    points.append([x, y, 0])
                
                # Add points to the mobject
                self.set_points_as_corners(points + [points[0]])
        
        # Create and display the star
        star = Star(color=YELLOW, fill_opacity=0.7)
        star.shift(LEFT * 3)
        
        # Create another custom mobject - a heart
        class Heart(VMobject):
            def __init__(self, **kwargs):
                super().__init__(**kwargs)
                self.create_heart()
            
            def create_heart(self):
                # Create points for a heart shape using parametric equations
                points = []
                for i in range(100):
                    t = i * 2 * PI / 99
                    x = 16 * np.sin(t)**3
                    y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)
                    # Scale down the heart
                    points.append([x/10, y/10, 0])
                
                # Add points to the mobject
                self.set_points_smoothly(points)
        
        # Create and display the heart
        heart = Heart(color=RED, fill_opacity=0.7)
        heart.shift(RIGHT * 3)
        
        # Display both custom mobjects
        self.play(Create(star), Create(heart), run_time=3)
        self.wait(2)
        
        # Apply transformations
        self.play(
            star.animate.scale(1.5).set_color(ORANGE),
            heart.animate.scale(1.5).set_color(PINK)
        )
        self.wait(2)
        
        # Move the mobjects
        self.play(
            star.animate.shift(UP * 2),
            heart.animate.shift(DOWN * 2)
        )
        self.wait(2)
        
        # Show how parameters could be adjusted
        self.play(
            star.animate.set_fill(opacity=0.9),
            heart.animate.set_fill(opacity=0.9),
            run_time=2
        )
        
        self.wait(2)
        
        # Final message
        final_text = Text("Try adjusting the widgets above!", font_size=30)
        final_text.next_to(explanation, DOWN, buff=1)
        self.play(Write(final_text))
        self.wait(2)
        
        # Fade out all objects
        self.play(FadeOut(title), FadeOut(explanation), FadeOut(star), 
                  FadeOut(heart), FadeOut(final_text))
        self.wait(1)

# Example usage in a Jupyter notebook:
"""
# In a Jupyter notebook cell, you would run:

from manim_tutorials.intermediate.05_custom_mobjects_interactive import interactive_custom_mobjects_demo

# Create the interactive controller
widgets_controller = interactive_custom_mobjects_demo()

# Then render the scene
%%manim -pql InteractiveCustomMobjects

from manim_tutorials.intermediate.05_custom_mobjects_interactive import InteractiveCustomMobjects

class InteractiveCustomMobjects(InteractiveCustomMobjects):
    def construct(self):
        super().construct()
"""

if __name__ == "__main__":
    # This is just for testing the file can be imported
    print("Interactive Custom Mobjects module loaded successfully")