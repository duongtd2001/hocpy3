'''
Py FCN
'''

# không truyền tham số


def fcn():
    print('PLC S7-1200 cpu 1214 dc/dc/dc')


fcn()

# truyền tham số


def fcn_1(plc):
    print(plc)


fcn_1('S7-1200')

# truyền nhiều tham số


def name_age(name, age):
    # return chấm dứt hàm, các câu lệnh sau return sẽ không chạy nữa
    return f'{name}: {age}'


name_age('Duong', 23)


# truyền vào list
def func(lst=[]):
    lst.append(2)
    print(lst)


func()
func()

fri = ['Thuy', 'Trang', 'Ngan']


def my_func():
    f = fri + ['Duong']
    print(f)


my_func()


# hàm không có tên
print((lambda x, y: x+y)(1, 2))


# first class Func, gọi 1 hàm bằng 1 hàm khác
def greet(msg):
    print('Hello ' + msg)
    return None


hello = greet
print(hello('Joe'))

# hàm trống phải để từ pass ngăn chặn lỗi xảy ra


def fc():
    pass

# toán tử *args(kiểu tuple) tập hợp các đối số vị trị


def add(*args):
    print(type(args))
    return sum(args)


print(add(1, 2, 3, 4))
# lưu ý
ls = [1, 25, 6, 8]
print(*ls)
first, *mid, last = ls
print(first)
print(mid)
print(last)
