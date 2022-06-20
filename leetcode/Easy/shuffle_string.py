class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        iterable_list = indices.copy()
        j = 0
        for i in indices:
            iterable_list[i] = s[j]
            j += 1
        
        return "".join(iterable_list)