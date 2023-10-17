a=list(input())
b=[]
for i in a:
    n=ord(i)-65
    if n<3:
        b.append(3)
    elif n<6:
        b.append(4)
    elif n<9:
        b.append(5)
    elif n<12:
        b.append(6)
    elif n<15:
        b.append(7)
    elif n<19:
        b.append(8)
    elif n<22:
        b.append(9)
    elif n<26:
        b.append(10)
print(sum(b))