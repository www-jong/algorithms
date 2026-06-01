from collections import defaultdict
def solution(want, number, discount):
    res=0
    def check():
        for k,v in d1.items():
            if k not in d2 or d2[k]!=v:
                return 0
        return 1
    d1,d2=defaultdict(int),defaultdict(int)
    for i,j in enumerate(want):
        d1[j]=number[i]
    for i in range(10):
        d2[discount[i]]+=1
    res+=check()
    for i in range(10,len(discount)):
        d2[discount[i-10]]-=1
        d2[discount[i]]+=1
        res+=check()
    return res