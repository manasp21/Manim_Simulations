from manim import *
import numpy as np

class ProjectileMotion(Scene):
    def construct(self):
        # Set up the scene
        title = Text("Projectile Motion", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # Create ground
        ground = Line(LEFT * 7, RIGHT * 7, color=GREEN)
        ground.shift(DOWN * 3)
        self.play(Create(ground))
        
        # Create projectile
        projectile = Dot(color=RED, radius=0.15)
        projectile.move_to(LEFT * 6 + DOWN * 3)
        
        # Show initial position
        init_label = Text("Initial Position", font_size=24)
        init_label.next_to(projectile, UP, buff=0.5)
        self.play(Create(projectile), Write(init_label))
        self.wait(1)
        
        # Remove initial label
        self.play(FadeOut(init_label))
        
        # Define projectile motion parameters
        v0 = 5  # Initial velocity
        angle = 60 * DEGREES  # Launch angle
        g = 9.8  # Acceleration due to gravity
        
        # Calculate components of initial velocity
        vx = v0 * np.cos(angle)
        vy = v0 * np.sin(angle)
        
        # Calculate time of flight
        time_of_flight = 2 * vy / g
        
        # Create trajectory path
        def trajectory(t):
            x = vx * t
            y = vy * t - 0.5 * g * t**2
            return np.array([x, y, 0]) + projectile.get_start()
        
        path = ParametricFunction(
            trajectory,
            t_range=[0, time_of_flight],
            color=YELLOW
        )
        
        # Show the trajectory path
        self.play(Create(path), run_time=2)
        self.wait(1)
        
        # Animate the projectile motion
        self.play(
            MoveAlongPath(projectile, path),
            run_time=time_of_flight,
            rate_func=linear
        )
        self.wait(2)
        
        # Show key points and labels
        # Maximum height point
        max_height_time = vy / g
        max_height_point = trajectory(max_height_time)
        max_height_dot = Dot(max_height_point, color=BLUE)
        max_height_label = Text("Max Height", font_size=20)
        max_height_label.next_to(max_height_dot, RIGHT, buff=0.3)
        
        # Range point (landing point)
        range_point = trajectory(time_of_flight)
        range_dot = Dot(range_point, color=GREEN)
        range_label = Text("Range", font_size=20)
        range_label.next_to(range_dot, DOWN, buff=0.3)
        
        # Show key points
        self.play(
            Create(max_height_dot),
            Create(range_dot)
        )
        self.play(
            Write(max_height_label),
            Write(range_label)
        )
        self.wait(2)
        
        # Show equations
        equations = VGroup(
            MathTex("x = v_0 \\cos(\\theta) t", font_size=30),
            MathTex("y = v_0 \\sin(\\theta) t - \\frac{1}{2} g t^2", font_size=30),
            MathTex("R = \\frac{v_0^2 \\sin(2\\theta)}{g}", font_size=30),
            MathTex("H = \\frac{v_0^2 \\sin^2(\\theta)}{2g}", font_size=30)
        )
        equations.arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        equations.to_edge(RIGHT).shift(UP)
        
        eq_labels = VGroup(
            Text("Horizontal position", font_size=20),
            Text("Vertical position", font_size=20),
            Text("Range", font_size=20),
            Text("Maximum height", font_size=20)
        )
        
        for i, label in enumerate(eq_labels):
            label.next_to(equations[i], LEFT, buff=0.5)
        
        self.play(
            Write(equations),
            Write(eq_labels),
            run_time=3
        )
        self.wait(3)

class MultipleProjectiles(Scene):
    def construct(self):
        # Set up the scene
        title = Text("Multiple Projectiles", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # Create ground
        ground = Line(LEFT * 7, RIGHT * 7, color=GREEN)
        ground.shift(DOWN * 3)
        self.play(Create(ground))
        
        # Create multiple projectiles with different angles
        angles = [30 * DEGREES, 45 * DEGREES, 60 * DEGREES]
        colors = [RED, BLUE, GREEN]
        v0 = 5  # Initial velocity
        g = 9.8  # Acceleration due to gravity
        
        projectiles = VGroup()
        paths = VGroup()
        
        for i, (angle, color) in enumerate(zip(angles, colors)):
            # Create projectile
            projectile = Dot(color=color, radius=0.15)
            projectile.move_to(LEFT * 6 + DOWN * 3)
            projectiles.add(projectile)
            
            # Calculate components of initial velocity
            vx = v0 * np.cos(angle)
            vy = v0 * np.sin(angle)
            
            # Calculate time of flight
            time_of_flight = 2 * vy / g
            
            # Create trajectory path
            def make_trajectory(vx, vy, g, start_pos):
                return lambda t: np.array([
                    vx * t,
                    vy * t - 0.5 * g * t**2,
                    0
                ]) + start_pos
            
            trajectory = make_trajectory(vx, vy, g, projectile.get_start())
            
            path = ParametricFunction(
                trajectory,
                t_range=[0, time_of_flight],
                color=color
            )
            paths.add(path)
        
        # Show the trajectory paths
        self.play(
            *[Create(path) for path in paths],
            run_time=2
        )
        self.wait(1)
        
        # Show the projectiles
        self.play(
            *[Create(projectile) for projectile in projectiles]
        )
        self.wait(1)
        
        # Animate the projectile motions
        max_time = max([
            2 * v0 * np.sin(angle) / g 
            for angle in angles
        ])
        
        # Create updaters for simultaneous animation
        for i, (projectile, path, angle) in enumerate(zip(projectiles, paths, angles)):
            vx = v0 * np.cos(angle)
            vy = v0 * np.sin(angle)
            time_of_flight = 2 * vy / g
            
            def make_updater(vx, vy, g, start_pos, time_of_flight):
                return lambda mob, dt: update_projectile(
                    mob, dt, vx, vy, g, start_pos, time_of_flight
                )
            
            updater = make_updater(vx, vy, g, projectile.get_start(), time_of_flight)
            projectile.add_updater(updater)
        
        self.add(*projectiles)
        self.wait(max_time + 1)
        
        # Remove updaters
        for projectile in projectiles:
            projectile.clear_updaters()
        
        self.wait(2)

def update_projectile(mob, dt, vx, vy, g, start_pos, time_of_flight):
    # This is a simplified updater for demonstration
    # In a real implementation, you would track the actual time
    pass