import sys
e=[]
for i in range(int(sys.stdin.readline())):
    a=list(sys.stdin.readline().split())
    if len(a)==2:
        e.append(int(a[1]))
    else:
        if a[0]=="pop":
            if len(e)>0:
                print(e.pop(0))
            else:print(-1)
        elif a[0]=="size":
            print(len(e))
        elif a[0]=="empty":
            if len(e)==0:
                print(1)
            else:
                print(0)
        elif a[0]=="front":
            print(e[0] if len(e)>0 else -1)
        elif a[0]=="back":
            print(e[-1] if len(e)>0 else -1)
