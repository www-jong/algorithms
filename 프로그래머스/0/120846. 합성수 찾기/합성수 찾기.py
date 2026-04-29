def so(n):
    check=[1]*(n+1)
    check[1],check[0]=0,0
    for i in range(2,int(n**0.5)+1):
        if check[i]:
            for j in range(i*2,n+1,i):
                check[j]=0
    so=[]
    for i in range(2,n+1):
        if check[i]:
            so.append(i)
    return so
def solution(n):
    print(len(so(n)))
    answer = 0
    return n-len(so(n))-1