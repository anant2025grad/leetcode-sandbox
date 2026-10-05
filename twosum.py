nums = [2, 7, 11, 15]
target = 9
def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    seen1 = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in seen1:
            return [seen1[complement], i]

        seen1[num] = i

print(twoSum(nums, target))