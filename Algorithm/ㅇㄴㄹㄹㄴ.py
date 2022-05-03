n = int(input())
array = [list(input().split()) for _ in range(n)]

array.sort(key=lambda x:x[0])

for i in range(len(array)):
    result = ' '.join(str(s) for s in array[i])
    print(result)