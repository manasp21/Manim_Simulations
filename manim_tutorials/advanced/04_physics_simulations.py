from manim import *
import numpy as np

class PhysicsSimulations(Scene):
    def construct(self):
        # Create a simple pendulum simulation
        # Pendulum parameters
        length = 3
        gravity = 9.8
        angle = PI / 4  # 45 degrees
        
        # Create pivot point
        pivot = Dot(point=ORIGIN, color=WHITE)
        
        # Create pendulum rod and bob
        rod = Line(ORIGIN, length * DOWN, color=WHITE)
        bob = Dot(point=length * DOWN, color=RED, radius=0.2)
        
        # Group pendulum parts
        pendulum = VGroup(pivot, rod, bob)
        pendulum.shift(UP * 2 + LEFT * 3)
        
        # Add to scene
        self.add(pendulum)
        self.wait(1)
        
        # Animate pendulum swing (simplified)
        def swing_pendulum(mob, alpha):
            # Simple harmonic motion approximation
            current_angle = angle * np.cos(alpha * 2 * PI)
            new_bob_pos = pendulum.get_center() + length * np.array([
                np.sin(current_angle),
                -np.cos(current_angle),
                0
            ])
            rod.put_start_and_end_on(pendulum.get_center(), new_bob_pos)
            bob.move_to(new_bob_pos)
        
        # Create an updater for the pendulum
        pendulum.add_updater(swing_pendulum)
        self.add(pendulum)
        
        # Let it swing for a few seconds
        self.wait(4)
        
        # Remove updater
        pendulum.clear_updaters()
        self.wait(1)
        
        # Create a bouncing ball simulation
        ball = Circle(radius=0.3, color=BLUE, fill_opacity=1)
        ball.shift(RIGHT * 3)
        
        ground = Line(LEFT * 4, RIGHT * 4, color=WHITE).shift(DOWN * 2)
        
        self.play(Create(ground))
        self.play(Create(ball))
        
        # Animate bouncing ball
        bounce_heights = [2, 1.5, 1, 0.5, 0.2]
        for i, height in enumerate(bounce_heights):
            # Move ball up
            self.play(ball.animate.shift(UP * height), rate_func=rush_into, run_time=0.5)
            # Move ball down
            self.play(ball.animate.shift(DOWN * height), rate_func=rush_from, run_time=0.5)
        
        self.wait(2)

class WaveSimulation(Scene):
    def construct(self):
        # Create a wave simulation
        # Parameters
        amplitude = 1
        wavelength = 2
        frequency = 1
        
        # Create axes
        axes = Axes(
            x_range=[0, 8, 1],
            y_range=[-2, 2, 1],
            axis_config={"color": BLUE},
        )
        axes_labels = axes.get_axis_labels(x_label="x", y_label="y")
        
        # Create wave function
        def wave_function(x, t=0):
            return amplitude * np.sin(2 * PI * (x / wavelength - frequency * t))
        
        # Create initial wave
        wave = axes.plot(wave_function, color=YELLOW)
        wave_label = Text("Wave Simulation", font_size=24).next_to(axes, UP)
        
        # Display static wave
        self.play(Create(axes), Write(axes_labels), Create(wave), Write(wave_label))
        self.wait(2)
        
        # Animate wave motion
        def update_wave(mob, alpha):
            t = alpha * 2  # Time parameter
            new_wave = axes.plot(lambda x: wave_function(x, t), color=YELLOW)
            mob.become(new_wave)
        
        # Apply the wave animation
        wave.add_updater(update_wave)
        self.add(wave)
        self.wait(4)
        
        # Remove updater and finish
        wave.clear_updaters()
        self.wait(1)