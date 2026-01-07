n,K=input().split()
a=[str(i).zfill(2) for i in range(60)]
print(sum([1 for k in a for j in a for i in a[:int(n)+1]if K in i+j+k]))