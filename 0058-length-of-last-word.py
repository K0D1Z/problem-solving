class Solution:
    # def lengthOfLastWord(self, s: str) -> int:
    #     s = s.split()
    #     return len(s[-1])
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        is_letter_found = False
        s = s[::-1]
        for i in s:
            print(i)
            if i == ' ' and is_letter_found:
                return length
            elif i != ' ':
                is_letter_found = True
                length += 1
        return length
