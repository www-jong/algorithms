def func(s):
    global res
    if len(s)==1:
        res='AKARAKA'
        return
    else:
        if s!=s[::-1]:
            return
        else:
            N=len(s)//2
            func(s[:N])
            func(s[-N:])
S=input()
res='IPSELENTI'
func(S)
print(res)
