n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
res=0

for i in range(n):
    x=[0,0]
    y=[0,0]
    xf,yf=0,0
    for j in range(n):
        if grid[i][j]==x[1]:
            x[0]+=1
        else:
            x=[1,grid[i][j]]
        if not xf and x[0]>=m:
            res+=1
            xf=1
        if grid[j][i]==y[1]:
            y[0]+=1
        else:
            y=[1,grid[j][i]]
        if not yf and y[0]>=m:
            res+=1
            yf=1
    if not xf and x[0]>=m:
        res+=1
        xf=1
    if not yf and y[0]>=m:
        res+=1
        yf=1
print(res)