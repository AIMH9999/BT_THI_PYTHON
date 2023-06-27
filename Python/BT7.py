#Sử dụng ngôn ngữ Python viết chương trình nhập vào một danh sách các số nguyên, xuất ra màn hình các số nguyên chẵn trong danh sách đó.
def so_le(n):
    le = []
    for i in n:
        if i%2!=0:
            le.append(i)
    print("So le la: ",le)
n = list(map(int, input("Nhap: ").split(" ")))
so_le(n)
