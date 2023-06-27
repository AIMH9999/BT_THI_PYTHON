#Sử dụng ngôn ngữ Python viết chương trình nhập vào một danh sách các số nguyên. Tìm kiếm số lớn thứ hai có trong danh sách và in kết quả ra màn hình.
def tim_so_lon_thu_hai(n):
    # Kiểm tra xem danh sách có ít nhất 2 số
    if len(n) < 2:
        print("Danh sách không đủ số để tìm kiếm số lớn thứ hai.")
        return None
    MAX = max(n)
    n.remove(MAX)
    S_MAX = max(n)
    return S_MAX
n = list(map(int, input("Nhap: ").split(" ")))
S_MAX = tim_so_lon_thu_hai(n)
if S_MAX is not None:
    print("Số lớn thứ hai trong danh sách là:", S_MAX)
