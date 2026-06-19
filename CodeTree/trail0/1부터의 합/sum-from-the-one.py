N=int(input())
r=0
for i in range(1,101):
    r+=i
    if r>=N:
        print(i)
        break