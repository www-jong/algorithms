for _ in range(3):
    N=int(input())
    res=0
    for i in range(N):
        res+=int(input())
    if res>0:
        print('+')
    elif res<0:
        print('-')
    else:
        print(0)