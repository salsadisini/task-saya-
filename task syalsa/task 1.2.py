import numpy as np

def three_point_stencil_derivative(x, y):
    n = len(x)
    h = x[1] - x[0]  # Assuming equally spaced points

    dy_dx = np.zeros_like(y, dtype=float)

    if n < 3:
        print("Insufficient points for the three-point stencil method.")
        return dy_dx

    # Use forward/backward differences for the first and last points
    dy_dx[0] = (y[1] - y[0]) / h
    dy_dx[1:-1] = (y[2:] - y[:-2]) / (2 * h)
    dy_dx[-1] = (y[-1] - y[-2]) / h

    return dy_dx

# Given data
x = np.array([1.1, 1.2, 1.3, 1.4])
y = np.array([9.025013, 11.02318, 13.46374, 16.44465])

# Calculate the derivative using the three-point stencil method
dy_dx = three_point_stencil_derivative(x, y)

# Print the result
print("Numerical Derivative:")
for i in range(len(x)):
    print(f"At x = {x[i]}, dy/dx = {dy_dx[i]}")