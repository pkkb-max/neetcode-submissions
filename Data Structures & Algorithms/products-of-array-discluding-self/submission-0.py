class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zeros = 0
        res = [0] * len(nums)
        for num in nums:
            if num != 0:
                prod = prod*num
            else:
                zeros+=1
        if zeros > 1: return res

        for ind in range(len(nums)):
            value = nums[ind]
            if zeros == 1 and value == 0:
                res[ind] = prod
            elif zeros == 1:
                res[ind] = 0
            else: 
                res[ind] = prod//value
        return res 