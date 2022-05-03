#더하기 사이클
import sys

n = int(sys.stdin.readline())
cnt=1
c = n
while(1):
    a = c//10
    b = c % 10
    c = int(str(b)+str((a+b)%10))
    if(c==n):
        break
    cnt+=1
print(cnt)


"""
숏코딩
a=n=int(input());c=1
while(a:=a%10*10+a*11//10%10)-n:c+=1
print(c)
"""