class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # idea: the element in the triplet must have members who are less than
        # the other triplets

        # check first triplet
        found = False
        for triplet in triplets:
            if triplet[0] != target[0]:
                continue
            if triplet[1] > target[1]:
                continue
            if triplet[2] > target[2]:
                continue
            found = True
            break
        if not found: return False

        # check first triplet
        found = False
        for triplet in triplets:
            if triplet[1] != target[1]:
                continue
            if triplet[2] > target[2]:
                continue
            if triplet[0] > target[0]:
                continue
            found = True
            break
        if not found: return False

        # check first triplet
        found = False
        for triplet in triplets:
            if triplet[2] != target[2]:
                continue
            if triplet[0] > target[0]:
                continue
            if triplet[1] > target[1]:
                continue
            found = True
            break
        if not found: return False

        return True