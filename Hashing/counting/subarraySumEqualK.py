from collections import defaultdict


def subarrayEqualK(nums, k):
    counts = defaultdict(int)
    counts[0] = 1
    ans = curr = 0
    for num in nums:
        curr += num
        ans += counts[curr - k]
        counts[curr] += 1
        print("num: ", num, "curr: ", curr, curr - k, counts[curr - k], ans, counts)
    return ans


print(subarrayEqualK([1, 2, 1, 2, 1], 3))
