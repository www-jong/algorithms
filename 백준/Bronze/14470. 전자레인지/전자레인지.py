A=int(input())
B=int(input())
C=int(input())
D=int(input())
E=int(input())
res=0
if A<0:
    res+=C*abs(A)+D+B*E
else:
    res+=(B-A)*E

print(res)