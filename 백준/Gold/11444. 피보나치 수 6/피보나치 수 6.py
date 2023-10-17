N=int(input())
p=1000000007
dic={}
def doganu(g):
    if g in dic:
        return dic[g]
    if g==1 or g==2:
        return 1
    if g==3:
        return 2
    if g==4:
        return 3
    if g%2==0:
        m=g//2
        m1=doganu(m-1)
        m2=doganu(m)
        m3=m1+m2
        fir=m1*m2%p
        sec=m2*m3%p
    else:
        m=g//2+1
        n=m-1
        m1=doganu(n)
        m2=doganu(m)
        fir=m1*m1%p
        sec=m2*m2%p
    ans=(fir+sec)%p
    if g in dic:
        return ans
    else:
        dic[g]=ans
        return ans
print(doganu(N))
