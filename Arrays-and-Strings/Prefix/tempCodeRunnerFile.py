(nums):
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