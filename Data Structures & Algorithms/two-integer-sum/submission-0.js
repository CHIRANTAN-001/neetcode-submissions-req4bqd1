class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        const map = new Map();

        for (let i = 0; i < nums.length; i++) {
            let isExist = map.has(target - nums[i])
            if (isExist) {
                let arr = [map.get(target - nums[i]), i]
                return arr
            } else {
                map.set(nums[i], i)
            }
        }
    }
}
