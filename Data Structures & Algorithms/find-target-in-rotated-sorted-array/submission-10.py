class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """O(n)
        for i in range (0, len(nums)): 
            if target == nums[i]:
                return i
        return -1 """

            # [3, 4, 5, 6, 1, 2] 

        l = 0
        r = len(nums)-1
        while l <= r:
            mid = (l+r) // 2
            if target == nums[mid]:
                return mid
            elif nums[l] <= nums[mid]:   # guarantees left part increasing
                if target < nums[mid] and target >= nums[l]: # checking in the increasing part 
                    r = mid-1
                else:
                    l = mid+1
            else: #right part is increasing 
                if target > nums[mid] and target <= nums[r]:  #checking in right increasing
                    l = mid+1
                else:
                    r = mid-1
        return -1 

