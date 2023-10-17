now=4
for i in range(10):
    t=input()
    if t=="1":
        if now==4:
            now=1
        else:
            now+=1
    elif t=="2":
        if now==2:
            now=4
        elif now==3:
            now=1
        elif now==1:
            now=3
        elif now==4:
            now=2
    elif t=="3":
        if now==1:
            now=4
        else:
            now-=1
if now==1:
    print("E")
elif now==2:
    print("S")
elif now==3:
    print("W")
else:
    print("N")