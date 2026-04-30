def solution(n, w, num):
    answer = 1
    li=[[0]*(w) for _ in range(n//w+1)]
    f=0
    tar=[0,0]
    for i in range(1,n+1):
        x=(i-1)//w
        y=w-1-((i-1)%w) if f else (i-1)%w
        li[x][y]=i
        if num==i:
            tar=[x,y]
        if i%w==0:
            f^=1

    for i in li:
        print(i)
    print(tar)
    for i in range(tar[0]+1,len(li)):
        if li[i][tar[1]]!=0:
            answer+=1
    return answer