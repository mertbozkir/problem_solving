class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        
        w = 0
        for account in accounts:
            if sum(account) > w:
                w = sum(account)
        return w
    
    
        # return max(map(sum, accounts))
        