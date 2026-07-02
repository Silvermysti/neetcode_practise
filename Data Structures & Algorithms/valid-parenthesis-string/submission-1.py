class Solution:
    def checkValidString(self, s: str) -> bool:
        length=len(s)
        def backtrack(ind,left,right):
            #print(ind, left, right)
            if ind==length:
                if left==right:
                    #print("True")
                    return True
                else:
                    #print("False")
                    return False
 
            if s[ind]==')':
                if left>right:
                    return backtrack(ind+1,left,right+1)
                else:
                    return False
            elif s[ind]=='(':
                return backtrack(ind+1,left+1,right)
            else:
                if (left>right and backtrack(ind+1,left,right+1)) or (backtrack(ind+1,left+1,right)) or (backtrack(ind+1,left,right)):
                    return True
                else:
                    return False
        return backtrack(0,0,0)