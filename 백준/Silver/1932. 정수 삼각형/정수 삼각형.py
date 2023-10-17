n=int(input())
s=[0]*n
for i in range(n):
    s[i]=list(map(int,input().split()))
for i in range(n-2,-1,-1):
    for j in range(len(s[i])):
        s[i][j]=s[i][j]+max(s[i+1][j],s[i+1][j+1])
print(s[0][0])