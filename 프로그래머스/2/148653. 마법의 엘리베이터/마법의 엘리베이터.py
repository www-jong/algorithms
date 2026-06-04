def solution(storey):
    res=0
    while storey:
        now=storey%10
        if now>5:
            res+=(10-now)
            storey+=10
        elif now<5:
            res+=now
        else:
            if storey//10%10>4:
                storey+=10
            res+=now
        storey//=10
    return res