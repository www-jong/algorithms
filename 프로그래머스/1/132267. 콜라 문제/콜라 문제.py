def solution(a, b, n):
    answer = 0
    while n>=a:
        c=(n//a)*b
        answer+=c
        n=(n%a)+c
        
    return answer