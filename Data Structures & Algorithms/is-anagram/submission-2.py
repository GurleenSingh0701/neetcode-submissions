class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hash1=dict()
        hash2=dict()
        count=0
        for item in s:
            if hash1.get(item)!=None:
                hash1.update({item:hash1.get(item)+1})
            else:
                hash1.update({item:1})
        for item in t:
            if hash2.get(item)!=None:
                hash2.update({item:hash2.get(item)+1})
            else:
                hash2.update({item:1})
        
        for items in hash1.items():
            if items not in hash2.items():
                return False
        return True