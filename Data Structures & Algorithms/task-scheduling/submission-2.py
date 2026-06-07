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
        
        heapcount=net_tasks
        remain=net_tasks

        count=list(count.values())
        heapq.heapify_max(count)

        N=0
        queue=deque()
        while N<n+1:
            N+=1
            if heapcount>0:
                queue.append(heapq.heappop_max(count))
                heapcount-=1
            else:
                queue.append(0)

        ts=0
        while remain>0:
            print(queue)

            ts+=1
            print(ts)
            temp=queue.popleft()
            if temp==0:
                queue.append(0)
                continue

            temp-=1
            if temp==0:
                remain-=1
                if heapcount>0:
                    heapcount-=1
                    queue.append(heapq.heappop_max(count))
                else:
                    queue.append(0)
                continue
            queue.append(temp)

        return ts