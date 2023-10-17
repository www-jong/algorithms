def h(n,f,t,a):
 if n==1:print(f,t);return
 h(n-1,f,a,t);print(f,t);h(n-1,a,t,f)
n=int(input());print(2**n-1);h(n,1,3,2)
