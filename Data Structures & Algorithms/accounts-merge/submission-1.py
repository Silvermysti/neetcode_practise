class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        emails=defaultdict(set)
        neighbours=defaultdict(set)
        names=defaultdict(set)
        res=[]

        ind=0
        for ind,i in enumerate(accounts):
            for email in i[1:]:
                emails[email].add(ind)
                names[email]=i[0]
        
        for email in emails:
            ne=set()
            for ID in emails[email]:
                for e in accounts[ID][1:]:
                    ne.add(e)
            neighbours[email]=ne
        #print(neighbours)

        visited=set()

        def dfs(email,emailset):

            emailset.add(email)
            visited.add(email)

            for e in neighbours[email]:
                if e not in visited:
                    emailset=dfs(e,emailset)
            return emailset


        for i in list(neighbours):
            if i not in visited:
                emailset=dfs(i, set())
                name=names[i]
                addtores=[name]
                emaillist=sorted(list(emailset))
                for email in emaillist:
                    addtores.append(email)
                #print(addtores)
                #print(' ')
                res.append(addtores)
            
        return res