def solution(myString, pat):
    tmp=''
    for i in myString:
        if i=='A':
            tmp+='B'
        else:
            tmp+='A'
    if pat in tmp:
        return 1
    else:
        return 0