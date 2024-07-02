"""
Given a 2D integer array nums where nums[i] is a non-empty array of distinct positive integers, return the list of integers that are present in each array of nums sorted in ascending order.

"""


def ex2(nums):
    seen = set(nums)
    for num in nums:
        if seen.has_key(num):
            return seen[num]


print(ex2([[1, 2, 3, 4], [3, 4, 5]]))
