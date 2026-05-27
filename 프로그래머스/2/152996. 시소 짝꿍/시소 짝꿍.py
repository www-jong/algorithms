from collections import defaultdict
def solution(weights):
    res=0
    li=[0]*4001
    same=[0]*1001
    for weight in weights:
        a,b,c=weight*2,weight*3,weight*4
        res+=li[a]+li[b]+li[c]
        res-=same[weight]*2
        
        same[weight]+=1
        li[a]+=1
        li[b]+=1
        li[c]+=1
    return res