from itertools import combinations
def solution(n, q, ans):
    m=len(q)
    res=0
    def check(now):
        tmp=[0]*m
        for i in now:
            for idx,j in enumerate(s):
                if i in j:
                    tmp[idx]+=1
        for i in range(m):
            if tmp[i]!=ans[i]:
                return 0
        return 1
    s=[set(i) for i in q]
    for i in combinations(range(1,n+1),5):
        if check(i):
            res+=1
    return res