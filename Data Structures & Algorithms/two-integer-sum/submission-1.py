class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash1 = {}  # val -> index

        for i, n in enumerate(nums):
            hash1[n] = i

        for i, n in enumerate(nums):
            diff = target - n
            if diff in hash1 and hash1[diff] != i:
                return [i, hash1[diff]]
        return []