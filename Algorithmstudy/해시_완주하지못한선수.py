participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]
answer = ''
# temp = 0
# dic = {}
# for part in participant:
#     dic[hash(part)] = part
#     temp += int(hash(part))
# for com in completion:
#     temp -= hash(com)
# answer = dic[temp]

# participant의 해시값을 key로 하여 딕셔너리에 key(해시값):value(참가자)의 형태로 저장한다.
# participant를 순회하며 해시의 값을 temp에 더해준다. 그리고 completion을 돌며 해시의 값을 temp에서 빼주면
# completion에 없는 participant 의 해시값많이 temp에 남는다. 그리고 그 해시값을 키값으로 딕셔너리에서 값을 서치하면
# 완주하지 못한 participant의 이름이 나온다.

# h = {}
# temp = 0
# for p in participant:
#     h[hash(p)] = p
#     temp += hash(p)
# for c in completion:
#     temp -= hash(c)
# print(h[temp])


# dict = {}
# for p in participant:
#     dict[p] = dict.get(p, 0) + 1
# # 딕셔너리 안에 찾으려는 키값이 없을때 정해둔 디폴트 값을 가져오게하는것.
# for i in completion:
#     dict[i] -= 1
#
# for k in dict:
#     if dict[k]:
#         print(k)


import collections
answer = collections.Counter(participant) - collections.Counter(completion)
print(list(answer.keys())[0])




# n = len(participant) * 2
# hash_table = list([0 for i in range(n)])
#
#
# def get_key(data):
#     return hash(data)
#
#
# def hash_function(key):
#     return key % n
#
#
# def save_data(data, value):
#     index_key = get_key(data)
#     hash_address = hash_function(index_key)
#     if hash_table[hash_address] != 0:
#         for index in range(len(hash_table[hash_address])):
#             if hash_table[hash_address][index][0] == index_key:
#                 if hash_table[hash_address][index][1] == 0 :
#                     hash_table[hash_address][index][1] = value
#                 else:
#                     hash_table[hash_address].append([index_key, value])
#                 return
#         hash_table[hash_address].append([index_key, value])
#     else:
#         hash_table[hash_address] = [[index_key, value]]
#
#
# def read_data(data):
#     index_key = get_key(data)
#     hash_address = hash_function(index_key)
#
#     if hash_table[hash_address] != 0:
#         for index in range(len(hash_table[hash_address])):
#             if hash_table[hash_address][index][0] == index_key:
#                 hash_table[hash_address][index] = 0
#                 return
#         return None
#     else:
#         return None
#
#
# for p in participant:
#     save_data('mislav', p)
#
# print(hash_table)
#
#
# for c in completion:
#     read_data(c)
#
# print(hash_table)

