class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        current = 0
        best = 0 

        for i in range(len(nums)):
            if nums[i] != 0:
                current += 1
                best = max(best, current )
            else: 
                current = 0  

        return best