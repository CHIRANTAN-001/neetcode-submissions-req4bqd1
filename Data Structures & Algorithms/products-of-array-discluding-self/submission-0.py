class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeros = 0
        idx = -1
        prod = 1

        for i in range(len(nums)):
            if nums[i] == 0:
                zeros += 1
                idx = i
            else:
                prod *= nums[i]

        res = [0] * len(nums)

        if zeros == 0:
            for i in range(len(nums)):
                res[i] = prod // nums[i]
        elif zeros == 1:
            res[idx] = prod

        return res