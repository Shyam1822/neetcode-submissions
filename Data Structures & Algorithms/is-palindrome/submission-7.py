class Solution:
    def isPalindrome(self, s: str) -> bool:
        #7/10/26

        st = ""
        for i in s:
            if i.isalnum():
                st+=i
        s = st.lower()
        #return s==s[::-1]
        a,b = 0,len(s)-1


        while a<b:
            if s[a]==s[b]:
                a+=1
                b-=1
                continue
            return False
        return True
