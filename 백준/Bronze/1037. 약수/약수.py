a=int(input())
n=list(map(int,input().split()))
print(n[0]**2 if a==1 else min(n)*max(n))