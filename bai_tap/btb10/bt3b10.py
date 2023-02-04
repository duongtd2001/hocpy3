'''Cho dict như sau:
people = {
  "Emma": 71,
  "Jack": 45,
  "Amy": 15,
  "Ben": 29
}
a. In ra người già nhất
b. Tạo ra một dict mới dựa vào people dict với tuổi của mỗi người tăng gấp đôi
c. In ra enumerate các key trong people dict
d. Sử dụng hàm dict để biến enumerate bên trên trở thành dict
'''
people = {
    "Emma": 71,
    "Jack": 45,
    "Amy": 15,
    "Ben": 29
}
# a
max_age = max(people.values())
for name, age in people.items():
    if age == max_age:
        print(name)


# b
double_age = {
    k: v*2
    for k, v in people.items()
}
print(double_age)

# c
print(list(enumerate(people)))

# d
dict = dict(enumerate(people))
print(dict)
