def solution(rows, columns, queries):
    answer = []
    li=[[j for j in range(i,i+columns)] for i in range(1,rows*columns+1,columns)]
    def func(x1,y1,x2,y2):
        tmp=[]
        for i in range(x1,x2+1):
            tmp.append((i,y1))
        for i in range(y1+1,y2+1):
            tmp.append((x2,i))
        for i in range(x2-1,x1-1,-1):
            tmp.append((i,y2))
        for i in range(y2-1,y1,-1):
            tmp.append((x1,i))
        return tmp
    
    for x1,y1,x2,y2 in queries:
        x1-=1
        y1-=1
        x2-=1
        y2-=1
        now=func(x1,y1,x2,y2)
        tmp=li[now[0][0]][now[0][1]]
        min_v=tmp
        for i in range(len(now)-1):
            li[now[i][0]][now[i][1]]=li[now[i+1][0]][now[i+1][1]]
            min_v=min(min_v,li[now[i+1][0]][now[i+1][1]])
        li[now[-1][0]][now[-1][1]]=tmp
        answer.append(min_v)

    return answer