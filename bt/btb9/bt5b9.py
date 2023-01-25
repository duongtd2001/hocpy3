# Nhập vào một số nguyên dương n tính tổng các chữ số của n. Ví dụ: n = 4312 => S = 4 + 3 + 1 + 2 = 10
n = int(input('nhập một số nguyên dương: '))
s = 0
while n > 0:
    p = n % 10
    s += p
    n = n//10
print(s)
