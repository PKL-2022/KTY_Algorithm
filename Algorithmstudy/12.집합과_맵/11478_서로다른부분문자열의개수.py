s = input()
answer = []
for i in range(len(s)):
    for j in range(i+1, len(s)+1):
        answer.append(s[i:j])
print(len(set(answer)))
