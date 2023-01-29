# Nhập vào một danh sách những số nguyên và hiển thị gấp đôi của các số trong danh sách sử dụng list comprehension
lst = map(int, input().split())
new_lst = [val*2 for val in lst]
print(new_lst)
