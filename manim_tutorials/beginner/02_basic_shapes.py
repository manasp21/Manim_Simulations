from manim import *

class BasicShapes(Scene):
    def construct(self):
        # Create various shapes
        circle = Circle()
        square = Square()
        triangle = Triangle()
        rectangle = Rectangle(height=2, width=3)
        ellipse = Ellipse()
        
        # Set colors for each shape
        circle.set_fill(PINK, opacity=0.5)
        square.set_fill(BLUE, opacity=0.5)
        triangle.set_fill(GREEN, opacity=0.5)
        rectangle.set_fill(YELLOW, opacity=0.5)
        ellipse.set_fill(ORANGE, opacity=0.5)
        
        # Position the shapes
        circle.shift(LEFT * 3)
        square.shift(LEFT)
        triangle.shift(RIGHT)
        rectangle.shift(RIGHT * 3)
        ellipse.shift(DOWN * 2)
        
        # Add shapes to the scene
        self.play(Create(circle))
        self.play(Create(square))
        self.play(Create(triangle))
        self.play(Create(rectangle))
        self.play(Create(ellipse))
        
        # Wait for a moment
        self.wait(2)