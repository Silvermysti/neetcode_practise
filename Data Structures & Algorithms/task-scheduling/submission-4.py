class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        ts=0
        maxheap={}
        net_tasks=0
        for i in tasks:
            if i in maxheap:
                maxheap[i]+=1
            else:
                maxheap[i]=1
                net_tasks+=1
        maxheap=list(maxheap.values())

        heapq._heapify_max(maxheap)
        queue=deque()
        while net_tasks>0:
            if len(queue)!=0:
                if queue[0][1]==ts:
                    heapq.heappush_max(maxheap, queue.popleft()[0])
                    print(maxheap)
            if len(maxheap)!=0:
                temp=heapq.heappop_max(maxheap)
                temp-=1
                if temp==0:
                    net_tasks-=1
                else:
                    queue.append([temp, ts+n+1])
            ts+=1
            print(maxheap, queue)
            print(ts)
            print("")

        return 1





