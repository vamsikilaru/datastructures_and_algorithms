from TrieNode import TrieNode

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    # get the index of character 't'
    def get_index(self,t):
        return ord(t)-ord('a')
    # function to insert a key in the Trie
    def insert(self,key:str):
        if not key:
            return False
        key = key.lower()
        current = self.root
        for letter in key:
            index = self.get_index(letter)

            if current.children[index] is None:
                current.children[index]= TrieNode(letter)
                current = current.children[index]
                print(letter," inserted")
        current.is_end_word = True
        print("'"+key+"' inserted")

keys = ["the", "a", "there", "answer", "any",
        "by", "bye", "their", "abc"]
t = Trie()
print("Keys to insert:\n", keys)
for words in keys:
    t.insert(words)