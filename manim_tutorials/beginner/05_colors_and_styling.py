from manim import *

class ColorsAndStyling(Scene):
    def construct(self):
        # Create circles with different colors
        circle1 = Circle(radius=1, color=RED)
        circle1.set_fill(RED, opacity=0.5)
        
        circle2 = Circle(radius=1, color=GREEN)
        circle2.set_fill(GREEN, opacity=0.5)
        
        circle3 = Circle(radius=1, color=BLUE)
        circle3.set_fill(BLUE, opacity=0.5)
        
        # Position the circles
        circle1.shift(LEFT * 2)
        circle3.shift(RIGHT * 2)
        
        # Create squares with different stroke widths
        square1 = Square(side_length=1, color=YELLOW)
        square1.set_fill(YELLOW, opacity=0.5)
        square1.set_stroke(width=5)
        
        square2 = Square(side_length=1, color=PURPLE)
        square2.set_fill(PURPLE, opacity=0.5)
        square2.set_stroke(width=10)
        
        # Position the squares below the circles
        square1.shift(DOWN * 2 + LEFT)
        square2.shift(DOWN * 2 + RIGHT)
        
        # Display all objects
        self.play(Create(circle1), Create(circle2), Create(circle3))
        self.play(Create(square1), Create(square2))
        self.wait(2)
        
        # Change colors
        self.play(
            circle1.animate.set_fill(ORANGE),
            circle2.animate.set_fill(PINK),
            circle3.animate.set_fill(WHITE)
        )
        self.wait(2)