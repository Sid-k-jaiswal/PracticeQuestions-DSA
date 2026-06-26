class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:

        n = len(nums)

        count_set = set()

        repeated_num = 0

        for i in nums:

            if i in count_set:
                repeated_num = i
            else:
                count_set.add(i)
        
        for i in range(1, n+1):

            if i not in count_set:
                return [repeated_num, i]