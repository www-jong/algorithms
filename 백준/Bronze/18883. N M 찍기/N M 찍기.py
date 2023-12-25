N,M=map(int,input().split())

c=1
for i in range(N):
    for j in range(M):
        if j!=M-1:
            print(c,end=" ")
        else:
            print(c,end="")
        c+=1
    print()