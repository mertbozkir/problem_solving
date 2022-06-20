class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        shuffled_list = []
        for i in range(len(nums)//2):
            j = i + n
            shuffled_list.append(nums[i])
            shuffled_list.append(nums[j])
        return shuffled_list