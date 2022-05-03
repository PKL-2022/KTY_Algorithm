# 평균

n = int(input())
l = list(map(int, input().split()))
m = max(l)
for i in range(len(l)):
    l[i] = (l[i]/m)*100

print(sum(l)/len(l))


# 계산에서 max(l)을 했더니 연산중에 max의 값이 바껴서 오류가 났다.


""" 다른사람의 풀이
n = int(input())
l = list(map(int, input().split()))
m = max(l)
for i in range(len(l)):
    l[i] = (l[i]/m)*100

print(sum(l)/len(l))
완전 같네
"""



"""
n,*l=map(int,open(0).read().split())
print(sum(l)*100/max(l)/n)"
방법은 똑같은거 같다.

"""