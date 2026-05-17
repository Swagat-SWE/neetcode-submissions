class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count_dict = {}
        for num in nums:
            if num in count_dict:
                count_dict[num]+=1
            else:
                count_dict[num] = 1 

        max_count = len(nums) / 2
        for k, v in count_dict.items():
            if v > max_count:
                return k
            


        