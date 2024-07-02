"""
You are given a 0-indexed array nums of n integers, and an integer k.

The k-radius average for a subarray of nums centered at some index i with the radius k is the average of all elements in nums between the indices i - k and i + k (inclusive). If there are less than k elements before or after the index i, then the k-radius average is -1.

Build and return an array avgs of length n where avgs[i] is the k-radius average for the subarray centered at index i.

The average of x elements is the sum of the x elements divided by x, using integer division. The integer division truncates toward zero, which means losing its fractional part.

For example, the average of four elements 2, 3, 1, and 5 is (2 + 3 + 1 + 5) / 4 = 11 / 4 = 2.75, which truncates to 2.
"""


def kRadius(nums: list[int], k: int) -> list:
    if k > len(nums):
        return [-1]

    ans = []
    right = left = 0

    for i in range(k):
        left += nums[i]

    for i in range(k + 1, k + k + 1):
        right += nums[i]

    for i in range(len(nums)):
        if i < k or len(nums[i:-1]) < k:
            ans.append(-1)
        else:
            if i == k:
                ans.append((left + nums[i] + right) // (k * 2 + 1))
            else:
                left -= nums[i - k - 1]
                left += nums[i - 1]
                right -= nums[i]
                right += nums[i + k]
                ans.append((left + nums[i] + right) // (k * 2 + 1))
    return ans


print(kRadius([1, 1], 1))

print(kRadius([7, 4, 3, 9, 1, 8, 5, 2, 6], 3))
print(kRadius([7, 4], 3))
