# coding: utf-8
# 检查成对的 {} [] ()

def isValid(s):
    while True:
        length = len(s)
        s = s.replace("{}", "").replace("[]", "").replace("()", "")
        if length == len(s):
            break
    return len(s) == 0

# stack
def isValid2(s):
    dic = {"}": "{", "]": "[", ")": "("}
    stack = []
    for i in s:
        if i not in dic:
            stack.append(i)
        elif not stack or dic[i] != stack.pop():
            return False
    return not stack

def test():
    s = '{[()]}'
    s2 = '{[(])}'
    assert isValid(s) == isValid2(s)
    assert isValid(s2) == isValid2(s2)

if __name__ == '__main__':
    test()
