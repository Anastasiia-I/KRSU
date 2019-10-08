x = 10000
while 10000 <= x < 100000:
    if x % 133 == 125 and x % 134 == 111:
        print(x)
    x += 1
