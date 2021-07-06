# coding: utf-8
# 单例 Singleton
# 全局的单实例，常用于配置文件，数据库连接池，日志记录，打印机后台处理程序等。
# 单例模式优缺点
# 单例模式优点很明显：只提供一个实例化的对象。
# 单例模式具有全局访问权限，全局变量可能在某处已经被修改，但是开发人员仍然认为他们没有发生变化。
# 可能会对同一个对象创建多个引用。
# 所有依赖于全局变量的类都会由于一个类的改变而紧密偶合为全局数据，从而可能在无意中影响另一个类。


class Singleton1(object):
    # 通过覆盖__new__方法来控制对象的创建。
    def __new__(cls, *args, **kwargs):
        # hasattr用于查看对象cls是否有instance属性，该属性作用是检测该类是否已经生成了一个对象
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton1, cls).__new__(cls)
        return cls.instance


s = Singleton1()
s1 = Singleton1()
print(s)
print(s1)


class Singleton2(object):
    __instance = None

    # 初始化时，如果存在对象，就直接返回这个对象，不存在就不管，也不new它
    def __init__(self):
        if Singleton2.__instance:
            self.get_instance()

    # 实际的对象创建发生在调用get_instance的时候
    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls.__instance = Singleton2()
        return cls.__instance


s = Singleton2()
print(s.get_instance())
s1 = Singleton2()
print(s1.get_instance())

class MetaSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton,
                                        cls).__call__(*args, **kwargs)
        return cls._instances


class Logger(metaclass=MetaSingleton):
    pass


logger1 = Logger()
logger2 = Logger()
print(logger1)
print(logger2)


# Adapter 适配器，通过适配层把两个不能直接沟通的层连接起来
# 比如 client 请求和 数据库
#     client 请求和 driver

