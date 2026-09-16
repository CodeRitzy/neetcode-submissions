class Solution:

    def encode(self, strs: List[str]) -> str:
        line = ""
        asciiCount = 129
        for s in strs:
            for i in s:
                line += chr(ord(i)) + chr(asciiCount)
                asciiCount = asciiCount + 1
            line += chr(128)
        return line

    def decode(self, s: str) -> List[str]:
        word = ""
        strList = []
        for i in range(len(s)):
            if ord(s[i]) == 128:
                strList.append(word)
                word = ""
            if ord(s[i]) >= 129:
                continue
            if ord(s[i]) < 128 and s[i] != chr(128):
                word += s[i]
        return strList
