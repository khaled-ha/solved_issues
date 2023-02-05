from functools import reduce
x = [1, 2, 3]
res = []

for i in range(len(x)):
    res.append([x[i]])
    for j in range(i+1, len(x)):
        res.append([x[i], x[j]])
    if x[i:] not in res:
        res.append(x[i:])
 
res.sort(key=lambda x : reduce(lambda a,b : a+b , x))
print(res)