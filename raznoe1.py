# def square(x):
#     """
#     Простая функция для вычисления квадрата числа путем сложения.
#     """
#     sum_so_far = 0
#     for counter in range(x):
#         sum_so_far = sum_so_far + x
#     return sum_so_far

# print(square(10))


# some_dict = {}
# some_dict[5.5] = "Ruby"
# some_dict[5.0] = "JavaScript"
# some_dict[5] = "Python"

# for x,y in some_dict.items():
#     print('X=',x,' : Y=',y)



# L = [[1, 2, 3], [4, 5], [6], [7, 8, 9]]
# print(sum(L, []))

# import itertools
# L = [[1, 2, 3], [4, 5], [6], [7, 8, 9]]
# print(list(itertools.chain.from_iterable(L)))


# a, b = 1, 2
# print('a=',a,' b=',b,sep='')
# a, b = b, a
# print('a=',a,' b=',b,sep='')

# for ((a, b), c) in [((1, 2), 3), ((4, 5), 6)]:
#     # print(a, b, c)
#     print('a=',a,' b=',b,' c=',c,sep='')


# items = [2, 2, 3, 3, 1]
# print(list(set(items)))

# items = [2, 2, 3, 3, 1]
# from collections import OrderedDict
# print(list(OrderedDict.fromkeys(items).keys()))


# def product(a, b):
#     return a * b

# def summarize(a, b):
#     return a + b

# c = False
# print((product if c else summarize)(3, 4))



# d = {'a':1, 'b':2}
# print(d.get('c'))
# print(d.get('c', 3))


# for i, item in enumerate(['a', 'b', 'c'], 1):
#     print(i, item)


# d = {'яблоки':40, 'апельсины':80, 'бананы':70}
# print(sorted(d, key=d.get))


# S = {i**2 for i in range(10)}
# D = {i: i**2 for i in range(10)}
# print(S)
# print(D)



a = [1, 2, 3, 1, 2, 3, 2, 2, 4, 5, 1]
print(max(set(a), key=a.count))

from collections import Counter
a = [1, 2, 3, 1, 2, 3, 2, 2, 4, 5, 1]
print(a)
print(type(a))
cnt = Counter(a)
print(cnt.most_common(1))
# print(cnt.)

# print(cnt+'zzzz')
# print(Counter(a))