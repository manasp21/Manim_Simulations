"""
Interactive version of Scene Composition tutorial with Jupyter widgets.
This file demonstrates how to use interactive widgets with Manim scene composition.
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
def interactive_scene_composition_demo():
    """
    Demonstrate interactive scene composition with widgets.
    This function would be called in a Jupyter notebook to create interactive controls.
    """
    # Create interactive widgets
    shape_count_slider = create_integer_slider_widget(
        min_val=1, max_val=10, step=1, value=3, description="Shape Count"
    )
    
    text_size_slider = create_slider_widget(
        min_val=10, max_val=72, step=1, value=36, description="Text Size"
    )
    
    spacing_slider = create_slider_widget(
        min_val=0.1, max_val=2.0, step=0.1, value=0.5, description="Spacing"
    )
    
    composition_type_dropdown = create_dropdown_widget(
        options=['Horizontal', 'Vertical', 'Grid'],
        value='Horizontal',
        description="Layout"
    )
    
    # Display the widgets
    controller = widgets.VBox([
        widgets.HTML("<h3>Interactive Scene Composition Controller</h3>"),
        shape_count_slider,
        text_size_slider,
        spacing_slider,
        composition_type_dropdown
    ])
    
    display(controller)
    
    return {
        'shape_count_slider': shape_count_slider,
        'text_size_slider': text_size_slider,
        'spacing_slider': spacing_slider,
        'composition_type_dropdown': composition_type_dropdown
    }

class InteractiveSceneComposition(Scene):
    """
    An interactive version of the SceneComposition scene that demonstrates
    how parameters could be controlled via widgets.
    """
    def construct(self):
        # Title
        title = Text("Interactive Scene Composition", font_size=36)
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
        
        # Create multiple sub-scenes as groups
        # Scene 1: Geometric shapes
        shapes_group = VGroup()
        circle = Circle(radius=0.5, color=RED, fill_opacity=0.5)
        square = Square(side_length=1, color=BLUE, fill_opacity=0.5)
        triangle = Triangle(color=GREEN, fill_opacity=0.5)
        
        shapes_group.add(circle, square, triangle)
        shapes_group.arrange(RIGHT, buff=0.5)
        
        # Scene 2: Text elements
        text_group = VGroup()
        title_text = Text("Scene Composition", font_size=36)
        subtitle = Text("Combining Multiple Elements", font_size=24)
        text_group.add(title_text, subtitle)
        text_group.arrange(DOWN, buff=0.3)
        
        # Scene 3: Mathematical expressions
        math_group = VGroup()
        equation1 = MathTex(r"e^{i\pi} + 1 = 0", font_size=36)
        equation2 = MathTex(r"\int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}", font_size=36)
        math_group.add(equation1, equation2)
        math_group.arrange(DOWN, buff=0.5)
        
        # Position the groups on screen
        shapes_group.shift(UP * 2)
        text_group.shift(ORIGIN)
        math_group.shift(DOWN * 2)
        
        # Animate each group separately
        self.play(
            Create(shapes_group),
            Write(text_group),
            Write(math_group),
            run_time=3
        )
        self.wait(2)
        
        # Transform the composition
        # Move shapes to form a pattern
        self.play(
            circle.animate.move_to(UP),
            square.animate.move_to(LEFT),
            triangle.animate.move_to(RIGHT),
            run_time=2
        )
        self.wait(1)
        
        # Highlight the title
        self.play(
            title_text.animate.set_color(YELLOW).scale(1.2),
            run_time=1
        )
        self.wait(1)
        
        # Transform equations
        equation3 = MathTex(r"F = ma", font_size=48)
        self.play(Transform(equation1, equation3))
        self.wait(1)
        
        # Fade out everything in sequence
        self.play(FadeOut(shapes_group), run_time=1)
        self.play(FadeOut(math_group), run_time=1)
        self.play(FadeOut(text_group), run_time=1)
        self.wait(1)
        
        # Second part of the scene
        # Create a sequence of scenes that transition into each other
        # Scene 1: Introduction
        intro_text = Text("Welcome to Multi-Scene Composition", font_size=36)
        self.play(Write(intro_text))
        self.wait(2)
        
        # Transition to Scene 2: Main Content
        main_title = Text("Main Content", font_size=48, color=BLUE)
        self.play(Transform(intro_text, main_title))
        self.wait(1)
        
        # Add content to the main scene
        content = VGroup()
        bullet1 = Text("• First point", font_size=24).shift(UP)
        bullet2 = Text("• Second point", font_size=24)
        bullet3 = Text("• Third point", font_size=24).shift(DOWN)
        content.add(bullet1, bullet2, bullet3)
        
        self.play(Write(content))
        self.wait(2)
        
        # Transition to Scene 3: Conclusion
        conclusion = Text("Thank You!", font_size=48, color=GREEN)
        self.play(
            FadeOut(main_title),
            FadeOut(content),
            run_time=1
        )
        self.play(Write(conclusion))
        self.wait(2)
        
        # Show how parameters could be adjusted
        self.play(
            conclusion.animate.set_color(YELLOW),
            run_time=1
        )
        
        self.wait(2)
        
        # Final message
        final_text = Text("Try adjusting the widgets above!", font_size=30)
        final_text.next_to(explanation, DOWN, buff=1)
        self.play(Write(final_text))
        self.wait(2)
        
        # Fade out all objects
        self.play(FadeOut(title), FadeOut(explanation), FadeOut(intro_text), 
                  FadeOut(conclusion), FadeOut(final_text))
        self.wait(1)

# Example usage in a Jupyter notebook:
"""
# In a Jupyter notebook cell, you would run:

from manim_tutorials.advanced.03_scene_composition_interactive import interactive_scene_composition_demo

# Create the interactive controller
widgets_controller = interactive_scene_composition_demo()

# Then render the scene
%%manim -pql InteractiveSceneComposition

from manim_tutorials.advanced.03_scene_composition_interactive import InteractiveSceneComposition

class InteractiveSceneComposition(InteractiveSceneComposition):
    def construct(self):
        super().construct()
"""

if __name__ == "__main__":
    # This is just for testing the file can be imported
    print("Interactive Scene Composition module loaded successfully")