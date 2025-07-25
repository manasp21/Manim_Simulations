from manim import *

class BarCharts(Scene):
    def construct(self):
        # Set up the scene
        title = Text("Bar Charts", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # Sample data
        categories = ["A", "B", "C", "D", "E"]
        values = [20, 35, 30, 25, 15]
        max_value = max(values)
        
        # Create axes
        axes = Axes(
            x_range=[0, len(categories), 1],
            y_range=[0, max_value * 1.2, max_value // 5],
            axis_config={"color": WHITE},
            x_axis_config={"include_ticks": False},
            y_axis_config={"include_ticks": True},
        )
        axes.shift(LEFT * 2 + DOWN)
        
        # Create bars
        bars = VGroup()
        bar_labels = VGroup()
        value_labels = VGroup()
        
        bar_width = 0.6
        for i, (category, value) in enumerate(zip(categories, values)):
            # Create bar
            bar_height = value / max_value * 5  # Scale to fit
            bar = Rectangle(
                width=bar_width,
                height=bar_height,
                fill_color=BLUE,
                fill_opacity=0.7,
                stroke_color=WHITE
            )
            
            # Position bar
            bar.move_to(axes.c2p(i, 0), DOWN)
            
            # Create category label
            label = Text(category, font_size=20)
            label.next_to(bar, DOWN, buff=0.1)
            
            # Create value label
            value_label = Text(str(value), font_size=20)
            value_label.next_to(bar, UP, buff=0.1)
            
            bars.add(bar)
            bar_labels.add(label)
            value_labels.add(value_label)
        
        # Display axes
        self.play(Create(axes))
        self.wait(1)
        
        # Animate bars growing
        for bar in bars:
            self.play(
                bar.animate.stretch_to_fit_height(bar.height),
                run_time=0.5
            )
        
        # Display labels
        self.play(
            Write(bar_labels),
            Write(value_labels)
        )
        self.wait(2)
        
        # Show updating data
        new_values = [15, 40, 25, 30, 20]
        
        # Animate bar height changes
        for i, (bar, old_value, new_value) in enumerate(zip(bars, values, new_values)):
            new_height = new_value / max_value * 5
            new_value_label = Text(str(new_value), font_size=20)
            new_value_label.next_to(bar, UP, buff=0.1)
            
            self.play(
                bar.animate.stretch_to_fit_height(new_height),
                Transform(value_labels[i], new_value_label),
                run_time=1
            )
        
        self.wait(2)

class Histogram(Scene):
    def construct(self):
        # Set up the scene
        title = Text("Histogram", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # Sample continuous data
        import random
        random.seed(42)
        data = [random.gauss(50, 15) for _ in range(200)]
        
        # Create bins
        min_val, max_val = min(data), max(data)
        bin_width = (max_val - min_val) / 10
        bins = [min_val + i * bin_width for i in range(11)]
        
        # Calculate histogram
        hist_values = [0] * 10
        for value in data:
            bin_index = min(int((value - min_val) / bin_width), 9)
            hist_values[bin_index] += 1
        
        max_count = max(hist_values)
        
        # Create axes
        axes = Axes(
            x_range=[min_val, max_val, (max_val - min_val) / 5],
            y_range=[0, max_count * 1.2, max_count // 5],
            axis_config={"color": WHITE},
        )
        axes.shift(DOWN)
        
        # Create histogram bars
        bars = VGroup()
        for i, count in enumerate(hist_values):
            # Create bar
            bar_width = axes.c2p(bins[i+1], 0)[0] - axes.c2p(bins[i], 0)[0]
            bar_height = count / max_count * 5  # Scale to fit
            
            bar = Rectangle(
                width=bar_width * 0.8,  # Leave some space between bars
                height=bar_height,
                fill_color=GREEN,
                fill_opacity=0.7,
                stroke_color=WHITE
            )
            
            # Position bar
            bar_x = (bins[i] + bins[i+1]) / 2
            bar.move_to(axes.c2p(bar_x, 0), DOWN)
            
            bars.add(bar)
        
        # Display axes
        self.play(Create(axes))
        self.wait(1)
        
        # Animate bars growing
        for bar in bars:
            self.play(
                bar.animate.stretch_to_fit_height(bar.height),
                run_time=0.3
            )
        
        self.wait(2)
        
        # Add labels
        x_label = Text("Value", font_size=24)
        x_label.next_to(axes.x_axis, DOWN, buff=0.3)
        
        y_label = Text("Frequency", font_size=24)
        y_label.next_to(axes.y_axis, LEFT, buff=0.3).rotate(90 * DEGREES)
        
        self.play(Write(x_label), Write(y_label))
        self.wait(2)

class StackedBarChart(Scene):
    def construct(self):
        # Set up the scene
        title = Text("Stacked Bar Chart", font_size=48)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)
        
        # Sample data for multiple categories
        categories = ["Q1", "Q2", "Q3", "Q4"]
        series_data = {
            "Product A": [20, 25, 30, 35],
            "Product B": [15, 20, 25, 20],
            "Product C": [10, 15, 20, 25]
        }
        
        # Colors for each series
        colors = [RED, BLUE, GREEN]
        series_names = list(series_data.keys())
        
        # Calculate totals and max
        totals = [sum(values) for values in zip(*series_data.values())]
        max_total = max(totals)
        
        # Create axes
        axes = Axes(
            x_range=[0, len(categories), 1],
            y_range=[0, max_total * 1.2, max_total // 5],
            axis_config={"color": WHITE},
            x_axis_config={"include_ticks": False},
            y_axis_config={"include_ticks": True},
        )
        axes.shift(LEFT * 2 + DOWN)
        
        # Create stacked bars
        bar_groups = VGroup()
        bar_width = 0.6
        
        for i, category in enumerate(categories):
            bar_stack = VGroup()
            cumulative_height = 0
            
            for j, (series, color) in enumerate(zip(series_names, colors)):
                value = series_data[series][i]
                bar_height = value / max_total * 5  # Scale to fit
                
                bar = Rectangle(
                    width=bar_width,
                    height=bar_height,
                    fill_color=color,
                    fill_opacity=0.7,
                    stroke_color=WHITE
                )
                
                # Position bar on top of previous bar
                bar.move_to(axes.c2p(i, cumulative_height), DOWN)
                
                bar_stack.add(bar)
                cumulative_height += bar_height
            
            bar_groups.add(bar_stack)
        
        # Display axes
        self.play(Create(axes))
        self.wait(1)
        
        # Animate bars growing from bottom to top
        for bar_group in bar_groups:
            for bar in bar_group:
                self.play(
                    bar.animate.stretch_to_fit_height(bar.height),
                    run_time=0.3
                )
        
        # Add category labels
        category_labels = VGroup()
        for i, category in enumerate(categories):
            label = Text(category, font_size=20)
            label.next_to(bar_groups[i], DOWN, buff=0.1)
            category_labels.add(label)
        
        self.play(Write(category_labels))
        self.wait(1)
        
        # Add legend
        legend = VGroup()
        for i, (series, color) in enumerate(zip(series_names, colors)):
            legend_item = VGroup(
                Rectangle(width=0.5, height=0.5, fill_color=color, fill_opacity=0.7),
                Text(series, font_size=20)
            )
            legend_item.arrange(RIGHT, buff=0.2)
            legend.add(legend_item)
        
        legend.arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        legend.to_edge(RIGHT).shift(UP)
        
        legend_title = Text("Legend", font_size=24)
        legend_title.next_to(legend, UP, buff=0.3)
        
        self.play(Write(legend_title))
        self.play(Write(legend))
        self.wait(3)