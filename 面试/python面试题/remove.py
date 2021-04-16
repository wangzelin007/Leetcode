# _*_ coding: utf-8 _*_
a = [2,4,5,6,7]
for i in a:
    if i % 2 == 0:
        a.remove(i)
print a # 4 5 7

# b = [2,4,5,6,7]
# for i in range(len(b)):
#     if i % 2 == 0:
#         b.pop(i)
# print b # pop index out of range

c = [2,4,5,6,7]
for index,i in enumerate(c):
    if i % 2 == 0:
        c.pop(index)
print c # 4 5 7

# 解决
d = [2,4,5,6,7]
for i in d[:]: # 浅拷贝
    if i % 2 == 0:
        d.remove(i)
print d