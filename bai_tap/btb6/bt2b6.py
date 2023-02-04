'''
2. Tạo một set trống có tên là set_a
a. Thêm 'Anna' vào set_a
b. Thêm một tuple ('Kenny', 'Jen', 'Danny')
c. In ra set_a và tính chiều dài của nó
d. Xóa 'Jen' ra khỏi set_a
e. Xóa tất cả các giá trị từ set_a
'''

set_a = set()

# a
set_a.add('Anna')
print(set_a)

# b
tup = ('Kenny', 'Jen', 'Danny')
set_a.update(tup)
print(set_a)

# c
print(set_a)
lengh = len(set_a)
print(lengh)

# d
set_a.remove('Jen')
print(set_a)

# e
set_a.clear()
print(set_a)
