def solution(dirs):
    d={"U":(-1,0),"D":(1,0),"L":(0,-1),"R":(0,1)}
    def to_1d(x,y):
        tx,ty=x+5,y+5
        return tx*11+ty

    answer = set()
    x,y=0,0
    for i in dirs:
        dir=d[i]
        nx,ny=x+dir[0],y+dir[1]
        if -5<=nx<=5 and -5<=ny<=5:
            a,b=to_1d(x,y),to_1d(nx,ny)
            answer.add((min(a,b),max(a,b)))
            x,y=nx,ny
    return len(answer)


print(solution("LULLLLLLU"))
