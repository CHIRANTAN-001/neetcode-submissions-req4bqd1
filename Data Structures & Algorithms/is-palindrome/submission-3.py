class Solution:
    def isPalindrome(self, s: str) -> bool:
        updated_String = ''.join([char.lower() for char in s if char.isalnum()])
        # print(updated_String)
        left = 0
        right = len(updated_String) - 1
        count = 0
        while left < right:
            if updated_String[left] != updated_String[right]:
                return False
            left += 1
            right -= 1

        return True