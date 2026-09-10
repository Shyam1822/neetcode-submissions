class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #10/9/26

        _dict = {}
        op = 0
        l_val = 0


        for i in range(len(s)):
            if s[i] in _dict:
                l_val = max(l_val,_dict[s[i]]+1)
            _dict[s[i]] = i
            
            op = max(op,i-l_val+1)
        return op
            
            
                
            
            