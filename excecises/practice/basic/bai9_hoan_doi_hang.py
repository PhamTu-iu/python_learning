import numpy as np
M = int(input("Nhập vào số nguyên M: "))
N = int(input("Nhập vào số nguyên N: "))
A = np.empty((M, N))
value =1
for i in range(M):
    for j in range(N):
        A[i, j] = value
        value += 1
print(A)
print("Ma trận sau khi hoán đổi hàng 1 và 2")
temp = A[0].copy()
A[0] = A[1]
A[1] = temp
print(A)