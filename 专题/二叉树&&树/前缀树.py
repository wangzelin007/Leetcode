class Node:
    def __init__(self):
        self.pas = 0
        self.end = 0
        self.next = {}

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        if not word: return
        cur = self.root
        cur.pas += 1
        for i in word:
            if i not in cur.next:
                cur.next[i] = Node()
            cur = cur.next[i]
            cur.pas += 1
        cur.end += 1

    def search(self, word):
        if not word: return
        cur = self.root
        for i in word:
            if i not in cur.next:
                return 0
            cur = cur.next[i]
        return cur.end

    def prefixNumber(self, pre):
        if not pre: return 0
        cur = self.root
        for i in pre:
            if i not in cur.next:
                return 0
            cur = cur.next[i]
        return cur.pas

    def delete(self, word):
        if self.search(word) != 0:
            cur = self.root
            cur.pas -= 1
            for i in word:
                if cur.next[i].pas == 0:
                    cur.next[i] == None
                    return
                cur = cur.next[i]
            cur.end -= 1

def test():
    t = Trie()
    t.insert('abc')
    t.insert('abcd')
    t.insert('abd')
    assert t.search('abc') == 1
    assert t.search('ac') == 0
    assert t.prefixNumber('ab') == 3
    assert t.prefixNumber('abc') == 2
    assert t.prefixNumber('abe') == 0
    t.insert('abc')
    assert t.search('abc') == 2
    t.delete('abc')
    assert t.search('abc') == 1
    t.delete('abc')
    assert t.search('abc') == 0
    t.delete('abc')
    assert t.search('abc') == 0

if __name__ == '__main__':
    test()