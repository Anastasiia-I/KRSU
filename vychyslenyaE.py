a = int(input())
H = a//3600
M = (a - 3600*H)//60
S = a - 3600*H - 60*M
print(H,M,S)
