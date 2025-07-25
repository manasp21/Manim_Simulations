from manim import *

class CustomMobjects(Scene):
    def construct(self):
        # Create a custom mobject - a star
        class Star(VMobject):
            def __init__(self, **kwargs):
                super().__init__(**kwargs)
                self.create_star()
            
            def create_star(self):
                # Create points for a 5-pointed star
                points = []
                for i in range(10):
                    angle = i * PI / 5
                    radius = 1 if i % 2 == 0 else 0.4
                    x = radius * np.cos(angle)
                    y = radius * np.sin(angle)
                    points.append([x, y, 0])
                
                # Add points to the mobject
                self.set_points_as_corners(points + [points[0]])
        
        # Create and display the star
        star = Star(color=YELLOW, fill_opacity=0.7)
        star.shift(LEFT * 3)
        
        # Create another custom mobject - a heart
        class Heart(VMobject):
            def __init__(self, **kwargs):
                super().__init__(**kwargs)
                self.create_heart()
            
            def create_heart(self):
                # Create points for a heart shape using parametric equations
                points = []
                for i in range(100):
                    t = i * 2 * PI / 99
                    x = 16 * np.sin(t)**3
                    y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)
                    # Scale down the heart
                    points.append([x/10, y/10, 0])
                
                # Add points to the mobject
                self.set_points_smoothly(points)
        
        # Create and display the heart
        heart = Heart(color=RED, fill_opacity=0.7)
        heart.shift(RIGHT * 3)
        
        # Display both custom mobjects
        self.play(Create(star), Create(heart), run_time=3)
        self.wait(2)
        
        # Apply transformations
        self.play(
            star.animate.scale(1.5).set_color(ORANGE),
            heart.animate.scale(1.5).set_color(PINK)
        )
        self.wait(2)
        
        # Move the mobjects
        self.play(
            star.animate.shift(UP * 2),
            heart.animate.shift(DOWN * 2)
        )
        self.wait(2)