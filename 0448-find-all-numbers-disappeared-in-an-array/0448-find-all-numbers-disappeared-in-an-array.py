class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        n = len(nums)

        total_nums = set()

        for i in range(1, n+1):
            total_nums.add(i)
        
        nums = set(nums)

        res = list(total_nums - nums)

        return(res)

        