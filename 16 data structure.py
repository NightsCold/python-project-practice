# # generative
# prices = {
#     'AAPL': 191.88,
#     'GOOG': 1186.96,
#     'IBM': 149.24,
#     'ORCL': 48.44,
#     'ACN': 166.89,
#     'FB': 208.09,
#     'SYMC': 21.29
# }
# new_p = {key: value for key, value in prices.items() if value > 100}
# print(new_p)

# # nesting
# names = ['GY', 'ZF', 'ZY', 'MC', 'HZ']
# courses = ['Chinese', 'Math', 'English']

# scores = [[None]*len(courses) for _ in range(len(names))]
# for row, name in enumerate(names):
#     for col, course in enumerate(courses):
#         scores[row][col]=float(input(f'{name}\'s {course} score is: '))
#         print(scores)

# # heapq
# import heapq
# list1 = [34, 25, 12, 99, 87, 63, 58, 78, 88, 92]
# list2 = [
#     {'name': 'IBM', 'shares': 100, 'price': 91.1},
#     {'name': 'AAPL', 'shares': 50, 'price': 543.22},
#     {'name': 'FB', 'shares': 200, 'price': 21.09},
#     {'name': 'HPQ', 'shares': 35, 'price': 31.75},
#     {'name': 'YHOO', 'shares': 45, 'price': 16.35},
#     {'name': 'ACME', 'shares': 75, 'price': 115.65}
# ]
# print(heapq.nlargest(3, list1))
# print(heapq.nsmallest(2, list1))
# print(heapq.nlargest(4, list2, key = lambda x:x['shares']))
# print(heapq.nsmallest(2, list2, key = lambda x:x['price']))

# # itertools
# import itertools
# xs1 = itertools.permutations('ABCD')
# xs2 = itertools.combinations('ABCDE',3)
# xs3 = itertools.product('ABCD','123')
# xs4 = itertools.cycle(('A','B','C'))

# for _ in xs4:
#     print(_) 

from collections import Counter

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around',
    'the', 'eyes', "don't", 'look', 'around', 'the', 'eyes',
    'look', 'into', 'my', 'eyes', "you're", 'under'
]
counter = Counter(words)
print(counter.most_common(4))

