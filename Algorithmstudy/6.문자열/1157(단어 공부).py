# import sys
#
# n = sys.stdin.readline().rstrip().upper()
#
# u = list(set(n))

# cnt = []
#
# for i in u:
#     c = n.count(i)
#     cnt.append(c)
#
#
# if cnt.count(max(cnt)) > 1:
#     print('?')
#
# else :
#     print(u[cnt.index(max(cnt))])



# 완전히 쳐발린 문제다 나중에 다시풀어야겠다
"""
1. upper를 통해 입력을받는다.
2. set를 통해 입력의 알파벳들을 리스트로 만든다.
3. 각 요소의 개수를 카운트하여 cnt리스트에 넣는다
4. 가장 큰값의 개수를 센다
5. 1 초과면 ?를 출력하고
6. 그렇지 않으면 가장 큰값의 인덱스를 찾아 출력한다.
"""

s,a=input().lower(),[]
for i in range(97,123):
 a.append(s.count(chr(i)))
print(a)
print('?'if a.count(max(a))>1 else chr(a.index(max(a))+97).upper())