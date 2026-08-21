class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome_range(left_idx: int, right_idx: int) -> bool:
            while left_idx < right_idx:
                if s[left_idx] != s[right_idx]:
                    return False
                left_idx += 1
                right_idx -= 1
            return True

        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return is_palindrome_range(left+1, right) or is_palindrome_range(left, right-1)
            left += 1
            right -= 1
        return True
        