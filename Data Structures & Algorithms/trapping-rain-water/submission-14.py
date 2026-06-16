class Solution:
    def trap(self, height: List[int]) -> int:
        """
        Time O(n), Space O(n) Solution

        Techniques used:
            - preffix/suffix arrays
        """
        # general variables
        n = len(height)

        # solution specific variables
        tall_left = []
        tall_right = []
        total_water = 0

        # construct tallest on the left side array
        comp = 0
        for bar in height:
            comp = max(comp, bar)
            tall_left.append(comp)

        # construct tallest on the right side array
        comp = 0
        for bar in height[::-1]:
            comp = max(comp, bar)
            tall_right.append(comp)
        tall_right = [x for x in tall_right[::-1]]

        # check tallest bar height on left and right sides 
        # at each bar level to calculate amount of total water.
        for i, bar in enumerate(height):
            tl, tr = tall_left[i], tall_right[i]
            if bar < tl and bar < tr:
                total_water += min(tl, tr) - bar
        
        return total_water
            
            
