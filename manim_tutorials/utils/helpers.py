"""
Helper utilities for Manim tutorials.
"""
from manim import *

def create_labeled_arrow(start, end, label_text, **kwargs):
    """
    Create an arrow with a label.
    
    Parameters
    ----------
    start : np.ndarray
        Start position of the arrow
    end : np.ndarray
        End position of the arrow
    label_text : str
        Text for the label
    **kwargs : dict
        Additional arguments for the arrow
        
    Returns
    -------
    VGroup
        Group containing the arrow and label
    """
    arrow = Arrow(start, end, **kwargs)
    label = Text(label_text, font_size=24)
    label.next_to(arrow, UP, buff=0.1)
    return VGroup(arrow, label)

def animate_counting(scene, start, end, run_time=3):
    """
    Animate counting from start to end.
    
    Parameters
    ----------
    scene : Scene
        The scene to add the animation to
    start : float
        Starting number
    end : float
        Ending number
    run_time : float
        Duration of the animation
        
    Returns
    -------
    AnimationGroup
        The animation group for the counting
    """
    tracker = ValueTracker(start)
    decimal = DecimalNumber(start)
    decimal.add_updater(lambda d: d.set_value(tracker.get_value()))
    
    scene.add(decimal)
    
    return AnimationGroup(
        tracker.animate.set_value(end),
        run_time=run_time
    )

def position_equation_labels(equation, labels):
    """
    Position labels next to equation parts.
    
    Parameters
    ----------
    equation : MathTex
        The equation object
    labels : list
        List of label texts
        
    Returns
    -------
    VGroup
        Group containing the equation and labels
    """
    label_group = VGroup()
    
    for i, label_text in enumerate(labels):
        if i < len(equation):
            label = Text(label_text, font_size=18)
            label.next_to(equation[i], DOWN, buff=0.1)
            label_group.add(label)
    
    return VGroup(equation, label_group)

def create_coordinate_system(x_range=None, y_range=None, **kwargs):
    """
    Create a coordinate system with default ranges.
    
    Parameters
    ----------
    x_range : list, optional
        [min, max, step] for x-axis
    y_range : list, optional
        [min, max, step] for y-axis
    **kwargs : dict
        Additional arguments for Axes
        
    Returns
    -------
    Axes
        The coordinate system
    """
    if x_range is None:
        x_range = [-5, 5, 1]
    if y_range is None:
        y_range = [-3, 3, 1]
        
    axes = Axes(
        x_range=x_range,
        y_range=y_range,
        **kwargs
    )
    
    return axes

def add_coordinate_labels(axes, x_labels=None, y_labels=None):
    """
    Add labels to coordinate system.
    
    Parameters
    ----------
    axes : Axes
        The coordinate system
    x_labels : list, optional
        Labels for x-axis
    y_labels : list, optional
        Labels for y-axis
        
    Returns
    -------
    VGroup
        Group containing axes and labels
    """
    if x_labels is None:
        x_labels = axes.get_x_axis().get_tick_range()
    if y_labels is None:
        y_labels = axes.get_y_axis().get_tick_range()
        
    axes.add_coordinates(x_labels, y_labels)
    return axes

def create_animated_title(scene, title_text, **kwargs):
    """
    Create an animated title.
    
    Parameters
    ----------
    scene : Scene
        The scene to add the title to
    title_text : str
        The title text
    **kwargs : dict
        Additional arguments for Text
        
    Returns
    -------
    Text
        The title object
    """
    title = Text(title_text, **kwargs)
    title.to_edge(UP)
    
    scene.play(Write(title))
    scene.wait(1)
    
    return title

def fade_out_all(scene):
    """
    Fade out all objects in the scene.
    
    Parameters
    ----------
    scene : Scene
        The scene to fade out objects from
    """
    if scene.mobjects:
        scene.play(*[FadeOut(mob) for mob in scene.mobjects])

def arrange_objects_in_grid(objects, rows=None, cols=None, buff=0.5):
    """
    Arrange objects in a grid.
    
    Parameters
    ----------
    objects : list
        List of objects to arrange
    rows : int, optional
        Number of rows
    cols : int, optional
        Number of columns
    buff : float
        Buffer between objects
        
    Returns
    -------
    VGroup
        Group with objects arranged in grid
    """
    group = VGroup(*objects)
    
    if rows is None and cols is None:
        # Auto arrange in square grid
        rows = cols = int(np.ceil(np.sqrt(len(objects))))
    elif rows is None:
        rows = int(np.ceil(len(objects) / cols))
    elif cols is None:
        cols = int(np.ceil(len(objects) / rows))
    
    group.arrange_in_grid(rows=rows, cols=cols, buff=buff)
    return group

def color_gradient_text(text, colors):
    """
    Apply gradient colors to text.
    
    Parameters
    ----------
    text : Text
        The text object
    colors : list
        List of colors to apply
        
    Returns
    -------
    Text
        The text object with gradient colors
    """
    text.set_color_by_gradient(*colors)
    return text

def create_highlight_box(object, color=YELLOW, buff=0.1):
    """
    Create a highlight box around an object.
    
    Parameters
    ----------
    object : Mobject
        The object to highlight
    color : str
        Color of the highlight box
    buff : float
        Buffer around the object
        
    Returns
    -------
    SurroundingRectangle
        The highlight box
    """
    box = SurroundingRectangle(object, color=color, buff=buff)
    return box

def animate_zoom(scene, object, scale_factor=1.5, run_time=2):
    """
    Animate zooming in on an object.
    
    Parameters
    ----------
    scene : Scene
        The scene to animate in
    object : Mobject
        The object to zoom to
    scale_factor : float
        Factor to scale the object
    run_time : float
        Duration of the animation
        
    Returns
    -------
    tuple
        (AnimationGroup for zoom, AnimationGroup for return)
    """
    original_scale = object.scale_factor if hasattr(object, 'scale_factor') else 1
    
    zoom_animation = object.animate.scale(scale_factor)
    return_animation = object.animate.scale(original_scale / scale_factor)
    
    return (
        AnimationGroup(zoom_animation, run_time=run_time),
        AnimationGroup(return_animation, run_time=run_time)
    )