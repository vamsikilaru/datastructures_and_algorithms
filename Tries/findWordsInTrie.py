from  TrieNode import TrieNode
from Trie import Trie

def find_words(root:TrieNode):
    result = []
    words_helper(root,result,'')
    return result

def words_helper(node: TrieNode,result,subword):

    if node.is_end_word:
        result.append(subword)
    
    for letter in node.children:
        if letter:
            words_helper(letter,result,subword+letter.char)
keys = ["the", "a", "there", "answer", "any", "by", "bye", "their", "abc"]

trie = Trie()

for key in keys:
    trie.insert(key)

print(find_words(trie.root))