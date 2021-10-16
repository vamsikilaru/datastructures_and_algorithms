from TrieNode import TrieNode
from Trie import Trie

def countWords(root:TrieNode):
    result = 0
    if root.is_end_word:
        result += 1
    for letter in root.children:
        if letter is not None:
            result += countWords(letter)
    return result

keys = ["the", "a", "there", "answer", "any", "by", "bye", "their", "abc"]

trie = Trie()

for key in keys:
    trie.insert(key)

print(countWords(trie.root))