def solution(n,a,b):
    answer = 1
    a,b=min(a,b),max(a,b)
    while True:
        if abs(a-b)==1 and a%2==1:
            return answer
        a=a//2+a%2
        b=b//2+b%2
        answer+=1