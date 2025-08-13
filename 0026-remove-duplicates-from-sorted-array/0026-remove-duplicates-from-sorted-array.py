class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        j = 0

        for i in range(1, len(nums)):

            if nums[j] != nums[i]:
                j += 1

                nums[j] = nums[i]

        # print(nums)
        # print(j)

        return j + 1

        # i = 0

        # while i < len(nums)-1:
        #     if nums[i] == nums[i+1]:
        #         nums.pop(i+1)
        #     else:
        #         i += 1
        # print(nums)
        # return len(nums)
