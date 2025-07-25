from manim import *

class CustomAnimations(Scene):
    def construct(self):
        # Create a custom animation class
        class ColorCycle(Animation):
            def __init__(self, mobject, colors, **kwargs):
                self.colors = colors
                super().__init__(mobject, **kwargs)
            
            def interpolate_mobject(self, alpha):
                # Calculate which color to use based on alpha
                index = int(alpha * len(self.colors)) % len(self.colors)
                self.mobject.set_color(self.colors[index])
        
        # Create a shape to apply the custom animation to
        square = Square(fill_color=RED, fill_opacity=0.8)
        
        # Define a list of colors to cycle through
        colors = [RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE]
        
        # Apply the custom animation
        self.play(ColorCycle(square, colors, run_time=3))
        self.wait(1)
        
        # Create another custom animation - spiral motion
        class SpiralMotion(Animation):
            def __init__(self, mobject, revolutions=2, **kwargs):
                self.revolutions = revolutions
                super().__init__(mobject, **kwargs)
            
            def interpolate_mobject(self, alpha):
                # Calculate spiral position
                angle = alpha * self.revolutions * 2 * PI
                radius = 1 - alpha  # Spiral inward
                x = radius * np.cos(angle)
                y = radius * np.sin(angle)
                self.mobject.move_to([x, y, 0])
        
        # Create a dot for the spiral animation
        dot = Dot(color=YELLOW)
        
        # Apply the spiral animation
        self.play(SpiralMotion(dot, revolutions=3, run_time=4))
        self.wait(2)
        
        # Create a third custom animation - pulse effect
        class Pulse(Animation):
            def __init__(self, mobject, scale_factor=1.5, **kwargs):
                self.scale_factor = scale_factor
                super().__init__(mobject, **kwargs)
            
            def interpolate_mobject(self, alpha):
                # Calculate scale based on alpha (pulse effect)
                scale = 1 + (self.scale_factor - 1) * np.sin(alpha * PI)
                self.mobject.set_width(self.mobject.width * scale / (1 + (self.scale_factor - 1) * np.sin((alpha - 0.01) * PI)))
        
        # Create a shape for the pulse animation
        circle = Circle(radius=1, fill_color=BLUE, fill_opacity=0.5)
        
        # Apply the pulse animation
        self.play(Pulse(circle, scale_factor=2, run_time=2))
        self.play(Pulse(circle, scale_factor=2, run_time=2))
        self.wait(2)