"""
Example 2: You are given a binary string s (a string containing only "0" and "1"). You may choose up to one "0" and flip it to a "1". What is the length of the longest substring achievable that contains only "1"?

For example, given s = "1101100111", the answer is 5. If you perform the flip at index 2, the string becomes 1111100111.
"""


# def length(s):
#     left = 0
#     ans = []
#     curr = 0
#     for right in range(len(s)):
#         if s[right] == "0" or right == len(s) - 1:
#             ans.append((right - left))
#         if s[right] == "0":
#             left = right + 1
#         if s[right] == "1":
#             curr += 1
#     return max([ans[i - 1] + ans[i] + 1 for i in range(1, len(ans))], default=curr)


def length2(s):
    sublength = [len(sub) for sub in s.split("0")]
    return max([sublength[i - 1] + sublength[i] + 1 for i in range(1, len(sublength))])


print(length2("1101100111"))
print(length2("0000"))


# Nguyễn Đức Thọ
# def solve(s):
#     max_length = 0
#     current_length = 0
#     length_since_flip = 0

#     for idx, c in enumerate(s):
#         if c == "1":
#             current_length += 1
#             length_since_flip += 1
#         else:
#             current_length = length_since_flip + 1
#             length_since_flip = 0

#         if (current_length > max_length):
#             max_length = current_length

#     return max_length

# if _name_ == "_main_":
#     print(solve("1101100111"))
#     print(solve("0"))
#     print(solve("1"))
#     print(solve("000011100111100"))
