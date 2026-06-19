A,B=map(int,input().split())
N=A
while N<=B:
    print(N,end=' ')
    if N%2:
        N*=2
    else:
        N+=3