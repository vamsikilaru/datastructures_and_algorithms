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
    
    def delete(self,key:str):
        if not key or self.root is None:
            return False
        print("Deleting :",key)
        self.delete_helper(key,self.root,len(key),0)
    
    def delete_helper(self,key:str,current:TrieNode,length,level):
        delete_self = False

        if not current:
            print("key does not exist")
            return delete_self
        
        if level is length:
            # reached end of the key alpahbet
            if current.children.count(None)==len(current.children): # no childeren
                print("- Node",current.char," : has no children. Delete it")
                current = None
                delete_self = True
            else:
                print("- Node",current.char," : has childrn, don't delete")
                current.is_end_word = False
                delete_self = False
        else:
            index = self.get_index(key[level])
            print("Traverse to :",key[level])
            child_node = current.children[index]
            child_deleted = self.delete_helper(key,child_node,length,level+1)
            if child_deleted:
                print("- Delete link from", current.char, "to", key[level])
                current.children[index]= None
                if current.is_end_word:
                    print("- Don't delete ",current.char," : word end")
                    delete_self = False
                elif current.children.count(None) != len(current.children):
                    print("- Don't delete ",current.char," : node has children")
                    delete_self = False
                else:
                    print("- Delete node ",current.char," : has no children")
                    current = None
                    delete_self = True
            else:
                delete_self = False
        return delete_self

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

t.delete("abc")
print("Deleted key \"abc\" \n")

print("abc --- " + res[1] if t.search("abc") else "abc --- " + res[0])