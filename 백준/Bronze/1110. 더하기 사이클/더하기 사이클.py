a=0
if (first:=int(input()))<10:
    first*=10
n=first
while True:
    n=(n%10+n//10)%10+(n%10)*10
    a+=1
    if n==first:
        print(a)
        break
    