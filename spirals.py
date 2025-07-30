import numpy as np
import matplotlib.pyplot as plt

def generate_julia(width, height, max_iter, c):
    # Define the bounds for the Julia set (adjusted for full view with spirals)
    xmin, xmax = -1.5, 1.5
    ymin, ymax = -1.5 * (height / width), 1.5 * (height / width)  # Maintain aspect ratio
    
    # Create the grid of complex numbers (z starts here)
    real = np.linspace(xmin, xmax, width)
    imag = np.linspace(ymin, ymax, height)
    z = real[np.newaxis, :] + imag[:, np.newaxis] * 1j
    
    # Initialize divergence iteration array
    divergence_iter = np.full(z.shape, max_iter)
    
    # Iterate to compute the Julia set
    for i in range(max_iter):
        z = z ** 2 + c
        diverged = (np.abs(z) > 2) & (divergence_iter == max_iter)
        divergence_iter[diverged] = i
        z[divergence_iter != max_iter] = 2  # Cap to prevent overflow
    
    return divergence_iter

# Set resolution (16:10 aspect ratio, high quality for wallpaper)
width = 1512
height = 982
max_iter = 20000  # High iteration count for detail

# Choose a c value that produces spiral patterns in the Julia set
# c = -0.123 + 0.745j  # Known for spiral structures
# Alternative: c = 0.285 + 0.01j for different spirals
# Or c = -0.8 + 0.156j for more twisted spirals
c = -0.123 + 0.745j

# Compute the fractal
fractal = generate_julia(width, height, max_iter, c)

# Save the image in greyscale (black for set, gradient to white for exterior)
plt.imsave('spiral_julia_fractal.png', fractal, cmap='gray')

# Optionally display the image (comment out if not needed)
# plt.imshow(fractal, cmap='gray', origin='lower')
# plt.axis('off')
# plt.show()

print("Spiral fractal image saved as 'spiral_julia_fractal.png'")