s=input()
ans=[-1 for i in range(26)]
count=0
for i in s:
    if ans[ord(i)-97] ==-1:
        ans[ord(i)-97]=count
    count+=1
print(*ans)

