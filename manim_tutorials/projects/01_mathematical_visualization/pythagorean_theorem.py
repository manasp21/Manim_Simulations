from manim import *

class PythagoreanTheorem(Scene):
    def construct(self):
        # Create a right triangle
        triangle = Polygon(
            [0, 0, 0],  # Point A
            [3, 0, 0],  # Point B
            [0, 4, 0],  # Point C
            color=WHITE
        )
        
        # Add right angle marker
        right_angle = RightAngle(
            Line(triangle.get_vertices()[1], triangle.get_vertices()[0]),
            Line(triangle.get_vertices()[0], triangle.get_vertices()[2]),
            length=0.5
        )
        
        # Label the vertices
        label_a = Text("A", font_size=24).next_to(triangle.get_vertices()[0], DL, buff=0.2)
        label_b = Text("B", font_size=24).next_to(triangle.get_vertices()[1], DR, buff=0.2)
        label_c = Text("C", font_size=24).next_to(triangle.get_vertices()[2], UP, buff=0.2)
        
        # Label the sides
        side_a = Text("a", font_size=24).next_to(
            Line(triangle.get_vertices()[1], triangle.get_vertices()[2]).get_center(), 
            RIGHT, buff=0.2
        )
        side_b = Text("b", font_size=24).next_to(
            Line(triangle.get_vertices()[0], triangle.get_vertices()[2]).get_center(), 
            LEFT, buff=0.2
        )
        side_c = Text("c", font_size=24).next_to(
            Line(triangle.get_vertices()[0], triangle.get_vertices()[1]).get_center(), 
            DOWN, buff=0.2
        )
        
        # Display the triangle and labels
        self.play(Create(triangle), Create(right_angle))
        self.play(Write(label_a), Write(label_b), Write(label_c))
        self.play(Write(side_a), Write(side_b), Write(side_c))
        self.wait(2)
        
        # Show the Pythagorean theorem
        theorem = MathTex("c^2", "=", "a^2", "+", "b^2", font_size=48)
        theorem.shift(UP * 2)
        self.play(Write(theorem))
        self.wait(2)
        
        # Show values for the specific triangle
        values = MathTex("c^2", "=", "3^2", "+", "4^2", "=", "9", "+", "16", "=", "25", font_size=36)
        values.next_to(theorem, DOWN)
        self.play(Write(values))
        self.wait(2)
        
        # Show that c = 5
        result = MathTex("c", "=", "\\sqrt{25}", "=", "5", font_size=36)
        result.next_to(values, DOWN)
        self.play(Write(result))
        self.wait(3)

class PythagoreanProof(Scene):
    def construct(self):
        # Create the proof visualization
        # Start with a square with side length (a+b)
        a, b = 3, 4
        side_length = a + b
        
        # Create the large square
        large_square = Square(side_length=side_length, color=BLUE)
        large_square.shift(LEFT * 2)
        
        # Create the inner square (side c)
        c = np.sqrt(a**2 + b**2)
        inner_square = Square(side_length=c, color=YELLOW, fill_opacity=0.3)
        
        # Create the four triangles
        triangle1 = Polygon([0, 0, 0], [a, 0, 0], [0, b, 0], color=WHITE, fill_opacity=0.5)
        triangle2 = triangle1.copy().rotate(PI/2).move_to([a, 0, 0], aligned_edge=DL)
        triangle3 = triangle1.copy().rotate(PI).move_to([a, b, 0], aligned_edge=UL)
        triangle4 = triangle1.copy().rotate(3*PI/2).move_to([0, b, 0], aligned_edge=UR)
        
        # Position triangles in the large square
        triangles = VGroup(triangle1, triangle2, triangle3, triangle4)
        triangles.shift(LEFT * 2 + DOWN * 1.5)
        
        # Display the large square and triangles
        self.play(Create(large_square))
        self.play(Create(triangles))
        self.wait(2)
        
        # Show that the inner shape is a square with side c
        self.play(Create(inner_square))
        inner_label = Text("c", font_size=24).next_to(inner_square, RIGHT, buff=0.2)
        self.play(Write(inner_label))
        self.wait(2)
        
        # Show area calculations
        area_text1 = MathTex(
            "\\text{Area of large square}", "=", "(a+b)^2", 
            font_size=36
        ).shift(RIGHT * 3 + UP * 2)
        
        area_text2 = MathTex(
            "\\text{Area of large square}", "=", 
            "\\text{Area of inner square}", "+", 
            "4", "\\times", "\\text{Area of triangle}",
            font_size=36
        ).next_to(area_text1, DOWN, buff=0.3)
        
        area_text3 = MathTex(
            "(a+b)^2", "=", "c^2", "+", "4", "\\times", "\\frac{1}{2}ab",
            font_size=36
        ).next_to(area_text2, DOWN, buff=0.3)
        
        area_text4 = MathTex(
            "a^2 + 2ab + b^2", "=", "c^2", "+", "2ab",
            font_size=36
        ).next_to(area_text3, DOWN, buff=0.3)
        
        area_text5 = MathTex(
            "a^2 + b^2", "=", "c^2",
            font_size=36
        ).next_to(area_text4, DOWN, buff=0.3)
        
        self.play(Write(area_text1))
        self.wait(1)
        self.play(Write(area_text2))
        self.wait(1)
        self.play(Write(area_text3))
        self.wait(1)
        self.play(Write(area_text4))
        self.wait(1)
        self.play(Write(area_text5))
        self.wait(3)