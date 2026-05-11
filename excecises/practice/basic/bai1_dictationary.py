# Nhập vào n và hiển thị i: i*i
n = int(input("Nhập vào số nguyên n: "))
for i in range(n+1):
    print(f"{i}:{i*i}", end = " ")