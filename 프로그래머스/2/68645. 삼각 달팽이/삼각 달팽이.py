def solution(n):
    li=[[0]*(i) for i in range(1,n+1)]
    m=sum([i for i in range(1,n+1)])
    idx=0
    d=[(1,0),(0,1),(-1,-1)]
    cnt,now=n,0
    x,y=0,0
    for i in range(1,m+1):
        li[x][y]=i
        now+=1
        if cnt==now:
            cnt-=1
            now=0
            idx=(idx+1)%3
        x+=d[idx][0]
        y+=d[idx][1]
            
    answer=[]
    for i in li:
        answer.extend(i)
    return answer