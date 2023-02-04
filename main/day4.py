'''# tạo một chuỗi
#               0           1           2           3
#               -4          -3          -2          -1
movies = ['peak blinder', 'avenger', 'python', 'tracking line']
# kiểu dữ liệu
print(type(movies))
movies.pop()
print(movies)
# truy cập phần tử của list
print(movies[-1])

# số lượng phần tử của list
print(len(movies))

# thay đổi giá trị của list, có thể thay bằng input
movies[1] = 'value'
print(movies)

# thêm giá trị vào list # append
movies.append('iphone')
print(movies)

# xóa 1 giá trị trong list # remove
movies.remove('iphone')
print(movies)
movies.remove(movies[2])
print(movies)

# thêm 1 list vào list ban đầu #extend
# movies2 = [1, 2, 3, 4, 5]
movies.extend(['matlab', 'solidworks', 'pubg'])
print(movies)

# đảo ngược list #reverse
movies.reverse()
print(movies)

# làm trống 1 list #clear
# movies.clear()
# print(movies)

# lấy chỉ số của phần tử trong list (lấy số vị trí của phần tử trong list) #index
index_movies = movies.index('pubg')
print(index_movies)

# lấy số lượng của phần tử trong list # count
movies = movies.count('pubg')
print(movies)

# number = [0,1,2,3,4,5,6,0,2,3,1,2,3,4,2]
# number = number.count(1)
# print(number)
# lấy giá cuối và xóa giá trị cuối # pop
move = movies.pop
print('a',move)
# chèn một giá trị vào vị trí bất kỳ trong list, giá trị âm chèn vào đầu, giá trị dương chèn cuối
movies.insert(2, 'david')
print(movies)

# dir(list)  in ra các phương thức biến đổi list
'''
# sort: sắp xếp thứ tự trong list, tăng dần
pi4 = [1, 5, 6, 3, 8, 7, 9, 5, 4, 2]
pi4.sort()
print(pi4)
# sort(revers): sắp xếp list  giảm dần

# del movies[1]: xóa đi giá trị phần tử 1 trong list

# min(): tìm giá trị nhỏ nhất trong list
# max(): tìm giá trị lớn nhất trong list
mn = min(pi4)
print(mn)
mx = max(pi4)
print(mx)
