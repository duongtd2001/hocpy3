# duyệt qua 1 list
# list ngoặc []
# tuple ngoặc ()
# set ngoặc {}, không có thứ tự
fri = {'Duong': 1,
       'Trang': 2,
       'Thuy': 3}
for item in fri.items():
    key, value = item
    print(key)
    print(value)
    print('*'*5)
'''

'''
# list comprehensions: tạo ra lst mới gấp đôi lst cũ
lst = [2, 4, 6, 8]
# new_lst = []
'''for x in lst:
    val = x*2
    new_lst.append(val)
print(new_lst)'''
new_lst = [val*2 for val in lst]  # cú pháp của lst comprehensions
print(new_lst)
# set comprehensions
set_a = {'a', 'c', 'd'}
new_set = {s.upper() for s in set_a}
print('new_set', new_set)
# dict comprehensions
zz = {'Duong': 1,
      'Trang': 2,
      'Thuy': 3}
new_zz = {
    k: v*2
    for k, v in zz.items()
}
print(new_zz)

'''
- zip
- enumerate
tạo ra hàng loạt tuple
'''
# zip
lst1 = ['a', 'b', 'c']
lst2 = [1, 2, 3, 4]
print(list(zip(lst1, lst2)))

# enumerate
lst5 = ['a', 'b', 'e']
print(list(enumerate(lst5)))  # lst5, start mặc định = 0
print(dict(zip(lst1, lst2)))
