class WordDictionary:

    def __init__(self):
        self.root={}

    def addWord(self, word: str) -> None:
        #print("add word", word)
        
        node=self.root
        for i in word:
            node=node.setdefault(i,{})
        node["is_end"]=True
        #print(self.root)

    def search(self, word: str) -> bool:
        #print(" ")
        #print(" ")
        #print("search word", word)
        length=len(word)
        self.result=False
        node=self.root

        def backtrack(node, start):
            if node==True:
                return
            #if start+1<length:
                #print(word[start],node)
            if start==length:
                if "is_end" in node.keys():
                    self.result=True
                return

            if word[start] in node.keys():
                #if start+1<length:
                    #print(node[word[start]],word[start+1])
                #if word[start]!="is_end":
                backtrack(node[word[start]],start+1)
            elif word[start]!='.':
                return
            else:
                for key in node.keys():
                    if self.result==True:
                        break
                    if key=="is_end":
                        #if start+1<length:
                            #print(node[key],word[start+1])
                        backtrack(node[key],start+1)

        backtrack(self.root,0)

        return self.result
