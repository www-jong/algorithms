li=list(map(int,input().split()))
for i in range(2,10):
    li.append((li[i-2]+li[i-1])%10)
print(*li)