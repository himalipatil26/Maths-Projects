# Arithmetic Progression Functions

def ap_nth_term(a, d, n):
    print("\nFormula: aₙ = a + (n-1)d")
    print(f"Step: aₙ = {a} + ({n}-1)*{d}")
    print(f"Step: aₙ = {a} + {(n-1)*d}")
    return a + (n - 1) * d

def ap_sum_n_terms(a, d, n):
    print("\nFormula: Sₙ = n/2 [2a + (n-1)d]")
    print(f"Step: Sₙ = {n}/2 * (2*{a} + ({n}-1)*{d})")
    print(f"Step: Sₙ = {n}/2 * ({2*a} + {(n-1)*d})")
    return n/2 * (2*a + (n - 1)*d)

def ap_menu():
    print("\n--- Arithmetic Progression ---")
    a = float(input("First term a: "))
    d = float(input("Common difference d: "))
    n = int(input("Term number n: "))

    print("\nChoose:")
    print("1. nth term")
    print("2. Sum of n terms")

    ch = input("Your choice: ")

    if ch == "1":
        result = ap_nth_term(a, d, n)
        print("Result:", result)

    elif ch == "2":
        result = ap_sum_n_terms(a, d, n)
        print("Result:", result)

    else:
        print("Invalid option.")


# Geometric Progression Functions

def gp_nth_term(a, r, n):
    print("\nFormula: aₙ = a * r^(n-1)")
    print(f"Step: aₙ = {a} * {r}^({n-1})")
    return a * (r ** (n - 1))

def gp_sum_n_terms(a, r, n):
    print("\nFormula: Sₙ = a * (rⁿ - 1) / (r - 1)   (r ≠ 1)")
    print(f"Step: Sₙ = {a} * ({r}^{n} - 1) / ({r} - 1)")
    return a * ((r**n - 1) / (r - 1))

def gp_menu():
    print("\n--- Geometric Progression ---")
    a = float(input("First term a: "))
    r = float(input("Common ratio r: "))
    n = int(input("Term number n: "))

    print("\nChoose:")
    print("1. nth term")
    print("2. Sum of n terms")

    ch = input("Your choice: ")

    if ch == "1":
        result = gp_nth_term(a, r, n)
        print("Result:", result)

    elif ch == "2":
        if r == 1:
            print("For r = 1, sum = a * n")
            print("Result:", a * n)
        else:
            result = gp_sum_n_terms(a, r, n)
            print("Result:", result)

    else:
        print("Invalid option.")


def main():
    while True:
        print("\n=== Arithmetic & Geometric Progression Tool ===")
        print("1. Arithmetic Progression (AP)")
        print("2. Geometric Progression (GP)")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            ap_menu()
        elif choice == "2":
            gp_menu()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")
            print("Please select a valid option.")  

if __name__ == "__main__":
    main()

