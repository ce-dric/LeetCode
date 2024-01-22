class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        list_unique = set(nums)
        for i in range(1, len(nums)+1):
            if i not in list_unique:
                return [sum(nums)-sum(list_unique), i]
        