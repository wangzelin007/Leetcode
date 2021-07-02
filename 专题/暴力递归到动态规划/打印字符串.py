# coding: utf-8
# 1. 打印字符串的全部子序列
def printSubs(s):
    path = ""
    ans = []
    process(s, 0, ans, path)
    return ans

def process(s, index, ans, path):
    if index == len(s):
        ans.append(path)
        return
    no = path
    process(s, index+1, ans, no)
    yes = path + s[index]
    process(s, index+1, ans, yes)

# 2. 打印字符串的全部子序列，要求不要出现重复的子序列
def printSubsNorepeat(s):
    ans = set()
    path = ""
    process1(s, 0, ans, path)
    return ans

def process1(s, index, ans, path):
    if index == len(s): # 最后一个选完了才能记录
        ans.add(path)
        return
    no = path
    process1(s, index+1, ans, no)
    yes = path + s[index]
    process1(s, index+1, ans, yes)

# 3. 打印字符串的全排列
def printAllPremutation(s):
    ans = []
    if not s or len(s) == 0:
        return ans
    s = list(s)
    def _process(s, i, ans):
        if i == len(s):
            ans.append(''.join(s))
            return
        for j in range(i, len(s)): # 不交换的也算呀
            s[i], s[j] = s[j], s[i]
            _process(s, i+1, ans)
            s[i], s[j] = s[j], s[i]
    _process(s, 0, ans)
    return ans

# 4. 打印字符串的全排列，要求不要出现重复的排列
def printAllPremutationNorepeat(s):
    ans = []
    if not s or len(s) == 0:
        return ans
    s = list(s)
    def _process(s, i, ans):
        if len(s) == i:
            ans.append(''.join(s))
            return
        visit = set()
        for j in range(i, len(s)):
            if s[j] not in visit:
                visit.add(s[j])
                s[i], s[j] = s[j], s[i]
                _process(s, i+1, ans)
                s[i], s[j] = s[j], s[i]

    _process(s, 0, ans)
    return ans

def test():
    s = 'abb'
    print(printSubs(s))
    print(printSubsNorepeat(s))
    print(printAllPremutation(s))
    print(printAllPremutationNorepeat(s))

if __name__ == '__main__':
    test()