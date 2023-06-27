#Sử dụng ngôn ngữ Python viết chương trình giải phương trình bậc 2: ax2 + bx + c = 0.
import math
a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
c = int(input("Nhập c: "))
if a == 0:
    if b == 0 and c != 0:
        print("Phương trình vô nghiệm")
    elif b != 0 and c == 0:
        print("Phương trình có một nghiệm x = 0")
    elif b == 0 and c == 0:
        print("Phương trình có vô số nghiệm")
    else:
        print("Phương trình có một nghiệm = %.1f" % (-c / b))
else:
    Delta = b**2-4*a*c
    if Delta < 0:
        print("Phương trình vô nghiệm")
    elif Delta == 0:
        print("Phương trình có một nghiệm: x = %.2f"%(-b/(2*a)))
    elif Delta > 0:
        print("Phương trình có hai nghiệm phân biệt:\nx1 = %.2f\nx2 = %.2f"%((-b-math.sqrt(Delta))/(2*a), (-b+math.sqrt(Delta))/(2*a)))

