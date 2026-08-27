class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #27/8/26
        return sorted(list(s))==sorted(list(t))