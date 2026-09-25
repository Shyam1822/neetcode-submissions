class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class WordDictionary:
    # 25/9/26
    # initial thought, should be a combination of tries and backtracking, where for dots, we go search for each elements on that level and if satisfying the regex, return true, else search for next element in the level, after popping the val[[[]]]


    #turns out, we need to use dfs(similar to backtracking, but dfs)

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for i in word:
            if not i in cur.children:
                cur.children[i] = TrieNode()
            
            
            cur = cur.children[i]
        cur.isEnd = True

    def search(self, word: str) -> bool:
        # write a dfs logic inside this search
        def dfs(j,root):
            cur = root
            for i in range(j,len(word)):
                c = word[i]
                if c=='.':
                    for child in cur.children.values():
                        if dfs(i+1,child):
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.isEnd
        return dfs(0,self.root)
            



            
