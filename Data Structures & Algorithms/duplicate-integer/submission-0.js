class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        const newArr = [...new Set(nums)]

        if(newArr.length === nums.length) return false;
        return true
    }
}
