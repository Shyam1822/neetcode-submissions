class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # 22/9/26

        op = []

        if not digits:
            return op

        char_set = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(cur_dig,cur_str):
            if cur_dig == "":
                op.append(cur_str)
                return
            
            elements = char_set[cur_dig[0]] # alpahbets in the current 1st number

            size = len(elements)

            for i in range(size):
                cur_str+=elements[i]
                backtrack(cur_dig[1:],cur_str)
                cur_str = cur_str[:-1]

        backtrack(digits,"")

        return op