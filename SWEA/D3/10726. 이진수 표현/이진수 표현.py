for i in range(int(input())):
 N,M=map(int,input().split())
 print(f'#{i+1}',['OFF','ON'][sum([int(j)for j in bin(M)[2:][-N:]])==N])