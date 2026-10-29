def solution(s):
    answer = True
    q=[]
    for i in s:
        if not q:
            q.append(i)
        else:
            if i=='(':
                q.append(i)
            else:
                if q[-1]=='(':
                    q.pop()
    
    return True if not q else False