a, b, c = list(map(int,input().split()))

if b <= a >= c:
    long = a
    short1 = b
    short2 = c
elif a <= b >= c:
    long = b
    short1 = a
    short2 = c
elif a <= c >= b:
    long = c
    short1 = a
    short2 = b

if int(long)== 0 or int(short1) == 0 or int(short2) == 0 :
    print("NO")
elif int(short1) + int(short2) >= int(long):
    print("YES")
else:
    print("NO")
