class Solution:
    def isValid(self, s: str) -> bool:
        openP = []
        closeMap = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for c in s:
            if c in closeMap:
                if openP and openP[-1] == closeMap[c]:
                    openP.pop()
                else:
                    return False
            else:
                openP.append(c)
        
        return True if not openP else False
            