c = int(input())

for _ in range(c):
    count = 0
    result=0
    a = list(map(int,input().split(' ')))
    b = (sum(a) - a[0]) / a[0] # 한 줄 평균
    for i in a[1:]:
        if (i > b):
            count += 1
            result = count / a[0] * 100
    print(f'{result:.3f}%')