class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        remainder = 1
        for i in range(len(digits)-1, -1, -1):
            print(i)
            number = digits[i] + remainder
            if number < 10:
                digits[i] = number
                return digits
            remainder = 1
            digits[i] = 0
        if remainder == 1:
            digits.insert(0, remainder)
        return digits