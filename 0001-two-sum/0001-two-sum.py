class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx = 0
        for idx, value in enumerate(nums):
            for idx2, value2 in enumerate(nums):
                if idx == idx2:
                    continue
                    
                if value + value2 == target:
                    return [idx, idx2]
            