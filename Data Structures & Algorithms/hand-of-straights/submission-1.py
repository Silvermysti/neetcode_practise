class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        if len(hand)%groupSize!=0:
            return False
        
        hand.sort()
        groups=deque()
        ngroups=0

        ind=0
        base=0

        for i in hand:
            while ind<len(groups) and groups[ind][-1]==i:
                ind+=1

            if ind==len(groups):
                groups.append([i])
            elif groups[ind][-1]==i-1:
                groups[ind].append(i)
            else:
                return False

            if len(groups[base])==groupSize:
                base+=1
            ind=base
            
            print(groups)
        
        return True