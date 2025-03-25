

def productExceptSelf(nums: list[int]) -> list[int]:

    result = [1] * len(nums)

    postfix = prefix = 1
    for i in range(1, len(nums)):
        result[i] = prefix
        prefix = prefix * nums[i]

    for i in range(len(nums) - 1, -1, -1):
        result[i] = result[i] * postfix
        postfix = postfix * nums[i]
    return result


print(productExceptSelf([1, 2, 3, 4]))
