def solution(n, lost, reserve):
    li=[1]*(n+2)
    for i in lost:
        li[i]-=1
    for i in reserve:
        li[i]+=1
    
    for i in range(1,n+1):
        if li[i]==2 and not li[i-1]:
            li[i-1]+=1
            li[i]-=1
        elif li[i]==2 and not li[i+1]:
            li[i+1]+=1
            li[i]-=1
    return n-li.count(0)