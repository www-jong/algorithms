from collections import defaultdict
from itertools import combinations
def solution(orders, course):
    answer = []
    d=defaultdict(int)
    max_n=0
    for i in range(len(orders)):
        tmp=''.join(sorted([j for j in orders[i]]))
        orders[i]=tmp
    for i in orders:
        max_n=max(max_n,len(i))
        for j in range(2,len(i)+1):
            for k in combinations(range(0,len(i)),j):
                tmp=''.join([i[z] for z in k])
                d[tmp]+=1
    li=[[] for _ in range(max_n+1)]
    check=[0]*(max_n+1)
    for k,v in d.items():
        if v>=2:
            if check[len(k)]<v:
                li[len(k)]=[k]
                check[len(k)]=v
            elif check[len(k)]==v:
                li[len(k)].append(k)
    for i in course:
        if i<=max_n:
            answer.extend(li[i])
    answer.sort()
    return answer