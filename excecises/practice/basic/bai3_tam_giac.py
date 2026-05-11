# Hiển thị tam giác tăng dần giá trị
n = int(input("Nhập vào số hàng n: "))
count=1
for i in range(1,n+1):
    for t in range(1, i+1):
        print(f"{count}",end = " ")
        count+=1
    print()