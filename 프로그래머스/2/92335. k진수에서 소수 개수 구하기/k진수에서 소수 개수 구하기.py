def solution(n, k):
    answer = 0
    def check(x):
        x=int(x)
        if x<2:
            return 0
        for i in range(2,int(x**0.5)+1):
            if x%i==0:
                return 0
        return 1

    tmp=''
    if k==10:
        tmp=str(n)
    else:
        while n>0:
            n,r=divmod(n,k)
            tmp=str(r)+tmp
    for i in tmp.split('0'):
        if i and check(i):
            answer+=1
    return answer