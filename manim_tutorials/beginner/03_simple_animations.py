from manim import *

class SimpleAnimations(Scene):
    def construct(self):
        # Create a circle
        circle = Circle()
        circle.set_fill(PINK, opacity=0.5)
        
        # Create a square
        square = Square()
        square.set_fill(BLUE, opacity=0.5)
        
        # Position the square to the right of the circle
        square.shift(RIGHT * 3)
        
        # Show creation of both shapes
        self.play(Create(circle), Create(square))
        self.wait(1)
        
        # Transform the circle into a square
        self.play(Transform(circle, square.copy()))
        self.wait(1)
        
        # Rotate the square
        self.play(Rotate(square, PI))
        self.wait(1)
        
        # Move the circle to the left
        self.play(circle.animate.shift(LEFT * 3))
        self.wait(1)
        
        # Fade out both objects
        self.play(FadeOut(circle), FadeOut(square))
        self.wait(1)