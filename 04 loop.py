# 输入正整数，判断是否是素数
from math import sqrt

n = int(input('输入正整数：'))
end = int(sqrt(n))
is_prime = True
for i in range(2,end+1):
    if n%i == 0:
        is_prime = False
        break
if  n == 1 or is_prime:
    print(f'{n}是素数')
else:
    print(f'{n}是合数')

# 求最大公约数和最小公倍数
a = int(input('第一个数：'))
b = int(input('第二个数：'))
c = min(a,b)
d = max(a,b)
for i in range(1,c+1):
    if a%i == 0 and b%i == 0:
        gy = i
print(f'最大公约数是{gy}\n最小公倍数是{a*b/gy}')

# 打印三角形
# ——————————left——————————
for i in range(1,6):
    star = ''
    while i > 0:
        star = star + '*'
        i = i - 1
    print(star)
# ——————————right——————————
for i in range(1,6):
    star = ''
    j = i
    while j < 5:
        star = star + ' '
        j = j+1
    while i > 0:
        star = star + '*'
        i = i-1
    print(star)
# ————————————mid————————————
for i in range(1,6):
    star = ''
    j = i
    k = i
    l = i
    while j < 5:
        star = star + ' '
        j = j+1
    while k > 0:
        star = star + '*'
        k = k-1
    stars1 = star
    star = ''
    while l > 1:
        star = star + '*'
        l = l - 1
    stars2 = star
    print(stars1+stars2)
