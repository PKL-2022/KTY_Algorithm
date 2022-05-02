import sys

a, b, v = map(int, sys.stdin.readline().split())



if (v-b)/(a-b) == int((v-b)/(a-b)):
    print(int((v-b)/(a-b)))
else:
    print(int((v-b)/(a-b)+1))






