class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        customer=defaultdict(set)
        email=defaultdict(set)
        ids=defaultdict(str)
        res=[]

        ind=0
        for i in accounts:
            ids[ind]=i[0]
            for j in i[1:]:
                customer[ind].add(j)
                email[j].add(ind)
            ind+=1
        #print(email,customer)
        
        visited=set()
        for ID in ids:
            merged=set()
            if ID in visited:
                continue
            emails=customer[ID] #all emails of the customer
            all_ids=set()
            for e in emails: #all ids that email belongs to
                for id_ in email[e]:
                    visited.add(id_)
                    all_ids.add(id_)

            for id_ in all_ids: #all emails in every ID
                for e in customer[id_]:
                    merged.add(e)
            
            merged=sorted(list(merged))
            addtores=[ids[ID]]
            for i in merged:
                addtores.append(i)
            res.append(addtores)

             
            #print(res)
            
        return (res)