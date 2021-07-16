arr = [1,2,3,5,5,5,7,8,9,10]

# 边界有问题！！！
def get_range(arr, target):
    l, r = 0, len(arr) - 1
    while l <= r:
        m = (l + r) // 2
        if arr[m] < target:
            small = m
            l = m + 1
        else:
            r = m - 1
    l, r = 0, len(arr) - 1
    while l <= r:
        m = (l + r) // 2
        if arr[m] > target:
            big = m
            r = m - 1
        else:
            l = m + 1
    return [small+1, big-1]

def test():
    assert  get_range(arr, 5) == [3,5]

if __name__ == '__main__':
    test()