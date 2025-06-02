class Solution:

    # def isAlphaNumeric(self, c):
    #     return     (ord('A') <= ord(c) <= ord('Z') or
    #                 ord('a') <= ord(c) <= ord('z') or
    #                 ord('0') <= ord(c) <= ord('9'))

    # def isPalindrome(self, s: str) -> bool:

    #     # s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

    #     i, j = 0, len(s) - 1

    #     while i < j:

    #         while i < j and not self.isAlphaNumeric(s[i]):
    #             i += 1
    #         while i < j and not self.isAlphaNumeric(s[j]):
    #             j -= 1

    #         if s[i].lower() == s[j].lower():
    #             i += 1
    #             j -= 1
    #         else:
    #             return False
        
    #     return True

    def isPalindrome(self, s: str) -> bool:

        s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

        i, j = 0, len(s) - 1

        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False
        
        return True
        