def missingNumber(nums):
    n = list(range(0, len(nums) + 1))
    for num in n:
        if num not in nums:
            return num
    return ""


print(missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))
