import sys
input=sys.stdin.readline

N=int(input())
li=[]
for i in range(N):
    li.append(list(map(int,input().split())))

li.sort()
res=li[0][1]-li[0][0]
b_x,b_y=li[0]
for x,y in li[1:]:
    if x<=b_y:
        if y>b_y:
            res+=y-x-(b_y-x)
        else:
            continue
    elif x>b_y:
        res+=y-x
    b_x,b_y=x,y
print(res)