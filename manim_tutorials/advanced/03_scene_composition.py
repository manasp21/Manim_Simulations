from manim import *

class SceneComposition(Scene):
    def construct(self):
        # Create multiple sub-scenes as groups
        # Scene 1: Geometric shapes
        shapes_group = VGroup()
        circle = Circle(radius=0.5, color=RED, fill_opacity=0.5)
        square = Square(side_length=1, color=BLUE, fill_opacity=0.5)
        triangle = Triangle(color=GREEN, fill_opacity=0.5)
        
        shapes_group.add(circle, square, triangle)
        shapes_group.arrange(RIGHT, buff=0.5)
        
        # Scene 2: Text elements
        text_group = VGroup()
        title = Text("Scene Composition", font_size=36)
        subtitle = Text("Combining Multiple Elements", font_size=24)
        text_group.add(title, subtitle)
        text_group.arrange(DOWN, buff=0.3)
        
        # Scene 3: Mathematical expressions
        math_group = VGroup()
        equation1 = MathTex(r"e^{i\pi} + 1 = 0", font_size=36)
        equation2 = MathTex(r"\int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}", font_size=36)
        math_group.add(equation1, equation2)
        math_group.arrange(DOWN, buff=0.5)
        
        # Position the groups on screen
        shapes_group.shift(UP * 2)
        text_group.shift(ORIGIN)
        math_group.shift(DOWN * 2)
        
        # Animate each group separately
        self.play(
            Create(shapes_group),
            Write(text_group),
            Write(math_group),
            run_time=3
        )
        self.wait(2)
        
        # Transform the composition
        # Move shapes to form a pattern
        self.play(
            circle.animate.move_to(UP),
            square.animate.move_to(LEFT),
            triangle.animate.move_to(RIGHT),
            run_time=2
        )
        self.wait(1)
        
        # Highlight the title
        self.play(
            title.animate.set_color(YELLOW).scale(1.2),
            run_time=1
        )
        self.wait(1)
        
        # Transform equations
        equation3 = MathTex(r"F = ma", font_size=48)
        self.play(Transform(equation1, equation3))
        self.wait(1)
        
        # Fade out everything in sequence
        self.play(FadeOut(shapes_group), run_time=1)
        self.play(FadeOut(math_group), run_time=1)
        self.play(FadeOut(text_group), run_time=1)
        self.wait(1)

class MultiSceneComposition(Scene):
    def construct(self):
        # Create a sequence of scenes that transition into each other
        # Scene 1: Introduction
        intro_text = Text("Welcome to Multi-Scene Composition", font_size=36)
        self.play(Write(intro_text))
        self.wait(2)
        
        # Transition to Scene 2: Main Content
        main_title = Text("Main Content", font_size=48, color=BLUE)
        self.play(Transform(intro_text, main_title))
        self.wait(1)
        
        # Add content to the main scene
        content = VGroup()
        bullet1 = Text("• First point", font_size=24).shift(UP)
        bullet2 = Text("• Second point", font_size=24)
        bullet3 = Text("• Third point", font_size=24).shift(DOWN)
        content.add(bullet1, bullet2, bullet3)
        
        self.play(Write(content))
        self.wait(2)
        
        # Transition to Scene 3: Conclusion
        conclusion = Text("Thank You!", font_size=48, color=GREEN)
        self.play(
            FadeOut(main_title),
            FadeOut(content),
            run_time=1
        )
        self.play(Write(conclusion))
        self.wait(2)