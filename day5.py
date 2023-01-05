'''
list in list
copy list
list slicing

'''
game_list = [['pubg', 23], ['3q', 34], ['army2', 56]]

# lấy giá trị trong list 'game_list'

# list in list
lst1 = [1, 2, 5]
# lst2 = lst1
lst2 = lst1.copy  # copy list
# kiểm tra lst1 và lst2 là một không

print(lst1 is lst2)
print(lst1 == lst2)

# id
print(id(lst1), id(lst2))


# list slicing => trả về 1 danh sách mới, ở vị trí bộ nhớ mới
number_list = [1, 2, 5, 3, 6, 4, 8]
new_list = number_list[0:2:1]  # start:stop:step
# [1:] lấy từ 1 => hết
# [:2] viết gọn của mặc định
# [1:-1] lấy từ 1 => cuối (không lấy giá trị cuối)
# [:] sao chép danh sách ban đầu
# [::-1] đảo ngược list (sử dụng list slicing)
print(new_list is number_list)
print(new_list)
