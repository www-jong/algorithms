def solution(s):
    def comp(A,B):
        if A==B:
            return 1

        return 0
    answer = 0
    res=set()
    for i in range(1,len(s)+1):
        tmp=''
        now=s[:i]
        chk=1
        for j in range(i*2,len(s)+1,i):
            if comp(now,s[j-i:j]):
                chk+=1
            else:
                tmp+=(str(chk)if chk!=1 else'')+now
                now=s[j-i:j]
                chk=1
        tmp+=(str(chk)if chk!=1 else'')+now
        tmp+=s[(len(s)//i)*i:]
        res.add(tmp)
    res=sorted(list(res),key=lambda x:len(x))
    return len(res[0])
