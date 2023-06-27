# Sử dụng ngôn ngữ Python viết chương trình tìm ước số chung lớn nhất (USCLN) và bội số chung nhỏ nhất (BSCNN) của hai số nguyên dương a và b nhập từ bàn phím

def uscln(a, b):
    while b != 0:
        a, b = b, a%b
    return a
def bscnn(a, b):
    ucln = uscln(a, b)
    bcnn = (a * b)//ucln
    return bcnn
a = int(input("Nhap so a: "))
b = int(input("Nhap so b: "))
ucln = uscln(a, b)
bcnn = bscnn(a, b)
print("Ước số chung lớn nhất (USCLN) của", a, "và", b, "là:", ucln)
print("Bội số chung nhỏ nhất (BSCNN) của", a, "và", b, "là:", bcnn)
