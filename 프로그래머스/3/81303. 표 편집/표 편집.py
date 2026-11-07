def solution(n, k, cmd):
    le=[i-1 for i in range(n)]
    ri=[i+1 for i in range(n)]
    ri[-1]=-1
    answer=['O']*n
    stk=[]
    now=k
    for i in cmd:
        if i[0]=='U':
            for _ in range(int(i[2:])):
                now=le[now]
        elif i[0]=='D':
            for _ in range(int(i[2:])):
                now=ri[now]
        elif i[0]=='C':
            l,r=le[now],ri[now]
            stk.append((now,l,r))
            answer[now]='X'
            if l!=-1:
                ri[l]=r
            if r!=-1:
                le[r]=l
            now=r if r!=-1 else l
        elif i[0]=='Z':
            idx,l,r=stk.pop()
            answer[idx]='O'
            if l!=-1:
                ri[l]=idx
            if r!=-1:
                le[r]=idx
    return ''.join(answer)