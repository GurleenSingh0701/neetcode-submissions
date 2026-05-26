class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left=0
        right=left
        while(right<=len(nums)-1):
            if nums[right]!=0:
                temp=nums[left]
                nums[left]=nums[right]
                nums[right]=temp
                left=left+1
                right=right+1
            else:
                right=right+1