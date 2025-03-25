


def containsDuplicate(nums: list[int]) -> bool:
    return False if len(set(nums)) == len(nums) else True


nums = [1, 2, 3, 1]
nums1 = [1, 2, 3, 4]
nums2 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
print(containsDuplicate(nums2))
