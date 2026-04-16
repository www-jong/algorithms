def solution(n):
    answer = 0
    if n%2:
        answer=sum([i for i in range(1,n+1,2)])
    else:
        answer=sum([i**2 for i in range(0,n+1,2)])
    return answer