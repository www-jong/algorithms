def gcd(a,b):
    while b>0:
        a,b=b,a%b
    return a
def lcm(a,b):
    return abs(a*b)//gcd(a,b)
def solution(n, m):
    answer = []
    return [gcd(n,m),lcm(n,m)]