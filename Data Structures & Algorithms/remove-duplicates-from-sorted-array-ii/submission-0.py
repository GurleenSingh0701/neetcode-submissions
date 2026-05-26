class Solution:
    def removeDuplicates(self, arr: List[int]) -> int:
        n = len(arr)
        if n <= 2:
            return n

        left = 0
        for right in range(n):
            # keep current element if we have stored fewer than 2 elements
            # or it differs from the element two positions before `left`.
            if left < 2 or arr[right] != arr[left - 2]:
                arr[left] = arr[right]
                left += 1

        return left