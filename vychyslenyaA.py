from math import sqrt
Ax, Ay = list(map(float,input().split())) 
Bx, By = list(map(float,input().split()))

line = abs(sqrt((Ax - Bx)**2 + (Ay - By)**2))
line1 = round(line, 3)
print(line1)
