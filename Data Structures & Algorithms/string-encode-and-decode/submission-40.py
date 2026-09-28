class Solution:

    def encode(self, strs: List[str]) -> str:
        strList = []
        for s in strs:
            strList.append(str(len(s)) + "#" + s)
        return "".join(strList)
        
    def decode(self, s: str) -> List[str]:
        strList = []
        i = 0
        while i < len(s):
            j = i
            length = 0
            while s[j] != "#":
                j = j + 1
            length = int(s[i : j])
            j = j + 1
            strList.append(s[j : j + length])

            i = j + length
        return strList
