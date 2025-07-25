from manim import *

class Updaters(Scene):
    def construct(self):
        # Create a moving dot
        dot = Dot(color=RED)
        
        # Create a text that follows the dot
        label = Text("Moving Dot", font_size=24)
        label.add_updater(lambda m: m.next_to(dot, UP))
        
        # Add objects to scene
        self.add(dot, label)
        
        # Move the dot in a square path
        self.play(dot.animate.shift(RIGHT * 2), run_time=2)
        self.play(dot.animate.shift(UP * 2), run_time=2)
        self.play(dot.animate.shift(LEFT * 2), run_time=2)
        self.play(dot.animate.shift(DOWN * 2), run_time=2)
        
        # Remove the updater
        label.clear_updaters()
        self.wait(1)
        
        # Create a rotating square with a dot
        square = Square(color=BLUE)
        dot2 = Dot(color=YELLOW)
        dot2.move_to(square.get_right())
        
        # Define updater for dot2 to move with square
        dot2.add_updater(lambda d: d.move_to(square.get_right()))
        
        self.play(Create(square))
        self.add(dot2)
        
        # Rotate the square
        self.play(Rotate(square, PI * 2), run_time=4)
        self.wait(1)
        
        # Remove updater and move dot independently
        dot2.clear_updaters()
        self.play(dot2.animate.shift(UP * 2))
        self.wait(2)