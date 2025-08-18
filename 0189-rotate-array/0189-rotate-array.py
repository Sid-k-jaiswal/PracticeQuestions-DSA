class Solution:

    # [1,2,3,4,5,6,7], k = 3 ----> 
    # l = 0, r = len -1 ---> [7,6,5,4,3,2,1]
    # l=0, r = k-1 ---> [5,6,7,4,3,2,1]
    # l=k, r = len - 1 ---> [5,6,7,1,2,3,4]
    
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

    # def rotate(self, nums: List[int], k: int) -> None:
    #     #     """
    #     #     Do not return anything, modify nums in-place instead.
    #     #     """

    #     tmp_array = [0]*len(nums)

    #     # k = k % len(nums)

    #     for i in range(len(nums)):
    #         tmp_array[(i+k)%len(nums)] = nums[i]
        
    #     for i in range(len(nums)):
    #         nums[i] = tmp_array[i]
        