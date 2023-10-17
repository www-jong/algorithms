n=int(input())
a=2
for i in range(100000):
    if n==1:
        print(n)
        break
    elif n>=a and n<=a+i*6-1:
        print(i+1)
        break
    a+=i*6