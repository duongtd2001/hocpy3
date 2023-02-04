''' 
1. Cho một list chứa các tuple như sau: friends = [("Bob", "Male"), ("Anna", "Female"), ("Max", "Male")]
a. Cho biết chiều dài của friends
b. Lấy ra phần tử đầu, cuối và giữa và kiểm tra kiểu của chúng
c. Nhập vào tên (name) và giới tính (gender) của một người bạn sau đó append vào friends tuple gồm hai giá trị (name, gender)
'''
# a
friends = [("Bob", "Male"), ("Anna", "Female"), ("Max", "Male")]
lengh = len(friends)
print(lengh)

# b
fri_1 = friends[0]
print('friends_1:', fri_1)
print(type(fri_1), '\n')

fri_2 = friends[1]
print('friends_2:', fri_2)
print(type(fri_2), '\n')

fri_3 = friends[-1]
print('friends_3:', fri_3)
print(type(fri_3), '\n')

# c
name = input('nhập tên:')
gender = input('nhập giới tính:')
fri_4 = (name, gender)
friends.append(fri_4)
print(friends)
