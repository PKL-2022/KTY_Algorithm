def d(n):
     if n>10000:
         return n
     d(n+int(str(n//10) + str(n%10)))



n = int(input())
print(d(n))