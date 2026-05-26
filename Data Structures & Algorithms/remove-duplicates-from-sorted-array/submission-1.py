class Solution:
    def removeDuplicates(self,arr: List[int]) -> int:
        slow=1
        for fast in range(0,len(arr)):
            if arr[slow-1]!=arr[fast]:
                arr[slow]=arr[fast]
                slow+=1
        return slow