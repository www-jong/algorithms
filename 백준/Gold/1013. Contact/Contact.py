import sys,re
input=sys.stdin.readline

T=int(input())
for i in range(T):
    S=input().rstrip()
    p=re.compile('(100+1+|01)+')
    print('YES' if p.fullmatch(S) else 'NO')