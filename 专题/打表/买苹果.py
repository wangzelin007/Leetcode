# 商店只有能装下6个苹果的袋子和能装下8个苹果的袋子。
# 小王去买苹果，要求：
# 1. 苹果必须装满每个袋子
# 2. 使用的袋子数量必须最少
# 输入：一个正整数N，返回最少使用的袋子数量。
# 如果N无法让每个袋子都装满，返回-1
# 直接通过找规律发现数学原理
def minBagBase(apple):
    # 基数返回 -1
    if apple & 1 != 0: return -1
    if apple < 18:
        return 0 if apple == 0 else (
            1 if apple == 6 or apple ==8 else (
            2 if apple == 12 or apple == 14 or apple == 16 else -1))
    return (apple - 18) // 8 + 3

def test():
    for i in range(1, 101):
        print(minBagBase(i), end='\n')

if __name__ == '__main__':
    test()