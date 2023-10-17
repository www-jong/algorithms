n=int(input())
dp=[0]*(n+1)
li=[i**2 for i in range(1,317)]
for i in range(1,n+1):
    temp=[]
    for j in li:
        if j>i:
            break
        temp.append(dp[i-j])
    dp[i]=min(temp)+1
print(dp[n])
