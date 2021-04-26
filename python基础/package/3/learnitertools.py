from itertools import *
arr1 = [1,2]; arr2=[3,4]
s = product(arr1,arr2) # 笛卡尔积
word = 'aaaeeee'
[[c,s] for c,s in groupby(word)]
# [['a', <itertools._grouper at 0x7f9e0a621730>],
# ['e', <itertools._grouper at 0x7f9e0ae58070>]]
[[c,list(s)] for c,s in groupby(word)]
# [['a', ['a', 'a', 'a', 'a']],
#  ['e', ['e']]]