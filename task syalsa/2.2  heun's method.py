import numpy as np

# Example Problem: dy/dx = y
def derivs(x, y):
    return y

# (a) Simple Heun without Corrector
def heun(x, y, h):
    dy1dx = derivs(x, y)
    ye = y + dy1dx * h
    dy2dx = derivs(x + h, ye)
    slope = (dy1dx + dy2dx) / 2
    ynew = y + slope * h
    xnew = x + h
    return xnew, ynew

# (b) Midpoint Method
def midpoint(x, y, h):
    dydx = derivs(x, y)
    ym = y + dydx * h / 2
    dymdx = derivs(x + h / 2, ym)
    ynew = y + dymdx * h
    xnew = x + h
    return xnew, ynew

# (c) Heun with Corrector
def heun_with_corrector(x, y, h):
    es = 0.01
    maxit = 20
    dy1dx = derivs(x, y)
    ye = y + dy1dx * h
    iter = 0

    while True:
        yeold = ye
        dy2dx = derivs(x + h, ye)
        slope = (dy1dx + dy2dx) / 2
        ye = y + slope * h
        iter += 1

        ea = np.abs((ye - yeold) / ye) * 100
        if ea < es or iter >= maxit:
            break

    ynew = ye
    xnew = x + h
    return xnew, ynew

# Solve the example problem using each method
x_initial = 0.0
y_initial = 1.0
step_size = 0.2

# (a) Simple Heun without Corrector
x_heun, y_heun = heun(x_initial, y_initial, step_size)
print(f"Heun without Corrector: x = {x_heun}, y = {y_heun}")

# (b) Midpoint Method
x_midpoint, y_midpoint = midpoint(x_initial, y_initial, step_size)
print(f"Midpoint Method: x = {x_midpoint}, y = {y_midpoint}")

# (c) Heun with Corrector
x_heun_corrector, y_heun_corrector = heun_with_corrector(x_initial, y_initial, step_size)
print(f"Heun with Corrector: x = {x_heun_corrector}, y = {y_heun_corrector}")