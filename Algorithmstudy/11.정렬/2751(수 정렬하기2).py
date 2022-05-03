import sys

a = int(sys.stdin.readline().rstrip())
n = [int(sys.stdin.readline().rstrip()) for _ in range(a)]

result = []
r = []

def move(i_idx):
    if i_idx <=1:
        return False
    p_idx = i_idx//2
    if result[i_idx] > result[p_idx]:
        return True
    else:
        return False


def down(idx):
    l = idx * 2
    r = idx * 2 + 1

    if l >= len(result):
        return False
    elif r >= len(result):
        if result[idx] < result[l]:
            return True
        else:
            return False
    else:
        if result[l] > result[r]:
            if result[idx] < result[l]:
                return True
            else:
                return False
        else:
            if result[idx] < result[r]:
                return True
            else:
                return False





def pop():
    if len(result) <= 1:
        return None
    returned_data = result[1]
    result[1] = result[-1]
    del result[-1]
    idx = 1

    while down(idx):
        l = idx * 2
        r = idx * 2 + 1

        if r >= len(result):
            if result[idx] < result[l]:
                result[idx], result[l] = result[l], result[idx]
                idx = l
        else:
            if result[l] > result[r]:
                if result[idx] < result[l]:
                    result[idx], result[l] = result[l], result[idx]
                    idx = l
            else:
                if result[idx] < result[r]:
                    result[idx], result[r] = result[r], result[idx]
                    idx = r

    return returned_data


def heap(v):
    if len(result) == 0:
        result.append(None)
        result.append(v)
        return True
    result.append(v)
    i_idx = len(result) - 1
    while move(i_idx):
        p_idx = i_idx // 2
        result[i_idx], result[p_idx] = result[p_idx], result[i_idx]
        i_idx = p_idx


for i in n:
    heap(i)

for i in n:
    r.append(pop())

r = r[::-1]

for i in r:
    print(i)

print('-'*20)
#
# n = [0] + n
#
# for i in range(n, 0, -1):

