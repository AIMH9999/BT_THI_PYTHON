# Sử dụng ngôn ngữ Python viết chương trình chấp nhận đầu vào là một câu, đếm số chữ cái và chữ số trong câu đó.
s = input("Nhập một câu: ")
chu = 0
so = 0
for x in s:
    if x.isdigit():
        so += 1
    if x.isalpha():
        chu +=1
print("Trong cau trên có {} chu va {} so".format(chu, so))
