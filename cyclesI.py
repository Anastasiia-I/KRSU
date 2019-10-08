num = 153
num = int(num)
a = 0
b = 0
c = 0
while num < 1000:
    a = num % 10
    b = num % 100 // 10
    c = num // 100
    if (a**3 + b**3 + c**3) == num:
        print(num)
    num += 1
