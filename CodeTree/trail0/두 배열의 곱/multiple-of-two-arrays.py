li1=[list(map(int,input().split())) for _ in range(3)]
input()
li2=[list(map(int,input().split())) for _ in range(3)]

for i in range(3):
    for j in range(3):
        print(li1[i][j]*li2[i][j],end=' ')
    print()