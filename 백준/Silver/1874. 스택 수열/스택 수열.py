import sys
li=[]
li2=[]
n=int(sys.stdin.readline())
count=1
check=0
for i in range(n):
    s=int(sys.stdin.readline())
    while count<=s:
        li.append(count)
        li2.append('+')
        count+=1
    if li[-1]==s:
        li.pop()
        li2.append('-')
    else:
        check=1
if check==1:
    print("NO")
else:
    print(*li2,sep='\n')



    
    