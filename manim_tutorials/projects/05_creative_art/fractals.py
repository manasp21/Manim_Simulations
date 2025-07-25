from manim import *
import numpy as np

class Fractals(Scene):
    def construct(self):
        # Set up the scene
        title = Text("Fractals", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # Create a Sierpinski triangle
        self.sierpinski_triangle()
        self.wait(2)
        
        # Clear the scene
        self.clear()
        self.play(Write(title))
        self.wait(1)
        
        # Create a fractal tree
        self.fractal_tree()
        self.wait(2)
    
    def sierpinski_triangle(self):
        # Create the initial triangle
        vertices = [
            np.array([0, 3, 0]),   # Top vertex
            np.array([-3, -1, 0]), # Bottom left vertex
            np.array([3, -1, 0])   # Bottom right vertex
        ]
        
        triangle = Polygon(*vertices, color=WHITE, stroke_width=2)
        self.play(Create(triangle))
        self.wait(1)
        
        # Function to create Sierpinski triangle recursively
        def create_sierpinski(vertices, depth):
            if depth == 0:
                return Polygon(*vertices, color=BLUE, fill_opacity=0.3)
            
            # Find midpoints
            midpoints = [
                (vertices[0] + vertices[1]) / 2,
                (vertices[1] + vertices[2]) / 2,
                (vertices[2] + vertices[0]) / 2
            ]
            
            # Create three sub-triangles
            sub_triangles = VGroup()
            for i in range(3):
                new_vertices = [
                    vertices[i],
                    midpoints[i],
                    midpoints[(i-1) % 3]
                ]
                sub_triangle = create_sierpinski(new_vertices, depth-1)
                sub_triangles.add(sub_triangle)
            
            return sub_triangles
        
        # Animate the creation of Sierpinski triangle
        sierpinski = create_sierpinski(vertices, 5)
        self.play(Create(sierpinski), run_time=3)
        self.wait(2)
        
        # Show the iterative process
        self.play(FadeOut(sierpinski), FadeOut(triangle))
        
        # Show iterations
        for i in range(1, 5):
            iteration = create_sierpinski(vertices, i)
            iteration_title = Text(f"Iteration {i}", font_size=24)
            iteration_title.next_to(iteration, DOWN, buff=0.5)
            
            self.play(Create(iteration), Write(iteration_title), run_time=2)
            self.wait(1)
            
            if i < 4:
                self.play(FadeOut(iteration), FadeOut(iteration_title))
        
        self.wait(2)
    
    def fractal_tree(self):
        # Create a fractal tree
        title = Text("Fractal Tree", font_size=36)
        title.to_edge(UP).shift(DOWN * 0.5)
        self.play(Write(title))
        self.wait(1)
        
        # Function to create a branch recursively
        def create_branch(start, angle, length, depth):
            if depth == 0:
                return VGroup()
            
            # Calculate end point
            end = start + length * np.array([np.sin(angle), np.cos(angle), 0])
            
            # Create branch
            branch = Line(start, end, color=GREEN)
            
            # Create sub-branches
            sub_branches = VGroup()
            if depth > 1:
                # Left branch
                left_branch = create_branch(
                    end, angle + 0.5, length * 0.7, depth - 1
                )
                sub_branches.add(left_branch)
                
                # Right branch
                right_branch = create_branch(
                    end, angle - 0.5, length * 0.7, depth - 1
                )
                sub_branches.add(right_branch)
            
            return VGroup(branch, sub_branches)
        
        # Create and animate the tree
        trunk_start = np.array([0, -3, 0])
        tree = create_branch(trunk_start, 0, 2, 7)
        
        # Animate the tree growth
        def animate_tree(mob, alpha):
            # This is a simplified animation
            # In a real implementation, you would animate each branch sequentially
            pass
        
        self.play(Create(tree), run_time=3)
        self.wait(2)

class MandelbrotSet(Scene):
    def construct(self):
        # Set up the scene
        title = Text("Mandelbrot Set", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # Explanation
        explanation = Text(
            "The Mandelbrot set is the set of complex numbers c for which\n"
            "the function f(z) = z² + c does not diverge when iterated.",
            font_size=24
        )
        explanation.next_to(title, DOWN, buff=0.5)
        
        self.play(Write(explanation))
        self.wait(2)
        
        # Show the mathematical formula
        formula = MathTex(
            "f_c(z)", "=", "z^2", "+", "c",
            font_size=48
        )
        formula.next_to(explanation, DOWN, buff=1)
        
        self.play(Write(formula))
        self.wait(2)
        
        # Show iteration process
        iteration_process = VGroup(
            MathTex("z_0", "=", "0", font_size=36),
            MathTex("z_1", "=", "z_0^2", "+", "c", "=", "0^2", "+", "c", "=", "c", font_size=36),
            MathTex("z_2", "=", "z_1^2", "+", "c", "=", "c^2", "+", "c", font_size=36),
            MathTex("z_3", "=", "z_2^2", "+", "c", font_size=36)
        )
        iteration_process.arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        iteration_process.next_to(formula, DOWN, buff=1)
        
        for step in iteration_process:
            self.play(Write(step))
            self.wait(1)
        
        self.wait(2)
        
        # Show example with c = -1
        example_title = Text("Example: c = -1", font_size=30)
        example_title.next_to(iteration_process, DOWN, buff=1)
        
        self.play(Write(example_title))
        self.wait(1)
        
        example_iterations = VGroup(
            MathTex("z_0", "=", "0", font_size=30),
            MathTex("z_1", "=", "0^2", "+", "(-1)", "=", "-1", font_size=30),
            MathTex("z_2", "=", "(-1)^2", "+", "(-1)", "=", "1", "-", "1", "=", "0", font_size=30),
            MathTex("z_3", "=", "0^2", "+", "(-1)", "=", "-1", font_size=30)
        )
        example_iterations.arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        example_iterations.next_to(example_title, DOWN, buff=0.3)
        
        for step in example_iterations:
            self.play(Write(step))
            self.wait(1)
        
        # Conclusion for this example
        conclusion = Text("The sequence oscillates between 0 and -1, so c = -1 is in the Mandelbrot set.", font_size=20)
        conclusion.next_to(example_iterations, DOWN, buff=0.3)
        
        self.play(Write(conclusion))
        self.wait(3)

class JuliaSet(Scene):
    def construct(self):
        # Set up the scene
        title = Text("Julia Set", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # Explanation
        explanation = Text(
            "Julia sets are related to the Mandelbrot set, but use a fixed complex number c\n"
            "and vary the initial value of z instead.",
            font_size=24
        )
        explanation.next_to(title, DOWN, buff=0.5)
        
        self.play(Write(explanation))
        self.wait(2)
        
        # Show the mathematical formula
        formula = MathTex(
            "f_c(z)", "=", "z^2", "+", "c",
            font_size=48
        )
        formula.next_to(explanation, DOWN, buff=1)
        
        self.play(Write(formula))
        self.wait(2)
        
        # For Mandelbrot: z varies, c is fixed
        mandelbrot_text = Text("Mandelbrot Set: z₀ = 0, c varies", font_size=24)
        mandelbrot_text.next_to(formula, DOWN, buff=0.5)
        
        # For Julia: z varies, c is fixed
        julia_text = Text("Julia Set: z₀ varies, c is fixed", font_size=24)
        julia_text.next_to(mandelbrot_text, DOWN, buff=0.3)
        
        self.play(Write(mandelbrot_text))
        self.play(Write(julia_text))
        self.wait(2)
        
        # Show different Julia sets for different values of c
        julia_examples = VGroup(
            Text("c = -0.7 + 0.27015i (Dendrite)", font_size=20),
            Text("c = -0.4 + 0.6i (Douady's Rabbit)", font_size=20),
            Text("c = -0.8 + 0.156i (San Marco)", font_size=20)
        )
        julia_examples.arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        julia_examples.next_to(julia_text, DOWN, buff=1)
        
        for example in julia_examples:
            self.play(Write(example))
            self.wait(1)
        
        self.wait(3)

class FractalAnimations(Scene):
    def construct(self):
        # Set up the scene
        title = Text("Fractal Animations", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # Create an animated fractal
        # This is a conceptual demonstration of how to animate fractals
        
        # Create a simple recursive pattern
        def create_pattern(depth, size, position):
            if depth == 0:
                return Square(side_length=size, color=BLUE, fill_opacity=0.3).move_to(position)
            
            # Create a group of smaller patterns
            pattern = VGroup()
            offsets = [
                np.array([-size/3, -size/3, 0]),
                np.array([size/3, -size/3, 0]),
                np.array([-size/3, size/3, 0]),
                np.array([size/3, size/3, 0]),
                np.array([0, 0, 0])
            ]
            
            for offset in offsets:
                sub_pattern = create_pattern(depth-1, size/2, position + offset)
                pattern.add(sub_pattern)
            
            return pattern
        
        # Animate the pattern creation
        pattern = create_pattern(4, 4, ORIGIN)
        self.play(Create(pattern), run_time=3)
        self.wait(2)
        
        # Animate transformation
        circle_pattern = Circle(radius=2, color=YELLOW, fill_opacity=0.3)
        self.play(Transform(pattern, circle_pattern), run_time=2)
        self.wait(1)
        
        # Animate color change
        self.play(pattern.animate.set_color(RED).set_fill(opacity=0.5), run_time=2)
        self.wait(1)
        
        # Animate rotation
        self.play(Rotate(pattern, 2*PI, run_time=3))
        self.wait(2)