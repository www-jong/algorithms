def solution(s):
    answer = ''
    print(len(s),len(s)//2+(0 if len(s)%2 else -1),len(s)//2+(1 if len(s)%2 else 1))
    return s[len(s)//2+(0 if len(s)%2 else -1):len(s)//2+(1 if len(s)%2 else 1)]