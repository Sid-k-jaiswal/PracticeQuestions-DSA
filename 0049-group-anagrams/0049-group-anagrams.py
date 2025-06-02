class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        my_map = {}

        for word in strs:

            key = ''.join(sorted(word))

            if key not in my_map:
                my_map[key] = []

            my_map[key].append(word)

        return list(my_map.values())
        