# # 跑马灯
# import os
# import time
# con='北京欢迎你，为你开天辟地...'
# while True:
#     os.system('clear')
#     print(con)
#     time.sleep(0.2)
#     con = con[1:] + con[0]

# # 验证码
# from random import randint
# def code(x=4):
#     s = ''
#     code_str='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     for i in range(x):
#         c = randint(0,61)
#         s = s + code_str[c]
#     return s

# a = code(5)
# print(a)


# # 返回文件的后缀名
# def get_suffix(filename, has_dot=False):
#     a = 0 if has_dot else 1
#     suf = filename[filename.index('.')+a:]
#     return suf

# t = get_suffix('xixi.word',has_dot=True)
# print(t)

# # 返回列表中最大和第二大的值
# def max2(li:list):
#     pli = sorted(li,reverse=True)
#     res = pli[:2]
#     return res

# s= max2([1,3,5,2,7,8,4,6,32,23,57,35])
# print(s)

# # 计算给的年月日是第几天
# def is_run(year):
#     if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#         return True
#     else:
#         return False
    
# def day_no(y,m,d):
#     m_num = [
#       [0,31,28,31,30,31,30,31,31,30,31,30,31],
#       [0,31,29,31,30,31,30,31,31,30,31,30,31]
#     ][is_run(y)]
#     if is_run(y):
#         b_m = m_num[:m]
#     else:
#         b_m = m_num[:m]
#     s = sum(b_m)+d
#     return s

# x = day_no(2000,3,1)
# print(x)

# # 杨辉三角
# def main():
#     num = int(input('Number of rows: '))
#     a = 0
#     li = [1]
#     if num==1:
#         res = '\t'.join('%s' %id for id in li)
#         print(res)
#     else:
#         res = '\t'.join('%s' %id for id in li)
#         print(res)
#         for i in range(2,num+1):
#             list_1=li
#             list_2=li
#             list_1=list_1+[0]
#             list_2=[0]+list_2
#             li=li+[0]
#             for j in range(len(list_1)):
#                 li[j] = list_1[j]+list_2[j]
#             res = '\t'.join('%s' %id for id in li)
#             print(res)

         
# if __name__ == '__main__':
#     main()       

