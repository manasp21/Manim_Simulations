from manim import *

class ThreeDSceneExample(ThreeDScene):
    def construct(self):
        # Set camera orientation
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        
        # Create 3D axes
        axes = ThreeDAxes()
        
        # Create a 3D sphere
        sphere = Sphere(radius=1, color=BLUE, fill_opacity=0.5)
        
        # Create a 3D cube
        cube = Cube(side_length=1, fill_color=RED, fill_opacity=0.5)
        cube.shift(RIGHT * 2)
        
        # Display axes
        self.play(Create(axes))
        self.wait(1)
        
        # Display 3D objects
        self.play(Create(sphere))
        self.play(Create(cube))
        self.wait(1)
        
        # Rotate the camera
        self.begin_ambient_camera_rotation(rate=0.2)
        self.wait(4)
        self.stop_ambient_camera_rotation()
        
        # Move objects
        self.play(
            sphere.animate.shift(UP * 2),
            cube.animate.shift(LEFT * 2)
        )
        self.wait(2)
        
        # Change camera orientation
        self.move_camera(phi=45 * DEGREES, theta=-45 * DEGREES, run_time=3)
        self.wait(2)

class SurfaceExample(ThreeDScene):
    def construct(self):
        # Set camera orientation
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        
        # Create a parametric surface
        surface = Surface(
            lambda u, v: np.array([
                u,
                v,
                np.sin(u) * np.cos(v)
            ]),
            u_range=[-3, 3],
            v_range=[-3, 3],
            fill_opacity=0.7,
            checkerboard_colors=[BLUE_D, BLUE_E],
        )
        
        # Display the surface
        self.play(Create(surface), run_time=3)
        self.wait(2)
        
        # Rotate the camera to view from different angles
        self.begin_ambient_camera_rotation(rate=0.1)
        self.wait(6)
        self.stop_ambient_camera_rotation()
        self.wait(1)