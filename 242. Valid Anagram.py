

from collections import defaultdict


def isAnagram(s: str, t: str) -> bool:
    dict = defaultdict(int)
    for c in s:
        dict[c] += 1
    for c in t:
        if dict[c] == 0:
            return False
        dict[c] -= 1
    for c in dict.values():
        if c != 0:
            return False

    return True


s = "anagram"
t = "nagaram"
s1 = "rat"
t1 = "car"
print(isAnagram(s, t))
