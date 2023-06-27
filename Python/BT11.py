#Sử dụng ngôn ngữ Python viết chương trình nhập vào một danh sách các phần tử nguyên, sau đó thực hiện:
#-  Xuất ra danh sách các phần tử đã nhập;
#-  Xuất ra danh sách các phần tử theo thứ tự tăng dần;
#-  Xuất ra danh sách các phần tử có giá trị chẳn.
def so_chan(n):
    chan = []
    for i in n:
        if i%2==0:
            chan.append(i)
    print("So chan la: ",chan)
def tang_dan(n):
    n.sort()
    print("Danh sách các phần tử theo thứ tự tăng dần:", n)
n = list(map(int, input("Nhap: ").split(" ")))
print("Danh sach da nhap la: ", n)
so_chan(n)
tang_dan(n)