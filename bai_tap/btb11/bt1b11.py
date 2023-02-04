# Định nghĩa 4 hàm add, subtract, divide, multiply (+, -, /, *). Mỗi hàm nhận vào hai tham số thực hiện lần lượt các phép toán cộng, trừ, chia, nhân. Lưu ý hàm nên trả về thay vì in ra.
# cộng
def add(x, y):
    return x+y


sm = add(3, 7)
print(sm)

# trừ


def subtract(x1, y1):
    return x1-y1


tru = (subtract(8, 5))
print(tru)

# chia


def divide(x2, y2):
    if y2 == 0:
        return 'Divide by zero'
    return x2/y2


chia = divide(20, 7)
print(chia)

# nhân


def multiply(x3, y3):
    return x3*y3


nhan = multiply(2, 5)
print(nhan)
