class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        frequency = set()

        for i in nums:
            if i in frequency:
                return True
            else:
                frequency.add(i)
        
        # print(frequency)

        return False