from itertools import product
def solution(word):
    li=[]
    d=['A','E','I','O','U']
    for i in range(5):
        for j in product(d,repeat=i+1):
            li.append(''.join(j))
    li.sort()
    return li.index(word)+1