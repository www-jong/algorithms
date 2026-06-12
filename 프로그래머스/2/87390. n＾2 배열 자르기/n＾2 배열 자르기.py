def solution(n, left, right):
    li=[]
    for i in range(left//n+1,right//n+2):
        li+=[i]*i
        for j in range(i+1,n+1):
            li.append(j)
    #print(li,(right//n-left//n+1)*n)
    return li[left%n:right-(left//n)*n+1]