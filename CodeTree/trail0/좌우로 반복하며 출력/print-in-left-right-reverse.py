N=int(input())
for i in range(N):
    if i%2:
        print(*[i for i in range(1,N+1)][::-1],sep='')
    else:
        print(*[i for i in range(1,N+1)],sep='')