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
    c = np.full(z.shape, c)  # Broadcast c to the grid
    
    # Initialize divergence array as float for smooth coloring
    divergence = np.zeros(z.shape, dtype=float)
    
    # Mask for points still iterating
    mask = np.ones(z.shape, dtype=bool)
    
    # Escape radius for smoother coloring (larger than 2 to avoid overflow and improve smoothing)
    escape_r = 100.0
    
    for i in range(max_iter):
        z[mask] = z[mask] ** 2 + c[mask]
        newly_diverged = (np.abs(z[mask]) > escape_r)
        if newly_diverged.any():
            abs_z = np.abs(z[mask][newly_diverged])
            # Smooth escape time formula
            nu = i + 1 - np.log(np.log(abs_z) / np.log(escape_r)) / np.log(2)
            divergence[mask][newly_diverged] = nu
            mask[mask] &= ~newly_diverged  # Update mask
        
        if not mask.any():
            break
    
    # Points that didn't diverge (inside the set) set to 0 (black)
    divergence[mask] = 0
    
    return divergence

# Set resolution (16:10 aspect ratio, high quality for wallpaper)
width = 1920
height = 1200
max_iter = 2000  # High iteration count for detail

# Choose a c value that produces prominent spiral patterns (Siegel disk with spirals)
c = complex(-0.726895347438, 0.188887129043)

# Compute the fractal
fractal = generate_julia(width, height, max_iter, c)

# Save the image with a colorful colormap (plasma for vibrant gradients)
plt.imsave('colorful_spiral_fractal.png', fractal, cmap='plasma')

# Optionally display the image (comment out if not needed)
# plt.imshow(fractal, cmap='plasma', origin='lower')
# plt.axis('off')
# plt.show()

print("Colorful spiral fractal image saved as 'colorful_spiral_fractal.png'")