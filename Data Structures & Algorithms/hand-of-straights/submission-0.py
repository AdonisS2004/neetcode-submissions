from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n%groupSize > 0:
            return False

        # build frequencies
        frequencies = Counter(hand)
        while frequencies:
            card = min(frequencies.keys())
            for i in range(groupSize):
                if card not in frequencies:
                    return False
                frequencies[card] -= 1
                if frequencies[card] == 0:
                    del frequencies[card]
                card += 1
        return True