class Person:

    def __init__(self):
        self.__age = 0

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, num):
        if num > 18:
            self.__age = num
        else:
            raise ValueError("age must < 18.")

    @age.deleter
    def age(self):
        print("will delete age")
        del self.__age

p = Person()
print(p.age)
p.age = 44
print(p.age)
del p.age
print(p.age)