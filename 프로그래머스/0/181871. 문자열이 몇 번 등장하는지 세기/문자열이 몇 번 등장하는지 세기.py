def solution(myString, pat):
    res=0
    for i in range(len(myString)-len(pat)+1):
        if myString[i:i+len(pat)]==pat:
            res+=1
    return res