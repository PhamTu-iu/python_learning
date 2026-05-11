# Nhập vào N và hiển thị các ước của N
N = int(input("Nhập vào số nguyên n: "))
for i in range(1,N):
    if N%i==0:
        print(f"{i}")