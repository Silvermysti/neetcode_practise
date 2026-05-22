class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups={}
        
        for i in strs:
            count=0
            set_=set()
            for j in i:
                count+=1
                set_.add(j)

            key=str(count)+" "+str(set_)
            print(key)

            if key not in groups:
                groups[key]=[i]
            else:
                groups[key].append(i)
        
        return [i for i in groups.values()]