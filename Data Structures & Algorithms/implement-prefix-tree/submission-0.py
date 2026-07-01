class PrefixTree:

    def __init__(self):
        self.prefix_map = dict()

    def insert(self, word: str) -> None:
        node = self.prefix_map
        for char in word:
            if char not in node:
                node[char] = dict()
                node[char]["#"] = False
            node = node[char]
        node["#"] = True

    def search(self, word: str) -> bool:
        node = self.prefix_map
        for char in word:
            if char not in node: return False
            node = node[char]
        return node["#"]

    def startsWith(self, prefix: str) -> bool:
        node = self.prefix_map
        for char in prefix:
            if char not in node: return False
            node = node[char]
        return True
        