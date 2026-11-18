class Solution:
    def uniqueMorseRepresentations(self, words: list[str]) -> int:
        def mapWordToMorse(s: str) -> str:
            codes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

            r = ''
            for i in s:
                r += codes[ord(i) - ord('a')]
            return r

        res = set()
        for w in words:
            res.add(mapWordToMorse(w))
        return len(res)

        