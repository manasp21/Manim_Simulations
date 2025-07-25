from manim import *

class Transformations(Scene):
    def construct(self):
        # Create initial shapes
        circle = Circle(fill_color=BLUE, fill_opacity=0.5)
        square = Square(fill_color=GREEN, fill_opacity=0.5)
        triangle = Triangle(fill_color=RED, fill_opacity=0.5)
        
        # Position the shapes
        circle.shift(LEFT * 3)
        triangle.shift(RIGHT * 3)
        
        # Display initial shapes
        self.play(Create(circle), Create(square), Create(triangle))
        self.wait(1)
        
        # Apply transformations
        # Scale the circle
        self.play(circle.animate.scale(2))
        self.wait(1)
        
        # Rotate the square
        self.play(square.animate.rotate(PI/4))
        self.wait(1)
        
        # Move the triangle
        self.play(triangle.animate.shift(UP * 2))
        self.wait(1)
        
        # Complex transformation - morph square to circle
        circle2 = Circle(radius=1, fill_color=YELLOW, fill_opacity=0.5)
        circle2.shift(RIGHT * 3)
        
        self.play(Transform(square, circle2))
        self.wait(1)
        
        # Apply multiple transformations at once
        self.play(
            circle.animate.shift(DOWN * 2).set_color(PURPLE),
            triangle.animate.shift(DOWN * 2).rotate(PI/2),
            square.animate.shift(DOWN * 2).scale(0.5)
        )
        self.wait(2)