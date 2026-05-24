class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        first=0
        second=0
        curlen=1
        maxlen=1
        visited={s[0]:0}
        print(visited)
        print(s[first])

        while second<len(s)-1:
            second+=1
            print(s[second])
            letter=s[second]
            if letter not in visited:
                visited[letter]=second
                curlen+=1
            else:
                maxlen=max(maxlen,curlen)
                first=visited[letter]+1
                second=first
                visited={}
                visited[s[first]]=first
                curlen=1
                print(" ")
                print(s[first])

        return maxlen
