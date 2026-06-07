def solution(cards): 
    answer = 0
    N=len(cards)
    visit=[0]*N
    li=[]
    for i in range(N):
        now=i
        cnt=0
        while True:
            if visit[now]:
                break
            visit[now]=1
            cnt+=1
            now=cards[now]-1
        if cnt:
            li.append(cnt)
    li.sort(reverse=True)
    if len(li)>=2:
        answer=li[0]*li[1]
    return answer