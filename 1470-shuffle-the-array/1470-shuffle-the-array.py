class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:

        ans = [0]*2*n

        i , j = 0, 0

        while i < n and j < 2*n :

            ans[j] = nums[i]
            ans[j+1] = nums[n+i]

            i = i+1
            j = j+2

            # print(ans)

        return ans

