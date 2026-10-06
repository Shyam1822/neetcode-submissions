class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class PrefixTree:

    # optimize the previous code
    # 6/10/26 random retry1

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur=self.root

        for i in word:
            if i not in cur.children:
                cur.children[i] = TrieNode()
            
            cur = cur.children[i]
        cur.isEnd = True

    def common(self,word):
        cur = self.root

        for i in word:
            if i not in cur.children:
                return False
            cur = cur.children[i]
        return [1,cur.isEnd]

    def search(self, word: str) -> bool:
        op = self.common(word)
        if op:
            return op[1]
        return False

    def startsWith(self, prefix: str) -> bool:
        return True if self.common(prefix) else False
        