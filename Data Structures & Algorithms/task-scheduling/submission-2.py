class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freqs = dict()
        for task in tasks:
            if task not in freqs:
                freqs[task] = 0
            freqs[task] += 1
        # create heap
        heap = [(v, k) for k,v in freqs.items()]
        heapq.heapify_max(heap)

        # use heap to create schedule
        cycles = 0
        cooldown = dict()
        schedule = []
        while (heap or cooldown):
            # print(cycles, heap, cooldown)
            # update cooldown
            toDel = []
            for task in cooldown:
                cooldown[task] -= 1
                if cooldown[task] == 0:
                    heapq.heappush_max(heap, task)
                    toDel.append(task)
            for task in toDel:
                del cooldown[task]

            # schedule
            if heap:
                freq, task = heapq.heappop_max(heap)
                freq -= 1
                if freq > 0:
                    cooldown[(freq, task)] = n+1
                schedule.append(task)
            cycles += 1
        return cycles