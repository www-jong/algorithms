N=int(input())
li=list(map(int,input().split()))
print(*[i for i in li[::-1] if i%2==0])