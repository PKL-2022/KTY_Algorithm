import sys
n = sys.stdin.readline().rstrip()
result = [-1] * 26


for i in range(ord('a'), ord('z')+1):
    if chr(i) in n:
        result[i-97] = n.index(chr(i))

print(*result)



# alphabet_list = []
# S = input()
# for ascii_code in range(97, 123): alphabet_list.append(S.find(chr(ascii_code)))
# print(*alphabet_list)
