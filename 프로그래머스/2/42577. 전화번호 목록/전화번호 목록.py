def solution(phone_book):
    d={}
    for i,j in enumerate(phone_book):
        d[j]=i
    for i,j in enumerate(phone_book):
        tmp=''
        for k in j:
            tmp+=k
            if tmp in d and d[tmp]!=i:
                return False
    return True