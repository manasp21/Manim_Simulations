# Text and LaTeX Issues

This guide addresses common text rendering and LaTeX issues in Manim and their solutions.

## Problem: Text Not Rendering or Appearing Garbled

### Description
Text objects don't appear, appear as boxes, or render incorrectly.

### Common Causes
1. Missing LaTeX dependencies
2. Incorrect text class usage
3. Font issues
4. Encoding problems

### Solutions

#### Solution 1: Install Required LaTeX Packages
```bash
# On Ubuntu/Debian
sudo apt update
sudo apt install texlive texlive-latex-extra texlive-fonts-extra texlive-latex-recommended texlive-science tipa

# On macOS with Homebrew
brew install --cask mactex

# On Windows
# Install MiKTeX or TeX Live
```

#### Solution 2: Use Correct Text Classes
```python
from manim import *

class CorrectTextUsage(Scene):
    def construct(self):
        # For simple text
        simple_text = Text("Hello World")
        
        # For mathematical expressions
        math_text = MathTex(r"\int_0^\infty e^{-x^2} dx = \frac{\sqrt{\pi}}{2}")
        
        # For LaTeX with more control
        latex_text = Tex(r"\LaTeX\ is \textbf{powerful}")
        
        self.play(Write(simple_text))
        self.wait(1)
        self.play(Write(math_text))
        self.wait(1)
        self.play(Write(latex_text))
```

#### Solution 3: Handle Special Characters
```python
class SpecialCharacters(Scene):
    def construct(self):
        # Use raw strings for backslashes
        text1 = Text(r"Use raw strings for \ and $")
        
        # Escape special characters when needed
        text2 = Text("Percent: 100\\%")
        
        # For LaTeX, use proper syntax
        latex1 = Tex(r"Special chars: \$ \& \# \%")
        
        self.play(Write(text1))
        self.play(Write(text2))
        self.play(Write(latex1))
```

## Problem: LaTeX Compilation Errors

### Description
Errors like "LaTeX compilation error" or "dvisvgm failed" during text rendering.

### Common Causes
1. Incomplete LaTeX installation
2. Incorrect LaTeX syntax
3. Missing LaTeX packages
4. Path issues with LaTeX executables

### Solutions

#### Solution 1: Verify LaTeX Installation
```bash
# Check if LaTeX is installed
latex --version
dvisvgm --version

# If not found, install full LaTeX distribution
# Ubuntu/Debian
sudo apt install texlive-full

# macOS
brew install --cask mactex

# Windows
# Download and install MiKTeX or TeX Live
```

#### Solution 2: Fix LaTeX Syntax
```python
class CorrectLaTeX(Scene):
    def construct(self):
        # Correct LaTeX syntax
        correct1 = MathTex(r"\int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}")
        
        # Use braces for multi-character subscripts/superscripts
        correct2 = MathTex(r"x^{2\alpha + 3\beta}")
        
        # Proper fraction syntax
        correct3 = MathTex(r"\frac{a + b}{c + d}")
        
        # Use \text for text within math mode
        correct4 = MathTex(r"\text{Probability} = \frac{\text{Favorable outcomes}}{\text{Total outcomes}}")
        
        self.play(Write(correct1))
        self.play(Write(correct2))
        self.play(Write(correct3))
        self.play(Write(correct4))
```

#### Solution 3: Add Missing Packages
```python
class CustomLaTeX(Scene):
    def construct(self):
        # If you need special packages, add them to the template
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{amssymb}")
        
        text = Tex(r"$\mathbb{R}$ is the set of real numbers", tex_template=myTemplate)
        
        self.play(Write(text))
```

## Problem: Font Issues

### Description
Text renders with wrong fonts, missing characters, or font warnings.

### Solutions

#### Solution 1: Specify Fonts
```python
class FontSpecification(Scene):
    def construct(self):
        # Use specific fonts
        text1 = Text("Hello World", font="Arial")
        text2 = Text("Hello World", font="Times New Roman")
        text3 = Text("Hello World", font="Courier New")
        
        # For system fonts, make sure they're installed
        text1.shift(UP)
        text3.shift(DOWN)
        
        self.play(Write(text1))
        self.play(Write(text2))
        self.play(Write(text3))
```

#### Solution 2: List Available Fonts
```python
# To see available fonts, you can use:
import manimpango
print(manimpango.list_fonts())
```

#### Solution 3: Use Font Weights
```python
class FontWeights(Scene):
    def construct(self):
        # Use different font weights
        normal = Text("Normal Text")
        bold = Text("Bold Text", weight="BOLD")
        italic = Text("Italic Text", slant="ITALIC")
        
        bold.shift(UP)
        italic.shift(DOWN)
        
        self.play(Write(normal))
        self.play(Write(bold))
        self.play(Write(italic))
```

## Problem: Text Alignment and Positioning Issues

### Description
Text doesn't align properly, overlaps, or is positioned incorrectly.

### Solutions

#### Solution 1: Proper Text Alignment
```python
class TextAlignment(Scene):
    def construct(self):
        # Create multiple text objects
        text1 = Text("Left aligned").to_edge(LEFT)
        text2 = Text("Centered").move_to(ORIGIN)
        text3 = Text("Right aligned").to_edge(RIGHT)
        
        # For vertical alignment
        text4 = Text("Top").to_edge(UP)
        text5 = Text("Middle").move_to(ORIGIN)
        text6 = Text("Bottom").to_edge(DOWN)
        
        self.play(Write(text1))
        self.play(Write(text2))
        self.play(Write(text3))
```

#### Solution 2: Text Spacing and Buffers
```python
class TextSpacing(Scene):
    def construct(self):
        # Use buff parameter for spacing
        texts = VGroup(
            Text("Line 1"),
            Text("Line 2"),
            Text("Line 3")
        )
        texts.arrange(DOWN, buff=0.5)  # 0.5 units between lines
        
        self.play(Write(texts))
        
        # For text within equations
        equation = MathTex(
            "a^2", "+", "b^2", "=", "c^2"
        )
        # Add spacing between elements
        equation.arrange(buff=0.2)
        
        self.play(Write(equation))
```

## Problem: Text Color and Styling Issues

### Description
Text colors don't apply correctly or styling is inconsistent.

### Solutions

#### Solution 1: Apply Colors Correctly
```python
class TextColors(Scene):
    def construct(self):
        # Apply color to entire text
        text1 = Text("Red Text", color=RED)
        
        # Apply color to parts of MathTex
        text2 = MathTex(
            r"\text{Red}", r"+", r"\text{Blue}",
            color=RED
        )
        text2[2].set_color(BLUE)  # Color specific parts
        
        # Use \textcolor in LaTeX
        text3 = Tex(r"\textcolor{GREEN}{Green Text}")
        
        text1.shift(UP)
        text3.shift(DOWN)
        
        self.play(Write(text1))
        self.play(Write(text2))
        self.play(Write(text3))
```

#### Solution 2: Gradient Colors
```python
class GradientText(Scene):
    def construct(self):
        # Create text with gradient
        text = Text("Gradient Text")
        text.set_color_by_gradient(RED, YELLOW, GREEN, BLUE, PURPLE)
        
        self.play(Write(text))
```

## Problem: Text Scaling Issues

### Description
Text appears too small, too large, or doesn't scale properly.

### Solutions

#### Solution 1: Use Font Size Parameters
```python
class TextScaling(Scene):
    def construct(self):
        # Different font sizes
        small = Text("Small Text", font_size=24)
        normal = Text("Normal Text", font_size=48)  # Default
        large = Text("Large Text", font_size=72)
        
        small.shift(UP)
        large.shift(DOWN)
        
        self.play(Write(small))
        self.play(Write(normal))
        self.play(Write(large))
```

#### Solution 2: Scale Text Objects
```python
class ScaleText(Scene):
    def construct(self):
        text = Text("Scaling Text")
        
        self.play(Write(text))
        
        # Scale the text
        self.play(text.animate.scale(2))  # Double size
        
        # Scale to specific width
        self.play(text.animate.scale_to_fit_width(5))
```

## Problem: Multilingual Text Issues

### Description
Non-English characters don't render correctly or cause errors.

### Solutions

#### Solution 1: Use Proper Encoding
```python
class MultilingualText(Scene):
    def construct(self):
        # UTF-8 encoding is usually sufficient
        english = Text("Hello World")
        spanish = Text("Hola Mundo")
        french = Text("Bonjour le Monde")
        german = Text("Hallo Welt")
        
        # For Asian languages, ensure proper fonts
        # chinese = Text("你好世界", font="Noto Sans CJK SC")
        # japanese = Text("こんにちは世界", font="Noto Sans CJK JP")
        # korean = Text("안녕하세요 세계", font="Noto Sans CJK KR")
        
        texts = VGroup(english, spanish, french, german)
        texts.arrange(DOWN, buff=0.3)
        
        for text in texts:
            self.play(Write(text))
            self.wait(0.5)
```

#### Solution 2: Configure for Specific Languages
```python
class LanguageSpecific(Scene):
    def construct(self):
        # For Arabic, you might need special handling
        # arabic = Text("مرحبا بالعالم", font="Arial")
        
        # For mathematical text in different languages
        math_in_english = MathTex(r"\text{Sum} = \sum_{i=1}^{n} i")
        # math_in_spanish = MathTex(r"\text{Suma} = \sum_{i=1}^{n} i")
        
        self.play(Write(math_in_english))
```

## Problem: Text Performance Issues

### Description
Scenes with lots of text render slowly or consume excessive memory.

### Solutions

#### Solution 1: Optimize Text Usage
```python
class OptimizedText(Scene):
    def construct(self):
        # Instead of many individual Text objects
        # lines = [Text(f"Line {i}") for i in range(100)]  # Inefficient
        
        # Use fewer, larger Text objects
        paragraphs = [
            Text(" ".join([f"Word{j}" for j in range(10)]))
            for i in range(10)
        ]
        
        text_group = VGroup(*paragraphs)
        text_group.arrange(DOWN, buff=0.3)
        
        self.play(Write(text_group))
```

#### Solution 2: Use MarkupText for Rich Text
```python
class RichText(Scene):
    def construct(self):
        # Use MarkupText for styling within a single object
        rich_text = MarkupText(
            f'''
            <span fgcolor="{RED}">Red text</span>
            <span fgcolor="{BLUE}">Blue text</span>
            <b>Bold text</b>
            <i>Italic text</i>
            ''',
            font_size=36
        )
        
        self.play(Write(rich_text))
```

## Prevention Tips

1. **Install full LaTeX distribution** during setup
2. **Test text rendering** early in development
3. **Use raw strings** for LaTeX expressions
4. **Verify font availability** on target systems
5. **Keep text objects reasonable** in size and number
6. **Use appropriate text classes** (Text, Tex, MathTex)

## Debugging Text Issues

### 1. Enable Verbose Output
```bash
# Run with verbose output to see LaTeX errors
manim -v DEBUG scene.py MyScene
```

### 2. Check Temporary Files
```python
# In your scene, you can check where temporary files are created
from manim import config
print(f"Temporary directory: {config['text_dir']}")
```

### 3. Test Simple Cases First
```python
class DebugText(Scene):
    def construct(self):
        # Start with simple text
        simple = Text("Test")
        self.play(Write(simple))
        
        # Then try more complex text
        # complex = MathTex(r"\int_0^\infty")
        # self.play(Write(complex))
```

## Additional Resources

- [Manim Text Documentation](https://docs.manim.community/en/stable/tutorials/using_text.html)
- [LaTeX Mathematical Expressions](https://en.wikibooks.org/wiki/LaTeX/Mathematics)
- [Pango Markup Documentation](https://docs.gtk.org/Pango/pango_markup.html)
- [Font Configuration Guide](https://docs.manim.community/en/stable/guides/configuration.html#fonts)