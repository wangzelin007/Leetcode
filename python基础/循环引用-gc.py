import gc


class Foo(object):
    def __init__(self):
        self.bar = None
        print('foo init')

    def __del__(self):
        print("foo del")


class Bar(object):
    def __init__(self):
        self.foo = None
        print('bar init')

    def __del__(self):
        print('bar del')


def collect_and_show_garbage():
    print("Collecting...")
    n = gc.collect() # 执行垃圾回收
    print("unreachable objects:", n)
    print(gc.garbage)


def func():
    foo = Foo()
    bar = Bar()
    foo.bar = bar
    bar.foo = foo

# gc.set_debug(gc.DEBUG_COLLECTABLE | gc.DEBUG_UNCOLLECTABLE)
func()
collect_and_show_garbage()
# py2.7
# foo init
# bar init
# Collecting...
# ('unreachable objects:', 4)
# [<__main__.Foo object at 0x7fa97f849710>, <__main__.Bar object at 0x7fa97f849790>]

# > py3.4
# foo init
# bar init
# Collecting...
# foo del
# bar del
# unreachable objects: 4
# []
