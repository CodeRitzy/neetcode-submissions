class Solution:

    def encode(self, strs: List[str]) -> str:
        strList = []
        for s in strs:
            strList.append(str(len(s)) + '#' + s)
        return "".join(strList)
    def decode(self, s: str) -> List[str]:
        out = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            j += 1
            out.append(s[j: j +length])
            i = j + length
        return out