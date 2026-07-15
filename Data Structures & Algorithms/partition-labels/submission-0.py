class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        letter_to_interval = dict() # letter: [start, end]
        for i, c in enumerate(s):
            if c not in letter_to_interval:
                letter_to_interval[c] = [i,i]
            letter_to_interval[c][-1] = i

        intervals = []
        for c in s:
            if not letter_to_interval:
                break
            if c not in letter_to_interval:
                continue
            intervals.append(letter_to_interval[c])
            del letter_to_interval[c]
        
        sub_strings = []
        for start, end in intervals:
            if not sub_strings:
                sub_strings.append([start, end])
            elif start < sub_strings[-1][-1]:
                prev_start, prev_end = sub_strings.pop()
                new_start = min(start, prev_start)
                new_end = max(end, prev_end)
                sub_strings.append([new_start, new_end])
            else:
                sub_strings.append([start,end])
        
        res = [end+1-start for start, end in sub_strings]
        return res