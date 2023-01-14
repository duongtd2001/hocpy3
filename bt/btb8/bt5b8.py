# Giải và biện luận phương trình bậc nhất một hai ax^2 + bx + c = 0 (ẩn x, a, b, c là ba số cho trước)
import math
a = float(input('nhập a: '))
b = float(input('nhập b: '))
c = float(input('nhập c: '))
delta = pow(b, 2) - 4*a*c
if delta < 0:
    print('pt vô nghiệm')
elif delta == 0:
    print('pt có nghiệm kép x1 = x2:', -b/2*a)
else:
    print('pt có 2 nghiệm phân biệt x1:', (-8+math.sqrt(delta)/2*a))
    print('pt có 2 nghiệm phân biệt x2:', (-8-math.sqrt(delta)/2*a))
