# Tổng mảng nhập đến khi có kí tự $
a = []
while True:
    x = input("Nhập vào một số nguyên: ")
    if x =="$":
        break
    else:
        a.append(int(x))
c = sum(a)/len(a)
print(f"{c}")