class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        current = 0
        best = 0
        final = 0 
        for i in range(len(nums)):
            if nums[i] == 1:
                current += 1
            else:
                current = 0

            best = max(best, current)

            if best>current:
                final = best
            else:
                final = current

        return final

            



        