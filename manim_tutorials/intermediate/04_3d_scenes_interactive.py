"""
Interactive version of 3D Scenes tutorial with Jupyter widgets.
This file demonstrates how to use interactive widgets with Manim 3D scenes.
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
def interactive_3d_scenes_demo():
    """
    Demonstrate interactive 3D scenes with widgets.
    This function would be called in a Jupyter notebook to create interactive controls.
    """
    # Create interactive widgets
    phi_slider = create_slider_widget(
        min_val=0, max_val=PI, step=0.1, value=75 * DEGREES, description="Phi Angle"
    )
    
    theta_slider = create_slider_widget(
        min_val=0, max_val=2*PI, step=0.1, value=30 * DEGREES, description="Theta Angle"
    )
    
    rotation_rate_slider = create_slider_widget(
        min_val=0.0, max_val=1.0, step=0.05, value=0.2, description="Rotation Rate"
    )
    
    sphere_radius_slider = create_slider_widget(
        min_val=0.5, max_val=3.0, step=0.1, value=1.0, description="Sphere Radius"
    )
    
    cube_size_slider = create_slider_widget(
        min_val=0.5, max_val=3.0, step=0.1, value=1.0, description="Cube Size"
    )
    
    sphere_color_picker = create_color_picker_widget(
        color="#0000FF", description="Sphere Color"
    )
    
    cube_color_picker = create_color_picker_widget(
        color="#FF0000", description="Cube Color"
    )
    
    # Display the widgets
    controller = widgets.VBox([
        widgets.HTML("<h3>Interactive 3D Scenes Controller</h3>"),
        phi_slider,
        theta_slider,
        rotation_rate_slider,
        sphere_radius_slider,
        cube_size_slider,
        sphere_color_picker,
        cube_color_picker
    ])
    
    display(controller)
    
    return {
        'phi_slider': phi_slider,
        'theta_slider': theta_slider,
        'rotation_rate_slider': rotation_rate_slider,
        'sphere_radius_slider': sphere_radius_slider,
        'cube_size_slider': cube_size_slider,
        'sphere_color_picker': sphere_color_picker,
        'cube_color_picker': cube_color_picker
    }

class InteractiveThreeDSceneExample(ThreeDScene):
    """
    An interactive version of the ThreeDSceneExample scene that demonstrates
    how parameters could be controlled via widgets.
    """
    def construct(self):
        # Title
        title = Text("Interactive 3D Scenes", font_size=36)
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
        
        # Set camera orientation
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        
        # Create 3D axes
        axes = ThreeDAxes()
        
        # Create a 3D sphere
        sphere = Sphere(radius=1, color=BLUE, fill_opacity=0.5)
        
        # Create a 3D cube
        cube = Cube(side_length=1, fill_color=RED, fill_opacity=0.5)
        cube.shift(RIGHT * 2)
        
        # Display axes
        self.play(Create(axes))
        self.wait(1)
        
        # Display 3D objects
        self.play(Create(sphere))
        self.play(Create(cube))
        self.wait(1)
        
        # Rotate the camera
        self.begin_ambient_camera_rotation(rate=0.2)
        self.wait(4)
        self.stop_ambient_camera_rotation()
        
        # Move objects
        self.play(
            sphere.animate.shift(UP * 2),
            cube.animate.shift(LEFT * 2)
        )
        self.wait(2)
        
        # Change camera orientation
        self.move_camera(phi=45 * DEGREES, theta=-45 * DEGREES, run_time=3)
        self.wait(2)
        
        # Show how parameters could be adjusted
        self.play(
            sphere.animate.scale(1.5).set_color(YELLOW),
            cube.animate.scale(0.8).set_color(GREEN),
            run_time=2
        )
        
        self.wait(2)
        
        # Final message
        final_text = Text("Try adjusting the widgets above!", font_size=30)
        final_text.next_to(explanation, DOWN, buff=1)
        self.play(Write(final_text))
        self.wait(2)
        
        # Fade out all objects
        self.play(FadeOut(title), FadeOut(explanation), FadeOut(axes), 
                  FadeOut(sphere), FadeOut(cube), FadeOut(final_text))
        self.wait(1)

class InteractiveSurfaceExample(ThreeDScene):
    """
    An interactive version of the SurfaceExample scene that demonstrates
    how parameters could be controlled via widgets.
    """
    def construct(self):
        # Title
        title = Text("Interactive Surface Example", font_size=36)
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
        
        # Set camera orientation
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        
        # Create a parametric surface
        surface = Surface(
            lambda u, v: np.array([
                u,
                v,
                np.sin(u) * np.cos(v)
            ]),
            u_range=[-3, 3],
            v_range=[-3, 3],
            fill_opacity=0.7,
            checkerboard_colors=[BLUE_D, BLUE_E],
        )
        
        # Display the surface
        self.play(Create(surface), run_time=3)
        self.wait(2)
        
        # Rotate the camera to view from different angles
        self.begin_ambient_camera_rotation(rate=0.1)
        self.wait(6)
        self.stop_ambient_camera_rotation()
        self.wait(1)
        
        # Show how parameters could be adjusted
        self.play(
            surface.animate.set_fill_opacity(0.9),
            run_time=2
        )
        
        self.wait(2)
        
        # Final message
        final_text = Text("Try adjusting the widgets above!", font_size=30)
        final_text.next_to(explanation, DOWN, buff=1)
        self.play(Write(final_text))
        self.wait(2)
        
        # Fade out all objects
        self.play(FadeOut(title), FadeOut(explanation), FadeOut(surface), FadeOut(final_text))
        self.wait(1)

# Example usage in a Jupyter notebook:
"""
# In a Jupyter notebook cell, you would run:

from manim_tutorials.intermediate.04_3d_scenes_interactive import interactive_3d_scenes_demo

# Create the interactive controller
widgets_controller = interactive_3d_scenes_demo()

# Then render the scene
%%manim -pql InteractiveThreeDSceneExample

from manim_tutorials.intermediate.04_3d_scenes_interactive import InteractiveThreeDSceneExample

class InteractiveThreeDSceneExample(InteractiveThreeDSceneExample):
    def construct(self):
        super().construct()
"""

if __name__ == "__main__":
    # This is just for testing the file can be imported
    print("Interactive 3D Scenes module loaded successfully")