


from collections import defaultdict


def topKFrequent(nums: list[int], k: int) -> list[int]:
    result = []
    dic = defaultdict(int)
    for num in nums:
        dic[num] += 1

    for _ in range(k):
        maxNum = max(dic, key=dic.get())
        result.append(maxNum)
        dic.pop(maxNum)
    return result


# another solution
def topKFrequent2(nums: list[int], k: int) -> list[int]:
    count = {}
    freq = [[] for i in range(len(nums) + 1)]

    for num in nums:
        count[num] = 1 + count.get(num, 0)
    for num, cnt in count.items():
        freq[cnt].append(num)

    res = []
    for i in range(len(freq) - 1, 0, -1):
        for num in freq[i]:
            res.append(num)
            if len(res) == k:
                return res
