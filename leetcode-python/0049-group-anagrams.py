class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s))
            res[sortedS].append(s)
        return list(res.values())

    # def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    #     result = {}
    #     for i in strs:
    #         temp = [0 for _ in range(26)] # letters counter
    #         for j in i:
    #             temp[ord(j) - ord("a")] += 1
    #         temp = tuple(temp)
    #         if temp not in result.keys():
    #             result[temp] = [i]
    #         else:
    #             result[temp].append(i)
    #     return list(result.values())

