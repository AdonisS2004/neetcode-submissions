class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num2freq = dict()
        freq2num = dict()
        maximum = 1

        # generatae num2freq
        for num in nums:
            if num not in num2freq:
                num2freq[num] = 0
            num2freq[num] += 1
        
        # generate freq2num and maximum freq
        for key, value in num2freq.items():
            if value > maximum:
                maximum = value
            if value not in freq2num:
                freq2num[value] = []
            freq2num[value].append(key)

        # fill res
        res = []
        remaining = k
        for freq in range(maximum, -1, -1):
            if remaining == 0:
                        break
            if freq in freq2num:
                for num in freq2num[freq]:
                    res.append(num)
                    remaining -= 1
                    if remaining == 0:
                        break

        return res