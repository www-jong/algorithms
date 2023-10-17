arr=[[i for i in range(15)] for i in range(15)]
for i in range(1,15):
    for j in range(1,15):
        arr[j][i]=arr[j][i-1]+arr[j-1][i]
for i in range(int(input())):
    a=int(input())
    b=int(input())
    print(arr[a][b])