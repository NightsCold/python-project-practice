def main():
    f = None
    try:
        f = open('GUI.txt', 'r', encoding = 'utf-8')
        print(f.read())
    except FileNotFoundError:
        print('not found this file')
    except UnicodeDecodeError:
        print('decode error')
    finally:
        if f:
            f.close()
# ========================================
import time
def main():
    with open('aaa.txt', 'r', encoding='utf-8') as f:
        print(f.read())
    with open('aaa.txt', 'r', encoding='utf-8') as f:
        for line in f:
            print(line,end='')
            time.sleep(0.5)
    print()
    with open('aaa.txt') as f:
        lines = f.readlines()
    print(lines)
    with open('aaa.txt') as f:
        line = f.readline()
    print(line)
# ========================================
from math import sqrt
def is_prime(n):
    assert n > 0, 'n must be lager than 0'
    for i in range(2,int(sqrt(n))+1):
        if n%i ==0:
            return False
    return True if n!=1 else False
        
def main():
    filenames = ('a.txt','b.txt','c.txt')
    fs_list = []
    try:
        for filename in filenames:
            fs_list.append(open(filename,'w',encoding='utf-8'))
        for number in range(1,10000):
            if is_prime(number):
                if number < 100:
                    fs_list[0].write(str(number)+'\n')
                elif number < 1000:
                    fs_list[1].write(str(number)+'\n')
                else:
                    fs_list[2].write(str(number)+'\n')
    except IOError as ex:
        print(ex)
        print('error when write into file')
    finally:
        for fs in fs_list:
            fs.close()
    print('complete')

             



if __name__ == '__main__':
    main()
        