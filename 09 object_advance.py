# 访问属性可以通过属性的getter（访问器）和setter（修改器）方法
# 通过在类中定义__slots__变量来进行限定自定义类型的对象只能绑定某些属性
# 类中的方法并不需要都是对象方法（在确实是否为对象前使用），静态方法来解决这类问题（形式：[类].[方法]，而不是[对象].[方法]）
# Python还可以在类中定义类方法，类方法的第一个参数约定名为cls，它代表的是当前类相关的信息的对象，通过这个参数我们可以获取和类相关的信息并且可以创建出类的对象
# 类和类之间的关系有三种：is-a（继承或泛化）、has-a—（关联）和use-a（依赖）关系
# 可以在已有类的基础上创建新类（形式：Class [子类]([父类])：  ... super().__init__(name, age)）
# 子类在继承了父类的方法后，可以对父类已有的方法给出新的实现版本，这个动作称之为方法重写（override），通过方法重写我们可以让父类的同一个行为在子类中拥有不同的实现版本，当我们调用这个经过子类重写的方法时，不同的子类对象会表现出不同的行为，这个就是多态（poly-morphism）。
# 抽象类就是不能够创建对象的类，这种类的存在就是专门为了让其他类去继承它。可以通过abc模块的ABCMeta元类和abstractmethod包装器来达到抽象类的效果，如果一个类中存在抽象方法那么这个类就不能够实例化（创建对象）。

# Ultraman VS Monster
from abc import ABCMeta, abstractclassmethod
from random import randint, randrange

class Fighter(object, metaclass = ABCMeta):
    __slots__ = ('_name', '_hp')     
    def __init__(self, name, hp):    
        self._name = name
        self._hp = hp

    @property                       
    def name(self):
        return self._name
    
    @property                       
    def hp(self):
        return self._hp
    
    @hp.setter
    def hp(self, hp):
        self._hp = hp if hp > 0 else 0

    @property
    def alive(self):
        return self._hp > 0
    
    @abstractclassmethod
    def attack(self, other):
        pass

class Ultraman(Fighter):
    __slots__ = ('_name', '_hp', '_mp')
    def __init__(self, name, hp, mp):
        super().__init__(name, hp)
        self._mp = mp
    
    def attack(self,other):
        other.hp -= randint(15, 25)

    def huge_attack(self, other):
        if self._mp >= 50:
            self._mp -= 50
            injury = other.hp * 3//4
            injury = injury if injury >= 50 else 50
            other.hp -= injury
            return True
        else:
            return False
    
    def magic_attack(self, others):
        if self._mp >= 20:
            self._mp -= 20
            for temp in others:
                if temp.alive:
                    temp.hp -= randint(10,15)
            return True
        else:
            return False
    
    def resume(self):
        incr_point = randint(1, 10)
        self._mp += incr_point
        return incr_point
    
    def __str__(self):
        return f'---{self._name} Ultraman---\nHp:{self._hp}\nMp:{self._mp}'
    
class Monster(Fighter):
    __slots__ = ('_name','_hp')
    
    def attack(self, other):
        other.hp -= randint(10, 15)
    
    def __str__(self):
        return f'---{self._name}Monster---\nHp:{self._hp}'
    
def is_any_alive(monsters):
    for monster in monsters:
        if monster.alive > 0:
            return True
    return False

def select_alive_one(monsters):
    monsters_len = len(monsters)
    while True:
        index = randrange(monsters_len)
        monster = monsters[index]
        if monster.alive > 0:
            return monster

def display_info(ultraman, monsters):
    print(ultraman)
    for monster in monsters:
        print(monster)

def main():
    u = Ultraman('Alex', 1000, 120)
    m1 = Monster('Bug', 250)
    m2 = Monster('Chaos', 500)
    m3 = Monster('Dave', 750)
    ms = [m1, m2, m3]
    fight_round = 1
    while u.alive and is_any_alive(ms):
        print(f'----------No.{fight_round} Round----------')
        m = select_alive_one(ms)
        skill = randint(1,10)
        if skill <= 6:
            print(f'{u.name} acctck {m.name}')
            u.attack(m)
            print(f'Mp recreat {u.resume()} point')
        elif skill <= 9:
            if u.magic_attack(ms):
                print(f'{u.name} uses magic acctck {m.name}')
            else:
                print(f'{u.name} fails to use magic')
        else:
            if u.huge_attack(m):
                print(f'{u.name} uses huge acctck {m.name}')
            else:
                print(f'{u.name} attcak {m.name}')
                u.attack(m)
                print(f'Mp recreat {u.resume()} point')
        if m.alive > 0:
            m.attack(u)
            print(f'{m.name} back-acctck  {u.name}')
        display_info(u,ms)
        fight_round += 1
    print('\n----------Fight Over!----------\n')
    if u.alive > 0:
        print(f'{u.name} Ultraman win!')
    else:
        print('Monsters win!')

if __name__ == '__main__':
    main()
        
            
# poker game
import random

class Card(object):
    __slots__ = ('_suite', '_face')
    def __init__(self, suite, face):
        self._suite = suite
        self._face = face
    @property
    def suite(self):
        return self._suite
    @property
    def face(self):
        return self._face
    
    def __str__(self):
        if self._face == 1:
            face_str = 'A'
        elif self._face == 11:
            face_str = 'J'
        elif self._face == 12:
            face_str = 'Q'
        elif self._face == 13:
            face_str = 'K'
        else:
            face_str = str(self._face)
        return f'{self._suite}{face_str}'
    
    def __repr__(self):
        return self.__str__()
    
class Poker(object):
    def __init__(self):
        self._cards = [Card(suite, face)
                      for suite in '♠♥♣♦'
                      for face in range(1,14)]
        self._current = 0

    @property
    def cards(self):
        return self._cards
    
    def shuffle(self):
        self._current = 0
        random.shuffle(self._cards)

    @property
    def next(self):
        card = self._cards[self._current]
        self._current += 1
        return card
    
    @property
    def has_next(self):
        return self._current < len(self._cards)
    
class Player():

    def __init__(self, name):
        self._name = name
        self._cards_on_hand = []

    @property
    def name(self):
        return self._name
    
    @property
    def cards_on_hand(self):
        return self._cards_on_hand
    
    def get(self, card):
        self._cards_on_hand.append(card)

    def arrange(self,card_key):
        self._cards_on_hand.sort(key=card_key)
    
def get_key(card):
    return(card.suite, card.face)

def main():
    p = Poker()
    p.shuffle()
    players = [Player('东邪'), Player('西毒'), Player('南帝'), Player('北丐')]
    for _ in range(13):
        for player in players:
            player.get(p.next)
    for player in players:
        print(f'{player.name}: ')
        player.arrange(get_key)
        print(player.cards_on_hand)

if __name__ == '__main__':
    main()


# salary caculate
from abc import ABCMeta, abstractclassmethod

class Employee(object, metaclass=ABCMeta):
    def __init__(self, name):
        self._name = name
    
    @property
    def name(self):
        return self._name
    
    @abstractclassmethod
    def get_salary(self):
        pass

class Manager(Employee):
    def get_salary(self):
        return 15000
    
class Programmer(Employee):
    def __init__(self, name, hours = 0):
        super().__init__(name)
        self._hours = hours
    @property
    def hours(self):
        return self._hours

    @hours.setter
    def hours(self, hours):
        self._hours = hours if hours > 0 else 0

    def get_salary(self):
        self._salary = 150 * self._hours
        return self._salary

class Salesman(Employee):
    def __init__(self, name, sale=0):
        super().__init__(name)
        self._sale = sale

    @property
    def sale(self):
        return self._sale
    
    @sale.setter
    def sale(self, sale):
        self._sale = sale if sale > 0 else 0
    
    def get_salary(self):
        self._salary = 1200 + self._sale * 0.05
        return self._salary

def main():
    emps = [
        Manager('liubei'), Programmer('zhugeliang'),
        Manager('caocao'), Salesman('xunyu'),
        Salesman('lvbu'), Programmer('zhangliao'),
        Programmer('zhaoyun')
    ]
    for emp in emps:
        if isinstance(emp, Programmer):
            emp.hours = int(input(f'{emp.name}\'s work hours of this month:'))
        elif isinstance(emp, Salesman):
            emp.sale = float(input(f'{emp.name}\'s sales of this month:'))
        print(f'{emp.name}\'s salary is {emp.get_salary()}')

if __name__ == '__main__':
    main()

    