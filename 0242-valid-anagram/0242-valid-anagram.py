class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        my_map = {}

        for i in s:
            my_map[i] = my_map.get(i,0) + 1

        for j in t:
            my_map[j] = my_map.get(j,0) - 1

        for key, val in my_map.items():
            if val != 0:
                return False

        return True
        