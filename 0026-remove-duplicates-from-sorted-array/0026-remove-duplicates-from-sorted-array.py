class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        i = 0
        l = len(nums)
        
        for j in range(1, l):

            if nums[i] != nums[j]:
                
                i += 1

                nums[i] = nums[j]

        return i + 1

        # i = 1

        # while i < len(nums):
        #     if nums[i] == nums[i-1]:
        #         nums.pop(i)
        #     else:
        #         i += 1
        # return len(nums)
        