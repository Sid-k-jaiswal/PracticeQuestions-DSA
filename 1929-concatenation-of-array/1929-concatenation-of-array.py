class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        # n = len(nums)
        # i = 0
        # ans = [0]*2*n

        # while i < n:
        #     ans[i] = nums[i]
        #     ans[i+n] = nums[i]

        #     i += 1

        # return ans

        ans = nums + nums

        print(ans)

        return ans

        