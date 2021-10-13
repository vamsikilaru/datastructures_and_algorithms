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
                #print(letter," inserted")
        current.is_end_word = True
        print("'"+key+"' inserted")

    def search(self,key:str):
        if not key:
            return False
        key = key.lower()
        current = self.root
        for letter in key:
            index = self.get_index(letter)
            if current.children[index] is None:
                return False
            current = current.children[index]
        if current is not None and current.is_end_word:
            return True
        return False



keys = ["the", "a", "there", "answer", "any",
        "by", "bye", "their", "abc"]

res = ["Not present in trie", "Present in trie"]
t = Trie()
print("Keys to insert:\n", keys)
for words in keys:
    t.insert(words)

print("the --- " + res[1] if t.search("the") else "the --- " + res[0])
print("these --- " + res[1] if t.search("these") else "these --- " + res[0])
print("abc --- " + res[1] if t.search("abc") else "abc --- " + res[0])