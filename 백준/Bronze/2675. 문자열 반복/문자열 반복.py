for i in range(int(input())):
    a,b=input().split()
    c=""
    for j in list(b):
        c+=j*int(a)
    print(c)