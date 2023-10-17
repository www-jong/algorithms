n=int(input())
a=2
while True:
    if n%a==0:
        print(a)
        n=n/a
    elif n==1:
        break
    else:
        a+=1