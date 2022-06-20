class Solution:
    """def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        CurSum = 0
        
        for n in nums:
            
            if CurSum < 0:
                CurSum = 0
                
            CurSum += n
            maxSub = max(maxSub, CurSum)
        return maxSub"""
    
    def maxSubArray(self, nums: List[int]) -> int:
            m = 0
            stack = []
            for each in nums:
                if m + each < each:
                    m = each
                else:
                    m = each + m
                stack.append(m)
            return max(stack)