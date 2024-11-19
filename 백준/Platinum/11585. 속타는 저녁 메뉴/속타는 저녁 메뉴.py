import math
def KMP_table(pattern):
    len_pattern=len(pattern)
    tmp_table=[0]*len_pattern

    p_idx=0
    for idx in range(1,len_pattern):
        while p_idx>0 and pattern[idx]!=pattern[p_idx]:
            p_idx=tmp_table[p_idx-1]

        if pattern[idx]==pattern[p_idx]:
            p_idx+=1
            tmp_table[idx]=p_idx
    return tmp_table

def KMP(word, pattern):
    table=KMP_table(pattern)

    res=[]
    p_idx=0

    for idx in range(len(word)):
        while p_idx>0 and word[idx]!=pattern[p_idx]:
            p_idx=table[p_idx-1]

        if word[idx]==pattern[p_idx]:
            if p_idx==len(pattern)-1:
                res.append(idx-len(pattern)+2)
                p_idx=table[p_idx]
            else:
                p_idx+=1
    return res
def gcd(a,b):
    if b>0:
        a,b=b,a%b
    return a
N=int(input())
P=''.join(input().split())
S=''.join(input().split())

S+=S[:-1]
v=len(KMP(S,P))
g=gcd(N,v)
print(f'{v//g}/{N//g if N//g else 1}')
