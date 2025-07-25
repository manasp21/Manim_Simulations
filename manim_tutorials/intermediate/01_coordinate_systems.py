from manim import *

class CoordinateSystems(Scene):
    def construct(self):
        # Create a number plane
        plane = NumberPlane()
        plane.add_coordinates()
        
        # Create axes
        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[-3, 3, 1],
            axis_config={"color": BLUE},
        )
        
        # Add labels to axes
        axes_labels = axes.get_axis_labels(x_label="x", y_label="y")
        
        # Create a function graph
        graph = axes.plot(lambda x: x**2, color=GREEN)
        graph_label = axes.get_graph_label(graph, label="y = x^2")
        
        # Create a point on the graph
        dot = Dot(axes.c2p(2, 4), color=YELLOW)
        dot_label = Text("Point (2, 4)", font_size=24).next_to(dot, UP)
        
        # Display the number plane
        self.play(Create(plane), run_time=2)
        self.wait(1)
        
        # Transform to axes
        self.play(Transform(plane, axes), run_time=2)
        self.play(Write(axes_labels))
        self.wait(1)
        
        # Plot the function
        self.play(Create(graph), run_time=3)
        self.play(Write(graph_label))
        self.wait(1)
        
        # Add the point
        self.play(Create(dot))
        self.play(Write(dot_label))
        self.wait(2)