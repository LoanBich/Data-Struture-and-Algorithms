def pv1(nums):
    left = 0
    total = sum(nums)
    for i in range(len(nums) - 1):
        left += nums[i]
        right = total - left
        if right == left:
            return i
    return False


print(pv1([1, 2, 3, 4, 2]))
