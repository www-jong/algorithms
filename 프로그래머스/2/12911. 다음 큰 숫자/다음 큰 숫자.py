def solution(n):
    x=n+1
    while True:
        if bin(x).count('1')==bin(n).count('1'):
            return x
        x+=1