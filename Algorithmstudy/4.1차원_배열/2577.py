l = [int(input()) for _ in range(3)]
result=l[0]
for i in l[1:]:
    result *= i

result_list = []
for i in range(0, 10):
    result_list.append(0)


for i in str(result):
    result_list[int(i)] += 1

for i in result_list:
    print(i)





a = int(input())
b = int(input())
c = int(input())

d = list(map(int, (str(a * b * c))))

for i in range(10):
    print(d.count(i))