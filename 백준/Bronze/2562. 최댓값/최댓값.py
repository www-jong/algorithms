a=[]
for i in range(9):
    a.append(int(input()))
print("{0}\n{1}".format(max(a),a.index(max(a))+1))