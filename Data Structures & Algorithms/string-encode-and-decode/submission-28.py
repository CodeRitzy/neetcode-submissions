class Solution:

    def encode(self, strs: List[str]) -> str:
        s = []
        for st in strs:
            s.append(str(len(st)))
            s.append('-')
            s.append(st)
        return "".join(s)

    def decode(self, s: str) -> List[str]:
        out = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '-':
                j = j + 1
            length = int(s[i:j])
            j = j + 1
            out.append(s[j:j + length])

            i = j + length
        return out

