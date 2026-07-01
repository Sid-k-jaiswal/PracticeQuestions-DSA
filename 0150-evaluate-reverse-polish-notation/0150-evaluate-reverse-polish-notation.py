class Solution:

    # tokens = ["2","1","+","3","*"], b = 2, a = 1
    # stack = [3,(a+b=3)], a = (a+b=3), b = 3 

    def evalRPN(self, tokens: List[str]) -> int:

        expressions = {"+", "-", "*", "/"}
        
        stack = []

        for i in tokens:

            if i in expressions:
                
                b = stack.pop()
                a = stack.pop()

                if i == "+":
                    stack.append(a+b)
                elif i == "-":
                    stack.append(a-b)
                elif i == "*":
                    stack.append(a*b)
                elif i == "/":
                    stack.append(int(a/b))

            else:
                stack.append(int(i))

        return stack[0]

        


        