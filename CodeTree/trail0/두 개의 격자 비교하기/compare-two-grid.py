N,M=map(int,input().split())
li1=[list(map(int,input().split())) for _ in range(N)]
li2=[list(map(int,input().split())) for _ in range(N)]
for i in range(N):
    for j in range(M):
        print(0 if li1[i][j]==li2[i][j] else 1,end=' ')
    print()