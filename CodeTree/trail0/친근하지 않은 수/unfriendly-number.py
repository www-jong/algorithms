N=int(input())
r=0
for i in range(1,N+1):
    if not(i%2==0 or i%3==0 or i%5==0):
        r+=1
print(r)