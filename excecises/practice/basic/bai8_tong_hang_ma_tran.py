import numpy as np
A = np.empty((4, 4))
value=1
for i in range(A.shape[0]):
    for j in range(A.shape[1]):
        A[i, j] = value
        value+=2

print(A)
print(f"Tổng hàng thứ 2 của ma trận: {A[1].sum()}")