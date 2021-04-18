# 全字母句 指包含英语字母表中每个字母至少一次的句子。
# 给你一个仅由小写英文字母组成的字符串 sentence ，请你判断 sentence 是否为 全字母句 。
# 如果是，返回 true ；否则，返回 false 。
# 示例 1：
# 输入：sentence = "thequickbrownfoxjumpsoverthelazydog"
# 输出：true
# 解释：sentence 包含英语字母表中每个字母至少一次。
# 示例 2：
# 输入：sentence = "leetcode"
# 输出：false

class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        c = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}
        c2 = set(sentence)
        if c - c2: return False
        else: return True

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return len(set(sentence)) == 26

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        a = [0 for _ in range(26)]
        for c in sentence:
            idx = ord(c) - ord('a')
            a[idx] = 1
        return sum(a)==26

if __name__ == '__main__':
    s = Solution()
    sentence = 'thequickbrownfoxjumpsoverthelazydog'
    assert s.checkIfPangram(sentence) == True
    sentence = 'leetcode'
    assert s.checkIfPangram(sentence) == False
