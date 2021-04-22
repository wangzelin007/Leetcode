# 小跟堆求第K大
# 可以先建立k个元素的小根堆，则堆顶就是最小值。
# 若k之后的元素大于堆顶，则应该插入该堆，从k开始，一直循环遍历完整个数组，则堆顶就是第k大的数。

#可借助python中的heapq模块实现堆的功能, 注意建立的是小根堆
class Solution1:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        import heapq as hq
        heap = []
        for i in nums:
            hq.heappush(heap, i)

            if len(heap) > k:
                hq.heappop(heap)
        return heap[0]

# 自己实现堆
class Solution2:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        n = len(nums)
        heap = nums[:k]
        # 建立含k个元素的小根堆
        for i in range((k-2)//2, -1, -1):
            self.sift(heap, i, k-1)

        #若k之后的元素大于根节点，则将该元素与根节点替换，然后做一次调整
        for j in range(k,n):
            if nums[j] > heap[0]: #找前k大的数
                heap[0] = nums[j]
                self.sift(heap, 0 , k-1)
        # print(heap)
        return heap[0] #堆顶就是第k大的数了

    # 注意这里要建立小根堆
    def sift(self, alist, low, high):
        # 假设只有根节点需要调整，两棵子树都是堆
        i = low
        j = i *2 +1 #j指向i的左子树
        tmp = alist[i]
        while j <=high:
            if j+1<= high and alist[j] > alist[j+1]: #右子树比较小,则指向右子树
                j = j+1
            if alist[j] < tmp:  # 若子树的值比较小，则根节点换成子树，然后向下看一层
                alist[i] = alist[j]
                i = j
                j = i *2 +1
            else:
                alist[i] = tmp # 子树的值大于根节点，则根节点就放在这一层
                break
        else:
            alist[i] = tmp # j越界跳出循环，则把根节点放在叶子节点

if __name__ == '__main__':
    s = Solution1()
    nums = [9,7,3,1,2,5,8,11]
    print (sorted(nums, reverse=True))
    k = 3
    print(s.findKthLargest(nums, k))
# 作者：xiao-xie-shui-bu-xing
# 链接：https://leetcode-cn.com/problems/kth-largest-element-in-an-array/solution/ge-chong-pai-xu-suan-fa-tu-xie-zong-jie-by-ke-ai-x/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。