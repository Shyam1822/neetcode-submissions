class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #1/6/26
        d = {}
        size = len(s)
        op = 0
        l = 0

        for i in range(size):
            if (s[i] in d.keys()):

                l = max(l,d[s[i]]+1) 
                # 2 cases: 
                # 1. if current repeated element is between current l and i, then we move l to repeated elemnt's prev index+1
                # 2. if repeated element is before current l, we just ignore as it isnt in current window

            d[s[i]] = i


            op = max(op,i-l+1)
        return op