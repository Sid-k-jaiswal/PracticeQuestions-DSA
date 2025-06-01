class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        parenthesis_map = {']':'[','}':'{',')':'('}

        for i in s:

            if i in parenthesis_map:
                top = stack.pop() if stack else '_'
                if top != parenthesis_map[i]:
                    return False
            else:
                stack.append(i)
        
        return stack == []

        # while '()' in s or '{' in s or '[]' in s:
        #     s = s.replace('()','')
        #     s = s.replace('{}','')
        #     s = s.replace('[]','')

        # return s == ''

        