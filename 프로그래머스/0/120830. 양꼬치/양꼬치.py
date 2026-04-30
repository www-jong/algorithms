def solution(n, k):
    answer = 12000*n+2000*(max(0,k-n//10))
    return answer