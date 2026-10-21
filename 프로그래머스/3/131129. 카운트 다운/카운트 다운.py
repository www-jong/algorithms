def solution(target):
    answer = []
    INF=float('inf')
    dp=[(INF,0)for _ in range(target+1)]
    dp[0]=(0,0)
    
    point=[(50,1)]
    for i in range(1,21):
        point.append((i,1))
        point.append((i*2,0))
        point.append((i*3,0))
    for i in range(1,target+1):
        for j,k in point:
            if i<j:
                continue
            cnt=dp[i-j][0]+1
            bull=dp[i-j][1]+k
            if cnt<dp[i][0]:
                dp[i]=(cnt,bull)
            elif cnt==dp[i][0]:
                dp[i]=(cnt,max(dp[i][1],bull))
    return list(dp[target])