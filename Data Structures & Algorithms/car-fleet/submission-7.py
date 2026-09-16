class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        cars = [(p,v) for p,v in zip(position,speed)]
        cars.sort(reverse=True,key=lambda x:x[0])

        # organize each fleet by the time it will take to get there
        # time_to_target --> t3
        stack = []
        for car in cars:
            t3 = (target-car[0])/car[1]
            if not stack:
                stack.append(t3)
            if t3 > stack[-1]:
                stack.append(t3)
        return len(stack)
