maps=[[0]*(10)]
emp=[]
for i in range(9):
    tmp=list(map(int,input().split()))
    for j in range(9):
        if tmp[j]==0:
            emp.append((i+1,j+1))
    maps.append([0]+tmp)

def check(a,b):
    re=set([1,2,3,4,5,6,7,8,9])
    tmp1=[]
    tmp2=[]
    tmp3=[]
    check=0
    ans=[]
    for i in range(1,10):
        if b!=i:
            tmp1.append(maps[a][i])
        if a!=i:
            tmp2.append(maps[i][b])
        if (((a-1)//3)*3+1+(i-1)//3,((b-1)//3)*3+1+(i-1)%3)!=(a,b):
            tmp3.append(maps[((a-1)//3)*3+1+(i-1)//3][((b-1)//3)*3+1+(i-1)%3])
    ans=list(re-set(tmp1)-set(tmp2)-set(tmp3))
    return ans
def mapcheck(maps):
    return True
def func(idx):
    if idx==(len(emp)):
        if mapcheck(maps):
            for i in range(1,10):
                print(*maps[i][1:10])
            exit(0)
        else:
            return
    aval=check(emp[idx][0],emp[idx][1])
    for i in aval:
        maps[emp[idx][0]][emp[idx][1]]=i
        func(idx+1)
        maps[emp[idx][0]][emp[idx][1]]=0
func(0)