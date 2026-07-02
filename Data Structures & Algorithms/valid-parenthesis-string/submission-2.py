class Solution:
    def checkValidString(self, s: str) -> bool:
        length=len(s)
        memo={}
        def backtrack(ind,left,right):
            #print(ind, left, right)
            if ind==length:
                if left==right:
                    #print("True")
                    return True
                else:
                    #print("False")
                    return False

            if (left,right,ind) in memo:
                return memo[(left,right,ind)]
 
            if s[ind]==')':
                if left>right:
                    result=backtrack(ind+1,left,right+1)
                else:
                    result=False
            elif s[ind]=='(':
                result=backtrack(ind+1,left+1,right)
            else:
                if (left>right and backtrack(ind+1,left,right+1)) or (backtrack(ind+1,left+1,right)) or (backtrack(ind+1,left,right)):
                    result=True
                else:
                    result=False
            memo[(left,right,ind)]=result
            return result
        return backtrack(0,0,0)