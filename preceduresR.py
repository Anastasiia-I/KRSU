def num(a):
    d = oct(a).replace("0o", "")
    for i in d:
        d = list(d)
    d.reverse()
    d = "".join(d)
    return d
a = int(input(), 2)
print(num(a))
