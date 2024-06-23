s=''
while True:
    s+='\n'
    try:
        s+=input()
    except:
        break
s=s.lstrip()
ls=list(s)
res=list(s.lower())
c=0
for i in range(len(ls)):
    if c==1 and ls[i].isalpha():
        res[i]=ls[i].upper()
        c=0
    elif c==1 and ls[i-1].isnumeric():
        c=0
    if ls[i] in '.?!':
        c=1
print(*res[:-1],sep="")