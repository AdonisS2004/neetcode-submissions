class CountSquares:

    def __init__(self):
        self.y2x = dict()

    def add(self, point: List[int]) -> None:
        x,y = point
        if y not in self.y2x:
            self.y2x[y] = dict()
        if x not in self.y2x[y]:
            self.y2x[y][x] = 0
        self.y2x[y][x] += 1
    
    def exists(self, point: List[int]) -> bool:
        x,y = point
        if y not in self.y2x:
            return False
        if x not in self.y2x[y]:
            return False
        return True

    def count(self, point: List[int]) -> int:
        count = 0
        px, py = point
        if py not in self.y2x:
            return count
        

        for ix in self.y2x[py]:
            if ix == px: continue
            dist = ix-px
            # top check
            top_count = 1
            for x,y in [(ix, py), (px+dist, py+dist), (px, py+dist)]:
                if not self.exists([x,y]):
                    top_count = 0
                    break
                top_count *= self.y2x[y][x]
            
            # bottom check
            bottom_count = 1
            for x,y in [(ix, py), (px+dist, py-dist), (px, py-dist)]:
                if not self.exists([x,y]):
                    bottom_count = 0
                    break
                bottom_count *= self.y2x[y][x]
            
            count += top_count + bottom_count
        
        return count
