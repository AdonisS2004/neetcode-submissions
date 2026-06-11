class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [[position[i], speed[i]] for i in range(len(position))]
        pairs = sorted(pairs, key = lambda x:x[0], reverse = True) # sort by position
        fleets = 1
        prev_time = (target - pairs[0][0])/pairs[0][1]
        for i in range(1, len(position)):
            time = (target - pairs[i][0])/pairs[i][1]
            if time > prev_time:
                fleets += 1
                prev_time = time
        return fleets