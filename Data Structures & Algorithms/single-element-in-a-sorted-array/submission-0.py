class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        sum = 0
        # for i in nums:
        #     sum = sum ^ i
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[left] <= nums[mid]:
                sum = sum ^ nums[left]
                left += 1
            else:
                sum = sum ^ nums[right]
                right -= 1
        return sum