class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups={}
        
        for i in strs:
            count=0
            addi=0
            for j in i:
                count+=1
                addi+=ord(j)

            key=str(count)+" "+str(addi)
            if key not in groups:
                groups[key]=[i]
            else:
                groups[key].append(i)
        
        return [i for i in groups.values()]