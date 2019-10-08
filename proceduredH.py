def degr(cel):
    far = cel*1.8 + 32
    far = int(far)
    return far
    
cel = int(input())
print(degr(cel))
