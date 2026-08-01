def solution(n):
    li=[0]*n
    def check(x,y,li):
        for i in range(x):
            if y==li[i] or abs(y-li[i])==x-i:
                return 0
        return 1
    
    def func(x,li):
        if x==n:
            return 1
        cnt=0
        for i in range(n):
            if check(x,i,li):
                li[x]=i
                cnt+=func(x+1,li)
        return cnt

    answer = func(0,li)
    return answer