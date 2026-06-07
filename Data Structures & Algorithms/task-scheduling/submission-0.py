class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        counts=[]
        prev=tasks[0]
        count=1
        for i in tasks[1:]:
            if i==prev:
                count+=1
                continue
            counts.append(count)
            count=1
            prev=i
        counts.append(count)

        remain=len(counts)

        heapq.heapify_max(counts)

        heapcount=remain
        ts=0
        N=0
        queue=deque()
        while N<n+1:
            if heapcount>0:
                queue.append(heapq.heappop_max(counts))
                heapcount-=1
            else:
                queue.append(0)
            N+=1
        
        temp=0
        while remain>0:
            print(queue)
            ts+=1
            temp=queue.popleft()
            if temp==0:
                queue.append(0)
                continue
            temp-=1
            if temp==0:
                remain-=1
                if len(counts)>0:
                    queue.append(heapq.heappop_max())
                else:
                    queue.append(0)
            else:
                queue.append(temp)
            print(ts)
            

        return ts
