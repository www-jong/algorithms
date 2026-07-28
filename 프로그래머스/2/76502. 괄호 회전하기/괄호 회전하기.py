from collections import deque
def solution(s):
    def check(s):
        q=[]
        for i in s:
            if i in "()":
                if i=="(":
                    q.append(1)
                elif not q or q[-1]!=1:
                    return 0
                else:
                    q.pop()
            elif i in "[]":
                if i=="[":
                    q.append(2)
                elif not q or q[-1]!=2:
                    return 0
                else:
                    q.pop()
            else:
                if i=="{":
                    q.append(3)
                elif not q or q[-1]!=3:
                    return 0
                else:
                    q.pop()
        return 0 if q else 1
    check(s)
    dq=deque([i for i in s])
    answer =0
    for i in range(len(s)):
        dq.append(dq.popleft())
        answer+=check(dq)
    return answer