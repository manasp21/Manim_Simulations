from manim import *

class AlgebraBasics(Scene):
    def construct(self):
        # Set up the scene
        title = Text("Algebra Basics", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # Show variables and constants
        var_x = MathTex("x", font_size=60, color=BLUE)
        var_y = MathTex("y", font_size=60, color=GREEN)
        const_5 = MathTex("5", font_size=60, color=YELLOW)
        const_3 = MathTex("3", font_size=60, color=RED)
        
        # Position elements
        var_x.shift(LEFT * 3)
        const_5.next_to(var_x, RIGHT, buff=1)
        var_y.next_to(const_5, RIGHT, buff=1)
        const_3.next_to(var_y, RIGHT, buff=1)
        
        # Display variables and constants
        self.play(Write(var_x))
        self.play(Write(const_5))
        self.play(Write(var_y))
        self.play(Write(const_3))
        self.wait(2)
        
        # Show combining like terms
        expr1 = MathTex("2x", "+", "3y", "+", "5x", "-", "y", font_size=48)
        expr1.shift(UP * 2)
        
        self.play(
            FadeOut(var_x),
            FadeOut(var_y),
            FadeOut(const_5),
            FadeOut(const_3),
            Write(expr1)
        )
        self.wait(2)
        
        # Group like terms
        expr2 = MathTex("(2x", "+", "5x)", "+", "(3y", "-", "y)", font_size=48)
        expr2.next_to(expr1, DOWN, buff=0.5)
        
        self.play(Write(expr2))
        self.wait(2)
        
        # Simplify
        expr3 = MathTex("7x", "+", "2y", font_size=48)
        expr3.next_to(expr2, DOWN, buff=0.5)
        
        self.play(Write(expr3))
        self.wait(2)
        
        # Show equation solving
        equation_title = Text("Solving Equations", font_size=36)
        equation_title.next_to(expr3, DOWN, buff=1)
        
        self.play(Write(equation_title))
        self.wait(1)
        
        # Linear equation
        eq1 = MathTex("2x", "+", "5", "=", "15", font_size=48)
        eq1.next_to(equation_title, DOWN, buff=0.5)
        
        self.play(Write(eq1))
        self.wait(2)
        
        # Subtract 5 from both sides
        eq2 = MathTex("2x", "+", "5", "-", "5", "=", "15", "-", "5", font_size=48)
        eq2.next_to(eq1, DOWN, buff=0.5)
        
        self.play(Write(eq2))
        self.wait(2)
        
        # Simplify
        eq3 = MathTex("2x", "=", "10", font_size=48)
        eq3.next_to(eq2, DOWN, buff=0.5)
        
        self.play(Write(eq3))
        self.wait(2)
        
        # Divide by 2
        eq4 = MathTex("\\frac{2x}{2}", "=", "\\frac{10}{2}", font_size=48)
        eq4.next_to(eq3, DOWN, buff=0.5)
        
        self.play(Write(eq4))
        self.wait(2)
        
        # Final result
        eq5 = MathTex("x", "=", "5", font_size=48)
        eq5.next_to(eq4, DOWN, buff=0.5)
        
        self.play(Write(eq5))
        self.wait(2)
        
        # Verify solution
        verify = Text("Verification: 2(5) + 5 = 10 + 5 = 15 ✓", font_size=24)
        verify.next_to(eq5, DOWN, buff=0.5)
        
        self.play(Write(verify))
        self.wait(3)

class QuadraticEquations(Scene):
    def construct(self):
        # Set up the scene
        title = Text("Quadratic Equations", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # Standard form
        standard_form = MathTex("ax^2", "+", "bx", "+", "c", "=", "0", font_size=48)
        standard_form.shift(UP * 2)
        
        self.play(Write(standard_form))
        self.wait(2)
        
        # Example equation
        example = MathTex("x^2", "-", "5x", "+", "6", "=", "0", font_size=48)
        example.next_to(standard_form, DOWN, buff=0.5)
        
        self.play(Write(example))
        self.wait(2)
        
        # Factoring method
        factoring_title = Text("Factoring Method", font_size=36)
        factoring_title.next_to(example, DOWN, buff=1)
        
        self.play(Write(factoring_title))
        self.wait(1)
        
        # Find two numbers that multiply to 6 and add to -5
        explanation = Text("Find two numbers that multiply to 6 and add to -5", font_size=24)
        explanation.next_to(factoring_title, DOWN, buff=0.5)
        
        self.play(Write(explanation))
        self.wait(2)
        
        # The numbers are -2 and -3
        numbers = MathTex("-2 \\times -3 = 6", "\\text{ and }", "-2 + (-3) = -5", font_size=36)
        numbers.next_to(explanation, DOWN, buff=0.5)
        
        self.play(Write(numbers))
        self.wait(2)
        
        # Factor the equation
        factored = MathTex("(x", "-", "2)", "(x", "-", "3)", "=", "0", font_size=48)
        factored.next_to(numbers, DOWN, buff=0.5)
        
        self.play(Write(factored))
        self.wait(2)
        
        # Solve for x
        solutions_title = Text("Solutions:", font_size=30)
        solutions_title.next_to(factored, DOWN, buff=0.5).shift(LEFT * 2)
        
        sol1 = MathTex("x", "-", "2", "=", "0", "\\Rightarrow", "x", "=", "2", font_size=36)
        sol1.next_to(solutions_title, DOWN, buff=0.3).shift(RIGHT * 0.5)
        
        sol2 = MathTex("x", "-", "3", "=", "0", "\\Rightarrow", "x", "=", "3", font_size=36)
        sol2.next_to(sol1, DOWN, buff=0.3)
        
        self.play(Write(solutions_title))
        self.play(Write(sol1))
        self.play(Write(sol2))
        self.wait(2)
        
        # Verify solutions
        verify_title = Text("Verification:", font_size=30)
        verify_title.next_to(sol2, DOWN, buff=0.5)
        
        self.play(Write(verify_title))
        self.wait(1)
        
        # Verify x = 2
        verify1 = MathTex("x = 2:", "2^2", "-", "5(2)", "+", "6", "=", "4", "-", "10", "+", "6", "=", "0", font_size=24)
        verify1.next_to(verify_title, DOWN, buff=0.3)
        
        self.play(Write(verify1))
        self.wait(1)
        
        # Verify x = 3
        verify2 = MathTex("x = 3:", "3^2", "-", "5(3)", "+", "6", "=", "9", "-", "15", "+", "6", "=", "0", font_size=24)
        verify2.next_to(verify1, DOWN, buff=0.2)
        
        self.play(Write(verify2))
        self.wait(3)

class Functions(Scene):
    def construct(self):
        # Set up the scene
        title = Text("Functions", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # Definition of a function
        definition = Text("A function is a relation where each input has exactly one output", font_size=24)
        definition.next_to(title, DOWN, buff=0.5)
        
        self.play(Write(definition))
        self.wait(2)
        
        # Function notation
        notation = MathTex("f(x)", "=", "y", font_size=48)
        notation.next_to(definition, DOWN, buff=1)
        
        self.play(Write(notation))
        self.wait(2)
        
        # Example function
        example_func = MathTex("f(x)", "=", "2x", "+", "3", font_size=48)
        example_func.next_to(notation, DOWN, buff=0.5)
        
        self.play(Write(example_func))
        self.wait(2)
        
        # Show function table
        table_title = Text("Function Table", font_size=36)
        table_title.next_to(example_func, DOWN, buff=1)
        
        self.play(Write(table_title))
        self.wait(1)
        
        # Create table
        x_vals = [-2, -1, 0, 1, 2]
        y_vals = [2*x + 3 for x in x_vals]
        
        # Table headers
        x_header = MathTex("x", font_size=36)
        y_header = MathTex("f(x)", font_size=36)
        
        # Table values
        x_column = VGroup(*[MathTex(str(x), font_size=36) for x in x_vals])
        y_column = VGroup(*[MathTex(str(y), font_size=36) for y in y_vals])
        
        # Arrange table
        x_header.shift(LEFT)
        y_header.shift(RIGHT)
        
        for i, (x_val, y_val) in enumerate(zip(x_column, y_column)):
            x_val.shift(LEFT + DOWN * (i + 1))
            y_val.shift(RIGHT + DOWN * (i + 1))
        
        # Display table
        self.play(Write(x_header), Write(y_header))
        self.play(Write(x_column), Write(y_column))
        self.wait(2)
        
        # Show graph
        graph_title = Text("Graph of f(x) = 2x + 3", font_size=36)
        graph_title.next_to(x_column[-1], DOWN, buff=1).shift(RIGHT)
        
        self.play(Write(graph_title))
        self.wait(1)
        
        # Create axes
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-3, 9, 2],
            axis_config={"color": WHITE},
        )
        axes.next_to(graph_title, DOWN, buff=0.5)
        
        # Create function graph
        graph = axes.plot(lambda x: 2*x + 3, color=BLUE)
        
        # Create points
        points = VGroup(*[
            Dot(axes.c2p(x, y), color=YELLOW)
            for x, y in zip(x_vals, y_vals)
        ])
        
        # Display graph
        self.play(Create(axes))
        self.play(Create(graph))
        self.play(Create(points))
        self.wait(3)