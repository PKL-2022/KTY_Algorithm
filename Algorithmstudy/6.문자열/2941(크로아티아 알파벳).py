
c = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
n = input()
for i in c:
    n = n.replace(i, '*',)

print(len(n))



# 파이썬 리스트는 replace 를 하고 대입을 해줘야 연산결과가 처리가된다....
# if i in n: 으로 했을때 중복되는데 전부 replace시키고 cnt++만 하는 예외가 있었다.

