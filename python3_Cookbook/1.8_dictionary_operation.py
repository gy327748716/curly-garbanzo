prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}


'''
zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。
如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，利用 * 号操作符，可以将元组解压为列表。
zip 方法在 Python 2 和 Python 3 中的不同：在 Python 3.x 中为了减少内存，zip() 返回的是一个对象。如需展示列表，需手动 list() 转换。
'''

min_price = min(zip(prices.values(), prices.keys()))
# min_price is (10.75, 'FB')
print(min_price)

max_price = max(zip(prices.values(), prices.keys()))
# max_price is (612.78, 'AAPL')
print(max_price)

prices_sorted = sorted(zip(prices.values(), prices.keys()))

print(prices_sorted)

prices_and_names = zip(prices.values(), prices.keys())

prices_sorted = sorted(zip(prices.values(), prices.keys()))
# prices_sorted is [(10.75, 'FB'), (37.2, 'HPQ'),
#                   (45.23, 'ACME'), (205.55, 'IBM'),
#                   (612.78, 'AAPL')]
print(prices_sorted)

print(max(prices))
print(min(prices))

prices2 = {'AAA':45.23, 'ZZZ':45.23}
print(zip(prices.keys(), prices.values()))
print(min(zip(prices.keys(), prices.values())))
