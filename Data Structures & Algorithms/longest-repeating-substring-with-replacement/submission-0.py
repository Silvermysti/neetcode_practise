class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        i=1
        buffer=k
        curr=s[0]
        curlen=1
        maxlen=1
        print(s[0])
        changed=False

        while i<len(s):
            print(s[i])
            print(curlen)
            if curr==s[i]:
                curlen+=1
                i+=1
            
            else:
                if changed==False:
                    change=i
                    changed=True
                if buffer!=0:
                    buffer-=1
                    i+=1
                    curlen+=1
                else:
                    maxlen=max(maxlen,curlen)
                    i=change+1
                    curr=s[change]
                    curlen=1
                    buffer=k
                    changed=False
                    print(" ")
                    print(s[change])
        maxlen=max(maxlen,curlen+buffer)    
        
        return maxlen
            
        
