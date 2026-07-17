def solution(s):
    q=[]
    for i in range(len(s)):
        if not q:
            q.append(s[i])
        elif q[-1]==s[i]:
            q.pop()
        else:
            q.append(s[i])
    return 1 if not q else 0