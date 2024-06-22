"""
Given an array of positive integers nums and an integer k, return the number of subarrays where the product of all the elements in the subarray is strictly less than k.

For example, given the input nums = [10, 5, 2, 6], k = 100, the answer is 8. The subarrays with products less than k are:

[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
"""


def subArray(nums, k):
    if k <= 1:
        return 0
    left = ans = 0
    curr = 1
    for right in range(len(nums)):
        curr *= nums[right]
        print(f"{curr=}")
        while curr >= k:
            print(f"{left=}")
            curr //= nums[left]
            left += 1
        ans += right - left + 1
    return ans


print(subArray([1, 2, 3], 0))


"""
def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
    count = len([num for num in nums if num < k])

    if count == 0:
        return 0

    left, right, prod = 0, 0, 1
    for right in range(len(nums)):
        prod *= nums[right]
        if (right > 0 and prod < k):
            count += right - left
        else:
            while prod >= k:
                prod //= nums[left]
                left += 1
            count += right - left if right - left > 0 else 0


    return count
"""
