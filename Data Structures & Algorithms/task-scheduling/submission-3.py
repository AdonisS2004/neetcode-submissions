class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # get frequencies
        freqs = dict()
        for task in tasks:
            if task not in freqs:
                freqs[task] = 0
            freqs[task] += 1
        
        # create heap
        heap = [(v, k) for k,v in freqs.items()]
        heapq.heapify_max(heap)

        # schedule tasks and manage cooldown
        cycles = 0
        cooldown = dict()
        while (heap or cooldown):
            # update cooldown
            toDel = []
            for task in cooldown:
                cooldown[task] -= 1
                if cooldown[task] == 0:
                    heapq.heappush_max(heap, task)
                    toDel.append(task)
            for task in toDel:
                del cooldown[task]
            # schedule task
            if heap:
                freq, task = heapq.heappop_max(heap)
                freq -= 1
                if freq > 0:
                    cooldown[(freq, task)] = n+1
            cycles += 1
        return cycles