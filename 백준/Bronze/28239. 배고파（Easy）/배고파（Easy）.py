N=int(input())

def bitcount(n):
    if n==0:
        return 0
    return n%2+bitcount(n//2)

for i in range(N):
    M=int(input())
    if M==1:
        print(0,0)
        continue
    m=bin(M)[-1:1:-1]

    if m.count('1')>=2:
        x=m.find('1')
        y=m.find('1',x+1)
        print(x,y)
    elif m.count('1')==1:
        x=m.find('1')
        print(x-1,x-1)