class Solution:
    def removeElement(self, nums1: List[int], val: int) -> int:
        left = 0
        right = len(nums1) - 1
        while left <= right:
            if nums1[left] != val:
                left = left + 1
            else:
                if nums1[right] == val:
                    right = right - 1
                else:
                    temp = nums1[left]
                    nums1[left] = nums1[right]
                    nums1[right] = temp
                    right = right - 1
                    left = left + 1
        nums1=sorted(nums1[:left])            
        return len(nums1)