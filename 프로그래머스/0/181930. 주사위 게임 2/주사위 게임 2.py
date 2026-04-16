def solution(a, b, c):
    A,B,C=a+b+c,a**2+b**2+c**2,a**3+b**3+c**3
    answer = 0
    if a==b==c:
        answer=A*B*C
    elif a==b or b==c or a==c:
        answer=A*B
    else:
        answer=A
    return answer