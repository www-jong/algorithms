def solution(numbers, target):
    answer = 0
    N=len(numbers)
    dp=[{} for _ in range(N)]
    dp[0][numbers[0]]=1
    dp[0][-numbers[0]]=1
    for i in range(N):
        for k,v in dp[i-1].items():
            if k+numbers[i] in dp[i]:
                dp[i][k+numbers[i]]+=v
            else:
                dp[i][k+numbers[i]]=v
            if k-numbers[i] in dp[i]:
                dp[i][k-numbers[i]]+=v
            else:
                dp[i][k-numbers[i]]=v

    return dp[N-1][target]

print(solution([1, 1, 1, 1, 1],3))