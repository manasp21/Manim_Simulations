"""
Widget utilities for interactive Manim tutorials in Jupyter notebooks.
"""
import ipywidgets as widgets
from IPython.display import display
import numpy as np
from manim import *

def create_slider_widget(min_val=0, max_val=10, step=0.1, value=5, description="Value"):
    """
    Create a slider widget for parameter manipulation.
    
    Parameters
    ----------
    min_val : float
        Minimum value of the slider
    max_val : float
        Maximum value of the slider
    step : float
        Step size of the slider
    value : float
        Initial value of the slider
    description : str
        Description label for the slider
        
    Returns
    -------
    widgets.FloatSlider
        The slider widget
    """
    return widgets.FloatSlider(
        value=value,
        min=min_val,
        max=max_val,
        step=step,
        description=description,
        continuous_update=True,
        style={'description_width': 'initial'}
    )

def create_integer_slider_widget(min_val=0, max_val=10, step=1, value=5, description="Value"):
    """
    Create an integer slider widget for parameter manipulation.
    
    Parameters
    ----------
    min_val : int
        Minimum value of the slider
    max_val : int
        Maximum value of the slider
    step : int
        Step size of the slider
    value : int
        Initial value of the slider
    description : str
        Description label for the slider
        
    Returns
    -------
    widgets.IntSlider
        The integer slider widget
    """
    return widgets.IntSlider(
        value=value,
        min=min_val,
        max=max_val,
        step=step,
        description=description,
        continuous_update=True,
        style={'description_width': 'initial'}
    )

def create_dropdown_widget(options, value=None, description="Select"):
    """
    Create a dropdown widget for selecting options.
    
    Parameters
    ----------
    options : list or dict
        Options for the dropdown
    value : any
        Initial value
    description : str
        Description label for the dropdown
        
    Returns
    -------
    widgets.Dropdown
        The dropdown widget
    """
    if value is None and isinstance(options, (list, tuple)):
        value = options[0] if options else None
    elif value is None and isinstance(options, dict):
        value = list(options.keys())[0] if options else None
        
    return widgets.Dropdown(
        options=options,
        value=value,
        description=description,
        style={'description_width': 'initial'}
    )

def create_color_picker_widget(color="#FF0000", description="Color"):
    """
    Create a color picker widget.
    
    Parameters
    ----------
    color : str
        Initial color in hex format
    description : str
        Description label for the color picker
        
    Returns
    -------
    widgets.ColorPicker
        The color picker widget
    """
    return widgets.ColorPicker(
        concise=False,
        description=description,
        value=color,
        style={'description_width': 'initial'}
    )

def create_toggle_buttons_widget(options, value=None, description="Options"):
    """
    Create toggle buttons widget.
    
    Parameters
    ----------
    options : list or dict
        Options for the toggle buttons
    value : any
        Initial value
    description : str
        Description label for the toggle buttons
        
    Returns
    -------
    widgets.ToggleButtons
        The toggle buttons widget
    """
    if value is None and isinstance(options, (list, tuple)):
        value = options[0] if options else None
    elif value is None and isinstance(options, dict):
        value = list(options.keys())[0] if options else None
        
    return widgets.ToggleButtons(
        options=options,
        value=value,
        description=description,
        style={'description_width': 'initial'}
    )

def create_text_widget(value="", placeholder="Enter text", description="Text"):
    """
    Create a text input widget.
    
    Parameters
    ----------
    value : str
        Initial value
    placeholder : str
        Placeholder text
    description : str
        Description label for the text input
        
    Returns
    -------
    widgets.Text
        The text input widget
    """
    return widgets.Text(
        value=value,
        placeholder=placeholder,
        description=description,
        style={'description_width': 'initial'}
    )

def create_play_widget(min_val=0, max_val=10, step=1, interval=100, description="Play"):
    """
    Create a play widget for animation control.
    
    Parameters
    ----------
    min_val : int
        Minimum value
    max_val : int
        Maximum value
    step : int
        Step size
    interval : int
        Interval between steps in milliseconds
    description : str
        Description label for the play widget
        
    Returns
    -------
    widgets.Play
        The play widget
    """
    return widgets.Play(
        value=min_val,
        min=min_val,
        max=max_val,
        step=step,
        interval=interval,
        description=description
    )

def create_checkbox_widget(value=False, description="Checkbox"):
    """
    Create a checkbox widget.
    
    Parameters
    ----------
    value : bool
        Initial value
    description : str
        Description label for the checkbox
        
    Returns
    -------
    widgets.Checkbox
        The checkbox widget
    """
    return widgets.Checkbox(
        value=value,
        description=description,
        style={'description_width': 'initial'}
    )

def create_linked_widgets(widget1, widget2, attr1='value', attr2='value'):
    """
    Link two widgets together.
    
    Parameters
    ----------
    widget1 : widgets.Widget
        First widget
    widget2 : widgets.Widget
        Second widget
    attr1 : str
        Attribute of first widget to link
    attr2 : str
        Attribute of second widget to link
        
    Returns
    -------
    widgets.jslink
        The link object
    """
    return widgets.jslink((widget1, attr1), (widget2, attr2))

def display_widgets(*widgets_list):
    """
    Display multiple widgets in a vertical box.
    
    Parameters
    ----------
    *widgets_list : widgets.Widget
        Widgets to display
        
    Returns
    -------
    widgets.VBox
        Vertical box containing the widgets
    """
    vbox = widgets.VBox(widgets_list)
    display(vbox)
    return vbox

def create_interactive_scene_controller():
    """
    Create a controller for interactive Manim scenes with common widgets.
    
    Returns
    -------
    dict
        Dictionary containing common interactive widgets
    """
    controller = {
        'speed_slider': create_slider_widget(
            min_val=0.1, max_val=5.0, step=0.1, value=1.0, description="Animation Speed"
        ),
        'size_slider': create_slider_widget(
            min_val=0.1, max_val=5.0, step=0.1, value=1.0, description="Object Size"
        ),
        'color_picker': create_color_picker_widget(
            color="#FF0000", description="Object Color"
        ),
        'shape_dropdown': create_dropdown_widget(
            options=['Circle', 'Square', 'Triangle', 'Rectangle'],
            value='Circle',
            description="Shape"
        ),
        'dimension_toggle': create_toggle_buttons_widget(
            options=['2D', '3D'],
            value='2D',
            description="Dimension"
        ),
        'play_controller': create_play_widget(
            min_val=0, max_val=100, step=1, interval=100, description="Animation"
        )
    }
    return controller

def update_scene_with_widgets(scene, widgets_dict):
    """
    Update a Manim scene based on widget values.
    
    Parameters
    ----------
    scene : Scene
        The Manim scene to update
    widgets_dict : dict
        Dictionary of widgets with their current values
        
    Returns
    -------
    Scene
        Updated scene
    """
    # This is a placeholder function that would be implemented
    # based on specific scene requirements
    return scene

# Example usage functions
def demo_slider_interaction():
    """
    Demonstrate slider interaction with a simple Manim scene.
    """
    # This would be used in a Jupyter notebook cell
    slider = create_slider_widget(min_val=0, max_val=2*PI, step=0.1, value=0, description="Angle")
    
    def update_scene(change):
        # This would update a Manim scene based on slider value
        print(f"Slider value: {change['new']}")
    
    slider.observe(update_scene, names='value')
    display(slider)
    
    return slider

def demo_color_interaction():
    """
    Demonstrate color picker interaction.
    """
    color_picker = create_color_picker_widget(color="#00FF00", description="Shape Color")
    
    def update_color(change):
        # This would update a Manim scene based on color value
        print(f"Selected color: {change['new']}")
    
    color_picker.observe(update_color, names='value')
    display(color_picker)
    
    return color_picker