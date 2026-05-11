import numpy as np
A = np.empty((5, 5))
for i in range(A.shape[0]):
    for j in range(A.shape[1]):
        A[i, j] = 5*i+j+1

print(A)
print(f"Tổng của ma trận: {A.sum()}")