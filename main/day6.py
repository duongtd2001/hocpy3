'''
set :biến chưa đc nhiều giá trị, tạo bỏi dấu ngoặc nhọn, 
không có thứ tự(không thể truy cập bằng chỉ số), không chứa phần tử trùng lặp
tuple: tạo bởi dấu ngoặc tròn, không thể thay đổi giá trị
'''
# tuple, hay dùng cho database
from copy import deepcopy
tup1 = 1, 2, 3, 4, 5
tup2 = (1, 2, 3, 4, 5)
tup3 = 1,
# truy cập giá trị trong tuple
print(tup1[0])
# thêm giá trị vào cuối tuple
tup1 += (3, 5, 7, 2, 6)

# set: không chứa phần tử trùng lặp, không thứ tự
set1 = set()  # set trống
# thêm giá trị vào set
set1.add(1)
print(set1)
# update bằng 1 list, các giá trị đều thành set (riêng lẻ từng giá trị)
set1.update([1, 2, 3, 4, 5, 6, 7])
# xóa giá trị
set1.remove(1)
# copy
set2 = set1.copy()
# so sánh id (bộ chỉ bộ nhớ)
print(set1 is set2)
# làm trống set
set1.clear()

# tạo 1 set
set3 = {1, 2, 3, 6, 8}
# lấy và xóa đi 1 giá trị bất kỳ
set3.pop()

# copy sâu vào bên trong list ban đầu
lsr = deepcopy(set1)
# kiểm tra giá trị có phải kiểu 'int' (hoặc các kiểu khác) không
print(isinstance('a', str))
