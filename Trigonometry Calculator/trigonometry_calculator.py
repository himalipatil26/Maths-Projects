import math

def ascii_unit_circle():
    circle = """
                 y
                 |
           1.0   |     sinθ
                 |
     -1.0 -------+---------> x
                 |
           -1.0  |    
                 |

            ASCII UNIT CIRCLE
      cosθ = x-coordinate, sinθ = y-coordinate
    """
    print(circle)


def trigonometry_calculator():
    while True:
        print("\n------ TRIGONOMETRY CALCULATOR ------")
        print("1. sin(x)")
        print("2. cos(x)")
        print("3. tan(x)")
        print("4. Inverse Trig (asin, acos, atan)")
        print("5. Degrees ↔ Radians")
        print("6. Show ASCII Unit Circle")
        print("0. Exit")

        choice = input("\nEnter your choice: ")

        # Exit
        if choice == "0":
            print("Goodbye!")
            break

        # sin
        elif choice == "1":
            x = float(input("Enter angle in degrees: "))
            print(f"sin({x}) = {math.sin(math.radians(x)):.5f}")

        # cos
        elif choice == "2":
            x = float(input("Enter angle in degrees: "))
            print(f"cos({x}) = {math.cos(math.radians(x)):.5f}")

        # tan
        elif choice == "3":
            x = float(input("Enter angle in degrees: "))
            try:
                print(f"tan({x}) = {math.tan(math.radians(x)):.5f}")
            except:
                print("Undefined (tan 90°, 270°, ... is not defined)")

        # inverse trig
        elif choice == "4":
            print("\n--- Inverse Trig ---")
            print("a. asin(x)")
            print("b. acos(x)")
            print("c. atan(x)")
            sub = input("Choose option: ")

            if sub == "a":
                x = float(input("Enter value (-1 to 1): "))
                print(f"asin({x}) = {math.degrees(math.asin(x)):.5f}°")

            elif sub == "b":
                x = float(input("Enter value (-1 to 1): "))
                print(f"acos({x}) = {math.degrees(math.acos(x)):.5f}°")

            elif sub == "c":
                x = float(input("Enter any value: "))
                print(f"atan({x}) = {math.degrees(math.atan(x)):.5f}°")

        # degree-radian conversions
        elif choice == "5":
            print("\n--- Angle Conversion ---")
            print("a. Degrees → Radians")
            print("b. Radians → Degrees")
            sub = input("Choose option: ")

            if sub == "a":
                deg = float(input("Enter degrees: "))
                print(f"{deg}° = {math.radians(deg):.5f} rad")
            elif sub == "b":
                rad = float(input("Enter radians: "))
                print(f"{rad} rad = {math.degrees(rad):.5f}°")

        # ASCII unit circle
        elif choice == "6":
            ascii_unit_circle()

        else:
            print("Invalid choice. Try again.")

# Run the calculator
trigonometry_calculator()
