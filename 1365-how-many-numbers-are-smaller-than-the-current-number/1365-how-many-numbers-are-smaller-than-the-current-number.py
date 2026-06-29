class Solution:

    # def count(self, num, nums):
    #     c = 0
    #     for i in nums:
    #         if i < num:
    #             c += 1
    #     return c


    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

    #     res = []

    #     for i in nums:
    #         j = self.count(i, nums)
    #         res.append(j)
        
    #     return res

    # nums = [8,1,2,2,3], temp = [1,2,2,3,8], mapping = {1:0,2:1,3:3,8:4}

        temp = sorted(nums)

        n = len(nums)
        mapping = {}
        res = []

        for i in range(n):

            if temp[i] not in mapping:
                mapping[temp[i]] = i

        for i in range(n):

            x = mapping[nums[i]]
            res.append(x)

        return(res)








        