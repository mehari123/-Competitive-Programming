class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        stack = []
        for a in asteroids:
            con = False
            # print(stack)
            if stack:
                
                # print(abs(stack[-1] + a),(abs(stack[-1]) + abs(a)))
                while stack and (stack[-1] > 0 and a < 0)and  abs((stack[-1] + a)) < (abs(stack[-1]) + abs(a)):

                    # print(stack,"in while",a)
                    b = stack.pop()
                    if abs(a) == abs(b):
                        
                        con = True
                    # print(stack,"in while",a,b)
                    a = a if abs(a) > abs(b) else b 

                if not con:

                    stack.append(a)
            elif not con:

                stack.append(a)

        return stack    