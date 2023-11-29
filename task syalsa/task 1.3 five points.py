import numpy as np

def five_point_stencil_derivative(x, y):
    n = len(x)
    h = x[1] - x[0]  # Assuming equally spaced points

    dy_dx = np.zeros_like(y, dtype=float)

    if n < 5:
        print("Insufficient points for the five-point stencil method.")
        return dy_dx

    for i in range(2, n - 2):
        dy_dx[i] = (y[i - 2] - 8 * y[i - 1] + 8 * y[i + 1] - y[i + 2]) / (12 * h)

    # Use forward/backward differences for the first and last two points
    dy_dx[0] = (-25 * y[0] + 48 * y[1] - 36 * y[2] + 16 * y[3] - 3 * y[4]) / (12 * h)
    dy_dx[1] = (-3 * y[0] - 10 * y[1] + 18 * y[2] - 6 * y[3] + y[4]) / (12 * h)

    dy_dx[-2] = (-y[-5] + 6 * y[-4] - 18 * y[-3] + 10 * y[-2] + 3 * y[-1]) / (12 * h)
    dy_dx[-1] = (3 * y[-5] - 16 * y[-4] + 36 * y[-3] - 48 * y[-2] + 25 * y[-1]) / (12 * h)

    return dy_dx

# Given data
x = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
y = np.array([-1.709847, -1.373823, -1.119214, -0.9160143, -0.6015966])

# Calculate the derivative using the five-point stencil method
dy_dx = five_point_stencil_derivative(x, y)

# Print the result
print("Numerical Derivative:")
for i in range(len(x)):
    print(f"At x = {x[i]}, dy/dx = {dy_dx[i]}")