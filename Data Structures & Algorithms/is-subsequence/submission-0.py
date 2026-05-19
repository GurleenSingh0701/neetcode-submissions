class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i,j=0,0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1  # Move forward in s only when we find a match
            j += 1    # Always move forward in t
        
        return i == len(s)  