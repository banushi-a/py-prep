class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sc = {}
        tc = {}

        for cs in s:
            sc[cs] = 1 + sc.get(cs, 0)
        
        for ct in t:
            tc[ct] = 1 + tc.get(ct, 0)

        for cs in sc.keys():
            if tc.get(cs, 0) == 0 or tc[cs] != sc[cs]:
                return False

        # if we make it out of the above loop, then we know everything in cs is in ct

        return len(sc.keys()) == len(tc.keys())