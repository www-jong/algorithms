def solution(babbling):
    answer = 0
    d={"aya","ye","woo","ma"}
    for i in babbling:
        idx=0
        now=''
        check=''
        while idx<len(i):
            now+=i[idx]
            if now in d and now!=check:
                check=now
                now=''

            idx+=1
        if not now:
            answer+=1
    return answer