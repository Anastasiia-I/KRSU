nums = int(input())
a = []
d = 3
while nums % 10 != 0:
    if nums%10 == nums //10 %10:
        d = 10
        print("YES")
        break
    nums = nums//10
if d != 10:
    print("NO")
