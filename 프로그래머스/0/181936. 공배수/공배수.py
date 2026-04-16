def solution(number, n, m):
    return [0,1][number%n==0 and number%m==0]