

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange
from scipy.interpolate import BarycentricInterpolator

# Define data points
tegangan = np.array([5, 10, 15, 20, 25, 30, 35, 40])
waktu_patah = np.array([40, 30, 25, 40, 18, 20, 22, 15])

# Perform Lagrange interpolation
poly_lagrange = lagrange(tegangan, waktu_patah)

# Perform Newton interpolation
poly_newton = BarycentricInterpolator(tegangan, waktu_patah)

# Generate points for plotting
x_range = np.linspace(5, 40, 400)

# Calculate interpolated values
y_lagrange = poly_lagrange(x_range)
y_newton = poly_newton(x_range)

# Plotting
plt.figure(figsize=(10, 6))

# Scatter plot for data points
plt.scatter(tegangan, waktu_patah, label='Data', color='red', marker='o', s=80, edgecolors='black', zorder=3)

# Plot Lagrange interpolation
plt.plot(x_range, y_lagrange, color='blue', label='Interpolasi Lagrange')

# Plot Newton interpolation with dashed line
plt.plot(x_range, y_newton, '--', color='black', label='Interpolasi Newton')

# Set labels and title
plt.xlabel('Tegangan', fontsize=14)
plt.ylabel('Waktu Patah', fontsize=14)
plt.title('Interpolasi Polinomial Lagrange dan Newton', fontsize=16)

# Add legend with shadow and adjust its position
plt.legend(loc='upper right', shadow=True)

# Add gridlines
plt.grid(True)

# Tight layout to prevent overlapping
plt.tight_layout()

# Show plot
plt.show()
