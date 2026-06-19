li=[int(input()) for _ in range(10)]
print(sum([1 for i in li if i%3==0]),sum([1 for i in li if i%5==0]))