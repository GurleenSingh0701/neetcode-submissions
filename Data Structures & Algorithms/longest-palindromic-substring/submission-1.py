class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return "", 0
        transformed = "^#" + "#".join(s) + "#$"
        p = [0] * len(transformed)
        center = right = 0

        for i in range(1, len(transformed) - 1):
            mirror = 2 * center - i
            if i < right:
                p[i] = min(right - i, p[mirror])

            while transformed[i + 1 + p[i]] == transformed[i - 1 - p[i]]:
                p[i] += 1

            if i + p[i] > right:
                center = i
                right = i + p[i]

        max_len = 0
        center_index = 0
        for i in range(1, len(transformed) - 1):
            if p[i] > max_len:
                max_len = p[i]
                center_index = i

        start = (center_index - max_len) // 2
        return s[start:start + max_len]