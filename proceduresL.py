def num(a):
    if a % 4 == 0:
        if a % 4 == 0 and a % 100 == 0 and a % 400 != 0:
            return "NO"
        return "YES"
    return "NO" 
a = int(input())

print(num(a))
