def solution(n):
    answer = 0
    li=[0]*(n+1)
    for i in range(1,n+1):
        li[i]=li[i-1]+i

    st,end=0,0
    while st<=end:
        if end==n+1:
            break
        now=li[end]-li[st]
        if now<=n:
            if now==n:
                answer+=1
            end+=1
        else:
            st+=1
    return answer

print(solution(15))