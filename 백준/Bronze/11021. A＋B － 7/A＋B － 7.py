n=int(input())
for i in range(1,n+1):
    print("Case #{0}: {1}".format(i,sum(map(int,input().split()))))