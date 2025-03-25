from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        :type s: String
        :type t: String
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)
    

#Another solution 

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        :type s: String
        :type t: String
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        dict = defaultdict(int)
        
        for c in s:
            dict[c] += 1
        for c in t: 
            if dict[c] == 0:
                return False
            dict[c] -= 1
        for c in dict.values() :
            if c !=0:
                return False
        
        return True