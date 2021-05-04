# https://zhuanlan.zhihu.com/p/71181926
# 这个词原来为Guerrilla Patch，杂牌军、游击队，说明这部分不是原装的，
# 在英文里guerilla发音和gorllia(猩猩)相似，再后来就写了monkey(猴子)。
# 还有一种解释是说由于这种方式将原来的代码弄乱了(messing with it)，
# 在英文里叫monkeying about(顽皮的)，所以叫做Monkey Patch。
# 猴子补丁（monkey patch）的主要功能就是动态的属性的替换。
# 虽然属性的运行时替换和猴子也没什么关系，所以说猴子补丁的叫法有些莫名其妙，
# 只要知道和“模块运行时替换的功能”对应就行了。
# monkey patch允许在运行期间动态修改一个类或模块（注意python中一切皆对象，包括类、方法、甚至是模块）。

class A:
    def func(self):
        print("Hi")
    def monkey(self):
        print("Hi, monkey")

def outer_monkey(a):  # a 这个参数是没有用到的，因为func有一个参数，如果这个函数没有参数的话不能这样直接赋值
    print("Hi,outer monkey")

import json
import ujson

def monkey_patch_json():
    json.__name__ = 'ujson'
    json.dumps = ujson.dumps
    json.loads = ujson.loads

monkey_patch_json()

# 场景1：
# 比如引用通用库里的一个模块，又想丰富模块的功能，
# 除了继承之外也可以考虑用Monkey Patch。
# Monkey Patch带了便利的同时也有搞乱源代码优雅的风险。
# 场景2：
# 现在我们再开发负载均衡，华三提供的插件基于原生开发。
# 为了快速上线，不会改动原生代码，但是原生有pool-listener protocol配对的限制
# 可以使用 monkey-patch 重写配对逻辑，或者直接 patch 掉配对 tuple constants

if __name__ == '__main__':
    a = A()
    A.func = A.monkey
    A.func=outer_monkey
    a.func()



