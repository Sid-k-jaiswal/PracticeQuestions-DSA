class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        my_map = {}

        for i, num in enumerate(nums):

            complement = target - num

            if complement in my_map:
                return [i, my_map[complement]]

            my_map[num] = i
        
        return [-1,-1]