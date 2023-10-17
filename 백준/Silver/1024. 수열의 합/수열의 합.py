N,L=map(int,input().split())

for i in range(L,101):
    x=N-(i*(i+1)/2)
    if x%i==0:
        x=int(x//i)
        if (x+1)>=0:
            for j in range(1,i+1):
                print(x+j,end=' ')
            print()
            break
else:
    print(-1)

'''
N=(x+1)+(x+2)...(X+L)
=Lx+(1+2+3+4...L-1)
=Lx+(L-1)L/2
=Lx+t

'''