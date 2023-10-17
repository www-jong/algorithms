#1004번
t=int(input())
n=0
for i in range(1,t+1):
    sx,sy,ex,ey=map(int,input().split())
    n=int(input())
    planet=[]
    count=0
    for j in range(1,n+1):
        x,y,r=map(int,input().split())
        r1=(abs(sy-y)**2+abs(sx-x)**2)**0.5
        r2=(abs(ey-y)**2+abs(ex-x)**2)**0.5
        count+=(1 if r2<r else 0) if r1> r else (1 if r2>r else 0)
    print(count)
    