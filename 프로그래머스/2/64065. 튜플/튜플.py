def solution(s):
    answer = []
    li=eval(s.replace("{","[").replace("}","]"))
    li.sort(key=lambda x:len(x))
    s=[]
    for i in li:
        s.append(set(i))
    v=[li[0].pop()]
    answer.append(v[0])
    for i in range(1,len(s)):
        for j in v:
            s[i].remove(j)
        now=s[i].pop()
        v.append(now)
        answer.append(now)
    return answer