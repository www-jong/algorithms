import sys
input=sys.stdin.readline
n=int(input())
li=[]
for i in range(n):
    a,b=map(int,input().split())
    li.append([a,b])
li.sort(key=lambda x:x[0])
li.sort(key=lambda x:x[1])

count=1
end=li[0][1]
for i in range(1,n):
    if li[i][0]>=end:
        count+=1
        end=li[i][1]
print(count)