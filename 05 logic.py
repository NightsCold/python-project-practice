# 寻找水仙花数（自幂数）
for i in range(100,1000):
    i_1 = i % 10
    i_10 = i // 10 % 10
    i_100 = i // 100
    if i_1**3 + i_10**3 + i_100**3 == i:
        print(i)

# 正整数的反转
n = int(input('请输入正整数：'))
res = 0
while n>0:
    u = n%10
    res = res*10 + u
    n = n//10
print(res)

# 百钱百鸡
for a in range(1,21):
    for b in range(1,34):
        c = 100 - a - b
        if a*5+b*3+c/3==100:
            print(f'公鸡有{a}只，母鸡有{b}只，小鸡有{c}只')

# CRAPS赌博游戏,假设有两人各有1000赌注
from random import randint
money = 1000
is_go_on = False
while money>0 and money<2000:
    print(f'你现在有{money}')
    while True:
        debt = int(input('请下注：'))
        if 0 < debt <= money:
            break
    first = randint(2,12)
    print(f'玩家掷了{first}点')
    if first == 7 or first == 11:
        money = money + debt
        print(f'玩家胜，获得{debt}，余额为{money}')
        is_go_on = False
    elif first == 2 or first == 3 or first == 12:
        money = money - debt
        print(f'玩家输，失去{debt}，余额为{money}')
        is_go_on = False
    else:
        is_go_on = True
    while is_go_on:
        current = randint(2,12)
        print(f'玩家掷了{current}点')
        if current == 7:
            money = money - debt
            print(f'玩家输，失去{debt}，余额为{money}')
            is_go_on = False
        elif current == first:
            money = money + debt
            print(f'玩家胜，获得{debt}，余额为{money}')
            is_go_on = False
        else:
            continue
if money<= 0:
    print('游戏结束，玩家输光了钱')
else:
    print('游戏结束，玩家赢够了')

# 斐波那契数列的前20个数
a = 1
b = 1
print(a)
print(b)
for i in range(3,21):
    c = a + b
    print(c)
    a = b
    b = c

# 10000以内的完美数
for i in range(1,10000):
    sum = 0
    for j in range(1,5000):
        if i%j == 0 and i!=j:
            sum+=j
    if sum == i:
        print(f'{i}是完美数')

# 100以内所有的素数
for i in range(2,100):
    c = 0
    for j in range(1,100):
        if i%j==0:
            c+=1
    if c == 2:
        print(f'{i}是素数')