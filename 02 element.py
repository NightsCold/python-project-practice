# 华氏度转摄氏度  C = (F - 32) / 1.8
print("华氏度转化摄氏度")
F = int(input("请输入华氏度:"))
C = (F - 32)/1.8
print(f'= 摄氏度{C}')


# 获得半径求圆的周长和面积
r = float(input('圆的半径r='))
l = 2*3.1416*r
s = 0.5*3.1416*r*r
print(f'周长是{l:.2f} 面积是{s:.2f}')


# 判断是否是闰年
y = int(input('请输入年份：'))
if y % 4 == 0 and y % 100 !=0 or y % 400 == 0:
    print(f'{y}是闰年')
else:
    print(f'{y}是平年') 

