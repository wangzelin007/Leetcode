import random
import string
import unittest


class Solution:
    def find_first_repeat(self, word: str) -> str:
        for id, w in enumerate(word):
            if w in word[id + 1: len(word)]:
                return w

    def find_first_repeat_by_dict(self, word: str) -> str:
        dic = {}
        opt = float('inf')
        for id, w in enumerate(word):
            if w in dic and dic[w] < opt:
                opt = dic[w]
            else:
                dic[w] = id
        return word[opt] if opt < len(word) else None


class TestSolution(unittest.TestCase):
    def test_base_case(self):
        s = Solution()
        # repeat at last
        assert s.find_first_repeat('catyzyxy') == 'y'
        # repeat at first
        assert s.find_first_repeat('cccyaty') == 'c'
        # repeat at middle
        assert s.find_first_repeat('message') == 'e'
        # multi repeat return the first one
        assert s.find_first_repeat('message') != 's'
        # no repeat
        assert s.find_first_repeat('bed') is None

    def test_by_compare(self):
        s = Solution()
        for i in range(100000):
            word = ''.join([random.choice(string.ascii_lowercase)
                            for _ in range(random.randint(1, 10))])
            assert s.find_first_repeat(word) == s.find_first_repeat_by_dict(word)
        print("Pass 100000 test cases")

if __name__ == '__main__':
    unittest.main()