class Solution:
    def isPalindrome(self, s: str) -> bool:
        w=""
        for i in range(len(s)):
            if s[i].isalnum():
                w=w+s[i].lower()
        print(w)
        left=0
        right=len(w)-1
        while left<right:
            if w[left]!=w[right]:
                return False
            else:
                left+=1   
                right-=1 
        return True 