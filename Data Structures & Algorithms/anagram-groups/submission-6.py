class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anaHash = {}
        for s in strs:
            charsArr = [0] * 26
            for i in s:
                charsArr[ord(i) - ord('a')] += 1
            anaHash.setdefault(tuple(charsArr), []).append(s)
        return list(anaHash.values())