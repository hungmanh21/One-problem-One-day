"""
Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.
 

Example:

Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True
"""


class TrieNode:
    def __init__(self):
        # alphabet has 26 chars from a->z
        self.child_nodes = [None] * 26
        self.wordEnd = False


class Trie():
    def __init__(self):
        self.root = TrieNode()

    def insert(self, text):
        current_node = self.root
        # traverse through all the characters of text
        for char in text:
            distance = ord(char) - ord('a')
            if current_node.child_nodes[distance] == None:
                current_node.child_nodes[distance] = TrieNode()
            current_node = current_node.child_nodes[distance]
        current_node.wordEnd = True

    def search(self, text):
        current_node = self.root
        for char in text:
            distance = ord(char) - ord('a')
            if current_node.child_nodes[distance] == None:
                return False
            current_node = current_node.child_nodes[distance]
        return current_node.wordEnd

    def startsWith(self, prefix):
        current_node = self.root
        for char in prefix:
            distance = ord(char) - ord('a')
            if current_node.child_nodes[distance] == None:
                return False
            current_node = current_node.child_nodes[distance]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
