import json
set1 = {1, 2, 3, 4, 7, 3}
set2 = {2, 3, 6, 5, 8, 9, 0}
setn = {12, 34, 56, 68, 2, 3}
# tìm các phần tử chung của 2 set (giao), đầu vào là set.....(list, tuple,...)
set3 = set1.intersection(set2)
print(set3)
# sử dụng toán tử tìm phần chung (cả 2 bên phải là set)
print(set1 & set2)

# tìm phần tử nằm trong set1 nhưng không có trong set2
set4 = set1.difference(set2)
print(set4)
# dùng toán tử trừ để tìm phần từ nằm trong set 1 nhưng k có trong set2
print(set2-set1)

# lấy tất cả các phần tử của 2 set
set5 = set1.union(set2).union(setn)
print(set5)
print(set1 | set2 | setn)

# lấy tất cả nhưng trừ đi phần chung của 2 set
set6 = set1.symmetric_difference(set2)
print(set6)
print(set1 ^ set2)

'''dicttionnary: là cấu trúc dữ liệu chứa các cặp keys, value
'''

student = {
    'name': 'Bob',
    'age': 21,
    'black': [0, 120, 255]
}  # 'name': keys, 'Bob': value
print(json.dumps(student, indent=4))

# tạo
student['id'] = 'tdmu'
print(student)
#
student.update(raspi='pi')
print(student)

# update bằng info
info = {
    'cf': 'barret',
    'cfs': 'm4a1'
}
student.update(info)
print(student)

# xóa phần tử trong dict
value = student.pop('cf')
print(value)
print(student)

# xóa đi phần tử cuối của dict
tup = student.popitem()
print(tup)

# trả về keys trong dict
keys = list(student)
print(keys)
# trả về giá trị trong dict
val = list(student.values())
print(val)
# lấy ra tất cả giá trị trong dict -> tup
items = list(student.items())
print(items)
# xóa tất cả các phần tử
student.clear()
print(student)


'''
sum, len, min, max, join
'''
lst = [[1, 2, 3, 4, 5, 6, 7]]
# total = sum(lst)
# print(total)
# list + list
totl = sum(lst, [1])
print(totl)
'''
join
'''
