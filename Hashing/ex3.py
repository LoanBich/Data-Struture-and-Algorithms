"""
Example 3: Given an integer array nums, find all the unique numbers x in nums that satisfy the following: x + 1 is not in nums, and x - 1 is not in nums.
"""


def ex3(nums):
    list = []
    for i in nums:
        if i - 1 not in nums and i + 1 not in nums:
            list.append(i)

    return list


print(ex3([0, 12, 26, 11, 2, 9]))
