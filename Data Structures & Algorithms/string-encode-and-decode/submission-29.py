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
            j = s.index('-', i)
            length = int(s[i:j])
            out.append(s[j + 1:j + length + 1])

            i = j + 1 + length
        return out

