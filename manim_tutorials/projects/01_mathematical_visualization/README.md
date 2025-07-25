# Mathematical Visualization Project

This project demonstrates how to visualize mathematical concepts and theorems using Manim.

## Prerequisites

Before running these scenes, ensure you have installed all required dependencies:

```bash
pip install -r ../../requirements.txt
```

This will install all necessary packages including Manim, Jupyter, and ipywidgets.

## Scenes

1. [Pythagorean Theorem](pythagorean_theorem.py) - Visual proof of the Pythagorean theorem
2. [Fourier Series](fourier_series.py) - Visualization of Fourier series approximation
3. [Derivatives](derivatives.py) - Visualizing the concept of derivatives
4. [Integration](integration.py) - Visualizing the concept of integration
5. [Complex Numbers](complex_numbers.py) - Visualizing complex number operations

## Usage

To run any of these scenes, use the following command:

```bash
manim -pql pythagorean_theorem.py PythagoreanTheorem
```

Replace `pythagorean_theorem.py` and `PythagoreanTheorem` with the appropriate file and class names.

## Scene Descriptions

### Pythagorean Theorem
A visual proof of the Pythagorean theorem showing how the areas of squares on the legs of a right triangle equal the area of the square on the hypotenuse.

### Fourier Series
An animation showing how complex waveforms can be approximated by summing simple sine and cosine waves.

### Derivatives
A visualization of the concept of derivatives as the slope of a tangent line to a curve at a point.

### Integration
A visualization of integration as the area under a curve, demonstrated through Riemann sums.

### Complex Numbers
An animation showing operations with complex numbers in the complex plane, including addition, multiplication, and exponentiation.