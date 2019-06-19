#问题: 怎样在两个字典中寻寻找相同点（比如相同的键、相同的值等等）？

a = {
    'x' :1,
    'y' :2,
    'z' :3
}

b = {
    'w' :10,
    'x' :11,
    'y' :2
}

print(a.keys() & b.keys()) #Find keys in common

print(a.keys() - b.keys()) #Find keys in a that are not in b

print(a.items() & b.items()) #Find (keys, value) pairs in common

#Make a new dictionary with certain keys removed

c = {key:a[key] for key in a.keys() - {'z','w'}}
print("c is",c)
