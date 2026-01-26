for _ in range(3):
    N=input()
    l=0
    cnt=1
    for i in range(1, len(N)):
        if N[i-1]==N[i]:
            cnt+=1
        else:
            cnt=1
        if cnt>l:
            l=cnt
    print(l)