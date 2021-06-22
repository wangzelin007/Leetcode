class LinkList:
    class Node:
        def __init__(self, item=None):
            self.item = item
            self.next = None

    class LinkListIterator:
        def __init__(self, node):
            self.node = node

        # py3
        def __next__(self):
            if self.node:
                cur_node = self.node
                self.node = cur_node.next
                return cur_node.item
            else:
                raise StopIteration

        def __iter__(self):
            return self

        # py2
        def next(self):
            if self.node:
                cur_node = self.node
                self.node = cur_node.next
                return cur_node.item
            else:
                raise StopIteration

        def iter(self):
            return self

    def __init__(self, iterable=None):
        self.head = None
        self.tail = None
        if iterable:
            self.extend(iterable)

    def append(self, obj):
        s = LinkList.Node(obj)
        if not self.head:
            self.head = s
            self.tail = s
        else:
            self.tail.next = s
            self.tail = s

    def extend(self, iterable):
        for obj in iterable:
            self.append(obj)

    def find(self, obj):
        for n in self:
            if n == obj:
                return True
        else:
            return False

    def remove(self, obj):
        pre = None
        cur = self.head
        while cur:
            if cur.item == obj:
                if not pre:
                    self.head = self.head.next
                else:
                    pre.next = cur.next
                return True
            pre = cur
            cur = cur.next
        else:
            return False

    def __iter__(self):
        return self.LinkListIterator(self.head)

    def __repr__(self):
        return "<<"+", ".join(map(str, self))+">"

class HashTable:
    def __init__(self, size=101):
        self.size = size
        self.T = [LinkList() for _ in range(self.size)]

    def h(self, k):
        return k % self.size

    def insert(self, k):
        i = self.h(k)
        if self.find(k):
            print("Duplicated Insert.")
        else:
            self.T[i].append(k)

    def find(self, k):
        i = self.h(k)
        return self.T[i].find(k)

    def remove(self, k):
        i = self.h(k)
        self.T[i].remove(k)

ht = HashTable()
ht.insert(0)
ht.insert(1)
ht.insert(102)
ht.insert(103)
print(ht.find(102))
print(ht.find(104))
ht.remove(102)
print(ht.find(1))
print(ht.find(102))
ht.remove(1)
print(ht.find(1))
