def d(n):
    n = n + sum(map(int, str(n)))
    return n


SelfNum = set()


for i in range(1, 10001):
    SelfNum.add(d(i))

for j in range(1, 10001):
    if j not in SelfNum:
        print(j)


#Set을 이용하자