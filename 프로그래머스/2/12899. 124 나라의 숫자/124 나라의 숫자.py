def solution(n):
    answer = ''
    tmp='412'
    while n>0:
        n,c=divmod(n,3)
        answer=tmp[c]+answer
        if c==0:
            n-=1
    return answer