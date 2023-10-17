while True:
    c=input()
    d=0
    if c=="0":
        break
    for i in range(len(c)//2):
        if c[i]!=c[len(c)-1-i]:
            d=1
            break
    if d==0:
        print("yes")
    else:
        print("no")
