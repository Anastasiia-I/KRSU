from math import sqrt
import math

x1, y1, x2, y2, x3, y3 = list(map(float,input().split()))

AB = sqrt((x2 - x1)**2 + (y2 - y1)**2)
BC = sqrt((x3 - x2)**2 + (y3 - y2)**2)
CA = sqrt((x3 - x1)**2 + (y3 - y1)**2) 

P = (AB) + (BC) + (CA)
p1 = round(P, 5)

s = 1/2 * math.fabs((x1 - x3)*(y2 - y3) - (x2 - x3)*(y1 - y3))
print(p1, s, sep = " ")
