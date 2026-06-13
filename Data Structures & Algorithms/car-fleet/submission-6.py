class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        def getTime(pos, vel):
            return (target - pos) / vel

        slowest_time = -1
        count = 0

        cars = sorted(
            [[float(pos), float(vel)] for pos, vel in zip(position, speed)], 
            key=lambda x:x[0], 
            reverse=True
        )

        for pos, vel in cars:
            arrival_time = getTime(pos, vel)
            if slowest_time == -1 or arrival_time > slowest_time:
                slowest_time = arrival_time
                count += 1
                
        return count