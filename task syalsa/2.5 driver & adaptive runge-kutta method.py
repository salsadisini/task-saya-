import numpy as np

# Example Problem: dy/dx = -y
def derivs(x, y):
    dy = np.zeros_like(y)
    dy[0] = -y[0]  # Replace with the actual derivative for dy1/dx
    return dy

# (b) Adaptive Step Routine
def adapt(x, y, htry, yscal, eps):
    safety = 0.9
    econ = 1.89e-4
    h = htry

    while True:
        ytemp, yerr = rkkc(y, x, h)
        
        # Avoid division by zero by checking if yscal is not zero
        if np.any(yscal == 0):
            emax = 0
        else:
            emax = np.abs(yerr / yscal / eps).max()

        if emax <= 1:
            break

        htemp = safety * h * emax**(-0.25)
        h = max(np.abs(htemp), 0.25 * np.abs(h))

    if emax > econ:
        hnxt = safety * emax**(-0.2) * h
    else:
        hnxt = 4.0 * h

    xnew = x + h
    return xnew, hnxt, ytemp

# (c) Runge-Kutta Cash-Karp Method
def rkkc(y, x, h):
    a2, a3, a4, a5, a6 = 0.2, 0.3, 0.6, 1.0, 0.875
    b21, b31, b32, b41, b42, b43, b51, b52, b53, b54 = 0.2, 0.075, 0.225, \
                                                        0.3, -0.9, 1.2,  \
                                                        -11.0 / 54.0, 2.5, -70.0 / 27.0, 35.0 / 27.0
    b61, b62, b63, b64, b65 = 1631.0 / 55296.0, 175.0 / 512.0, 575.0 / 13824.0, \
                              44275.0 / 110592.0, 253.0 / 4096.0
    c1, c3, c4, c6 = 37.0 / 378.0, 250.0 / 621.0, 125.0 / 594.0, 512.0 / 1771.0
    c2, c5 = 0.0, 277.0 / 14336.0

    k1 = h * derivs(x, y)
    k2 = h * derivs(x + a2 * h, y + b21 * k1)
    k3 = h * derivs(x + a3 * h, y + b31 * k1 + b32 * k2)
    k4 = h * derivs(x + a4 * h, y + b41 * k1 + b42 * k2 + b43 * k3)
    k5 = h * derivs(x + a5 * h, y + b51 * k1 + b52 * k2 + b53 * k3 + b54 * k4)
    k6 = h * derivs(x + a6 * h, y + b61 * k1 + b62 * k2 + b63 * k3 + b64 * k4 + b65 * k5)

    ytemp = y + c1 * k1 + c3 * k3 + c4 * k4 + c6 * k6
    yerr = c1 * k1 + c3 * (k3 - k4) + c4 * (k4 - k5) + c6 * (k6 - k5)

    return ytemp, yerr

# (a) Driver Program
def main():
    xi = 0.0
    xf = 0.4
    yi = np.array([0.0])  # Initial value for the dependent variable
    maxstep = 100
    hi = 0.5
    tiny = 1.0e-30
    eps = 0.00005

    print(xi, yi)
    x = xi
    y = yi
    h = hi
    istep = 0

    while True:
        if istep >= maxstep and x >= xf:
            break

        istep += 1
        yscal = np.abs(y) * np.abs(h * derivs(x, y)) * tiny

        if x + h > xf:
            h = xf - x

        adapt_result = adapt(x, y, h, yscal, eps)
        x, hnxt, y = adapt_result

        print(x, y)

    print("Done.")

# Call the main function to start the integration process
main()