# Tổng mản np
import numpy as np
M = int(input("Nhập vào M: "))
N = int(input("Nhập vào N: "))
A = np.empty((M, N))
for i in range(M):
    for j in range(N):
        A[i, j] = float(input(f"A[{i}][{j}] = "))

print(f"Tổng các phần tử trong mảng:{A.sum()} ")

