def so(n):
    N=int(n**0.5)+1
    check=[1]*(n+1)
    check[0]=0
    check[1]=0
    for i in range(2,N):
        if check[i]:
            for j in range(i*i,n+1,i):
                check[j]=0
    return sum(check)
def solution(n):
    answer = so(n)
    return answer