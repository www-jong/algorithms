N=int(input())

for i in range(N,101):
    r='F'
    if i>=90:
        r='A'
    elif i>=80:
        r='B'
    elif i>=70:
        r='C'
    elif i>=60:
        r='D'
    print(r,end=' ')