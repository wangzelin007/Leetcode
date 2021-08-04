class Solution:
    def find_first_repeat(self, word: str) -> str:
        for id, w in enumerate(word):
            if w in word[id + 1: len(word)]:
                return w


def test():
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

if __name__ == '__main__':
    test()