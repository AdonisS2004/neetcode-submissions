class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        def getTime(pos, vel):
            return (target - pos) / vel

        stack = []
        cars = sorted(
            [[float(pos), float(vel)] for pos, vel in zip(position, speed)], 
            key=lambda x:x[0], 
            reverse=True
        )
        
        for pos, vel in cars:
            arrival_time = getTime(pos, vel)
            if not stack or arrival_time > stack[-1]:
                stack.append(arrival_time)
        return len(stack)