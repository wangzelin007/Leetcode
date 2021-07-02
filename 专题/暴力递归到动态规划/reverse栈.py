# f 作用是 return 栈底元素
def f(stack):
    result = stack.pop()
    if len(stack) == 0:
        return result
    else:
        last = f(stack)
        stack.append(result)
        return last

# BA
# AB
def reverse(stack):
    if len(stack) == 0:
        return
    # 获取原来栈中栈底元素
    i = f(stack)
    # reverse栈
    reverse(stack)
    # 追加到栈顶
    stack.append(i)

def test():
    stack = [1,2,3]
    reverse(stack)
    assert stack == [3,2,1]

if __name__ == '__main__':
    test()