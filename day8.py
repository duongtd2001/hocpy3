'''
if-elif-else: sau mỗi điều kiện phải có dấu hai chấm (:), 
'''
# eval: đánh giá biểu thức trong chuỗi
print(eval('1+2'))
# input nhiều giá trị
lst = map(eval, input().split())
print(lst)
# in ra các giá trị cách nhau 1 dấu cách
print(*lst)

# làm trong số thập phân
x = 2.34568
print(x)

# sorted : sắp xếp nhỏ -> lớn (tạo 1 ls mới)
ls = [1, 2, 5, 6, 3, 5, 8, 9, 5]
newls = sorted(ls)
print(newls)
# lớn -> nhỏ
newls2 = sorted(ls, reverse=True)
print(newls2)

# ord - chr
char = 'a'
print('ASCII Code:', ord(char))

ascii_code = 97
print(chr(ascii_code))


# list
s = 'ntgbd'
print(list(s))
# biến các giá trị thành list
lsc = list(map(eval, input().split()))
print(lsc)


# divmod: thương và phần dư
print(divmod(6, 3))

# bin: chuyển đổi hệ nhị phân
print(bin(10)[2:])
print(f'{10:b}')
