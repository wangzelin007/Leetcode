def countOne(num):
    count = 0
    while num:
        rightOne = num & (-num)
        num ^= rightOne
        count += 1
    return count

def countOne2(num):
    count = 0
    while num:
        num &= num - 1
        count += 1
    return count

def test():
    # 11 1011
    assert countOne(11) == 3
    assert countOne2(11) == 3

if __name__ == '__main__':
    test()