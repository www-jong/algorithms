def gcd(a,b):
    while b:
        a, b = b, a % b
    return a
def solution(a, b):
    g=gcd(a,b)
    a//=g
    b//=g
    while b%2==0:
        b//=2
    while b%5==0:
        b//=5
    return 1 if b==1 else 2