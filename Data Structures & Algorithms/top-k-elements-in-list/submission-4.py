class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n2f = dict()
        f2n = dict()
        res = []

        # map numbers to freq
        for num in nums:
            if num not in n2f:
                n2f[num] = 0
            n2f[num]+= 1

        # map freq to numbers
        top_freq = 0
        for num, freq in n2f.items():
            if freq not in f2n:
                f2n[freq] = []
            f2n[freq].append(num)
            top_freq = max(freq, top_freq)

        # get top k
        remaining = k
        while remaining:
            if top_freq in f2n:
                for num in f2n[top_freq]:
                    if not remaining:
                        break
                    res.append(num)
                    remaining -= 1
            top_freq -= 1
            
        return res