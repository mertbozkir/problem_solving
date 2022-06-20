class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums2 = nums.copy()
        
        return nums + nums2
        
        """for i in range(len(nums)):
            nums.append(nums[i])
            
        return nums"""