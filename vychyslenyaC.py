A = int(input())

st = A//100
nd = (A - st*100)//10
rd = (A - st*10)%10

print(st,", ", nd,", ", rd, sep = "")
