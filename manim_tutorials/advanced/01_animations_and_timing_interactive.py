"""
Interactive version of Animations and Timing tutorial with Jupyter widgets.
This file demonstrates how to use interactive widgets with Manim animation timing scenes.
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
def interactive_animations_and_timing_demo():
    """
    Demonstrate interactive animations and timing with widgets.
    This function would be called in a Jupyter notebook to create interactive controls.
    """
    # Create interactive widgets
    rate_func_dropdown = create_dropdown_widget(
        options=['linear', 'smooth', 'rush_into', 'rush_from', 'there_and_back'],
        value='smooth',
        description="Rate Function"
    )
    
    run_time_slider = create_slider_widget(
        min_val=0.5, max_val=5.0, step=0.1, value=2.0, description="Run Time"
    )
    
    lag_ratio_slider = create_slider_widget(
        min_val=0, max_val=1.0, step=0.1, value=0.5, description="Lag Ratio"
    )
    
    shape_count_slider = create_integer_slider_widget(
        min_val=1, max_val=10, step=1, value=5, description="Shape Count"
    )
    
    # Display the widgets
    controller = widgets.VBox([
        widgets.HTML("<h3>Interactive Animations and Timing Controller</h3>"),
        rate_func_dropdown,
        run_time_slider,
        lag_ratio_slider,
        shape_count_slider
    ])
    
    display(controller)
    
    return {
        'rate_func_dropdown': rate_func_dropdown,
        'run_time_slider': run_time_slider,
        'lag_ratio_slider': lag_ratio_slider,
        'shape_count_slider': shape_count_slider
    }

class InteractiveAnimationsAndTiming(Scene):
    """
    An interactive version of the AnimationsAndTiming scene that demonstrates
    how parameters could be controlled via widgets.
    """
    def construct(self):
        # Title
        title = Text("Interactive Animations and Timing", font_size=36)
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
        
        # Create multiple circles
        circles = VGroup(*[Circle(radius=0.5, color=WHITE) for _ in range(5)])
        circles.arrange(RIGHT, buff=0.5)
        
        # Display circles with different timing functions
        self.play(
            circles[0].animate.shift(UP).set_color(RED),
            rate_func=linear,
            run_time=2
        )
        
        self.play(
            circles[1].animate.shift(UP).set_color(BLUE),
            rate_func=smooth,
            run_time=2
        )
        
        self.play(
            circles[2].animate.shift(UP).set_color(GREEN),
            rate_func=rush_into,
            run_time=2
        )
        
        self.play(
            circles[3].animate.shift(UP).set_color(YELLOW),
            rate_func=rush_from,
            run_time=2
        )
        
        self.play(
            circles[4].animate.shift(UP).set_color(PURPLE),
            rate_func=there_and_back,
            run_time=2
        )
        
        self.wait(1)
        
        # Reset positions
        self.play(
            *[circle.animate.shift(DOWN).set_color(WHITE) for circle in circles]
        )
        self.wait(1)
        
        # Create a sequence of animations with different run times
        square = Square(color=BLUE)
        triangle = Triangle(color=RED)
        pentagon = Polygon(
            *[[np.cos(2*PI*i/5), np.sin(2*PI*i/5), 0] for i in range(5)],
            color=GREEN
        )
        
        shapes = VGroup(square, triangle, pentagon).arrange(RIGHT, buff=1)
        
        # Animate with different run times
        self.play(
            Create(square, run_time=1),
            Create(triangle, run_time=2),
            Create(pentagon, run_time=3)
        )
        self.wait(1)
        
        # Apply animations with lag
        self.play(
            *[shape.animate.shift(UP).scale(1.5) for shape in shapes],
            lag_ratio=0.5,
            run_time=3
        )
        self.wait(2)
        
        # Show how parameters could be adjusted
        self.play(
            shapes.animate.set_color(YELLOW),
            run_time=1
        )
        
        self.wait(2)
        
        # Final message
        final_text = Text("Try adjusting the widgets above!", font_size=30)
        final_text.next_to(explanation, DOWN, buff=1)
        self.play(Write(final_text))
        self.wait(2)
        
        # Fade out all objects
        self.play(FadeOut(title), FadeOut(explanation), FadeOut(circles), 
                  FadeOut(shapes), FadeOut(final_text))
        self.wait(1)

# Example usage in a Jupyter notebook:
"""
# In a Jupyter notebook cell, you would run:

from manim_tutorials.advanced.01_animations_and_timing_interactive import interactive_animations_and_timing_demo

# Create the interactive controller
widgets_controller = interactive_animations_and_timing_demo()

# Then render the scene
%%manim -pql InteractiveAnimationsAndTiming

from manim_tutorials.advanced.01_animations_and_timing_interactive import InteractiveAnimationsAndTiming

class InteractiveAnimationsAndTiming(InteractiveAnimationsAndTiming):
    def construct(self):
        super().construct()
"""

if __name__ == "__main__":
    # This is just for testing the file can be imported
    print("Interactive Animations and Timing module loaded successfully")