class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.count += 1
    
    def getPrefixCount(self, word):
        node = self.root
        newArr = []
        for char in word:
            # node = node.children[char]
            node = node.children.get(char)
            if node:
                newArr.append(node.count)
            else:
                break
        return newArr

    def calculateSum(self,arr):
        sum = 0
        for ele in arr:
            sum+=ele
        return sum
    
    def getPrefixSum(self, arr):

        for word in arr:
            self.insert(word)
        
        result = []
        for word in arr:
            prefixSum = self.getPrefixCount(word)
            result.append(self.calculateSum(prefixSum))
        
        return result


trie = Trie()
arr = ['abc', 'ab', 'bc', 'b']
print(trie.getPrefixSum(arr))