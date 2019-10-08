a, b, c = list(map(int,input().split()))

if a == b == c:
    print(3)
elif a == b != c:
    print(2)
elif a != b == c:
    print(2)
elif a == c != b:
    print(2)
elif a != b != c:
    print(1)
