# x..x......x..x.
# x代表墙，无法放灯也不需要照亮
# .代表居民，需要全部照亮，可以放灯
# 每一盏灯可以照亮本身和左右一个位置

# 暴力，每个位置都可以放灯或者不放灯
# 记得还原现场
def minLight(road):
    if not road or len(road) == 0: return 0
    return process(road, 0, set())

def process(road, index, lights):
    if index == len(road):
        for i in range(len(road)):
            if road[i] != 'X':
                if i-1 not in lights and i not in lights and i+1 not in lights:
                    return float('inf')
        return len(lights)
    else:
        no = process(road, index+1, lights)
        yes = float('inf')
        if road[index] == '.':
            lights.add(index)
            yes = process(road, index+1, lights)
            lights.remove(index)
        return min(no, yes)

# 1. 当前为止是 x ，直接去下一步做决定
# 2. 当前位置是 . ，继续分析
#   2.0 一定会放灯，只是暂时不知道放哪里，灯++
#   2.1 如果没有路了，结束
#   2.2 如果下一步是x 相当于2.0灯就放在了i位置，直接跳到i+2继续决策
#   2.3 如果下一步也是. 那么无论下下一步是什么 ... or ..x 都在i+1放灯，即2.0的灯放在了i+1位置，直接跳到i+3继续决策
def minLight2(road):
    index, lights = 0, 0
    while index < len(road):
        if road[index] == 'x':
            index += 1
        else: # i = '.'
            lights += 1
            if index + 1 == len(road): # 没有路
                break
            else:
                if road[index+1] == 'x':
                    index += 2
                else:
                    index += 3
    return lights


def test():
    road = ['X','.','.','X','.','.','.','.','X']
    # print(minLight(road))
    assert minLight(road) == minLight2(road)

if __name__ == '__main__':
    test()