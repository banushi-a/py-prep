class Solution:
    def getKey(self, s):
        startIndex = ord("a")
        out = [0] * 26
        for c in s:
            thisIndex = ord(c)
            out[thisIndex-startIndex] += 1
        return str(out)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {} # "[..(26 key array)..]" -> List[str]

        for s in strs:
            key = self.getKey(s)
            if key in groups:
                groups[key].append(s)
            else:
                groups[key] = [s]

        return [groups[k] for k in groups.keys()]