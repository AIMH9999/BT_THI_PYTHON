# Sử dụng ngôn ngữ Python viết chương trình phân tích số nguyên n thành tích các thừa số nguyên tố
n = int(input("Nhập một số: "))
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
print("tích các thừa số nguyên tố là = ", str(tsnt).strip("[]").replace(",",".").replace(" ",""))