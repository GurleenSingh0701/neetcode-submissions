class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, m = len(s1), len(s2)
        if n > m:
            return False

        target = [0] * 26
        window = [0] * 26
        for ch in s1:
            target[ord(ch) - 97] += 1

        left = 0
        for right, ch in enumerate(s2):
            window[ord(ch) - 97] += 1
            # keep window size == n
            if right - left + 1 > n:
                window[ord(s2[left]) - 97] -= 1
                left += 1
            if window == target:
                return True
        return False