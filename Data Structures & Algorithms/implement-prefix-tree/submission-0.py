class TrieNode:

  def __init__(self):
    self.children = {}
    self.isEnd = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        s = len(word)
        cur = self.root

        for i in range(s):
            if word[i] in cur.children:
                cur = cur.children[word[i]]
                continue
            cur.children[word[i]] = TrieNode()
            cur = cur.children[word[i]]
        
        cur.isEnd = True
    def search(self, word: str) -> bool:
        s = len(word)
        cur = self.root

        for i in range(s):
            # print(cur.children)
            if word[i] not in cur.children:
                return False
            
            cur = cur.children[word[i]]
        return cur.isEnd

    def startsWith(self, prefix: str) -> bool:
        s = len(prefix)
        cur = self.root

        for i in range(s):
            # print(cur.children)
            if prefix[i] not in cur.children:
                return False
            
            cur = cur.children[prefix[i]]
        return True

        
        