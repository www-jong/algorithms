N=int(input())
li=[int(input()) for _ in range(N)]
M=int(input())
res=sum([li[int(input())-1] for _ in range(M)])
print(res)
