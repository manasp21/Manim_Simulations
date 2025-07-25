"""
Interactive version of Interactive Scenes tutorial with Jupyter widgets.
This file demonstrates how to use interactive widgets with Manim interactive scenes.
"""
from manim import *
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from utils.widget_utils import *
import ipywidgets as widgets
from IPython.display import display
import numpy as np

# This would be used in a Jupyter notebook cell
def interactive_scenes_demo():
    """
    Demonstrate interactive scenes with widgets.
    This function would be called in a Jupyter notebook to create interactive controls.
    """
    # Create interactive widgets
    button_count_slider = create_integer_slider_widget(
        min_val=1, max_val=10, step=1, value=2, description="Button Count"
    )
    
    value_tracker_min_slider = create_slider_widget(
        min_val=0, max_val=10, step=0.1, value=0, description="Min Value"
    )
    
    value_tracker_max_slider = create_slider_widget(
        min_val=0, max_val=20, step=0.1, value=5, description="Max Value"
    )
    
    interaction_type_dropdown = create_dropdown_widget(
        options=['Buttons', 'Value Trackers', 'Keyboard Input'],
        value='Buttons',
        description="Interaction Type"
    )
    
    color_picker = create_color_picker_widget(
        color="#FF0000", description="Button Color"
    )
    
    # Display the widgets
    controller = widgets.VBox([
        widgets.HTML("<h3>Interactive Scenes Controller</h3>"),
        button_count_slider,
        value_tracker_min_slider,
        value_tracker_max_slider,
        interaction_type_dropdown,
        color_picker
    ])
    
    display(controller)
    
    return {
        'button_count_slider': button_count_slider,
        'value_tracker_min_slider': value_tracker_min_slider,
        'value_tracker_max_slider': value_tracker_max_slider,
        'interaction_type_dropdown': interaction_type_dropdown,
        'color_picker': color_picker
    }

class InteractiveScenesWithWidgets(Scene):
    """
    An interactive version of the InteractiveScenes scene that demonstrates
    how parameters could be controlled via widgets.
    """
    def construct(self):
        # Title
        title = Text("Interactive Scenes with Widgets", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # Explanation text
        explanation = Text(
            "In a Jupyter notebook, you could control\n"
            "these parameters using interactive widgets!",
            font_size=24
        )
        explanation.next_to(title, DOWN, buff=0.5)
        self.play(Write(explanation))
        self.wait(1)
        
        # Create interactive elements (visual representation)
        button1 = Rectangle(height=1, width=3, color=BLUE, fill_opacity=0.5)
        button1_text = Text("Button 1", font_size=24).move_to(button1)
        button1_group = VGroup(button1, button1_text)
        
        button2 = Rectangle(height=1, width=3, color=GREEN, fill_opacity=0.5)
        button2_text = Text("Button 2", font_size=24).move_to(button2)
        button2_group = VGroup(button2, button2_text)
        
        # Position buttons
        button1_group.shift(LEFT * 2 + DOWN)
        button2_group.shift(RIGHT * 2 + DOWN)
        
        # Display buttons
        self.play(Create(button1_group), Create(button2_group))
        self.wait(1)
        
        # Simulate button interactions
        self.play(button1_group.animate.set_color(YELLOW))
        info_text = Text("Button 1 Pressed!", font_size=24).shift(UP)
        self.play(Write(info_text))
        self.wait(1)
        
        self.play(
            button1_group.animate.set_color(BLUE),
            button2_group.animate.set_color(YELLOW)
        )
        self.play(Transform(info_text, Text("Button 2 Pressed!", font_size=24).shift(UP)))
        self.wait(2)
        
        # Remove interactive elements
        self.play(
            FadeOut(button1_group),
            FadeOut(button2_group),
            FadeOut(info_text)
        )
        self.wait(1)
        
        # Second part - Value trackers
        # Demonstrate value trackers for interactive elements
        # Create a value tracker
        value_tracker = ValueTracker(0)
        
        # Create a number display
        number = DecimalNumber(0, num_decimal_places=2, font_size=36)
        number.add_updater(lambda d: d.set_value(value_tracker.get_value()))
        
        # Create a bar representing the value
        bar = Rectangle(height=0.5, width=0, color=BLUE, fill_opacity=0.7)
        bar.next_to(number, DOWN, buff=0.5)
        bar.add_updater(lambda b: b.stretch_to_fit_width(value_tracker.get_value() * 2).move_to(bar.get_left(), aligned_edge=LEFT))
        
        # Add elements to scene
        self.add(number, bar)
        self.wait(1)
        
        # Animate the value tracker
        self.play(value_tracker.animate.set_value(5), run_time=3)
        self.wait(1)
        
        # Change color based on value
        def update_color(mob):
            value = value_tracker.get_value()
            if value < 2:
                mob.set_color(RED)
            elif value < 4:
                mob.set_color(YELLOW)
            else:
                mob.set_color(GREEN)
        
        bar.add_updater(update_color)
        self.add(bar)
        
        self.play(value_tracker.animate.set_value(0), run_time=3)
        self.wait(1)
        
        # Remove updaters
        number.clear_updaters()
        bar.clear_updaters()
        self.wait(1)
        
        # Third part - Keyboard input
        # Demonstrate keyboard input handling (conceptual)
        title2 = Text("Keyboard Input Example", font_size=36)
        self.play(Transform(title, title2))
        self.wait(1)
        
        # Create text input visualization
        input_box = Rectangle(height=1, width=6, color=WHITE)
        input_text = Text("Press keys to type...", font_size=24).move_to(input_box)
        input_group = VGroup(input_box, input_text)
        input_group.shift(UP)
        
        self.play(Create(input_box), Write(input_text))
        self.wait(1)
        
        # Simulate typing
        typed_text = Text("Hello Manim!", font_size=24).move_to(input_box)
        self.play(Transform(input_text, typed_text))
        self.wait(1)
        
        # Show key press visualization
        key_a = Rectangle(height=0.8, width=0.8, color=YELLOW, fill_opacity=0.5)
        key_a_text = Text("A", font_size=24).move_to(key_a)
        key_a_group = VGroup(key_a, key_a_text)
        key_a_group.shift(DOWN * 2)
        
        self.play(Create(key_a_group))
        self.play(key_a_group.animate.set_fill(YELLOW, opacity=1))
        self.wait(0.5)
        self.play(key_a_group.animate.set_fill(YELLOW, opacity=0.5))
        self.wait(1)
        
        # Update text with new character
        new_text = Text("Hello Manim! A", font_size=24).move_to(input_box)
        self.play(Transform(input_text, new_text))
        self.wait(2)
        
        # Show how parameters could be adjusted
        self.play(
            input_box.animate.set_color(YELLOW),
            key_a_group.animate.set_color(GREEN),
            run_time=1
        )
        
        self.wait(2)
        
        # Final message
        final_text = Text("Try adjusting the widgets above!", font_size=30)
        final_text.next_to(explanation, DOWN, buff=1)
        self.play(Write(final_text))
        self.wait(2)
        
        # Fade out all objects
        self.play(FadeOut(title), FadeOut(explanation), FadeOut(input_box), 
                  FadeOut(input_text), FadeOut(key_a_group), FadeOut(number),
                  FadeOut(bar), FadeOut(final_text))
        self.wait(1)

# Example usage in a Jupyter notebook:
"""
# In a Jupyter notebook cell, you would run:

from manim_tutorials.advanced.05_interactive_scenes_interactive import interactive_scenes_demo

# Create the interactive controller
widgets_controller = interactive_scenes_demo()

# Then render the scene
%%manim -pql InteractiveScenesWithWidgets

from manim_tutorials.advanced.05_interactive_scenes_interactive import InteractiveScenesWithWidgets

class InteractiveScenesWithWidgets(InteractiveScenesWithWidgets):
    def construct(self):
        super().construct()
"""

if __name__ == "__main__":
    # This is just for testing the file can be imported
    print("Interactive Scenes with Widgets module loaded successfully")