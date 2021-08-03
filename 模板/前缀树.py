# -*- coding: utf-8 -*-
"""
    :author: Wang Zelin (王泽霖)
    :url: 
    :copyright: © 2018 Wang Zelin <1064534588@qq.com>
    :license: MIT, see LICENSE for more details.
"""
from pprint import pprint

class Trie(object):
    def __init__(self):
        self.root = {}
        self.end_of_word = "#"

    def insert(self, word):
        node = self.root
        for char in word:
            # 如果键不存在于字典中，将会添加键并将值设为默认值。
            node = node.setdefault(char, {})
        node[self.end_of_word] = self.end_of_word

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node:
                return False
            node = node[char]
        return self.end_of_word in node

    def startsWith(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node:
                return False
            node = node[char]
        return True

def test():
    t = Trie()
    t.insert('word')
    t.insert('peace')
    pprint(t.root)
    assert t.search('word') == True
    assert t.search('wordy') == False
    assert t.startsWith('wo') == True

if __name__ == '__main__':
    test()