n=int(input())
li=[10000]*(5000//3+1)
for i in range(0,n//3+1):
    m=n
    if m==3*i:
        li[i]=i
    else:
        m=n-3*i
        for j in range(1,m//5+1):
            if m==5*j and li[i]>(j+i):
                li[i]=j+i

min=min(li)
if min==10000:
    print(-1)
else:
    print(min)