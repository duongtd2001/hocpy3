# Giải và biện luận phương trình bậc nhất một ẩn ax + b = 0 (ẩn x, a và b là hai số cho trước)
a = float(input('nhập a: '))
b = float(input('nhập b: '))
if a == 0 and b == 0:
    print('pt vô số nghiệm')
elif a == 0 and b != 0:
    print('pt vô nghiệm')
else:
    print('pt có 1 nghiệm:', -b/a)
