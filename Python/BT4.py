# Sử dụng ngôn ngữ Python viết chương trình tìm ước số chung lớn nhất (USCLN) và bội số chung nhỏ nhất (BSCNN) của hai số nguyên dương a và b nhập từ bàn phím
def ts_nt(n):
    m = []
    tsnt = []
    for i in range(2, n+1):
        if i == 2:
            m.append(i)
        for j in range(2, i):
            if i % j == 0:
                break
            if j == i-1:
                m.append(i)
    i = 0
    while n != 1:
        if n % m[i] == 0:
            tsnt.append(m[i])
            n = n/m[i]
            i = 0
            continue
        else:
            i=i+1
    return tsnt
a = int(input("Nhap so a: "))
b = int(input("Nhap so b: "))
tsnt_a = ts_nt(a)
tsnt_b = ts_nt(b)
tsnt_ab = []
for i in range(len(tsnt_a)):
    for j in range(len(tsnt_b)):
        if tsnt_a[i] == tsnt_b[j]:
            tsnt_ab.append(tsnt_a[i])
            tsnt_b[j] = 0
            break
ucln = 1
for i in tsnt_ab:
    ucln *= i
bcnn = (a * b)// ucln
print(ucln)
print(bcnn)

