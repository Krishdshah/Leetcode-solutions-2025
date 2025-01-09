class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        c=0
        n=len(pref)
        for i in words:
            if pref==i[:n]:
                c+=1
        return c
