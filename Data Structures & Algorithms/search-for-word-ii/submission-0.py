class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None # instead of isEnd, we directly add word here


class Solution:
    # 27/9/26
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root
        for i in word:
            if i not in cur.children:
                cur.children[i] = TrieNode()
            cur = cur.children[i]
        cur.word = word #actual word is added instead of isEnd variable

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        op = []
        for i in words:
            self.insert(i)

        row, col = len(board), len(board[0])

        def dfs(r, c, node):
            if r < 0 or c < 0 or r == row or c == col or board[r][c] not in node.children:
                return

            char = board[r][c]
            node = node.children[char]

            if node.word is not None:

                # add word to output and avoid duplicates
                op.append(node.word)
                node.word = None
            

            board[r][c] = '#'

            dfs(r + 1, c, node)
            dfs(r - 1, c, node)
            dfs(r, c + 1, node)
            dfs(r, c - 1, node)

            board[r][c] = char

        for r in range(row):
            for c in range(col):
                dfs(r, c, self.root)
        return op
