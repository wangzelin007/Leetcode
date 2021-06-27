def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        left = 0
        right = i - 1
        tmp = arr[i]
        j = i
        while left <= right:
            mid = (left + right) // 2
            #利用二分查找的特性，对中间位置的值与待插入数字比较
            if tmp > arr[mid]:
                left = mid+1
            elif tmp < arr[mid]:
                right = mid-1
                j = mid
            else:
                j = mid
        right = i - 1
        id = j
        # 将插入位置之后的数逆序依次往后移动一位。
        while id <= right:
            arr[right+1] = arr[right]
            right -= 1
        arr[j] = tmp
    print(arr)

arr = [7, 9, 14, 51, 2, 8, 32, 1, 88, 29, 30, 11, 18]
insertion_sort(arr)