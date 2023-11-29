import numpy as np

# Example Problem: dy1/dx = y1, dy2/dx = y2
def derivs(x, y, dy):
    dy[0] = y[0]  # Replace with the actual derivative for dy1/dx
    dy[1] = y[1]  # Replace with the actual derivative for dy2/dx

# (b) Routine to Take One Output Step
def integrator(x, y, n, h, xend):
    while x < xend:
        if xend - x < h:
            h = xend - x
        rk4(x, y, n, h)
        x += h

# (c) Fourth-Order RK Method for a System of ODEs
def rk4(x, y, n, h):
    k1 = np.zeros(n)
    k2 = np.zeros(n)
    k3 = np.zeros(n)
    k4 = np.zeros(n)

    derivs(x, y, k1)
    ym = y + k1 * h / 2

    derivs(x + h / 2, ym, k2)
    ym = y + k2 * h / 2

    derivs(x + h / 2, ym, k3)
    ye = y + k3 * h

    derivs(x + h, ye, k4)

    for i in range(n):
        slope = (k1[i] + 2 * (k2[i] + k3[i]) + k4[i]) / 6
        y[i] += slope * h

# (a) Main or “Driver” Program
def main():
    n = 2  # number of equations
    yi = np.array([1.0, 0.0])  # initial values of n dependent variables
    xi = 0.0  # initial value independent variable
    xf = 1.0  # final value independent variable
    dx = 0.1  # calculation step size
    xout = 0.1  # output interval

    x = xi
    m = 0
    xpm = x

    # Store the values for each dependent variable
    ypm = yi.copy()

    while True:
        xend = x + xout
        if xend > xf:
            xend = xf
        h = dx
        integrator(x, yi, n, h, xend)
        m += 1
        xpm = x
        ypm = yi.copy()
        if x >= xf:
            break

    # Display results
    print("Results:", xpm, ypm)

# Call the main function to start the integration process
main()