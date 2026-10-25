n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
d=[(-1,1),(-1,-1,),(1,-1),(1,1)]
res=0
def func(x,y,w,h):
    tmp=0
    for idx,cnt in enumerate([w,h,w,h]):
        for _ in range(cnt):
            x+=d[idx][0]
            y+=d[idx][1]
            if not (0<=x<n and 0<=y<n):
                return 0
            tmp+=grid[x][y]

    return tmp

for x in range(n):
    for y in range(n):
        for w in range(1,n):
            for h in range(1,n):
                res=max(res,func(x,y,w,h))
print(res)