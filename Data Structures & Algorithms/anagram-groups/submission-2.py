class Solution:
    def key_to_list(self,key):
        op = [0] * 26
        for i in key:
            op[ord(i)-97]+=1
        return op
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #28/8/26

        dict_check = {}

        for i in strs:
            conv_check = str(self.key_to_list(i))
            if conv_check in dict_check:
                dict_check[conv_check].append(i)
            else:
                dict_check[conv_check] = [i]
        return [x for x in dict_check.values()]


