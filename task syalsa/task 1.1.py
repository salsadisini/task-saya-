import numpy as np

def backward_difference(x, y):
    n = len(x)
    h = x[1] - x[0]  # Assuming x values are equally spaced
    
    # Initialize the differences array with zeros
    dy_dx = np.zeros_like(y)
    
    # Calculate backward differences
    for i in range(1, n):
        dy_dx[i] = (y[i] - y[i-1]) / h
    
    return dy_dx

# Given data
x = np.array([0.0, 0.2, 0.4])
y = np.array([0.0000, 0.7140, 1.3718])

# Calculate backward differences
result = backward_difference(x, y)

# Print the result
print("Backward Differences:", result)