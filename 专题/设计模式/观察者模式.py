# coding: utf-8
# 观察者模式
# 是一种行为型设计模式
# 行为型设计模式
# 创建型模式基于对象的创建机制，隔离对象的创建细节，使得代码能够与对象类***相互独立***。
# 结构型设计模式用于***设计对象和类的结构***，从而优化他们的结构，和他们之间的关系。
# 行为型设计模式在于***关注对象的职责***，用来处理对象之间的交互。
# 实现
# 定义对象之间一对多的关系，使得对象的变化可以通知其他对象
# 封装主题核心组件
# 实例：分布式系统中事件服务、新闻机构、股票通知
# 一个新闻发布机构和他的订阅者们（观察者们）例子：

# 主题行为类
class NewsPublisher:
    def __init__(self):
        self.__subscribers = [] # 存放这个类的对象的观察者们
        self.__latestNews = None

    # 观察者通过这个方法注册进来，放在客户端的列表里
    def attach(self, subscriber):
        self.__subscribers.append(subscriber)

    # 删除观察者
    def detach(self):
        return self.__subscribers.pop()

    # 返回已经注册的所有观察者
    def subscribers(self):
        return [type(x).__name__ for x in self.__subscribers]

    # 遍历所有观察者，通过观察者的update方法打印出观察者获取的最新消息
    def notify_subscribers(self):
        for sub in self.__subscribers:
            sub.update()

    # 添加新消息
    def add_news(self, news):
        self.__latestNews = news

    # 返回最新消息
    def get_news(self):
        return self.__latestNews


# 观察者接口，抽象方法
from abc import ABCMeta, abstractmethod
class Subscriber(metaclass=ABCMeta):
    @abstractmethod
    def update(self):
        pass


# 观察者email
class EmailSubscriber:
    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)

    def update(self):
        print(type(self).__name__, self.publisher.get_news())


# 观察者sms
class SMSSubscriber:
    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)

    def update(self):
        print(type(self).__name__, self.publisher.get_news())


# 用来演示Observers和Subject的松耦合关系
class AnyOtherSubscriber:
    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)

    def update(self):
        print(type(self).__name__, self.publisher.get_news())


if __name__ == '__main__':
    # 创建一个客户端对象
    news_publisher = NewsPublisher()

    # 创建3个观察者
    for subscribers in [SMSSubscriber, EmailSubscriber, AnyOtherSubscriber]:
        subscribers(news_publisher)

    # 打印出所有观察者列表
    print('\nsubscribers:', news_publisher.subscribers())

    # 添加一个消息
    news_publisher.add_news('hello')

    # 提醒所有观察者新消息，
    news_publisher.notify_subscribers()

    print(type(news_publisher.detach()).__name__)
    print(news_publisher.subscribers())

    news_publisher.add_news('第二个消息')
    news_publisher.notify_subscribers()


# 观察者模式的通知方式
# 拉模型
# 观察者是积极的，每当发生变化主题都会给所有观察者广播
# 出现变化的时候，观察者负责获取
# 效率比较低，因为他要先主题通知观察者，再观察者从主题那提取数据
# 推模型
# 主题是主导的一方，只发送观察者所需的数据
# 出现的变化，由主题直接推送到观察者，避免了不必要的数据，节省了时间

# 观察者模式优缺点
# 优点：
# 可以保持松耦合
# 无需对主题或者观察者修改也能高效的发送数据到其他对象。
# 可以随时添加删除观察者
# 缺点：
# 观察者接口必须有具体观察者实现，需要继承。无法进行组合，因为他可以实例化。
# 实现不当会增加观察者的复杂性
# 通知可能不可靠，导致不一致性。

# 一些问题
# 可能存在多个主题或者观察者吗？
# 可以，这种情况要正常工作就必须通知观察者那些主题发生了变化以及各个主题中发生了什么变化
# 谁负责触发更新？
# 一般情况下，主题触发更新方法。如果有特别需要，可以观察者触发，但要注意频率不能太高。
# 主题或者观察者可以在任何其他用例中访问吗？
# 可以，这是松耦合的强大体现，可以独立使用。