from manim import *

class TextAndLaTeX(Scene):
    def construct(self):
        # Create simple text
        text = Text("Hello, Manim!")
        text.shift(UP * 2)
        
        # Create LaTeX mathematical expressions
        latex = MathTex(r"\int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}")
        
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
        
        # Transform the text
        self.play(Transform(text, Text("Text Transformations").shift(UP * 2)))
        self.wait(1)
        
        # Fade out all
        self.play(FadeOut(text), FadeOut(latex), FadeOut(equation))
        self.wait(1)