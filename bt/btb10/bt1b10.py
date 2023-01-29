# Đếm số chẵn và lẻ trong đoạn [0, 1000] theo 2 cách: thông thường và list comprehension
even = 0
odd = 0
for i in range(1001):
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
print(even)
print(odd)

# list comprehensions
even_cphs = sum(1 for n in range(1001) if n % 2 == 0)
odd_cphs = sum(1 for n in range(1001) if n % 2 != 0)
print(even_cphs)
print(odd_cphs)
