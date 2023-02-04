'''print('hello world!')
print(1, 2, 3, 4, sep=' @ ')  # chèn vào giữa các kí tự
print(1, 2, 3, 4, end=' ### ')  # khi kết thúc, end='' sẽ in 2 dòng trên 1
print(
line
    line
line)

# Shift + Alt +mũi tên xuống "copy dong code"
# Ctrl + x " xóa 1 dòng"
# Ctrl + Alt + up,down " them con trở chuột "
# Ctrl + Shift + P " mở theme"venv\Scripts\activate
print("❤️")'''

'''n = int(input("n = "))

while n <= 0:
    print("n phải là số nguyên dương")
    n = int(input("n = "))
    
S = 0

while n > 0:
    last = n % 10
    S += last
    n //= 10
    
print(S)'''
lss = [1, 'd']
fp = open('data.txt', mode='w')  # r: read, w: write, a: append
fp.write(' - '.join(map(str, lss)))
# data = fp.read()
# print(data)
fp.close()
