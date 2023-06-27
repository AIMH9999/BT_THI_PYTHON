#Sử dụng ngôn ngữ Python viết chương trình liệt kê tất cả các số nguyên tố nhỏ hơn n với số nguyên dương n được nhập từ bàn phím.
n = int(input("Nhập một số: "))
snt = []
for i in range(2, n+1):
    if i == 2:
        snt.append(i)
    for j in range(2, i):
        if i % j == 0:
            break
        if j == i-1:
            snt.append(i)
print("Cac so nguyen to nho hon {} la : {} ".format(n, snt))