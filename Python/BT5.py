#Sử dụng ngôn ngữ Python viết chương trình nhập vào danh sách tên sinh viên, sau đó tìm kiếm vị trí của sinh viên bất kỳ có trong danh sách đó.
def tim_VT_sinh_vien(danh_sach, ten_sinh_vien):
    for i, ten in enumerate(danh_sach):
        if ten == ten_sinh_vien:
            return i
    return -1

DSSV = input("Nhập vào danh sách tên sinh viên (cách nhau bằng dấu phẩy): ").split(",")

TIM = input("Nhập vào tên sinh viên cần tìm kiếm: ")

VT = tim_VT_sinh_vien(DSSV, TIM)

if VT != -1:
    print("Sinh viên '{0}' được tìm thấy tại vị trí {1}.".format(TIM, VT))
else:
    print("Sinh viên '{0}' không có trong danh sách.".format(TIM))
