class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) & 1:
            return False
        
        pair = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        res = []

        for c in s:
            if c in pair:
                if not res or res.pop() != pair[c]:
                    return False
            else:
                res.append(c)
            
        return not res