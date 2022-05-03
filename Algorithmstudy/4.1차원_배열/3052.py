# 나머지

l = [int(input()) for _ in range(10)]

result=[]
for i in l:
    if i%42 not in result:
        result.append(i%42)

print(len(result))




"""
b = [int(input())%42 for i in range(10)]
print(len(set(b)))

set 함수를 이용하자.
"""