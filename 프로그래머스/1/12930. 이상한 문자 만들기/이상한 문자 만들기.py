def solution(s):
    answer = ''
    c=0
    for i in range(len(s)):
        if c==0 and s[i]!=' ':
            c=1
            answer+=s[i].upper()
        elif c!=0 and s[i]!=' ':
            if c%2:
                answer+=s[i].lower()
            else:
                answer+=s[i].upper()
            c+=1
        else:
            answer+=' '
            c=0
    return answer