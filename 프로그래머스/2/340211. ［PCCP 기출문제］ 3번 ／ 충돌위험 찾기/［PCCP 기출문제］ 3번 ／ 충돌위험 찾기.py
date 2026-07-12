def solution(points, routes):
    def func(a,b,flag=0):
        x1,y1=a
        x2,y2=b
        path=[(x1,y1)]
        while x1!=x2:
            x1+=1 if x1<x2 else -1
            path.append((x1,y1))

        while y1!=y2:
            y1+=1 if y1<y2 else -1
            path.append((x1,y1))
        if flag:
            return path[1:]
        return path
    answer = 0
    d={}
    for i,route in enumerate(routes):
        tmp=[]
        for j in range(len(route)-1):
            st,end=j,j+1
            tmp+=func(points[route[st]-1],points[route[end]-1],0 if j==0 else 1)
        for idx,j in enumerate(tmp):
            if idx not in d:
                d[idx]={j:1}
            else:
                if j not in d[idx]:
                    d[idx][j]=1
                else:
                    d[idx][j]+=1
    for k,v in d.items():
        for k2,v2 in v.items():
            if v2>=2:
                answer+=1
    return answer
