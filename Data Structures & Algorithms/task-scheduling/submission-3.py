class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        count={}
        net_tasks=0

        for i in tasks:
            if i not in count:
                net_tasks+=1
                count[i]=1
            else:
                count[i]+=1
        
        queue=deque(count.values())
        while len(queue)<n+1:
            queue.append(0)
        print(queue)

        ts=0
        remain=net_tasks
        while remain>0:
            ts+=1
            temp=queue.popleft()
            if temp==0:
                queue.append(0)
                continue
                print(queue)
            temp-=1
            if temp==0:
                remain-=1
                if len(queue)<n+1:
                    queue.append(0)
            else:
                queue.append(temp)
            print(queue)

        return ts