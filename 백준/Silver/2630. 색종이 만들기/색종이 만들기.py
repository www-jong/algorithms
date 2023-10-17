n=int(input())
maps=[[0]*(n+1)]

for i in range(n):
    maps.append([0]+list(map(int,input().split())))

white=0
blue=0

def func(st,en):
    global white,blue
    tmp=0
    half=(en[0]-st[0]+1)//2
    if st==en:
        if maps[en[0]][en[1]]==1:
            blue+=1
        else:
            white+=1
    else:
        for i in range(st[0],en[0]+1):
            for j in range(st[1],en[1]+1):
                tmp+=maps[i][j]
        if tmp==((half*2)**2):
            blue+=1
        elif tmp==0:
            white+=1
        else:
            func((st[0],st[1]),(en[0]-half,en[1]-half))
            func((st[0],st[1]+half),(en[0]-half,en[1]))
            func((st[0]+half,st[1]),(en[0],en[1]-half))
            func((st[0]+half,st[1]+half),(en[0],en[1]))
func((1,1),(n,n))
print(white)
print(blue)