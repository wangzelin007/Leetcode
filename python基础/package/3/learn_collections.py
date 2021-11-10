# _*_ coding: utf-8 _*_
# namedtuple() 创建命名元组子类的工厂函数
# deque 类似列表(list)的容器，实现了在两端快速添加(append)和弹出(pop)
# ChainMap 类似字典(dict)的容器类，将多个映射集合到一个视图里面
# ChainMap实际上是把放入的字典存储在一个队列中，当进行字典的增加删除等操作只会在第一个字典上进行，当进行查找的时候会依次查找。
# new_child()方法实质上是在列表的第一个元素前放入一个字典，默认是{}，而parents是去掉了列表开头的元素
import os, argparse

defaults = {'color': 'red', 'user': 'guest'}
parser = argparse.ArgumentParser()
parser.add_argument('-u', '--user')
parser.add_argument('-c', '--color')
namespace = parser.parse_args()
command_line_args = {k: v for k, v in vars(namespace).items() if v is not None}

combined = ChainMap(command_line_args, os.environ, defaults)
print(combined['color'])
print(combined['user'])

# Counter 字典的子类，提供了可哈希对象的计数功能
# OrderedDict 字典的子类，保存了他们被添加的顺序
# defaultdict 字典的子类，提供了一个工厂函数，为字典查询提供一个默认值
# UserDict 封装了字典对象，简化了字典子类化
# UserList 封装了列表对象，简化了列表子类化
# UserString 封装了列表对象，简化了字符串子类化

