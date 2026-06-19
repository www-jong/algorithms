N=int(input())
li=[[0]*N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if i%2==0:
            li[j][i]=j+1
        else:
            li[j][i]=N-j

for i in li:
    print(*i,sep='')