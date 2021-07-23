# -*- coding: utf-8 -*-
import hashlib
# from hash_ring import HashRing

content = """In computer science, consistent hashing is a special kind of 
hashing such that when a hash table is resized, only K/n keys need to be 
remapped on average, where K is the number of keys, and n is the number of 
slots. In contrast, in most traditional hash tables, a change in the number 
of array slots causes nearly all keys to be remapped because the mapping 
between the keys and the slots is defined by a modular operation."""

servers = [
    "10.10.1.1",
    "10.10.2.2",
    "10.10.3.3",
    "10.10.4.4",
]
database = {s: [] for s in servers}

class HashRing:
    def __init__(self, nodes=None, replicas=3):
        """
        :param nodes:           所有的节点
        :param replicas:        一个节点对应多少个虚拟节点，为了解决实际节点过少导致的分配不均问题。
        :return:
        """
        self.replicas = replicas # 每一个节点对应多少个虚拟节点
        self.ring = dict()       # 保存虚拟节点的hash值与node的对应关系
        self._sorted_keys = []   # 用于存放所有的虚拟节点的hash值，这里需要保持排序

        if nodes:
            for node in nodes:
                self.add_node(node)

    def add_node(self, node):
        """
        Adds a `node` to the hash ring (including a number of replicas)
        添加node，首先要根据虚拟节点的数目，创建所有的虚拟节点，并将其与对应的node对应起来
        当然还需要将虚拟节点的hash值放到排序的里面
        这里在添加了节点之后，需要保持虚拟节点hash值的顺序
        """
        for i in range(self.replicas):
            virtual_node = f"{node}#{i}"
            key = self.gen_key(virtual_node)
            self.ring[key] = node
            self._sorted_keys.append(key)
            # print(f"{virtual_node} --> {key} --> {node}")

        self._sorted_keys.sort()
        print([self.ring[key]+':'+key for key in self._sorted_keys])

    def remove_node(self, node):
        """
        Removes `node` from the hash ring and its replicas
        一个节点退出，需要将这个节点的所有的虚拟节点都删除
        """
        for i in range(self.replicas):
            key = self.gen_key(f"{node}#{i}")
            del self.ring[key]
            self._sorted_keys.remove(key)

    def get_node(self, string_key):
        """
        Given a string key a corresponding node in the hash ring is returned.
        If the hash ring is empty, `None` is returned.
        """
        return self.get_node_pos(string_key)[0]

    def get_node_pos(self, string_key):
        """
        Given a string key a corresponding node in the hash ring is returned
        along with it's position in the ring.
        If the hash ring is empty, (`None`, `None`) is returned.
        返回这个字符串应该对应的node，这里先求出字符串的hash值，然后找到第一个小于的虚拟节点，然后返回node
        如果hash值大于所有的节点，那么用第一个虚拟节点
        """
        if not self.ring:
            return None, None

        key = self.gen_key(string_key)
        virtual_nodes = self._sorted_keys
        for i in range(len(virtual_nodes)):
            virtual_node = virtual_nodes[i]
            if key < virtual_node:
                print(f"{string_key} --> {key} --> {virtual_node}")
                return self.ring[virtual_node], i

        # 如果key > node，那么让这些key落在第一个node上就形成了闭环
        # print(f"{string_key} --> {key} --> {nodes[0]}")
        # 返回的是node 和 virtual_node 下标
        return self.ring[virtual_nodes[0]], 0

    def get_nodes(self, string_key):
        """Given a string key it returns the nodes as a generator that can hold the key.
        The generator is never ending and iterates through the ring
        starting at the correct position.
        """
        if not self.ring:
            yield None, None
        node, pos = self.get_node_pos(string_key)
        for key in self._sorted_keys[pos:]:
            yield self.ring[key]
        while True:
            for key in self._sorted_keys:
                yield self.ring[key]

    def gen_key(self, string_key):
        """
        Given a string key it returns a long value, this long value represents
        a place on the hash ring
        通过key，返回当前key的hash值，这里采用md5
        """
        m = hashlib.md5()
        m.update(string_key.encode('utf-8'))
        return m.hexdigest()


def consistent_hash(replicas):
    hr = HashRing(servers, replicas)
    words = content.split()

    for w in words:
        database[hr.get_node(w)].append(w)
    print(f"words={len(words)}\n")

    for node, result in database.items():
        print(f"{node}={len(result)}\nresult={result}")

    print("\nserver 3 down ,remove server 3")
    # remove node
    hr.remove_node(servers[2])
    for w in database[servers[2]]:
        database[hr.get_node(w)].append(w)
    del database[servers[2]]
    for node, result in database.items():
        print(f"{node}={len(result)}\nresult={result}")

    # print("\nserver 3 up ,add server 3")
    # add node
    # hr.add_node(servers[2])
    # todo
    # 如何找到需要迁移的key?
    # 1. 找到 比新增的虚拟节点大的虚拟节点。 这些虚拟节点可能位于多个 node 上，所以比较麻烦。
    # 2. 获取这些虚拟节点上的 key。
    # 3. 依次删除这些 key 并重新执行 hash。
    # 不然只能遍历所有的 key 才知道哪些需要迁移。



if __name__ == '__main__':
    consistent_hash(3)
