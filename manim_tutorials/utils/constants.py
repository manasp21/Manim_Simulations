"""
Constants for Manim tutorials.
"""
from manim import *

# Color schemes
PRIMARY_COLORS = [RED, BLUE, GREEN, YELLOW, PURPLE, ORANGE]
SECONDARY_COLORS = [MAROON, DARK_BLUE, GREEN_E, GOLD, PURPLE_E, LIGHT_BROWN]
NEUTRAL_COLORS = [WHITE, LIGHT_GREY, GREY, DARK_GREY, BLACK]

# Mathematical constants
PI_APPROX = 3.14159
EULER_NUMBER = 2.71828
GOLDEN_RATIO = 1.61803

# Animation timing
DEFAULT_ANIMATION_RUN_TIME = 1.5
FAST_ANIMATION_RUN_TIME = 0.8
SLOW_ANIMATION_RUN_TIME = 3.0
PAUSE_TIME = 1.0

# Scene dimensions
DEFAULT_SCENE_WIDTH = 14
DEFAULT_SCENE_HEIGHT = 8

# Text settings
DEFAULT_FONT_SIZE = 24
TITLE_FONT_SIZE = 48
LARGE_FONT_SIZE = 36
SMALL_FONT_SIZE = 18

# Graph settings
DEFAULT_AXES_RANGE = [-5, 5, 1]
DEFAULT_AXES_X_RANGE = [-5, 5, 1]
DEFAULT_AXES_Y_RANGE = [-3, 3, 1]

# 3D settings
DEFAULT_3D_CAMERA_PHI = 75 * DEGREES
DEFAULT_3D_CAMERA_THETA = 30 * DEGREES
DEFAULT_3D_CAMERA_GAMMA = 0

# Quality settings
QUALITY_SETTINGS = {
    "low": {
        "pixel_width": 480,
        "pixel_height": 270,
        "frame_rate": 15
    },
    "medium": {
        "pixel_width": 854,
        "pixel_height": 480,
        "frame_rate": 30
    },
    "high": {
        "pixel_width": 1920,
        "pixel_height": 1080,
        "frame_rate": 60
    },
    "production": {
        "pixel_width": 3840,
        "pixel_height": 2160,
        "frame_rate": 60
    }
}

# Common shapes
COMMON_SHAPES = {
    "circle": Circle,
    "square": Square,
    "triangle": Triangle,
    "rectangle": Rectangle,
    "arrow": Arrow,
    "line": Line
}

# Animation types
CREATION_ANIMATIONS = [
    Create, Write, DrawBorderThenFill, ShowIncreasingSubsets
]

TRANSFORMATION_ANIMATIONS = [
    Transform, ReplacementTransform, FadeTransform, ScaleInPlace
]

MOVEMENT_ANIMATIONS = [
    Rotate, ScaleInPlace
]

FADE_ANIMATIONS = [
    FadeIn, FadeOut, FadeToColor, FadeTransform
]

# Coordinate system settings
COORDINATE_SYSTEM_SETTINGS = {
    "axis_color": WHITE,
    "axis_stroke_width": 2,
    "tick_frequency": 1,
    "label_font_size": 24
}

# Default configurations
DEFAULT_CONFIG = {
    "background_color": BLACK,
    "font": "Arial",
    "stroke_width": 4,
    "fill_opacity": 0.8
}

# Educational settings
EDUCATIONAL_SCENE_SETTINGS = {
    "pause_between_animations": True,
    "show_object_names": False,
    "add_explanations": True
}

# Performance settings
PERFORMANCE_SETTINGS = {
    "max_objects_for_caching": 100,
    "use_partial_movie_cache": True,
    "disable_caching_for_simple_scenes": True
}

# Style guide
STYLE_GUIDE = {
    "text_color": WHITE,
    "highlight_color": YELLOW,
    "emphasis_color": RED,
    "explanation_color": GREY,
    "title_color": BLUE,
    "subtitle_color": LIGHT_GREY
}

# Common mathematical functions for plotting
COMMON_FUNCTIONS = {
    "linear": lambda x: x,
    "quadratic": lambda x: x**2,
    "cubic": lambda x: x**3,
    "sqrt": lambda x: np.sqrt(x),
    "sin": lambda x: np.sin(x),
    "cos": lambda x: np.cos(x),
    "tan": lambda x: np.tan(x),
    "exp": lambda x: np.exp(x),
    "log": lambda x: np.log(x),
    "abs": lambda x: np.abs(x)
}

# Animation groups
ANIMATION_GROUPS = {
    "sequential": AnimationGroup,
    "parallel": LaggedStart,
    "succession": Succession
}

# Updater settings
UPDATER_SETTINGS = {
    "default_dt": 1/15,  # Default time step
    "max_updaters": 100,  # Maximum number of updaters
    "continuous_update": True
}