n=int(input())
n_arr=list(map(int,str(n)))
if n<18:
    m=n-9*(len(n_arr)-1)
elif n<1000:
    m=n-9*(len(n_arr))
else:
    m=n-1000
ch=0
if n<=9:
    if n%2==0:
        print(int(n/2))
        ch=1
    else:
        ch=0
else:
    for i in range(m,n+1):
        m_s=i+sum([int(j) for j in str(i)])
        if n==m_s:
            print(i)
            ch=1
            break
if ch==0:
    print("0")
    