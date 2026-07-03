class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # helper fuction to get all exisiting neighbors
        def getNeighbors(row, col, m , n):
            offsets = [(-1, 0), (0, 1), (1,0), (0,-1)]
            out = []
            for x, y in offsets:
                new_row, new_col = row+x, col+y
                if new_row >= 0 and new_row < m:
                    if new_col >= 0 and new_col < n:
                        out.append((new_row, new_col))
            return out

        trie = dict()
        t = max([len(word) for word in words])
        m, n = len(board), len(board[0])
        words = set(words)
        res = []

        for row in range(m):
            for col in range(n):
                queue = [(row, col, 0, trie, set(), "")] # 
                while queue:
                    crow, ccol, count, node, visited, cword = queue.pop()
                    if count < t and (crow, ccol) not in visited:
                        char = board[crow][ccol]
                        if char not in node:
                            node[char] = {"#":False}
                        node = node[char]
                        new_word = cword+char
                        if new_word in words:
                            res.append(new_word)
                            node["#"] = True
                        new_visited = visited.copy()
                        neighbors = getNeighbors(crow, ccol, m, n)
                        new_visited.add((crow, ccol))
                        for x,y in neighbors:
                            if (x,y) not in new_visited:
                                queue.append((x,y,count+1, node, new_visited, new_word))
        return list(set(res))

                