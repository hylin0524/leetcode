class TrieTree:
    def __init__(self):
        self.children = {}
        self.is_end = False
    

class Trie:
    def __init__(self) -> None:
        self.root = TrieTree()
    
    def insert(self, word):
        curr_node = self.root
        for w in word:
            if w not in curr_node.children:
                curr_node.children[w] = TrieTree()
            curr_node = curr_node.children[w]
        curr_node.is_end = True

    def completed_search(self, word):
        curr_node = self.root
        for w in word:
            if w not in curr_node.children:
                return False
            curr_node = curr_node.children[w]
        return curr_node.is_end
    
    def partial_search(self, word):
        curr_node = self.root
        for w in word:
            if w not in curr_node.children:
                return False
            curr_node = curr_node.children[w]
        return True

T = Trie()
T.insert("apple")
print(T.completed_search("apple")) # True
print(T.completed_search("appla")) # False
print(T.partial_search("app")) # True

print(T.partial_search("ape")) # False
T.insert("ape")
print(T.partial_search("ape")) # True