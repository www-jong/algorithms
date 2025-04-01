S=input()
key=input()
key=key*(len(S)//len(key)+1)
t=[97+i for i in range(26)]
res=''
for i in range(len(S)):
    if S[i]==' ':
        res+=' '
    else:
        res+=chr(t[ord(S[i])-ord(key[i])-1])
print(res)