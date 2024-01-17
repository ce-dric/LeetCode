class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = dict.fromkeys((set(arr)))
        for num in arr:
            if num in set(arr):
                d[num] = int(0 if d[num] is None else d[num]) + 1
        
        return False if len(d) != len(set(d.values())) else True