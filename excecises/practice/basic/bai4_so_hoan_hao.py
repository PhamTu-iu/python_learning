# Số hoàn hảo
n = int(input("Nhập vào số nguyên n: "))
sum =0
for i in range(n):
    if n%i==0:
        sum+=i
if sum == n:
    print("Số vừa nhập là số hoàn hảo")
else:
    print("Số vừa nhập không phải là số hoàn hảo")