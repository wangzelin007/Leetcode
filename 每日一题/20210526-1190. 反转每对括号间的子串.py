# 给出一个字符串s（仅含有小写英文字母和括号）。
# 请你按照从括号内到外的顺序，逐层反转每对匹配括号中的字符串，并返回最终的结果。
# 注意，您的结果中 不应 包含任何括号。
# 示例 1：
# 输入：s = "(abcd)"
# 输出："dcba"
# 示例 2：
# 输入：s = "(u(love)i)"
# 输出："iloveu"
# 示例 3：
# 输入：s = "(ed(et(oc))el)"
# 输出："leetcode"
# 示例 4：
# 输入：s = "a(bcdefghijkl(mno)p)q"
# 输出："apmnolkjihgfedcbq"
# 提示：
# 0 <= s.length <= 2000
# s 中只有小写英文字母和括号
# 我们确保所有括号都是成对出现的
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/reverse-substrings-between-each-pair-of-parentheses
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
#                   (ed(et(oc))el)
# c                                                   l                     l
# o                      o                            e                     e
# (                      c                      e     e                     e
# t                 t    t                      t     t                     t
# e  -> tmp: co ->  e -> e -> tmp: octe ->   -> c ->  c -> tmp: leetcode -> c -> leetcode
# (                 (    (                      o     o                     o
# d                 d    d                 d    d     d                     d
# e                 e    e                 e    e     e                     e
# (                 (    (                 (    (     (

class Solution1:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for c in s:
            if c != ')':
                stack.append(c)
            elif c == ')':
                tmp = []
                while stack and stack[-1] != '(':
                    tmp.append(stack.pop())
                stack.pop()
                stack += tmp
        return "".join(stack)

class Solution2:
    def reverseParentheses(self, s: str) -> str:
        stack = [[]]
        for c in s:
            if c == '(':
                stack.append([])
            elif c == ')':
                temp = reversed(stack.pop())
                stack[-1] += temp
            else:
                stack[-1].append(c)
        return "".join(stack[0])

if __name__ == '__main__':
    s = Solution2()
    print(s.reverseParentheses("(ed(et(oc))el)"))