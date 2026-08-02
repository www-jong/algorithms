N = int(input())
records = input()
if N%2==1:
    print('No')
    exit()
res='Yes'
q=[]
a,b=0,0
for i in records:
    if i=='(':
        a+=1
        b+=1
    elif i==')':
        a-=1
        b-=1
    else:
        a-=1
        b+=1
    if b<0:
        res='No'
        break
    a=max(a,0)
if a!=0:
    res='No'

print(res)
