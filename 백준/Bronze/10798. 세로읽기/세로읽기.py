li=['']*15
n=0
for i in range(5):
    s=input()
    for j in range(len(s)):
        li[j]+=s[j]
print(*li,sep="")
