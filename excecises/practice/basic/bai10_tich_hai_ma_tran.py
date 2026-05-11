import numpy as np
M = int(input("Nhập vào số nguyên M: "))
N = int(input("Nhập vào số nguyên N: "))
A = np.empty((M, N))
B = np.empty((M, N))
print("Nhập vao ma trận A: ")
for i in range(M):
    for j in range(N):
        A[i, j] = int(input(f"A[{i}][{j}] = "))
print("Nhập vao ma trận B: ")
for i in range(M):
    for j in range(N):
        B[i, j] = int(input(f"B[{i}][{j}] = "))
C = A*B
print("Ma trận A")
print(A)
print("Ma trận B")
print(B)
print("Tích hai ma trận: ")
print(C)
