class PrefixTree:

    def __init__(self):
        self.root={}

    def insert(self, word: str) -> None:
        node=self.root
        for char in word:
            # setdefault looks up the char; if it doesn't exist, it inserts {}
            node = node.setdefault(char, {})
        node["is_end"]=True
        #print(self.root)
        

    def search(self, word: str) -> bool:
        node=self.root
        length=len(word)
        i=0
        while i<length and word[i] in node:
            node=node[word[i]]
            i+=1

        if i==length and "is_end" in node:
            return True
        else:return False
        

    def startsWith(self, prefix: str) -> bool:
        node=self.root
        length=len(prefix)
        i=0
        while i<length and prefix[i] in node:
            node=node[prefix[i]]
            i+=1

        if i<length:
            return False
        else:return True
        