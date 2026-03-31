class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += (f"{len(s)}#{s}")
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        curr_len = ""
        curr_str = ""
        i = 0

        while i < len(s):
            while s[i] != "#":
                curr_len += s[i]
                i += 1
            i += 1
            length = int(curr_len)
            curr_str = s[i : i + length]
            res.append(curr_str)
            i += length
            
            curr_len = ""
            curr_str = ""

        return res