def missingNumber(self, nums: List[int]) -> int:
    n = range(0, len(nums))
    for num in nums:
        if num not in n:
            return num
    return ""