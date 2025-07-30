import numpy as np
import matplotlib.pyplot as plt

def generate_mandelbrot(width, height, max_iter):
    # Define the bounds for the Mandelbrot set to fit 16:10 aspect ratio
    # Vertical span: 2.4 (from -1.2 to 1.2)
    # Horizontal span: 2.4 * 1.6 = 3.84, centered around -0.5 on real axis
    xmin = -2.42
    xmax = 1.42
    ymin = -1.2
    ymax = 1.2
    
    # Create the grid of complex numbers
    real = np.linspace(xmin, xmax, width)
    imag = np.linspace(ymin, ymax, height)
    c = real[np.newaxis, :] + imag[:, np.newaxis] * 1j
    
    # Initialize arrays
    z = np.zeros_like(c)
    divergence_iter = np.full(c.shape, max_iter)
    
    # Iterate to compute the Mandelbrot set
    for i in range(max_iter):
        z = z ** 2 + c
        diverged = (np.abs(z) > 2) & (divergence_iter == max_iter)
        divergence_iter[diverged] = i
        z[diverged] = 2  # Cap to prevent overflow in further iterations
    
    return divergence_iter

# Set resolution (16:10 aspect ratio, high quality)
width = 1920
height = 1200
max_iter = 20000  # High iteration count for detail and quality

# Compute the fractal
fractal = generate_mandelbrot(width, height, max_iter)

# Save the image in greyscale (Mandelbrot set in black, exterior gradient to white)
plt.imsave('mandelbrot_fractal.png', fractal, cmap='gray')

# Optionally display the image (comment out if not needed)
# plt.imshow(fractal, cmap='gray', origin='lower')
# plt.axis('off')
# plt.show()

print("Fractal image saved as 'mandelbrot_fractal.png'")