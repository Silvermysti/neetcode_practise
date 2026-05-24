class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0

        first=0
        second=0
        curlen=1
        maxlen=1
        visited={s[0]:0}

        while second<len(s)-1:
            second+=1
            letter=s[second]
            if letter not in visited:
                visited[letter]=second
                curlen+=1
            else:
                if maxlen<curlen:
                    maxlen=curlen
                first=visited[letter]+1
                second=first
                visited={}
                visited[s[first]]=first
                curlen=1
            
        if maxlen<curlen:
            maxlen=curlen
            
        return maxlen
