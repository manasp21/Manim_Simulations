from manim import *

class GettingStarted(Scene):
    def construct(self):
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