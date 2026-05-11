import random
import numpy as np
mydict = {i: random.randint(1, 100) for i in range(1, 11)}
print("Tự điển")
print(mydict)
L = list(mydict.items())
A = np.array(L)
print("Ma trận")
print(A)