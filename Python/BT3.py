"""
Sử dụng ngôn ngữ Python viết chương trình nhập vào một danh sách số nguyên gồm n phần tử, sau đó thực hiện:
Tính tổng phần tử là số lẻ trong danh sách;
Tìm vị trí của phần tử có giá trị lớn nhất trong danh sách.
"""


def tong_le(n):
    tongle = 0
    for i in range(len(n)):
        if n[i] % 2 == 1:
            tongle +=n[i]
    print("Tong so le la: ",tongle)
def vt_max(n):
    max = n[0]
    vt = 0
    for i in range(1, len(n)):
        if max <= n[i]:
            max = n[i]
            vt = i
    print("MAX = n[{}] = {}".format(vt, max))
n = list(map(int, input("Nhap: ").split(" ")))
tong_le(n)
vt_max(n)