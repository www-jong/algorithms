def solution(s):
    answer = ''
    s=s.lower()
    c=0
    for i in range(len(s)):
        if c==0:
            if s[i].islower():
                answer+=s[i].upper()
            else:
                answer+=s[i]
            if s[i]!=' ':
                c=1
        else:
            if s[i]==' ':
                c=0
            answer+=s[i]
    return answer