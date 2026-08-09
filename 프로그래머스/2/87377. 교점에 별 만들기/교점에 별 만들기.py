def solution(line):
    answer = []
    point=set()
    N=len(line)
    for i in range(N):
        for j in range(i+1,N):
            a,b,e=line[i]
            c,d,f=line[j]
            if (a*d)-(b*c)!=0:
                x=(b*f-e*d)/(a*d-b*c)
                y=(e*c-a*f)/(a*d-b*c)
            if int(x)==x and int(y)==y:
                x=int(x)
                y=int(y)
                point.add((x,y))
    x1=min(i[0] for i in point)
    x2=max(i[0] for i in point)
    y1=min(i[1]for i in point)
    y2=max(i[1]for i in point)

    for i in range(y2,y1-1,-1):
        tmp=''
        for j in range(x1,x2+1):
            if (j,i) in point:
                tmp+='*'
            else:
                tmp+='.'
        answer.append(tmp)


    return answer
