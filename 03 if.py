# 英尺和厘米转化
v = input('值：')
u = input('单位(in/cm)：')
if u == 'in':
    print(f'{v}英寸 = {float(v)*2.54:.2f}厘米')
elif u == 'cm':
    print(f'{v}厘米 = {float(v)/2.54:.2f}英寸')
else:
    print('单位错误')


# 如果输入的成绩在90分以上（含90分）输出A；80分-90分（不含90分）输出B；70分-80分（不含80分）输出C；60分-70分（不含70分）输出D；60分以下输出E。
s = float(input('成绩分数是：'))
if 0<= s <=100:
    if s >= 90:
        print('等级是A')
    elif s > 80:
        print('等级是B')
    elif s > 70:
        print('等级是C')
    elif s > 60:
        print('等级是D')
    elif s < 60:
        print('等级是E')
else:
    print('成绩输入错误！')


# 输入三边之长，若是三角形则求周长和面积
a = float(input('第一条长：'))
b = float(input('第二条长：'))
c = float(input('第三条长：'))
if a+b>c and a+c>b and b+c>a:
    l = a+b+c
    p = 0.5*l
    s = (p-a)*(p-b)*(p-c)**0.5 #海伦公式
    print(f'组成的三角形周长是{l:.2f}，面积是{s:.2f}')


