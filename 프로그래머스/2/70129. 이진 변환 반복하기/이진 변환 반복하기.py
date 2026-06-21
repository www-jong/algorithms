def solution(s):
    a=0
    b=0
    while s!='1':
        a+=1
        cnt=s.count('1')
        b+=len(s)-cnt
        s=bin(cnt)[2:]
    return [a,b]