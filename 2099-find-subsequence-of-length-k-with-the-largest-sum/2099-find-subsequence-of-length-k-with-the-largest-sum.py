import heapq

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        # Find the k largest elements along with their indices
        largest_elements = heapq.nlargest(k, enumerate(nums), key=lambda x: x[1])
        
        # Extract the indices of the k largest elements
        indices = [index for index, element in largest_elements]
        
        # Sort the indices to maintain the original order
        indices.sort()
        
        # Construct the subsequence using the sorted indices
        subsequence = [nums[i] for i in indices]
        
        return subsequence
