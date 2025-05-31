class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        j = 0

        for i in range(len(nums)):

            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
        
        print(nums)

        return j
        
        # i = 0
        # n = len(nums)

        # while i < n:
        #     if nums[i] == val:
        #         n -= 1
        #         nums[i] = nums[n]
        #     else:
        #         i += 1

        # print(nums)

        # return i
