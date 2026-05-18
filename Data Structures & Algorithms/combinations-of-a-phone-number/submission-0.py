class Solution:
    def letterCombinations(self, s: str) -> List[str]:
        DICT1 = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        if not s:
            return []

        result = []

        def backtrack(index, current):
            if index == len(s):
                    result.append(current)
                    return

            for letter in DICT1.get(s[index], ""):
                    backtrack(index + 1, current + letter)

        backtrack(0, "")
        return result