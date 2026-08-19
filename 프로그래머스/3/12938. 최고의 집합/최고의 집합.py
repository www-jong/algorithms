import math
def solution(n, s):
    if n>s:
        return [-1]
    answer = [0]*n
    v=math.ceil(s/n)
    print(v)
    tmp=v*n-s
    for i in range(n):
        answer[i]=v
        if tmp>0:
            answer[i]-=1
            tmp-=1
    
    return answer