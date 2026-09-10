class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # the given array nums is sorted
        # implementing binary search with a two pointer apprach
        

        l = 0 # left pointer at the start of the list
        r = len(nums) - 1 # right pointer at the end of the list

        while l<=r:
            mid = (l+r)//2
            if target > nums[mid]:
                l = mid + 1
            elif target < nums[mid]:
                r = mid - 1
            else:
                return mid
        return -1