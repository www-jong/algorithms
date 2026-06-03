def solution(numbers):
    N=len(numbers)
    answer = [-1]*N
    q=[]
    for i,j in enumerate(numbers):
        while q:
            x,y=q[-1]
            if j>y:
                answer[x]=j
                q.pop()
            else:
                break
        q.append((i,j))
    return answer