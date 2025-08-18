class Solution:

    def swap(self, nums, l, r):
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        return nums

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        k = k % len(nums)

        nums = self.swap(nums, 0, len(nums)-1)
        nums = self.swap(nums, 0, k-1)
        nums = self.swap(nums, k, len(nums)-1)

        