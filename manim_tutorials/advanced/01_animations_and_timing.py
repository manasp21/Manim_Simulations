from manim import *

class AnimationsAndTiming(Scene):
    def construct(self):
        # Create multiple circles
        circles = VGroup(*[Circle(radius=0.5, color=WHITE) for _ in range(5)])
        circles.arrange(RIGHT, buff=0.5)
        
        # Display circles with different timing functions
        self.play(
            circles[0].animate.shift(UP).set_color(RED),
            rate_func=linear,
            run_time=2
        )
        
        self.play(
            circles[1].animate.shift(UP).set_color(BLUE),
            rate_func=smooth,
            run_time=2
        )
        
        self.play(
            circles[2].animate.shift(UP).set_color(GREEN),
            rate_func=rush_into,
            run_time=2
        )
        
        self.play(
            circles[3].animate.shift(UP).set_color(YELLOW),
            rate_func=rush_from,
            run_time=2
        )
        
        self.play(
            circles[4].animate.shift(UP).set_color(PURPLE),
            rate_func=there_and_back,
            run_time=2
        )
        
        self.wait(1)
        
        # Reset positions
        self.play(
            *[circle.animate.shift(DOWN).set_color(WHITE) for circle in circles]
        )
        self.wait(1)
        
        # Create a sequence of animations with different run times
        square = Square(color=BLUE)
        triangle = Triangle(color=RED)
        pentagon = Polygon(
            *[[np.cos(2*PI*i/5), np.sin(2*PI*i/5), 0] for i in range(5)],
            color=GREEN
        )
        
        shapes = VGroup(square, triangle, pentagon).arrange(RIGHT, buff=1)
        
        # Animate with different run times
        self.play(
            Create(square, run_time=1),
            Create(triangle, run_time=2),
            Create(pentagon, run_time=3)
        )
        self.wait(1)
        
        # Apply animations with lag
        self.play(
            *[shape.animate.shift(UP).scale(1.5) for shape in shapes],
            lag_ratio=0.5,
            run_time=3
        )
        self.wait(2)