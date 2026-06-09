n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
d=[[(0,0),(0,1),(0,2)],[(0,0),(1,0),(2,0)],[(0,0),(0,1),(1,1)],[(0,0),(0,1),(1,0)],[(0,0),(1,0),(1,1)],[(0,0),(0,1),(-1,1)]]

res=0
for x in range(n):
    for y in range(m):
        for i in d:
            now=0
            for dx,dy in i:
                nx,ny=x+dx,y+dy
                if 0<=nx<n and 0<=ny<m:
                    now+=grid[nx][ny]
                else:
                    break
            else:
                res=max(res,now)
print(res)
