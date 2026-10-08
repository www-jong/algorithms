def solution(user_id, banned_id):
    answer = 0
    tmp=set()
    def func(idx,now):
        if idx==M:
            tmp.add(tuple(sorted(list(now))))
            return
        for i in li[idx]-now:
            func(idx+1,now.union({i}))
    
    N,M=len(user_id),len(banned_id)
    li=[set() for _ in range(M)]
    for i in range(M):
        ban_word=banned_id[i]
        now=[]
        for word in user_id:
            f=0
            if len(word)!=len(ban_word):
                continue
            for idx in range(len(word)):
                if ban_word[idx]!='*' and word[idx]!=ban_word[idx]:
                    break
            else:
                li[i].add(word)
    func(0,set())
    print(li,len(tmp))
    return len(tmp)