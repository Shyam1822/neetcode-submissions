class Solution:

    def encode(self, strs: List[str]) -> str:
        op = ""
        for i in strs:
            op+=str(len(i))+"#"+i
        return op
    def decode(self, s: str) -> List[str]:
        ret = []
        cur_num = ''
        i = 0
        while i<len(s):
            print(cur_num)
            if s[i] != "#":
                cur_num+=s[i]
                i+=1
                continue
            ret.append(s[i+1:i+int(cur_num)+1])
            i += int(cur_num)+1
            cur_num = ""
        return ret


            