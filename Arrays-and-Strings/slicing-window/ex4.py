"""
Example 4: Given an integer array nums and an integer k, find the sum of the subarray with the largest sum whose length is k.
"""


def sumSub(nums, k):
    curr = 0
    for i in range(k):
        curr += nums[i]

    ans = curr
    for i in range(k, len(nums)):
        curr += nums[i] - nums[i - k]
        ans = max(ans, curr)

    return ans


print(sumSub([3, -1, 4, 12, -8, 5, 6], 4))
