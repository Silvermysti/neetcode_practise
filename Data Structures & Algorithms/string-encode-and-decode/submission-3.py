class Solution:

    def encode(self, strs: List[str]) -> str:
        res=""

        for i in strs:
            res = res + i + "."

        return res

    def decode(self, s: str) -> List[str]:
        res=[]
        word=""

        for i in s:
            if i != ".":
                word = word + i
            else:
                res.append(word)
                word=""
        
        return(res)