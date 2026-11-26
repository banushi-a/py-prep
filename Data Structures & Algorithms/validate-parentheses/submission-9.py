class Solution:
    def isValid(self, s: str) -> bool:
        openers = {
            ")": "(",
            "}": "{",
            "]": "[",
        }

        out = []

        for c in s:
            if c in openers.values():
                out.append(c)
                continue
            if len(out) == 0:
                return False
            if openers[c] is not out[-1]:
                return False
            out.pop()

        return len(out)==0