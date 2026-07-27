def solution(n, info):
    answer = [-1,[]]
    def calc(a,b):
        A,B=0,0
        for i in range(11):
            if a[i]>=b[i] and a[i]!=0:
                A+=10-i
            elif a[i]<b[i] and b[i]!=0:
                B+=10-i
        return A,B

    def func(cnt,idx,point,li):
        nonlocal answer
        if cnt==n or idx==11:
            res=li[:]
            if idx==11 and cnt<n:
                res[10]=n-cnt
            A,B=calc(info,res)
            if B>A:
                if B-A>answer[0]:
                    answer=[B-A,res[:]]
                elif B-A==answer[0]:
                    for i in range(10,-1,-1):
                        if res[i]>answer[1][i]:
                            answer[1]=res
                            break
                        elif res[i]<answer[1][i]:
                            break
            return

        func(cnt,idx+1,point,li)
        if cnt+d[10-idx]<=n:
            li[idx]=d[10-idx]
            point+=10-idx
            func(cnt+d[10-idx],idx+1,point,li)
            point-=10-idx
            li[idx]-=d[10-idx]

    d={}
    for i,j in enumerate(info):
        d[10-i]=j+1
    func(0,0,0,[0]*11)
    return answer[1] if answer[0]!=-1 else [-1]
