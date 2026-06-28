class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        index = {}
        for num in nums:
            index[num] = 1
        max_c = 0
        end = max(index.keys())
        for start in index.keys():
            count= 0
            while start in index and start <= end:
                count += 1
                start+=1
            max_c = max(max_c, count)
        return max_c