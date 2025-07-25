"""
Interactive version of Coordinate Systems tutorial with Jupyter widgets.
This file demonstrates how to use interactive widgets with Manim coordinate system scenes.
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
def interactive_coordinate_systems_demo():
    """
    Demonstrate interactive coordinate systems with widgets.
    This function would be called in a Jupyter notebook to create interactive controls.
    """
    # Create interactive widgets
    x_range_slider = create_slider_widget(
        min_val=-10, max_val=10, step=0.5, value=5, description="X Range"
    )
    
    y_range_slider = create_slider_widget(
        min_val=-10, max_val=10, step=0.5, value=3, description="Y Range"
    )
    
    graph_function_dropdown = create_dropdown_widget(
        options=['x^2', 'sin(x)', 'cos(x)', 'x^3', 'sqrt(x)'],
        value='x^2',
        description="Function"
    )
    
    point_x_slider = create_slider_widget(
        min_val=-5, max_val=5, step=0.1, value=2, description="Point X"
    )
    
    axis_color_picker = create_color_picker_widget(
        color="#0000FF", description="Axis Color"
    )
    
    graph_color_picker = create_color_picker_widget(
        color="#00FF00", description="Graph Color"
    )
    
    # Display the widgets
    controller = widgets.VBox([
        widgets.HTML("<h3>Interactive Coordinate Systems Controller</h3>"),
        x_range_slider,
        y_range_slider,
        graph_function_dropdown,
        point_x_slider,
        axis_color_picker,
        graph_color_picker
    ])
    
    display(controller)
    
    return {
        'x_range_slider': x_range_slider,
        'y_range_slider': y_range_slider,
        'graph_function_dropdown': graph_function_dropdown,
        'point_x_slider': point_x_slider,
        'axis_color_picker': axis_color_picker,
        'graph_color_picker': graph_color_picker
    }

class InteractiveCoordinateSystems(Scene):
    """
    An interactive version of the CoordinateSystems scene that demonstrates
    how parameters could be controlled via widgets.
    """
    def construct(self):
        # Title
        title = Text("Interactive Coordinate Systems", font_size=36)
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
        
        # Create a number plane
        plane = NumberPlane()
        plane.add_coordinates()
        
        # Create axes
        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[-3, 3, 1],
            axis_config={"color": BLUE},
        )
        
        # Add labels to axes
        axes_labels = axes.get_axis_labels(x_label="x", y_label="y")
        
        # Create a function graph
        graph = axes.plot(lambda x: x**2, color=GREEN)
        graph_label = axes.get_graph_label(graph, label="y = x^2")
        
        # Create a point on the graph
        dot = Dot(axes.c2p(2, 4), color=YELLOW)
        dot_label = Text("Point (2, 4)", font_size=24).next_to(dot, UP)
        
        # Display the number plane
        self.play(Create(plane), run_time=2)
        self.wait(1)
        
        # Transform to axes
        self.play(Transform(plane, axes), run_time=2)
        self.play(Write(axes_labels))
        self.wait(1)
        
        # Plot the function
        self.play(Create(graph), run_time=3)
        self.play(Write(graph_label))
        self.wait(1)
        
        # Add the point
        self.play(Create(dot))
        self.play(Write(dot_label))
        self.wait(2)
        
        # Show how parameters could be adjusted
        self.play(
            axes.animate.scale(1.2),
            graph.animate.set_color(YELLOW),
            dot.animate.set_color(RED),
            run_time=2
        )
        
        self.wait(2)
        
        # Final message
        final_text = Text("Try adjusting the widgets above!", font_size=30)
        final_text.next_to(explanation, DOWN, buff=1)
        self.play(Write(final_text))
        self.wait(2)
        
        # Fade out all objects
        self.play(FadeOut(title), FadeOut(explanation), FadeOut(plane), 
                  FadeOut(axes_labels), FadeOut(graph), FadeOut(graph_label),
                  FadeOut(dot), FadeOut(dot_label), FadeOut(final_text))
        self.wait(1)

# Example usage in a Jupyter notebook:
"""
# In a Jupyter notebook cell, you would run:

from manim_tutorials.intermediate.01_coordinate_systems_interactive import interactive_coordinate_systems_demo

# Create the interactive controller
widgets_controller = interactive_coordinate_systems_demo()

# Then render the scene
%%manim -pql InteractiveCoordinateSystems

from manim_tutorials.intermediate.01_coordinate_systems_interactive import InteractiveCoordinateSystems

class InteractiveCoordinateSystems(InteractiveCoordinateSystems):
    def construct(self):
        super().construct()
"""

if __name__ == "__main__":
    # This is just for testing the file can be imported
    print("Interactive Coordinate Systems module loaded successfully")