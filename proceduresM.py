def num(a):
    d = hex(a).replace("0x", "")
    for i in d:
        d = list(d)
    d.reverse()
    d = "".join(d)
    d = d.replace("f", "F")
    d = d.replace("a", "A")
    d = d.replace("b", "B")
    d = d.replace("c", "C")
    d = d.replace("d", "D")
    d = d.replace("e", "E")
    return d
a = int(input())
print(num(a))
