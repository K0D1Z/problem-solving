class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        a_count = 1
        vowels = ('a','e','i', 'o','u')
        sentence = sentence.split(' ')
        res = []

        for i in sentence:
            f = i[0]
            if f.lower() in vowels:
                i = i + 'ma'
            else:
                i = i[1:] + f + 'ma'
            i += 'a' * a_count
            a_count += 1
            res.append(i)
        
        return " ".join(res)
