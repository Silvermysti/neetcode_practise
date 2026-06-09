class PrefixTree:

    def __init__(self):
        self.root={}

    def insert(self, word: str) -> None:
        node=self.root

        length=len(word)
        i=0
        while i<length and word[i] in node:
            node=node[word[i]]
            i+=1
        while(i<length):
            node[word[i]]={}
            node=node[word[i]]
            i+=1
        print(self.root)
        

    def search(self, word: str) -> bool:
        node=self.root
        length=len(word)
        i=0
        while i<length and word[i] in node:
            node=node[word[i]]
            i+=1

        if i<length:return False
        else:return True
        

    def startsWith(self, prefix: str) -> bool:
        return prefixTree.search(prefix)
        