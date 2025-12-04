# --- MATRIX OPERATIONS PROGRAM (Single File) ---

import numpy as np

# ---------------- MATRIX FUNCTIONS ----------------

def add(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def subtract(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def multiply(A, B):
    if len(A[0]) != len(B):
        raise ValueError("Columns of A must match rows of B")
    result = [[0] * len(B[0]) for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result

def transpose(A):
    return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]

def determinant(A):
    if len(A) == 1:
        return A[0][0]
    if len(A) == 2:
        return A[0][0]*A[1][1] - A[0][1]*A[1][0]
    det = 0
    for c in range(len(A)):
        minor = [row[:c] + row[c+1:] for row in A[1:]]
        det += ((-1)**c) * A[0][c] * determinant(minor)
    return det

# --------------- HELPER: Read Matrix ----------------

def get_matrix(n, m):
    print(f"Enter {n}x{m} matrix row by row:")
    return [list(map(float, input().split())) for _ in range(n)]

# ----------------------- MENU -----------------------

def main():
    while True:
        print("\n==== MATRIX OPERATIONS ====")
        print("1. Add matrices")
        print("2. Subtract matrices")
        print("3. Multiply matrices")
        print("4. Transpose matrix")
        print("5. Determinant")
        print("6. Solve Linear Equations (Ax = b)")
        print("7. Exit")

        choice = int(input("Choose option: "))

        if choice in [1, 2, 3]:
            r1 = int(input("Rows of Matrix A: "))
            c1 = int(input("Cols of Matrix A: "))
            A = get_matrix(r1, c1)

            r2 = int(input("Rows of Matrix B: "))
            c2 = int(input("Cols of Matrix B: "))
            B = get_matrix(r2, c2)

            if choice == 1:
                print("\nResult:", add(A, B))
            elif choice == 2:
                print("\nResult:", subtract(A, B))
            elif choice == 3:
                print("\nResult:", multiply(A, B))

        elif choice == 4:
            r = int(input("Rows: "))
            c = int(input("Cols: "))
            A = get_matrix(r, c)
            print("\nTranspose:", transpose(A))

        elif choice == 5:
            n = int(input("Size of square matrix (n×n): "))
            A = get_matrix(n, n)
            print("\nDeterminant:", determinant(A))

        elif choice == 6:
            n = int(input("Number of variables: "))
            print("Enter coefficient matrix A:")
            A = np.array(get_matrix(n, n))
            print("Enter constant vector b:")
            b = np.array(list(map(float, input().split())))
            print("\nSolution x =", np.linalg.solve(A, b))

        elif choice == 7:
            print("Exiting program...")
            break

        else:
            print("Invalid choice! Try again.")

# -----------------------------------------------------

if __name__ == "__main__":
    main()
