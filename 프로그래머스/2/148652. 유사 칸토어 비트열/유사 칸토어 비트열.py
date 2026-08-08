def solution(n, l, r):
    answer = 0
    def func(n,a):
        if n==1:
            return a if a<=2 else a-1
        div=5**(n-1)
        mul=4**(n-1)
        loc=a//div
        if a%div==0:
            loc-=1
        if loc<2:
            return mul*loc+func(n-1,a-loc*div)
        elif loc==2:
            return mul*loc
        else:
            return mul*(loc-1)+func(n-1,a-loc*div)
        
    return func(n,r)-func(n,l-1)