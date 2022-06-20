class Solution:
    def minPartitions(self, n: str) -> int:
        
        
        # return max(n)
        
        
        return max(list(n))  
        
        
        """partitions = list(n)
        partitions.sort(reverse = True)
        return partitions[0]"""
        
        # return sorted(list(n), reverse = True)[0]
        