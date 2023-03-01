# # 创建函数：1 求最大公约数 2 求最小公倍数
# def max_gy(x,y):
#     (x,y) = (y,x) if x>y else (x,y)
#     for i in range(x,0,-1):
#         if x%i == 0 and y%i == 0:
#             return i

# def min_gb(x,y):
#     z = max_gy(x,y)
#     return x*y/z

# s= max_gy(12,8)
# ss=min_gb(15,6)
# print(ss)

# 判断是否是回文数
def is_hw(x):
    a=x
    sum = 0
    while a > 0:
        sum = sum*10 + a%10
        a = a//10
    if sum == x:
        return True
    else:
        return False

# 判断是否是素数
def is_su(x):
    if x>0 and type(x) == int:
        c = 0
        for i in range(1,x):
            if x%i==0:
                c+=1
        if c == 1:
            return True
        else:
            return False
    else:
        return False
    
# 判断是否是回文素数
def is_suhw(x):
    if is_su(x) and is_hw(x):
        return True
    else:
        return False

print(is_su(132))
print(is_hw(132))
print(is_suhw(132))