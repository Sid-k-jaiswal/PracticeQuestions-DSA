class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # brute force -------------- O(n*n)
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[j] + nums[i] == target:
        #             return [i,j]
        # return []

        # hashmap ------------------ O(n)
        hashmap = {}
        for i in range(len(nums)):
            res = target - nums[i]

            if res in hashmap:
                return [i, hashmap[res]]

            hashmap[nums[i]] = i

        return []
