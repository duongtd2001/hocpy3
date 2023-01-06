'''
Cho danh sách (list) friends = ["Jen", "Jack", "Kenny", "Jelly", "Bob", "Henry", "Anne"]
Yêu cầu:
a. Lấy ra 4 người bạn đầu tiên trong friends
b. Lấy ra 4 người bạn cuối trong friends
c. Đảo ngược danh sách friends
d. Lấy ra những người bạn từ vị trí 1 đến hết
e. Copy danh sách ban đầu thành một danh sách mới
f. Lấy ra những người bạn từ vị trí 2 đến sát cuối
'''

friends = ["Jen", "Jack", "Kenny", "Jelly", "Bob", "Henry", "Anne"]

# a
four_friends = friends[0:4:1]
print(four_friends)

# b
four_friends2 = friends[-4:]
print(four_friends2)

# c
rev = friends[::-1]
print(rev)

# d
new_friends = friends[1:]
print(new_friends)

# e
friends_copy = friends.copy()
print(friends_copy)

# f
two_end_friends = friends[2:-1]
print(two_end_friends)
