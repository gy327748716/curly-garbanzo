#问题：如果你的程序包含了大量无法直视的硬编码切片，并且你想清理一下代码。

######    0123456789012345678901234567890123456789012345678901234567890'
record = '....................100 .......513.25 ..........'
cost = int(record[20:23]) * float(record[31:37])

#print(record)
#print(cost)

SHARES = slice(20,23)
PRICE = slice(31,37)
cost = int(record[SHARES]) * float(record[PRICE])

#print(cost)

items = [0,1,2,3,4,5,6]
a = slice(2,4)
print(items[2:4])
print(items[a])

items[a] = [10, 11]
print(items)

del items[a]
print(items)

print(items)
