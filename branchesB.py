Anton, Boris, Victor = list(map(int,input().split()))

if Anton == Boris == Victor:
    print("Same age")

if Anton == Boris > Victor:
    print("Victor")
elif Anton == Victor > Boris:
    print("Boris")
elif Boris == Victor > Anton:
    print("Anton")
elif Anton < Boris > Victor:
    print("Boris")
elif Boris < Anton > Victor:
    print("Anton")
elif Boris < Victor > Anton:
    print("Victor")
