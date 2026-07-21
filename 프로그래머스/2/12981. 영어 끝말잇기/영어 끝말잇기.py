def solution(n, words):
    d={words[0]}
    rnd,idx=1,1
    word=words[0]
    while rnd!=len(words)//n+1:
        for i in range(n):
            if rnd==1 and i==0:
                continue
            if words[idx] not in d and word[-1]==words[idx][0]:
                word=words[idx]
                d.add(word)
            else:
                return i+1,rnd
            idx+=1
        rnd+=1
    return 0,0