#!/usr/bin/env python3
"""
Mensuration Formula Book (Interactive)

Features:
- Choose a shape from a menu
- Shows formula(s) for Area, Perimeter, and Volume (if applicable)
- Allows user to enter dimensions or use example values
- Displays step-by-step example calculation
- Simple, clear, and easy to extend

Run: python mensuration_formula_book.py
"""

import math

# ---------- Utilities ----------

def fmt(x):
    try:
        if float(x).is_integer():
            return str(int(x))
        else:
            return f"{x:.4f}"
    except Exception:
        return str(x)


def get_positive(prompt):
    while True:
        try:
            val = float(input(prompt))
            if val <= 0:
                print("Please enter a positive number.")
                continue
            return val
        except ValueError:
            print("That's not a number — try again.")


def choose_example_or_input(example_fn, input_fn):
    print("\nChoose: \n1) Use example values\n2) Enter your own values")
    choice = input("Enter 1 or 2: ")
    if choice.strip() == "1":
        return example_fn()
    else:
        return input_fn()


# ---------- Shape handlers ----------

# Each handler returns a dict with keys: name, formulas (list of strings), results (dict), steps (list of strings)

# 2D shapes

def square():
    def example():
        a = 5
        return a
    def user_input():
        return get_positive("Enter side length: ")

    a = choose_example_or_input(lambda: example(), lambda: user_input())
    area = a * a
    perimeter = 4 * a
    steps = [f"Side a = {fmt(a)}",
             f"Area = a^2 = {fmt(a)}^2 = {fmt(area)}",
             f"Perimeter = 4a = 4*{fmt(a)} = {fmt(perimeter)}"]
    return {"name": "Square", "formulas": ["Area = a^2", "Perimeter = 4a"], "results": {"Area": area, "Perimeter": perimeter}, "steps": steps}


def rectangle():
    def example():
        return (8, 3)
    def user_input():
        l = get_positive("Enter length: ")
        w = get_positive("Enter width: ")
        return (l, w)

    l, w = choose_example_or_input(lambda: example(), lambda: user_input())
    area = l * w
    perimeter = 2 * (l + w)
    steps = [f"Length = {fmt(l)}, Width = {fmt(w)}",
             f"Area = l*w = {fmt(l)}*{fmt(w)} = {fmt(area)}",
             f"Perimeter = 2(l+w) = 2({fmt(l)}+{fmt(w)}) = {fmt(perimeter)}"]
    return {"name": "Rectangle", "formulas": ["Area = l*w", "Perimeter = 2(l + w)"], "results": {"Area": area, "Perimeter": perimeter}, "steps": steps}


def triangle():
    def example():
        return (3, 4, 5)  # right triangle
    def user_input():
        a = get_positive("Enter side a: ")
        b = get_positive("Enter side b: ")
        c = get_positive("Enter side c: ")
        return (a, b, c)

    a, b, c = choose_example_or_input(lambda: example(), lambda: user_input())
    s = (a + b + c) / 2
    area = math.sqrt(max(0, s * (s - a) * (s - b) * (s - c)))
    perimeter = a + b + c
    steps = [f"Sides = {fmt(a)}, {fmt(b)}, {fmt(c)}",
             f"Semi-perimeter s = (a+b+c)/2 = {fmt(s)}",
             f"Area (Heron's) = sqrt(s(s-a)(s-b)(s-c)) = {fmt(area)}",
             f"Perimeter = a+b+c = {fmt(perimeter)}"]
    return {"name": "Triangle", "formulas": ["Area (Heron) = sqrt(s(s-a)(s-b)(s-c)), s=(a+b+c)/2", "Perimeter = a+b+c"], "results": {"Area": area, "Perimeter": perimeter}, "steps": steps}


def circle():
    def example():
        return 7
    def user_input():
        return get_positive("Enter radius r: ")

    r = choose_example_or_input(lambda: example(), lambda: user_input())
    area = math.pi * r * r
    circumference = 2 * math.pi * r
    steps = [f"Radius r = {fmt(r)}",
             f"Area = πr^2 = π*{fmt(r)}^2 = {fmt(area)}",
             f"Circumference = 2πr = 2π*{fmt(r)} = {fmt(circumference)}"]
    return {"name": "Circle", "formulas": ["Area = πr^2", "Circumference = 2πr"], "results": {"Area": area, "Circumference": circumference}, "steps": steps}


def parallelogram():
    def example():
        return (6, 4)  # base, height
    def user_input():
        b = get_positive("Enter base b: ")
        h = get_positive("Enter height h: ")
        return (b, h)

    b, h = choose_example_or_input(lambda: example(), lambda: user_input())
    area = b * h
    # perimeter needs side length; ask for side
    side = get_positive("Enter side length (adjacent to base) for perimeter: ")
    perimeter = 2 * (b + side)
    steps = [f"Base = {fmt(b)}, Height = {fmt(h)}, Side = {fmt(side)}",
             f"Area = b*h = {fmt(b)}*{fmt(h)} = {fmt(area)}",
             f"Perimeter = 2(b+side) = 2({fmt(b)}+{fmt(side)}) = {fmt(perimeter)}"]
    return {"name": "Parallelogram", "formulas": ["Area = b*h", "Perimeter = 2(b + side)"] , "results": {"Area": area, "Perimeter": perimeter}, "steps": steps}


def trapezoid():
    def example():
        return (8, 5, 4)  # a, b, height
    def user_input():
        a = get_positive("Enter base a (parallel side 1): ")
        b = get_positive("Enter base b (parallel side 2): ")
        h = get_positive("Enter height h: ")
        return (a, b, h)

    a, b, h = choose_example_or_input(lambda: example(), lambda: user_input())
    area = ((a + b) / 2) * h
    # perimeter needs the non-parallel sides; ask user
    side1 = get_positive("Enter non-parallel side 1: ")
    side2 = get_positive("Enter non-parallel side 2: ")
    perimeter = a + b + side1 + side2
    steps = [f"Bases = {fmt(a)}, {fmt(b)}, Height = {fmt(h)}, Other sides = {fmt(side1)}, {fmt(side2)}",
             f"Area = ((a+b)/2)*h = (({fmt(a)}+{fmt(b)})/2)*{fmt(h)} = {fmt(area)}",
             f"Perimeter = a+b+side1+side2 = {fmt(perimeter)}"]
    return {"name": "Trapezoid", "formulas": ["Area = ((a+b)/2)*h", "Perimeter = a+b+side1+side2"], "results": {"Area": area, "Perimeter": perimeter}, "steps": steps}


def rhombus():
    def example():
        return (6, 8)  # diagonals
    def user_input():
        d1 = get_positive("Enter diagonal d1: ")
        d2 = get_positive("Enter diagonal d2: ")
        return (d1, d2)

    d1, d2 = choose_example_or_input(lambda: example(), lambda: user_input())
    area = (d1 * d2) / 2
    side = get_positive("Enter side length for perimeter: ")
    perimeter = 4 * side
    steps = [f"Diagonals = {fmt(d1)}, {fmt(d2)}, Side = {fmt(side)}",
             f"Area = (d1*d2)/2 = ({fmt(d1)}*{fmt(d2)})/2 = {fmt(area)}",
             f"Perimeter = 4*side = 4*{fmt(side)} = {fmt(perimeter)}"]
    return {"name": "Rhombus", "formulas": ["Area = (d1*d2)/2", "Perimeter = 4*side"], "results": {"Area": area, "Perimeter": perimeter}, "steps": steps}

# 3D shapes

def cube():
    def example():
        return 4
    def user_input():
        return get_positive("Enter side length a: ")

    a = choose_example_or_input(lambda: example(), lambda: user_input())
    volume = a**3
    surface_area = 6 * a**2
    steps = [f"Side a = {fmt(a)}",
             f"Volume = a^3 = {fmt(a)}^3 = {fmt(volume)}",
             f"Surface Area = 6a^2 = 6*{fmt(a)}^2 = {fmt(surface_area)}"]
    return {"name": "Cube", "formulas": ["Volume = a^3", "Surface Area = 6a^2"], "results": {"Volume": volume, "Surface Area": surface_area}, "steps": steps}


def cuboid():
    def example():
        return (5, 3, 2)
    def user_input():
        l = get_positive("Enter length l: ")
        w = get_positive("Enter width w: ")
        h = get_positive("Enter height h: ")
        return (l, w, h)

    l, w, h = choose_example_or_input(lambda: example(), lambda: user_input())
    volume = l * w * h
    surface_area = 2 * (l*w + w*h + h*l)
    steps = [f"l = {fmt(l)}, w = {fmt(w)}, h = {fmt(h)}",
             f"Volume = l*w*h = {fmt(volume)}",
             f"Surface Area = 2(lw+wh+hl) = {fmt(surface_area)}"]
    return {"name": "Cuboid", "formulas": ["Volume = l*w*h", "Surface Area = 2(lw + wh + hl)"], "results": {"Volume": volume, "Surface Area": surface_area}, "steps": steps}


def sphere():
    def example():
        return 3
    def user_input():
        return get_positive("Enter radius r: ")

    r = choose_example_or_input(lambda: example(), lambda: user_input())
    volume = (4/3) * math.pi * r**3
    surface_area = 4 * math.pi * r**2
    steps = [f"Radius r = {fmt(r)}",
             f"Volume = (4/3)πr^3 = (4/3)π*{fmt(r)}^3 = {fmt(volume)}",
             f"Surface Area = 4πr^2 = 4π*{fmt(r)}^2 = {fmt(surface_area)}"]
    return {"name": "Sphere", "formulas": ["Volume = (4/3)πr^3", "Surface Area = 4πr^2"], "results": {"Volume": volume, "Surface Area": surface_area}, "steps": steps}


def cylinder():
    def example():
        return (3, 5)  # r, h
    def user_input():
        r = get_positive("Enter radius r: ")
        h = get_positive("Enter height h: ")
        return (r, h)

    r, h = choose_example_or_input(lambda: example(), lambda: user_input())
    volume = math.pi * r**2 * h
    surface_area = 2 * math.pi * r * (r + h)  # total surface area
    steps = [f"r = {fmt(r)}, h = {fmt(h)}",
             f"Volume = πr^2h = π*{fmt(r)}^2*{fmt(h)} = {fmt(volume)}",
             f"Surface Area = 2πr(r+h) = {fmt(surface_area)}"]
    return {"name": "Cylinder", "formulas": ["Volume = πr^2h", "Surface Area = 2πr(r+h)"], "results": {"Volume": volume, "Surface Area": surface_area}, "steps": steps}


def cone():
    def example():
        return (3, 5)  # r, h
    def user_input():
        r = get_positive("Enter radius r: ")
        h = get_positive("Enter height h: ")
        return (r, h)

    r, h = choose_example_or_input(lambda: example(), lambda: user_input())
    l = math.sqrt(r*r + h*h)
    volume = (1/3) * math.pi * r**2 * h
    surface_area = math.pi * r * (r + l)  # total surface area
    steps = [f"r = {fmt(r)}, h = {fmt(h)}, slant height l = sqrt(r^2 + h^2) = {fmt(l)}",
             f"Volume = (1/3)πr^2h = {fmt(volume)}",
             f"Surface Area = πr(r+l) = {fmt(surface_area)}"]
    return {"name": "Cone", "formulas": ["Volume = (1/3)πr^2h", "Surface Area = πr(r + l), l = sqrt(r^2 + h^2)"], "results": {"Volume": volume, "Surface Area": surface_area}, "steps": steps}


def prism():
    # Generic right prism: base area given or choose triangle/rectangle
    def example():
        # triangular prism example
        base_area = (3*4)/2  # right triangle 3,4
        height = 10
        return (base_area, 10, 3+4+5)  # base_area, prism height, perimeter of base
    def user_input():
        print("For a prism you need: base area (A_base), perimeter of base (P_base), prism height (H)")
        A_base = get_positive("Enter base area A_base: ")
        P_base = get_positive("Enter base perimeter P_base: ")
        H = get_positive("Enter prism height H: ")
        return (A_base, H, P_base)

    A_base, H, P_base = choose_example_or_input(lambda: example(), lambda: user_input())
    volume = A_base * H
    surface_area = 2 * A_base + P_base * H
    steps = [f"Base area = {fmt(A_base)}, Base perimeter = {fmt(P_base)}, Prism height = {fmt(H)}",
             f"Volume = A_base * H = {fmt(volume)}",
             f"Surface Area = 2*A_base + P_base*H = {fmt(surface_area)}"]
    return {"name": "Prism (right)", "formulas": ["Volume = A_base * H", "Surface Area = 2*A_base + P_base*H"], "results": {"Volume": volume, "Surface Area": surface_area}, "steps": steps}

# Map menu keys to functions
SHAPES = {
    "1": ("Square", square),
    "2": ("Rectangle", rectangle),
    "3": ("Triangle", triangle),
    "4": ("Circle", circle),
    "5": ("Parallelogram", parallelogram),
    "6": ("Trapezoid", trapezoid),
    "7": ("Rhombus", rhombus),
    "8": ("Cube", cube),
    "9": ("Cuboid", cuboid),
    "10": ("Sphere", sphere),
    "11": ("Cylinder", cylinder),
    "12": ("Cone", cone),
    "13": ("Prism (right)", prism),
}


def print_menu():
    print("\n=== Mensuration Formula Book ===")
    for k, (name, _) in SHAPES.items():
        print(f"{k}. {name}")
    print("0. Exit")


def show_result(res):
    print(f"\n--- {res['name']} ---")
    print("Formulas:")
    for f in res['formulas']:
        print(" ", f)
    print("\nResults:")
    for key, val in res['results'].items():
        print(f" {key}: {fmt(val)}")
    print("\nExample / Steps:")
    for s in res['steps']:
        print(" -", s)


def main():
    while True:
        print_menu()
        choice = input("Choose a shape (number): ")
        if choice.strip() == "0":
            print("Goodbye — keep exploring geometry!")
            break
        if choice.strip() not in SHAPES:
            print("Invalid choice — try again.")
            continue
        _, fn = SHAPES[choice.strip()]
        try:
            res = fn()
            show_result(res)
        except Exception as e:
            print("An error occurred while computing — details:", e)

if __name__ == '__main__':
    main()
