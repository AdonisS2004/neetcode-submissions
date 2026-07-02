class WordDictionary:

    def __init__(self):
        self.trie = dict()
        self.trie["#"] = False

    def addWord(self, word: str) -> None:
        node = self.trie
        for char in word:
            if char not in node:
                node[char] = dict()
                node = node[char]
                node["#"] = False
            else:
                node = node[char]
        node["#"] = True

    def search(self, word: str) -> bool:
        stack = [(self.trie, 0)]
        n = len(word)
        while stack:
            node, idx = stack.pop()
            while idx < n:
                char = word[idx]
                if char == ".":
                    for key, value in node.items():
                        if key != "#":
                            stack.append((node[key], idx + 1))
                    if stack:
                        node, idx = stack.pop()
                        continue
                    else:
                        break
                elif char not in node:
                    break
                node = node[char]
                idx += 1
            if idx >= n and node["#"]: return True
        return False

