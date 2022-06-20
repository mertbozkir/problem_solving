class Solution:
    def search(self, nums: List[int], target: int) -> int:
        high = len(nums) - 1
        low, mid  = 0, 0
        
        while low <= high:
            mid = (high + low)// 2
        
            if nums[mid] < target:
                low = mid + 1
            
            elif nums[mid] > target:
                high = mid - 1
            
            else:
                return mid
        
        return -1