# 6. Nhập vào một số nguyên dương n. Đếm số lượng số chẵn và lẻ trong đoạn [0, n]
n = int(input('nhập một số nguyên dương: '))
even = 0
odd = 0
for n in range(n+1):
    if n % 2 == 0:
        even += 1
    else:
        odd += 1
print('even:', even)
print('odd:', odd)