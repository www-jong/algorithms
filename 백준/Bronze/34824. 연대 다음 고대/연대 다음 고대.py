N=int(input())
a,b=0,0
for i in range(N):
    S=input()
    if S=='yonsei':
        a=i
    elif S=='korea':
        b=i
print('Yonsei Won!' if a<b else 'Yonsei Lost...')