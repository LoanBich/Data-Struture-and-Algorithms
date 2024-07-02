"""
A pangram is a sentence where every letter of the English alphabet appears at least once.

Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.



Example 1:

Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
Output: true
Explanation: sentence contains at least one of every letter of the English alphabet.
"""


def checkIfPangram(sentence):
    seen = set(sentence)
    if len(seen) == 26:
        return True
    else:
        return False


print(checkIfPangram("thequickbrownfoxjumpsoverthelazydog"))
print(checkIfPangram("thequickbrownfoxjumpsoverthelazyd"))
