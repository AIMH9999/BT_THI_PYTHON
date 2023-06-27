#Sử dụng ngôn ngữ Python viết chương trình nhập từ bàn phím thông tin cá nhân bao gồm: mã sinh viên, họ tên, tuổi, email, địa chỉ:
#- Lưu các thông tin trên vào file data.txt;
#- Đọc thông tin từ file và hiển thị ra màn hình

c = int(input("1:Nhap SV, 2:Tim SV --"))
if c == 1:
    MSSV = []
    HO_TEN = []
    TUOI = []
    EMAIL = []
    DIA_CHI = []
    sv = int(input("Nhap so luong sinh vien:"))
    for i in range(sv):
        MSSV.append(input("Nhap MSSV:"))
        HO_TEN.append(input("Nhap ho va ten:").replace(" ", "_"))
        TUOI.append(input("Nhap tuoi:"))
        EMAIL.append(input("Nhap email:"))
        DIA_CHI.append(input("Nhap dia chi:"))
    file = open("data.txt", "w")
    file.writelines(str(MSSV).replace("[", "").replace("]", "").replace("'", "").replace(" ", "") + "\n")
    file.writelines(str(HO_TEN).replace("[", "").replace("]", "").replace("'", "").replace(" ", "") + "\n")
    file.writelines(str(TUOI).replace("[", "").replace("]", "").replace("'", "").replace(" ", "") + "\n")
    file.writelines(str(EMAIL).replace("[", "").replace("]", "").replace("'", "").replace(" ", "") + "\n")
    file.writelines(str(DIA_CHI).replace("[", "").replace("]", "").replace("'", "").replace(" ", "") + "\n")
    file.close()
elif c == 2:
    file = open("data.txt", "r")
    MSSV = file.readline().strip("\n").replace(" ", "").split(",")
    HO_TEN = file.readline().strip("\n").replace(" ", "").replace("_", " ").split(",")
    TUOI = file.readline().strip("\n").replace(" ", "").split(",")
    EMAIL = file.readline().strip("\n").replace(" ", "").split(",")
    DIA_CHI = file.readline().strip("\n").replace(" ", "").split(",")
    choose = int(input("1: Tim theo MSSV, 2:Tim theo Ho va Ten--"))
    if choose == 1:
        findMSSV = input("Nhap MSSV can tim:")
        if findMSSV in MSSV:
            vt = MSSV.index(findMSSV)
            print(MSSV[vt])
            print(HO_TEN[vt])
            print(TUOI[vt])
            print(EMAIL[vt])
            print(DIA_CHI[vt])
    elif choose == 2:
        vt = []
        findHO_TEN = input("Nhap Ho va Ten can tim:")
        for i in range(len(HO_TEN)):
            if findHO_TEN == HO_TEN[i] :
                vt.append(i)
        for j in vt: 
            print("Thong tin sinh vien la:")              
            print("MSSV: ",MSSV[j])
            print("Ho va ten: ",HO_TEN[j])
            print("Tuoi: ",TUOI[j])
            print("Email: ",EMAIL[j])
            print("Dia chi: ",DIA_CHI[j])
            print("----------------")
    file.close()