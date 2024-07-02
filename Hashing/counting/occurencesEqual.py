def areOccurrencesEqual(s: str) -> bool:
    dict = {}
    for char in s:
        if char not in dict:
            dict[char] = 1
        else:
            dict[char] += 1
    return len(set(dict.values())) == 1


from collections import Counter


def areOccurrencesEqual2(s):
    return len(set(Counter(s).values())) == 1


print(areOccurrencesEqual2("abacbc"))
