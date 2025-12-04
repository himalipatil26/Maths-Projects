import cmath
import matplotlib.pyplot as plt
import numpy as np

print("=== Quadratic Equation Solver ===")

# Input coefficients
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

# Discriminant
D = b**2 - 4*a*c
print(f"\nDiscriminant (D) = {D}")

# Explain discriminant
if D > 0:
    print("D > 0 → Two distinct real roots.")
elif D == 0:
    print("D = 0 → One real repeated root.")
else:
    print("D < 0 → Two complex roots.")

# Roots using quadratic formula
root1 = (-b + cmath.sqrt(D)) / (2*a)
root2 = (-b - cmath.sqrt(D)) / (2*a)

print(f"\nRoot 1 = {root1}")
print(f"Root 2 = {root2}")

# Plotting the parabola
x = np.linspace(-10, 10, 400)
y = a*x**2 + b*x + c

plt.plot(x, y)
plt.axhline(0)  # x-axis
plt.axvline(0)  # y-axis
plt.title("Quadratic Function Plot")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)

# Mark roots on graph if real
if D >= 0:
    plt.scatter([root1.real, root2.real], [0, 0])
    plt.text(root1.real, 0, f"{root1.real:.2f}")
    plt.text(root2.real, 0, f"{root2.real:.2f}")

plt.show()
