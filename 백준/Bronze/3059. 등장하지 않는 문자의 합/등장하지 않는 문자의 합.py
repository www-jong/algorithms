for _ in range(int(input())):
    s=set(list(input()))
    res=2015
    for i in s:
        res-=ord(i)
    print(res)