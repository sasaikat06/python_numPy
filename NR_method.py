import sympy as sp
import math

x = sp.symbols("x")
f = x**3 - 5*x +3

x0 = sp.pi
tolerance = 1e-2
maxIteration = 20
iteration = 0
oldX0 = x0

for iteration in range(maxIteration):
    xn = x0 - (f.subs(x,x0)/(sp.diff(f,x).subs(x,x0)))
    abs_x = abs(xn - x0)
    iteration += 1
    if abs_x <= tolerance:

        printing = "approximate root is : "
        print(f"{printing} {xn:.5f}")
        break
#    subsFunc = f.subs(x,x0)
#    print({f'Iteration = {iteration} , x0 = {x0:.5f}, fun = {subsFunc:.5f} xn = {xn:.5f}'})
 #   iteration += 1
    
    x0 = xn
print(xn)
#with open("numeric.txt", "a+") as file:
#    data = file.write(f"For the function f(x) = {f},\n for the initial value x0 = {oldX0:.5f},\n the root approximation is {xn:.5f}\n \n")
