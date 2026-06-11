def solution(m, n, startX, startY, balls):
    def func(x,y,a,b):
        return abs(x-a)**2+abs(y-b)**2
    answer = []
    for x,y in balls:
        li=[]
        if not (startY == y and startX > x):
            li.append((-x, y))
        if not (startY == y and startX < x):
            li.append((2 * m - x, y))
        if not (startX == x and startY > y):
            li.append((x, -y))
        if not (startX == x and startY < y):
            li.append((x, 2 * n - y))
        
        v=func(startX,startY,x,y)
        r=10**9
        for nx,ny in li:
            now=func(startX,startY,nx,ny)
            if now!=v and now<r:
                r=now
        answer.append(r)
        
    return answer