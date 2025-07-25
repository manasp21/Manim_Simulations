"""
Interactive version of Text and LaTeX tutorial with Jupyter widgets.
This file demonstrates how to use interactive widgets with Manim text scenes.
"""
from manim import *
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from utils.widget_utils import *
import ipywidgets as widgets
from IPython.display import display

# This would be used in a Jupyter notebook cell
def interactive_text_latex_demo():
    """
    Demonstrate interactive text and LaTeX with widgets.
    This function would be called in a Jupyter notebook to create interactive controls.
    """
    # Create interactive widgets
    text_input = create_text_widget(
        value="Hello, Manim!", placeholder="Enter text", description="Text Content"
    )
    
    font_size_slider = create_integer_slider_widget(
        min_val=10, max_val=100, step=5, value=48, description="Font Size"
    )
    
    text_color_picker = create_color_picker_widget(
        color="#FFFFFF", description="Text Color"
    )
    
    latex_input = create_text_widget(
        value=r"\int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}", 
        placeholder="Enter LaTeX", 
        description="LaTeX Content"
    )
    
    equation_input = create_text_widget(
        value=r"e^{i\pi} + 1 = 0", 
        placeholder="Enter equation", 
        description="Equation"
    )
    
    # Display the widgets
    controller = widgets.VBox([
        widgets.HTML("<h3>Interactive Text and LaTeX Controller</h3>"),
        text_input,
        font_size_slider,
        text_color_picker,
        latex_input,
        equation_input
    ])
    
    display(controller)
    
    return {
        'text_input': text_input,
        'font_size_slider': font_size_slider,
        'text_color_picker': text_color_picker,
        'latex_input': latex_input,
        'equation_input': equation_input
    }

class InteractiveTextAndLaTeX(Scene):
    """
    An interactive version of the TextAndLaTeX scene that demonstrates
    how parameters could be controlled via widgets.
    """
    def construct(self):
        # Title
        title = Text("Interactive Text and LaTeX", font_size=36)
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
        
        # Create simple text
        text = Text("Hello, Manim!")
        text.shift(UP * 1)
        
        # Create LaTeX mathematical expressions
        latex = MathTex(r"\int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}")
        latex.shift(DOWN * 0.5)
        
        # Create more complex LaTeX equation
        equation = MathTex(r"e^{i\pi} + 1 = 0")
        equation.shift(DOWN * 2)
        
        # Display the text and equations
        self.play(Write(text))
        self.wait(1)
        
        self.play(Write(latex))
        self.wait(1)
        
        self.play(Write(equation))
        self.wait(2)
        
        # Show how parameters could be adjusted
        self.play(
            text.animate.set_color(YELLOW),
            latex.animate.set_color(BLUE),
            equation.animate.set_color(GREEN),
            run_time=2
        )
        
        self.wait(2)
        
        # Transform the text
        self.play(Transform(text, Text("Text Transformations").shift(UP * 2)))
        self.wait(1)
        
        # Final message
        final_text = Text("Try adjusting the widgets above!", font_size=30)
        final_text.next_to(explanation, DOWN, buff=1)
        self.play(Write(final_text))
        self.wait(2)
        
        # Fade out all objects
        self.play(FadeOut(title), FadeOut(explanation), FadeOut(text), 
                  FadeOut(latex), FadeOut(equation), FadeOut(final_text))
        self.wait(1)

# Example usage in a Jupyter notebook:
"""
# In a Jupyter notebook cell, you would run:

from manim_tutorials.beginner.04_text_and_latex_interactive import interactive_text_latex_demo

# Create the interactive controller
widgets_controller = interactive_text_latex_demo()

# Then render the scene
%%manim -pql InteractiveTextAndLaTeX

from manim_tutorials.beginner.04_text_and_latex_interactive import InteractiveTextAndLaTeX

class InteractiveTextAndLaTeX(InteractiveTextAndLaTeX):
    def construct(self):
        super().construct()
"""

if __name__ == "__main__":
    # This is just for testing the file can be imported
    print("Interactive Text and LaTeX module loaded successfully")