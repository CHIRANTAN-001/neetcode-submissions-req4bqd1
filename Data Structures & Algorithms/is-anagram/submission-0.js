class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        let sArr = s.split('')
        sArr.sort()
        let sortedSArr = sArr.join('')

        let tArr = t.split('')
        tArr.sort()
        let sortedTArr = tArr.join('')

        if(sortedSArr === sortedTArr) return true;
        return false
    }
}
