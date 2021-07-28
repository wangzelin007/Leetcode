def get_most_value(arr):
    n = len(arr)
    most_value = arr[0]
    count = 1
    for i in range(1, n):
        if count > 0:
            if most_value == arr[i]:
                count += 1
            else:
                count -= 1
        else:
            most_value = arr[i]
            count += 1
    return most_value

def test():
    arr = [1, 1, 1, 1, 2, 3, 2, 3, 1, 1]
    assert get_most_value(arr) == 1

if __name__ == '__main__':
    test()