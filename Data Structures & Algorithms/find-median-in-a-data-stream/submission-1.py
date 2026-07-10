class MedianFinder:

    def __init__(self):
        # left side of the median
        self.left = []
        heapq.heapify_max(self.left)
        self.leftcount = 0
        # right side of the median
        self.right = []
        heapq.heapify(self.right)
        self.rightcount = 0

    def push_left(self, num):
        heapq.heappush_max(self.left, num)
        self.leftcount += 1

    def pop_left(self):
        self.leftcount -= 1
        return heapq.heappop_max(self.left)
    
    def push_right(self, num):
        heapq.heappush(self.right, num)
        self.rightcount += 1
    
    def pop_right(self):
        self.rightcount -= 1
        return heapq.heappop(self.right)

    def addNum(self, num: int) -> None:
        if not self.left or num < self.left[0]:
            self.push_left(num)
        else:
            self.push_right(num)
        
        # rebalance if necesary
        while self.leftcount - self.rightcount > 1:
            self.push_right(self.pop_left())
        
        while self.rightcount - self.leftcount > 1:
            self.push_left(self.pop_right())

    def findMedian(self) -> float:
        if self.leftcount > self.rightcount:
            return self.left[0]
        if self.rightcount > self.leftcount:
            return self.right[0]
        return (self.left[0] + self.right[0])/2
        