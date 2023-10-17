
N=int(input())
li=list(map(int,input().split()))

if li[-1]<0:
    print(-1)
else:
    res=[0]*(N)
    adds,minus=N,1
    for i in range(N):
        if li[i]>0:
            res[i]=adds
            adds-=1
        else:
            res[i]=minus
            minus+=1

    print(*res)

