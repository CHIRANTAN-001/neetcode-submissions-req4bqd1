class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mapp = dict.fromkeys(range(256), -1)

        left = 0
        right = 0

        n = len(s)

        max_length = 0

        while right < n:
            if mapp[ord(s[right])] != -1:
                if mapp[ord(s[right])] >= left:
                    left = mapp[ord(s[right])] + 1

            length = right - left + 1
            max_length = max(length, max_length)

            mapp[ord(s[right])] = right
            right += 1
        return max_length
