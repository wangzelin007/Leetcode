# coding: utf-8
# 工厂模式 Factory Method
# 在面向对象中，工厂表示一个负责创建其他类型对象的类。

# 工厂具有：
# 松耦合
# 客户端无需了解创建对象的类，但是照样可以使用它来创建对象。
# 可以轻松的在工厂中添加其他类来创建其他类型的对象。

# 工厂模式有3种变体：
# 简单工厂：允许接口创建对象，但不会暴露对象的创建逻辑。
# 工厂方法：允许接口创建对象，但使用哪个类来创建对象是交给子类决定。
# 抽象工厂：抽象工厂是一个能够创建一系列相关对象而无需指定其具体类的接口。它可以提供其他工厂的对象，在内部创建其他对象。

# 简单工厂
# ABCMeta是Python的特殊的元类，用来生成抽象类
from abc import ABCMeta, abstractmethod


# 动物类，定义say方法，但不实现
class Animal(metaclass=ABCMeta):
    @abstractmethod
    def say(self):
        pass


# 狗类，继承动物，重写say方法
class Dog(Animal):
    def say(self):
        print('i am dog')


# 猫类，继承动物，重写say方法
class Cat(Animal):
    def say(self):
        print('i am cat')


# 工厂类
class ForestFactory(object):
    # say方法的统一接口，传入子类对象，调用他们的say方法
    def say_something(self, object_type):
        return eval(object_type)().say()


# 工厂方法
# 定义一个接口来创建对象，工厂本身并不创建对象，而交给子类完成，子类决定要实例化哪些类。
# Factory方法的创建时通过继承而不是通过实例化。
# 工厂方法更加具有可定制性，它可以返回相同的实例或者子类，而不是某种类型的对象。
# 更好的灵活性，代码更通用，因为他不是单纯的实例某个类，而是取决于接口
# 松耦合，创建对象的代码和使用它的代码是分开的，添加新类更容易。

# 假设每个页面都有一块区域显示个人信息，但是内容不同，设计代码如下：
from abc import ABCMeta, abstractmethod

# 一个区表示哪方面内容，抽象的
class Section(metaclass=ABCMeta):
    @abstractmethod
    def describe(self):
        pass

# 接下来创建多个区域，用来分别显示不同的区域（简化只打印出来）
# 个人区
class PersonalSection(Section):
    def describe(self):
        print('personal section')

# 音乐部分
class AlbumSection(Section):
    def describe(self):
        print('album')

# 专利部分
class PatentSection(Section):
    def describe(self):
        print('patent')

# 出版部分
class PublicationSection(Section):
    def describe(self):
        print('publication')

# 接下来创建抽象类，提供工厂方法create_profile
class Profile(metaclass=ABCMeta):
    def __init__(self):
        self.sections = []
        self.create_profile()

    @abstractmethod
    def create_profile(self):
        pass

    def get_sections(self):
        return self.sections

    def add_sections(self, section):
        self.sections.append(section)

# 接下来创建两个具体实现工厂方法的子类
class ConcreteCreator1(Profile):
    def create_profile(self):
        # 添加个人区域、专利区域、出版区域
        self.add_sections(PersonalSection())
        self.add_sections(PatentSection())
        self.add_sections(PublicationSection())

class ConcreteCreator2(Profile):
    def create_profile(self):
        # 添加个人区域、音乐区域
        self.add_sections(PersonalSection())
        self.add_sections(AlbumSection())


# 抽象工厂
# 抽象工厂主要目的是提供一个接口来创建一系列相关对象，而无需指定具体的类。
# 相比于之前的需要我们去指定创建什么对象，抽象工厂不需要。

# 假设一个披萨店提供多种披萨，对应的抽象工厂：
from abc import ABCMeta, abstractmethod


class PizzaFactory(metaclass=ABCMeta):
    # 有蔬菜的披萨
    @abstractmethod
    def create_veg_pizza(self):
        pass

    # 没蔬菜的披萨
    @abstractmethod
    def create_non_veg_pizza(self):
        pass


class USAPizzaFactory(PizzaFactory):
    # USA披萨店里有蔬菜的披萨是玉米披萨
    def create_veg_pizza(self):
        return CornPizza()

    # USA店里没蔬菜的披萨是牛肉披萨
    def create_non_veg_pizza(self):
        return BeefPizza()


class ChinaPizzaFactory(PizzaFactory):
    # 中国披萨店里有蔬菜的披萨是水果披萨
    def create_veg_pizza(self):
        return FruitsPizza()

    # 中国披萨店里没有蔬菜的披萨是羊肉披萨
    def create_non_veg_pizza(self):
        return MuttonPizza()


# 接下来定义4种披萨和他们的父类（有蔬菜和无蔬菜）
class VegPizza(metaclass=ABCMeta):
    @abstractmethod
    def prepare(self, veg_pizza):
        pass


# 没蔬菜的披萨在有蔬菜的披萨上面加肉就可以
class NonVegPizza(metaclass=ABCMeta):
    @abstractmethod
    def serve(self, veg_pizza):
        pass


class CornPizza(VegPizza):
    def prepare(self):
        print(type(self).__name__, '来了')


class BeefPizza(NonVegPizza):
    def serve(self, veg_pizza):
        print(type(self).__name__, '来了，牛肉是加在', type(veg_pizza).__name__,'里面的')


class FruitsPizza(VegPizza):
    def prepare(self):
        print(type(self).__name__, '来了')


class MuttonPizza(NonVegPizza):
    def serve(self, veg_pizza):
        print(type(self).__name__, '来了，羊肉是加在', type(veg_pizza).__name__,'里面的')


class PizzaStore(object):
    def __init__(self):
        pass

    def make_pizzas(self):
        # 创建的是所有对象（所有披萨），而不是单个指定对象
        for factory in [USAPizzaFactory(), ChinaPizzaFactory()]:
            self.factory = factory
            self.non_veg_pizza = self.factory.create_non_veg_pizza()
            self.veg_pizza = self.factory.create_veg_pizza()
            # 调用
            self.veg_pizza.prepare()
            self.non_veg_pizza.serve(self.veg_pizza)


# 工厂方法和抽象工厂的比较
# 工厂方法	                    抽象工厂
# 开放一个创建对象的方法	        包含一个或多个工厂方法来创建一系列对象
# 使用继承和子类来决定创建什么对象	实用组合将创建对象的任务交给其他类
# 创建一个产品	                创建相关系列（一群组）产品

def test():
    # 1
    ff = ForestFactory()
    animal = 'Cat'
    ff.say_something(animal)
    # 结果 i am cat

    # 2
    # 要创建ConcreteCreator1这个对象
    profile_type = 'ConcreteCreator1'
    profile = eval(profile_type)()
    print(type(profile).__name__)
    print(profile.get_sections())

    # 3
    pizza = PizzaStore()
    pizza.make_pizzas()


if __name__ == '__main__':
    test()