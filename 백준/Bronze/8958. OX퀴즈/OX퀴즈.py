n=int(input())
for i in range(n):
    a=str(input())
    point=0
    arr=[]
    for j in a:
        if len(arr)==0:
            if j=='O':
                arr.append(1)
            else:arr.append(0)
        elif j=='O':
            arr.append(arr[-1]+1)
        else:arr.append(0)
    print(sum(arr))
            
            