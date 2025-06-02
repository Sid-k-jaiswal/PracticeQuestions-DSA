class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        my_map = {}

        # for i, num in enumerate(nums):

        #     complement = target - num

        #     if complement in my_map:
        #         return [i, my_map[complement]]

        #     my_map[num] = i
        
        # return [-1,-1]

        n = len(nums)

        for i in range(n):
            my_map[nums[i]] = i

        for j in range(n):
            complement = target - nums[j]

            if complement in my_map and my_map[complement] != j:
                return [my_map[complement],j]
        
        return [-1,-1]

