r=[2,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,14,13,12,11,10,9,8,7,6,5,4,3]
for i in range(int(input())):
    N=int(input())
    key=N%28
    ch="{0:b}".format(r[key]).zfill(4)
    for j in ch:
        if j=='0':
            print('V',end='')
        else:
            print('딸기',end='')
    print('')