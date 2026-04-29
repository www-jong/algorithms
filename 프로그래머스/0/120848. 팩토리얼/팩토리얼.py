def solution(n):
    now=1
    idx=1
    while True:
        print(idx,now,idx*now)
        now*=idx
        if now>n:
            return idx-1
        idx+=1
    return answer