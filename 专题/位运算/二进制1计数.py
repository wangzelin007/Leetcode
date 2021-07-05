def countOne(num):
    count = 0
    while num:
        rightOne = num & (-num)
        num ^= rightOne
        count += 1
    return count

def test():
    # 11 1011
    assert countOne(11) == 3

if __name__ == '__main__':
    test()