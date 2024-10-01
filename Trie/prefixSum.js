class TrieNode {
    constructor() {
        this.children = {};
        this.count = 0;
    }
}

class Trie {
    constructor() {
        this.root = new TrieNode()
    }

    insert(words) {
        let node = this.root;
        for (let char of words) {
            if (!node.children[char]) {
                node.children[char] = new TrieNode();
            }
            node = node.children[char];
            node.count++
        }
    }

    getPrefixCounts(words) {
        let node = this.root;
        let prefixCounts = [];
        for (let char of words) {
            node = node.children[char]
            if (node) {
                prefixCounts.push(node.count)
            }
        }
        return prefixCounts;
    }
}

function calculatePrefix(words) {
    const trie = new Trie;

    for (let word of words) {
        trie.insert(word)
    }
    let newArr = []
    for (let word of words) {
        let prefixCounts = trie.getPrefixCounts(word);
        console.log(prefixCounts)
        let sum = prefixCounts.reduce((acc, val) => acc + val, 0);
        newArr.push(sum);
    }
    console.log(newArr)
}

const words = ["abc", "ab", "bc", "b"]
calculatePrefix(words);