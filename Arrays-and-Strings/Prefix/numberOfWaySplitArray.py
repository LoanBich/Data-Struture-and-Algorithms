"""
Example 2: 2270. Number of Ways to Split Array

Given an integer array nums, find the number of ways to split the array into two parts so that the first section has a sum greater than or equal to the sum of the second section. The second section should have at least one number.
"""


def numberWaysSplitArray(nums: list[int]) -> int:
    prefix = [nums[0]]
    for i in range(1, len(nums)):
        prefix.append(nums[i] + prefix[i - 1])

    ans = []
    for i in range(len(prefix) - 1):
        ans.append(prefix[i] >= prefix[-1] - prefix[i])

    return ans.count(True)


print(numberWaysSplitArray([10, 4, -8, 7]))
