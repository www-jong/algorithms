from collections import deque
def solution(places):
    answer = []
    d=[0,0,1,-1]
    
    for place in places:
        flag=1
        for x in range(5):
            for y in range(5):
                if place[x][y] in 'OX':
                    continue
                visit=[[0]*5 for _ in range(5)]
                visit[x][y]=1
                q=deque()
                q.append((x,y,0))
                while q:
                    nx,ny,c=q.popleft()
                    for i in range(4):
                        dx,dy=nx+d[i],ny+d[3-i]
                        if 0<=dx<5 and 0<=dy<5 and place[dx][dy]!='X' and not visit[dx][dy]:
                            if place[dx][dy]=='P' and c<2:
                                flag=0
                                break
                            else:
                                visit[dx][dy]=c+1
                                q.append((dx,dy,c+1))
                if not flag:
                    break
            if not flag:
                break
        answer.append(flag)
                            
    return answer