class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        # target = [1,2], n = 4, integers = [1,2,3, 4]
        #  stack = [1,2]<----- push, push

        # stack = [1, 2], integers = [1, 2, 3, 4], integer_pointer = 2, stack_pointer = 2

        integers = []
        stack = []
        res = []

        for i in range(1, n+1):
            integers.append(i)

        integer_pointer = 0
        stack_pointer = 0

        while stack != target:

            if len(integers) != 0:
                stack.append(integers[integer_pointer])
                res.append("Push")

                if stack[stack_pointer] == target[stack_pointer]:
                    stack_pointer += 1
                    integer_pointer += 1
                else:
                    stack.pop(stack_pointer)
                    res.append("Pop")
                    integer_pointer += 1
        
        return res

                
                



        
 

