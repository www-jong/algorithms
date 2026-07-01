from itertools import combinations
def solution(relation):
    answer=0
    def func(x):
        tmp=set()
        for i in range(len(relation)):
            c=''
            for j in x:
                c+='_'+relation[i][j]
            if c not in tmp:
                tmp.add(c)
            else:
                return 0
        return 1

    def func2(x):
        for i in range(1,len(x)):
            for j in combinations(x,i):
                if j in d:
                    return 0
        return 1

    N=len(relation[0])
    d=set()
    for i in range(N):
        if func((i,)):
            d.add((i,))
            answer+=1

    for i in range(2,N+1):
        for j in combinations([i for i in range(N) if i not in d],i):
            if func(j) and func2(j):
                d.add(j)
                answer+=1

    return answer