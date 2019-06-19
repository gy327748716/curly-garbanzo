#问题：怎样在一个序列上面保持元素顺序的同时消除重复的值？

def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

#yield 是一个类似 return 的关键字，迭代一次遇到yield时就返回yield后面(右边)的值。
#重点是：下一次迭代时，从上一次迭代遇到的yield后面的代码(下一行)开始执行。

a = [1, 5, 2, 1, 9, 1, 5, 10]
print("list1:", list(dedupe(a)))

def dedupe(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


a = [{'x':1, 'y':2}, {'x':1, 'y':3}, {'x':2, 'y':3}]
print(list(dedupe(a, key=lambda d: (d['x'], d['y']))))


