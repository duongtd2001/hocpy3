'''
1. Cho hai tập hợp (set)
art_students = {"John", "Max", "Anna", "Bob", "Obito"}
math_students = {"Max", "Mery", "David", "Anna", "Naruto", "John"}
a. Tìm những người bạn học cả vẽ lẫn toán
b. Tìm những người bạn học vẽ nhưng không học toán
c. Tìm những người bạn học toán nhưng không học vẽ
d. Tìm những người bạn học vẽ hay toán không phải cả hai
e. Tìm tất cả những người bạn
'''
art_students = {"John", "Max", "Anna", "Bob", "Obito"}
math_students = {"Max", "Mery", "David", "Anna", "Naruto", "John"}

# a
print(art_students & math_students)

# b
art_not_math = art_students.difference(math_students)
print(art_not_math)

# c
math_not_art = math_students.difference(art_students)
print(math_not_art)

# d
print(art_students ^ math_students)
# e
print(art_students | math_students)