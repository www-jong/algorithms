def solution(number, limit, power):
    answer = 0
    c=[0]*(number+1)
    for i in range(1,number+1):
        for j in range(i,number+1,i):
            c[j]+=1
    for i in range(1,number+1):
        if c[i]<=limit:
            answer+=c[i]
        else:
            answer+=power
    return answer