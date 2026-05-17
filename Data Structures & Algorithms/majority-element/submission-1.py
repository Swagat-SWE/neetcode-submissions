class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        max_count = 0
        element = 0
        for num in nums:
            if max_count == 0:
                element = num
            if num == element:
                max_count += 1
            else:
                max_count -= 1
        return element 
