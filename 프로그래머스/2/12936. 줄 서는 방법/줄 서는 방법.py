import math
def solution(n, k):
    answer = []
    li=[i for i in range(1,n+1)]
    k-=1
    while li:
        now=k//math.factorial(n-1)
        answer.append(li[now])
        del li[now]
        k%=math.factorial(n-1)
        n-=1
    return answer