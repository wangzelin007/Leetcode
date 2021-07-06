# coding: utf-8
# 给定一个字符串str，给定一个字符串类型的数组arr。
# arr里的每一个字符串，代表一张贴纸，你可以把单个字符剪开使用，目的是拼出str来。
# 返回至少需要多少张贴纸可以完成这个任务。
# str = "babac"; arr=["ba","c","abcd"]
# 至少需要两张 "ba" + "abcd" 即可拼出。

def minStickers(arr, str):
    n = len(arr)
    arr_dict = {}

    for index, value in enumerate(arr):
        arr_dict[index] = {}
        for s in arr[index]:
            arr_dict[index][s] = 1 if s not in arr_dict[index] else arr_dict[index][s] + 1
    rest_dict = {}
    for s in str:
        rest_dict[s] = 1 if s not in rest_dict else rest_dict[s] + 1
    return process(arr_dict, rest_dict)


def process(arr, rest):
    if sum(rest.values()) == 0:
        return 0
    ans = float("inf")
    for i in arr.keys():
        restKeys = filter(lambda i: rest[i] != 0, rest.keys())
        continueFlag = True
        for key in restKeys:
            if key in arr[i].keys():
                continueFlag = False
                break
        if continueFlag:
            continue
        # restDict = rest - arr[i]
        reverse = {}
        for key, value in arr[i].items():
            if key in rest and rest[key] != 0:
                if arr[i][key] >= rest[key]:
                    reverse[key] = rest[key]
                    rest[key] = 0
                else:
                    reverse[key] = rest[key]
                    rest[key] -= arr[i][key]
        restMin = process(arr, rest)
        # 还原现场
        for key in reverse:
            rest[key] = reverse[key]
        ans = min(ans, restMin)
    return ans + 1

def minStickers1(arr, str):
    n = len(arr)
    arr_map = [[0] * 26 for _ in range(n)]
    for index, str in enumerate(arr):
        for s in str:
            # Return the integer ordinal of a one-character string.
            arr_map[index][ord(s)-ord('a')] += 1
    dp = {"": 0}
    return process1(arr_map, str, dp)

# 动态规划的本质是在傻缓存的基础上做细粒度的分解
# 但是本题 rest 的可能性太多，不好分解。
def process1(arr, rest, dp):
    if rest in dp:
        return dp[rest]
    ans = float("inf")
    n = len(arr)
    rmap = [0] * 26
    for s in rest:
        rmap[ord(s) - ord('a')] += 1
    for i in range(n):
        if arr[i][ord(rest[0]) - ord('a')] == 0:
            continue
        stringBuilder = []
        for j in range(26):
            if rmap[j] > 0:
                for k in range(max(0, rmap[j] - arr[i][j])):
                    stringBuilder.append(chr(ord('a') + j))
        sb = "".join(stringBuilder)
        tmp = process1(arr, sb, dp)
        if tmp != -1:
            ans = min(ans, tmp + 1)
    dp[rest] = -1 if ans == float("inf") else ans
    return dp[rest]


def test():
    arr = ["ba","c","abcd","cabab"]
    str = "babac"
    print(minStickers(arr, str))
    print(minStickers1(arr, str))

if __name__ == '__main__':
    test()