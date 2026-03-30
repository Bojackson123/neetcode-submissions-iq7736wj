class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += s + "##:;"
        print(res)
        return res
        

    def decode(self, s: str) -> List[str]:
        decoded = s.split("##:;")

        if decoded == [""]:
            return ""
        
        if decoded[-1] == "":
            decoded.pop()
        
        return decoded