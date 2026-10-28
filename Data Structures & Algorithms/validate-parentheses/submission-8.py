class Solution:
    def isValid(self, s: str) -> bool:
        closing = {
            ']': '[',
            ')': '(',
            '}': '{'
        }

        so_far = []
        # ]()

        for c in s:
            if c not in closing.keys():
                so_far.append(c)
            elif len(so_far) is not 0 and so_far[-1] == closing[c]:
                so_far.pop()
            else:
                so_far.append(c)

        return len(so_far) == 0
            