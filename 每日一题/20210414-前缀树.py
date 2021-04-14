# _*_ coding: utf-8 _*_
# Trie（发音类似 "try"）或者说 前缀树 是一种树形数据结构，用于高效地存储和检索字符串数据集中的键。
# 这一数据结构有相当多的应用情景，例如自动补完和拼写检查。
# 请你实现 Trie 类：
# Trie() 初始化前缀树对象。
# void insert(String word) 向前缀树中插入字符串 word 。
# boolean search(String word) 如果字符串 word 在前缀树中，返回 true（即，在检索之前已经插入）；否则，返回 false 。
# boolean startsWith(String prefix) 如果之前已经插入的字符串 word 的前缀之一为 prefix ，返回 true ；否则，返回 false 。
#
# 示例：
# 输入
# ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
# [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
# 输出
# [null, null, true, false, true, null, true]
# 解释
# Trie trie = new Trie();
# trie.insert("apple");
# trie.search("apple");   // 返回 True
# trie.search("app");     // 返回 False
# trie.startsWith("app"); // 返回 True
# trie.insert("app");
# trie.search("app");     // 返回 True
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/implement-trie-prefix-tree
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.lookup = {}


    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        tree = self.lookup
        for a in word:
            if a not in tree:
                tree[a] = {}
            tree = tree[a] # 为了搜索下一个而移动tree
        tree['#'] = '#'
        print self.lookup

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        tree = self.lookup
        for a in word:
            if a not in tree:
                return False
            tree = tree[a] # 为了搜索下一个而移动tree
        if '#' in tree:
            return True
        return False

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        tree = self.lookup
        for a in prefix:
            if a not in tree:
                return False
            tree = tree[a] # 为了搜索下一个而移动tree
        return True

if __name__ == '__main__':
    obj = Trie()
    print(obj.insert('apple'))
    print(obj.search('apple'))
    print(obj.search('app'))
    print(obj.startsWith('app'))
    print(obj.insert('app'))
    print(obj.search('app'))
    strs = 'abc'
    strs.startswith('a')
    strs.endswith('a')
    import collections

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)