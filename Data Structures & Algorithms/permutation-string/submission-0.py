class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2)<len(s1):
            return False

        freq=[0]*26
        curfreq=[0]*26
        for i in range(len(s1)):
            element=ord(s1[i])%26
            freq[element]+=1
            element=ord(s2[i])%26
            curfreq[element]+=1
        print(freq,curfreq)
        
        if curfreq==freq:
            return true
        
        last=0
        for i in range(len(s1),len(s2)):
            current=ord(s2[i])%26
            prev=ord(s2[last])%26
            curfreq[current]+=1
            curfreq[prev]-=1
            last+=1
            print(curfreq)
            if curfreq==freq:
                return True

        return False
            
