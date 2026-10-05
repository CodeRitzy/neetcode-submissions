class Solution:

    def encode(self, strs: List[str]) -> str:
        out = []
        for s in strs:
            out.append(str(len(s)) + '#' + s)
        return "".join(out)
    def decode(self, s: str) -> List[str]:
        out = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length =  int(s[i : j])
            j += 1
            i = j + length
            out.append(s[j : j + length])
            

        return out