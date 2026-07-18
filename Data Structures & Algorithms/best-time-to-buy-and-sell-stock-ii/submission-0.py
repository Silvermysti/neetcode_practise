class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return

        prices.append(0)
        current=None
        ind=0
        profit=0
        while ind<len(prices)-1:
            print(prices[ind])
            if prices[ind]<prices[ind+1]:
                print("current is ", prices[ind])
                current=prices[ind]            
                while prices[ind]<prices[ind+1]:
                    ind+=1
                print("profit: ", prices[ind], " - ",current)
                profit+=prices[ind]-current
            ind+=1
        
        return profit