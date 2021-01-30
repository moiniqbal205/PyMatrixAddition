def matrix(m, n):
    output = []
    for i in range(m):
        row = []
        for j in range(n):
            user_in = int(input(f"Enter matrix[{i}][{j}]: "))
            row.append(user_in)
        output.append(row)
    return output

def add_matrix(i, j):
    addition = []
    for i in range(len(A)):
        row = []
        for j in range(len(A[0])):
            row.append(A[i][j] + B[i][j])
        addition.append(row)
    return addition

row = int(input("Enter number of row(s): "))
col = int(input("Enter number of column(s): "))

print("Enter 1st Matrix")
A = matrix(row, col)
print(A)

print("Enter 2nd Matrix")
B = matrix(row, col)
print(B, "\n")

print("Matrix A + B = ", add_matrix(A, B))