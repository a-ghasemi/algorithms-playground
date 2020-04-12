import sympy as sp

x = sp.Symbol("x")
y = sp.Symbol("y")

print(sp.solve(x ** 4 - 1, x))

print(sp.solve([x + 5 * y - 2, -3 * x + 6 * y - 15], [x, y]))