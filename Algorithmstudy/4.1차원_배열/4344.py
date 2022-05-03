# # # 평균은 넘겠지
import sys
n = int(sys.stdin.readline())
for _ in range(n):
    l = list(map(int, sys.stdin.readline().split()))
    # cnt = 0
    # avg = sum(l[1:]) / l[0]
    # for score in l[1:]:
    #     if score > avg:
    #         cnt += 1
    # result = cnt / l[0] * 100


    result = (len([i for i in l if sum(l[1:]) / l[0] < int(i)])/l[0]) * 100
    print(f'{result:.3f}%')



# n = int(input())
#
# for i in range(n):
#   input_score = list(map(int, input().split(' ')))
#
#   avg = sum(input_score[1:])/input_score[0]
#   cnt = 0
#
#   for score in input_score[1:]:
#     if score > avg:
#       cnt += 1
#   rate = cnt / input_score[0] * 100
#   print(f'{rate:.3f}%')


"""
왜 왜왜 틀렸을까 알수가 없다.
"""