import sys

dial = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']

n = sys.stdin.readline().rstrip()
result = 0
for i in n:
    for j in dial:
        if i in j:
            result += dial.index(j)+3
print(result)

